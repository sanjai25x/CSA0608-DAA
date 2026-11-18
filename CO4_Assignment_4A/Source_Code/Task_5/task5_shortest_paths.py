"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 5: SHORTEST PATHS - DIJKSTRA, BELLMAN-FORD, AND FLOYD-WARSHALL
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

def dijkstra(vertices, edges, source):
    """
    Greedy Single-Source Shortest Path (Dijkstra)
    Assumes all edge weights are non-negative.
    Time Complexity: O(V^2) or O((V + E) log V) with priority queue.
    """
    dist = {v: float('inf') for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0
    unvisited = set(vertices)
    trace = []

    step = 1
    while unvisited:
        # Greedy Choice: Select unvisited vertex with minimum tentative distance
        u = min(unvisited, key=lambda v: dist[v])
        if dist[u] == float('inf'):
            break  # Remaining vertices unreachable
            
        unvisited.remove(u)
        
        # Edge Relaxation for adjacent neighbors
        relaxations = []
        for (src, dst, weight) in edges:
            if src == u and dst in unvisited:
                if dist[u] + weight < dist[dst]:
                    old_d = dist[dst]
                    dist[dst] = dist[u] + weight
                    pred[dst] = u
                    relaxations.append(f"Relax {u}->{dst}({weight}): dist[{dst}] updated {old_d}->{dist[dst]}")
                    
        trace.append({
            "step": step,
            "selected_u": u,
            "dist_u": dist[u],
            "relaxations": relaxations,
            "dist_snapshot": dict(dist)
        })
        step += 1

    return dist, pred, trace


def bellman_ford(vertices, edges, source):
    """
    Dynamic Programming Single-Source Shortest Path (Bellman-Ford)
    Supports negative-weight edges and detects negative cycles.
    Time Complexity: O(V * E)
    """
    dist = {v: float('inf') for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0
    
    # Relax all edges |V| - 1 times
    num_v = len(vertices)
    for i in range(1, num_v):
        for (u, v, w) in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                
    # Check for negative-weight cycles (|V|-th pass)
    has_negative_cycle = False
    for (u, v, w) in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break
            
    return dist, pred, has_negative_cycle


def floyd_warshall(vertices, edges):
    """
    All-Pairs Shortest Path (Floyd-Warshall)
    State Transition: D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j])
    Time Complexity: Theta(V^3)
    """
    idx_map = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    
    # Initialize Distance Matrix
    D = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
        
    for (u, v, w) in edges:
        D[idx_map[u]][idx_map[v]] = w
        
    # Floyd's Triple Loop over intermediate vertex k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    
    return D, idx_map


def run_task5_demo():
    print("=" * 80)
    print("TASK 5: SHORTEST PATHS - DIJKSTRA, BELLMAN-FORD, AND FLOYD-WARSHALL")
    print("=" * 80)

    # Given Graph in Problem Statement
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 7),
        ('B', 'C', 2),
        ('B', 'D', 6),
        ('C', 'D', 1),
        ('D', 'E', 3),
        ('C', 'E', 8)
    ]
    source = 'A'

    print("Given Directed Graph:")
    for src, dst, w in edges:
        print(f"  {src} -> {dst} (Weight: {w})")

    # 1. Dijkstra Execution
    print(f"\n--- 1. Dijkstra's Algorithm from Source '{source}' ---")
    d_dist, d_pred, d_trace = dijkstra(vertices, edges, source)
    for t in d_trace:
        print(f"Step {t['step']}: Selected vertex '{t['selected_u']}' (dist={t['dist_u']})")
        for r in t['relaxations']:
            print(f"   -> {r}")
        print(f"   Current Distances: {t['dist_snapshot']}")

    print("\nFinal Dijkstra Distances from Source A:")
    for v in vertices:
        path = []
        curr = v
        while curr:
            path.append(curr)
            curr = d_pred[curr]
        path.reverse()
        print(f"  Destination {v}: Distance = {d_dist[v]}, Path = {' -> '.join(path)}")

    # 2. Bellman-Ford Execution
    print(f"\n--- 2. Bellman-Ford Algorithm from Source '{source}' ---")
    bf_dist, bf_pred, bf_neg_cycle = bellman_ford(vertices, edges, source)
    print(f"Bellman-Ford Distances     : {bf_dist}")
    print(f"Reachable Negative Cycle?  : {bf_neg_cycle}")

    # 3. Floyd-Warshall Execution
    print(f"\n--- 3. Floyd-Warshall All-Pairs Shortest Path Matrix ---")
    D_mat, idx_map = floyd_warshall(vertices, edges)
    header_str = " | ".join(f"{v:>6}" for v in vertices)
    print(f"From / To | {header_str}")
    print("-" * 50)
    for u in vertices:
        row_vals = [str(D_mat[idx_map[u]][idx_map[v]]) if D_mat[idx_map[u]][idx_map[v]] != float('inf') else "inf" for v in vertices]
        row_str = " | ".join(f"{val:>6}" for val in row_vals)
        print(f"{u:>9} | {row_str}")

    print("\n[SUCCESS] Task 5 Verification Complete.")
    return d_dist, bf_dist, D_mat

if __name__ == "__main__":
    run_task5_demo()
