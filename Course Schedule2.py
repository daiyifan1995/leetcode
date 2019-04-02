from collections import defaultdict
class Solution:

    def findOrder(self, numCourses, prerequisites):

        adj_list = defaultdict(list)#方式无key出现keyError错误

        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1 #dict.get（）返回dest键的值，若不存在，则返回默认值0

        # 查找indegree为0的node
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree.keys()]

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

if __name__ == "__main__":
    Solution=Solution()
    input=[[1,0],[2,0],[3,1],[3,2]]
    print(Solution.findOrder(4,input))