# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# import sys
#
#
# def isDoublePalindrome(input):
#     if len(input) % 2 == 1:  # test length
#         return False
#     single = ""
#     for i in range(0, len(input) - 1, 2):  # test double
#         if input[i] == input[i + 1]:
#             single += input[i]
#         else:
#             return False
#     # test isPalindrome
#     stack = []
#     while i < len(single):
#         if i < len(single) // 2:
#             stack.append(single[i])
#         else:
#             if single[i] == stack.pop():
#                 continue
#             else:
#                 return False
#     return single
#
#
# if __name__ == "__main__":
#     for input in sys.stdin:
#         input = input.strip()
#         res = isDoublePalindrome(input)
#         if res == False:
#             print('false')
#         else:
#             print(res)


# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def getShortestDistent(routes, start, end):
    S_to_pages_diatance = {}
    for i in range(len(routes)):
        S_to_pages_diatance[i] = sys.maxsize
    queue = []
    i = 0
    while i < len(routes[start-1]):
        if routes[start - 1][i] != 0:
            queue.append(i)
            S_to_pages_diatance[i] = routes[start - 1][i]
        i = i + 1

    i = 0
    visited_adj = set()
    while len(queue) != 0:
        if queue[i] < len(routes)-1:
            j = 0
            while j < len(routes[queue[i] - 1]):
                if routes[queue[i] - 1][j] != 0:
                    S_to_pages_diatance[j] = min(S_to_pages_diatance[queue[i]] + routes[queue[i] - 1][j] - 1,
                                                 S_to_pages_diatance[j])
                if j not in visited_adj:
                    queue.append(j)
                j = j + 1
        visited_adj.add(queue.pop(i))

    return S_to_pages_diatance[end - 1]


if __name__ == "__main__":
    l1 = [int(i) for i in sys.stdin.readline().strip().split(" ")]
    loc_count = l1[0]
    route_count = l1[1]
    routes = [[0 for i in range(loc_count)] for i in range(loc_count)]
    # adjustgraph intial
    for i in range(route_count):
        line = [int(i) for i in sys.stdin.readline().strip().split(" ")]
        start = line[1]
        end = line[2]
        price = line[3]

        # if routes[start - 1][end - 1] > price or routes[start - 1][end - 1] == 0:
        routes[start - 1][end - 1] = price
    l2 = sys.stdin.readline().strip().split(" ")
    start = int(l2[0])
    end = int(l2[1])
    price=getShortestDistent(routes, start, end)
    if price!=sys.maxsize:
        print(price)
    else:
        print("NA")



