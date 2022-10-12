# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 3 - Problem D. First Time Chapter 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-3/problems/D1
#
# Time:  O(M + NlogN)
# Space: O(N)
#

def ceil_divide(a, b):
    return (a+b-1)//b

def first_time_chapter_1():
    def merge(a, b, cnt):
        if len(group[a]) > len(group[b]):
            group[a], group[b]
        while group[a]:
            x = group[a].pop()
            if x in group[b]:
                cnt -= 1
            else:
                group[b].add(x)
        return cnt

    N, M, K = map(int, input().split())
    group = [{i//K} for i in range(N)]
    result = -1
    cnt = N-ceil_divide(N, K)
    for t in range(1, M+1):
        A, B = map(int, input().split())
        cnt = merge(A-1, B-1, cnt)
        if cnt == 0 and result == -1:
            result = t
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, first_time_chapter_1()))
