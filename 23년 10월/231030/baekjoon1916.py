import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(graph, start, end, num):
    cost = [INF] * (num + 1)
    q = []

    heappush(q, (0, start))

    while q:
        current_cost, current_node = heappop(q)
        if cost[current_node] < current_cost:
            continue
        if current_node == end:
            print(cost[end])
            exit()

        for new_node, new_cost in graph[current_node].items():
            val = current_cost + new_cost
            if val < cost[new_node]:
                cost[new_node] = val
                heappush(q, (val, new_node))


def main():
    N = int(input())
    M = int(input())

    g = [dict() for _ in range(N + 1)]

    for _ in range(M):
        s, e, c = map(int, input().split())
        if e in g[s]:
            g[s][e] = min(g[s][e], c)
        else:
            g[s][e] = c

    x, y = map(int, input().split())
    dijkstra(g, x, y, N)


if __name__ == "__main__":
    main()
