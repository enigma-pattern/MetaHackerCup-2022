# Copyright (c) 2022 kamyu. All rights reserved.
#
# Meta Hacker Cup 2022 Round 2 - Problem B. Balance Sheet
# https://www.facebook.com/codingcompetitions/hacker-cup/2022/round-2/problems/B
#
# Time:  O(NlogN + N * K)
# Space: O(N * K)
#

from functools import reduce

def balance_sheet():
    def topk(a, b):
        result = []
        i = j = 0
        while (i < len(a) or j < len(b)) and len(result) < K:
            if j == len(b) or (i < len(a) and a[i] > b[j]):
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        return result

    N, K = map(int, input().split())
    events = []
    for i in range(N):
        A, B, X, Y = map(int, input().split())
        events.append((A, X, i, 'B'))
        events.append((B, Y, i, 'S'))
    events.sort(reverse=True)
    P = [[0] for _ in range(N)]
    prev = -1
    curr = []
    for d, p, i, t in events:
        if d != prev:
            curr.clear()
        if t == 'B':
            curr = topk(curr, [x+p for x in P[i]])
        else:
            P[i] = topk(P[i], [x-p for x in curr if x > p])
        prev = d
    curr.clear()
    for i in range(N):
        curr = topk(curr, P[i])
    return reduce((lambda x, y:(x+y)%MOD), curr, 0)

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, balance_sheet()))
