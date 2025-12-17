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

