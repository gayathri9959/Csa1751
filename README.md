BFS(G, start)
    create empty set VISITED
    create empty queue Q

    add start to VISITED
    enqueue start into Q

    while Q is not empty do
        node ← dequeue from Q
        print node

        for each neighbour in G[node] do
            if neighbour not in VISITED then
                add neighbour to VISITED
                enqueue neighbour into Q
                
DFS(v):
    mark v visited
    print v
    for each adjacent u of v
        if u not visited
            DFS(u)
A_STAR(G, H, start, goal)
    create empty list OPEN
    create empty set CLOSED
    create map g_cost
    create map PARENT

add start to OPEN
g_cost[start] ← 0
PARENT[start] ← NULL

while OPEN is not empty do
    node ← element in OPEN with lowest (g_cost[node] + H[node])
    remove node from OPEN

    if node = goal then
        return path using PARENT

    add node to CLOSED

    for each neighbour, cost in G[node] do
        if neighbour not in CLOSED then
            new_cost ← g_cost[node] + cost
            if neighbour not in g_cost OR new_cost < g_cost[neighbour] then
                g_cost[neighbour] ← new_cost
                PARENT[neighbour] ← node
                add neighbour to OPEN
            
            

