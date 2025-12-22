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
ALPHABETA(depth, node, maximizingPlayer, values, alpha, beta)

if depth = maximumDepth then
    return values[node]

if maximizingPlayer then
    best ← −∞
    for each child of node do
        val ← ALPHABETA(depth+1, child, FALSE, values, alpha, beta)
        best ← max(best, val)
        alpha ← max(alpha, best)
        if beta ≤ alpha then
            break        // Beta cut-off
    return best

else
    best ← +∞
    for each child of node do
        val ← ALPHABETA(depth+1, child, TRUE, values, alpha, beta)
        best ← min(best, val)
        beta ← min(beta, best)
        if beta ≤ alpha then
            break        // Alpha cut-off
    return best
WATER_JUG(jug1, jug2, target)
    create empty set VISITED
    create empty queue Q

enqueue (0, 0, path) into Q

while Q is not empty do
    (a, b, path) ← dequeue from Q

    if (a, b) is in VISITED then
        continue
    add (a, b) to VISITED

    if a = target OR b = target then
        return path

    enqueue (a, jug2) into Q          // fill jug2
    enqueue (jug1, b) into Q          // fill jug1
    enqueue (0, b) into Q             // empty jug1
    enqueue (a, 0) into Q             // empty jug2
    pour ← min(a, jug2 − b)
    enqueue (a − pour, b + pour)      // jug1 → jug2
    pour ← min(jug1 − a, b)
    enqueue (a + pour, b − pour)      // jug2 → jug1

return NO SOLUTION
DECISION_TREE(outlook, humidity)

if outlook = "Sunny" then
    if humidity = "High" then
        return "No"
    else
        return "Yes"

else if outlook = "Overcast" then
    return "Yes"

else if outlook = "Rain" then
    return "Yes"
            
            

