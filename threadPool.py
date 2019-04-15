import sys
import threading
import queue
import traceback


class NoResultsPending(Exception):
    """All works requests have been processed"""
    pass


class NoWorkersAvailable(Exception):
    """No worket threads available to process remaining requests."""
    pass


class WorkRequest(object):
    """
        工作线程任务请求类, 封装工作线程的一些功能
        @ execute_fun: 执行函数
        @ execute_args: 执行函数的参数
        @ done_callback: 执行函数返回结果后的回调
    """

    def __init__(self, execute_fun, execute_args=None, done_callback=None):
        """
            初始化请求包装类
        """
        # 请求的标识初始化
        self.request_id = id(self)
        # 请求参数的初始化
        self.execute_fun = execute_fun
        self.execute_args = execute_args
        self.done_callback = done_callback
        self.exception = False

    def __str__(self):
        """
            请求类的相关信息
        """
        return 'WorkRequest: %s %s %s' % (self.request_id, self.execute_fun, self.exception)


class WorkerThread(threading.Thread):
    """
        工作线程
    """

    def __init__(self, requestQueue, resultQueue, time_out=5):
        """
            工作线程初始化
        """
        super(WorkerThread, self).__init__()
        self.setDaemon(True)

        # 线程初始化
        self._requestQueue = requestQueue
        self._resultQueue = resultQueue
        self.time_out = time_out
        self._stop_event = threading.Event()

        # 线程启动
        self.start()

    def run(self):
        """
            工作线程启动函数
        """
        while True:

            # 检查线程是否被停止
            if self._stop_event.is_set():
                break

            # 请求队列中取出
            try:
                request = self._requestQueue.get(True, self.time_out)
            except queue.Queue.empty():
                continue

            # 检查线程是否被停止
            if self._stop_event.is_set():
                self._requestQueue.put(request)
                break

            # 执行请求队列中的请求
            try:
                result = request.execute_fun(*request.execute_args)
                self._resultQueue.put((request, result))
            except:
                request.exception = True
                self._resultQueue.put((request, sys.exc_info()))

    def stop_work(self):
        """
            停止工作线程
        """
        self._stop_event.set()


class ThreadingPool(object):
    """
        线程池
    """

    def __init__(self, worker_num, request_size, time_out=5):
        """
            @ worker_num: 线程数量
            @ request_size: 请求队列的大小
            @ time_out: 队列请求超时时间
        """
        # 线程池参数初始化
        self._requestQueue = queue.Queue.Queue(request_size)
        self._resultQueue = queue.Queue.Queue(request_size)
        self.workers = []
        self.stoped_works = []
        self.workRequests = {}
        self.create_workers(worker_num, time_out)

    def create_workers(self, worker_num, time_out=5):
        """
            创建工作线程
        """
        for i in range(worker_num):
            worker = WorkerThread(self._requestQueue, self._resultQueue, time_out=time_out)
            self.workers.append(worker)

    def stop_workers(self, stop_num, do_join=False):
        """
            停用一定数量的线程
        """
        # 停用部分线程
        stop_list = []
        for i in range(min(stop_num, len(self.workers))):
            worker = self.workers.pop()
            worker.stop_work()
            stop_list.append(worker)

        if do_join:
            for worker in stop_list:
                worker.join()
        else:
            self.stoped_works.extend(stop_list)

    def join_all_stoped_workers(self):
        """
            join 所有停用的线程
        """
        for worker in self.stoped_works:
            worker.join()
        self.stoped_works = []

    def put_request(self, request, block=True, timeout=None):
        """
            添加请求
        """
        assert isinstance(request, WorkRequest)
        assert not getattr(request, 'exception', None)
        self._requestQueue.put(request, block, timeout)
        self.workRequests[request.request_id] = request

    def poll(self, block=False):
        """
            拉取数据进行处理, 用于wait
        """
        while True:
            if not self.workRequests:
                raise NoResultsPending
            elif block and not self.workers:
                raise NoWorkersAvailable

            # 取数据进行处理
            try:
                request, result = self._resultQueue.get(block=block)
                if request.exception:
                    print
                    result
                elif request.done_callback:
                    request.done_callback(result)
                del self.workRequests[request.request_id]
            except queue.Queue.Empty:
                break

    def wait(self):
        """
            等待所有请求处理完毕
        """
        while True:
            try:
                self.poll(True)
            except NoResultsPending:
                break

    def get_worker_size(self):
        """
            返回工作线程的个数
        """
        return len(self.workers)

    def stop(self):
        """
            停止线程池， 确保所有线程停止工作
        """
        self.stop_workers(self.get_worker_size(), True)
        self.join_all_stoped_workers()
