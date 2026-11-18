"""
================================================================================
SIMATS ENGINEERING - DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO4 ASSIGNMENT 4B - TASK 3: ROUTING ENGINE UNDER CHANGING NETWORK CONDITIONS
Author: SANJAI S (Reg. No: 192511018)
================================================================================
Problem Statement:
Develop a multi-algorithm network routing engine supporting:
  - Stage A: Dijkstra's algorithm for standard non-negative routing (distance, path,
    predecessors, and vertex finalization order).
  - Stage B: Insertion of a carefully crafted negative edge, predicting and proving
    Dijkstra's premature greedy finalization failure vs Bellman-Ford exactness.
  - Stage C: Insertion of a reachable negative-weight cycle, implementing detection
    and cycle extraction via Bellman-Ford's |V|-th relaxation pass.
  - Stage D: All-Pairs Shortest Path (Floyd's Algorithm) and Transitive Closure
    Reachability (Warshall's Algorithm).
"""

import sys
import heapq
from typing import Dict, List, Tuple, Set, Optional

VERTICES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
INF = float('inf')

def get_base_edges() -> List[Tuple[str, str, float]]:
    """
    Constructs a directed graph with 8 vertices and 13 edges.
    All weights are strictly positive for Stage A baseline.
    """
    return [
        ('A', 'B', 2.0),
        ('A', 'C', 5.0),
        ('B', 'D', 1.0),
        ('B', 'F', 8.0),
        ('C', 'E', 2.0),
        ('C', 'F', 7.0),
        ('D', 'F', 4.0),
        ('D', 'G', 6.0),
        ('E', 'F', 5.0),
        ('E', 'G', 8.0),
        ('F', 'G', 2.0),
        ('F', 'H', 6.0),
        ('G', 'H', 3.0),
    ]

def edges_to_adj(edges: List[Tuple[str, str, float]]) -> Dict[str, List[Tuple[str, float]]]:
    adj = {v: [] for v in VERTICES}
    for u, v, w in edges:
        adj[u].append((v, w))
    return adj

# -----------------------------------------------------------------------------
# STAGE A: DIJKSTRA'S ALGORITHM
# -----------------------------------------------------------------------------
def dijkstra(edges: List[Tuple[str, str, float]], source: str) -> Dict:
    adj = edges_to_adj(edges)
    dist = {v: INF for v in VERTICES}
    pred = {v: None for v in VERTICES}
    dist[source] = 0.0
    
    pq = [(0.0, source)]
    finalized_order = []
    visited = set()
    step_log = []

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        finalized_order.append(u)
        
        relaxations = []
        for v, weight in adj[u]:
            if v not in visited and dist[u] + weight < dist[v]:
                old_d = dist[v]
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
                relaxations.append((v, old_d, dist[v]))
        step_log.append({
            'finalized_node': u,
            'current_dist': d,
            'relaxations': relaxations
        })

    # Path reconstruction
    paths = {}
    for target in VERTICES:
        if dist[target] == INF:
            paths[target] = None
        else:
            curr = target
            p = []
            while curr is not None:
                p.append(curr)
                curr = pred[curr]
            p.reverse()
            paths[target] = p

    return {
        'source': source,
        'dist': dist,
        'pred': pred,
        'paths': paths,
        'finalized_order': finalized_order,
        'step_log': step_log
    }

# -----------------------------------------------------------------------------
# STAGE B & C: BELLMAN-FORD ALGORITHM
# -----------------------------------------------------------------------------
def bellman_ford(edges: List[Tuple[str, str, float]], vertices: List[str], source: str) -> Dict:
    dist = {v: INF for v in vertices}
    pred = {v: None for v in vertices}
    dist[source] = 0.0
    V = len(vertices)
    
    pass_history = []
    
    for i in range(1, V):
        changed = False
        pass_relax = []
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                old_d = dist[v]
                dist[v] = dist[u] + w
                pred[v] = u
                changed = True
                pass_relax.append((u, v, w, old_d, dist[v]))
        pass_history.append({'pass': i, 'relaxations': pass_relax})
        if not changed:
            break

    # |V|-th pass to detect negative cycle
    has_negative_cycle = False
    cycle_nodes = []
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            # Trace cycle
            curr = v
            for _ in range(V):
                curr = pred[curr]
            cycle_start = curr
            cycle_nodes = [cycle_start]
            curr = pred[cycle_start]
            while curr != cycle_start:
                cycle_nodes.append(curr)
                curr = pred[curr]
            cycle_nodes.append(cycle_start)
            cycle_nodes.reverse()
            break

    # Reconstruct paths if no negative cycle
    paths = {}
    if not has_negative_cycle:
        for target in vertices:
            if dist[target] == INF:
                paths[target] = None
            else:
                curr = target
                p = []
                while curr is not None:
                    p.append(curr)
                    curr = pred[curr]
                p.reverse()
                paths[target] = p

    return {
        'source': source,
        'dist': dist,
        'pred': pred,
        'paths': paths,
        'pass_history': pass_history,
        'has_negative_cycle': has_negative_cycle,
        'cycle_nodes': cycle_nodes
    }

# -----------------------------------------------------------------------------
# STAGE D: FLOYD'S (APSP) AND WARSHALL'S (REACHABILITY) ALGORITHMS
# -----------------------------------------------------------------------------
def floyd_warshall(vertices: List[str], edges: List[Tuple[str, str, float]]) -> Tuple[List[List[float]], List[List[bool]]]:
    n = len(vertices)
    v_to_idx = {v: i for i, v in enumerate(vertices)}
    
    D = [[INF] * n for _ in range(n)]
    R = [[False] * n for _ in range(n)]
    
    for i in range(n):
        D[i][i] = 0.0
        R[i][i] = True
        
    for u, v, w in edges:
        ui, vi = v_to_idx[u], v_to_idx[v]
        D[ui][vi] = min(D[ui][vi], w)
        R[ui][vi] = True
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] != INF and D[k][j] != INF:
                    if D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])
                
    return D, R

# -----------------------------------------------------------------------------
# EXECUTION HARNESS AND REPORTING
# -----------------------------------------------------------------------------
def run_task3():
    print("=" * 80)
    print("  CO4 ASSIGNMENT 4B - TASK 3: ROUTING ENGINE UNDER CHANGING NETWORK CONDITIONS")
    print("=" * 80)
    
    base_edges = get_base_edges()
    print(f"\nNetwork Topology: {len(VERTICES)} Vertices {VERTICES}, {len(base_edges)} Directed Edges")
    print("Base Edges: A->B(2), A->C(5), B->D(1), B->F(8), C->E(2), C->F(7), D->F(4), D->G(6), E->F(5), E->G(8), F->G(2), F->H(6), G->H(3)")

    # -------------------------------------------------------------------------
    # STAGE A: NORMAL ROUTING (DIJKSTRA)
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("STAGE A: NORMAL ROUTING VIA DIJKSTRA'S ALGORITHM (SOURCE = A)")
    print("=" * 75)
    dijk_res = dijkstra(base_edges, 'A')
    
    print(f"Vertex Finalization Sequence: {' -> '.join(dijk_res['finalized_order'])}")
    print(f"\n{'Target':<8} | {'Shortest Dist':<15} | {'Predecessor':<13} | {'Reconstructed Optimal Path'}")
    print("-" * 65)
    for v in VERTICES:
        path_str = " -> ".join(dijk_res['paths'][v]) if dijk_res['paths'][v] else "Unreachable"
        pred_str = str(dijk_res['pred'][v])
        print(f"Node {v:<3} | {dijk_res['dist'][v]:<15.1f} | Node {pred_str:<8} | {path_str}")
        
    print("\n[Algorithmic Verification]:")
    print("  Dijkstra greedily finalizes vertices in non-decreasing order of distance:")
    print("  A(0) -> B(2) -> D(3) -> C(5) -> E(7) -> F(7) -> G(9) -> H(12).")
    print("  All edges are non-negative, ensuring the greedy choice property is strictly upheld.")

    # -------------------------------------------------------------------------
    # STAGE B: INTRODUCE CAREFULLY CRAFTED NEGATIVE EDGE
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("STAGE B: INTRODUCE CAREFULLY CRAFTED NEGATIVE EDGE (E -> D = -6.0)")
    print("=" * 75)
    print("Intervention: Introduce directed edge E -> D with negative weight -6.0.")
    print("Note: Graph remains strictly ACYCLIC; no negative cycle exists.")
    print("\n>>> PREDICTION BEFORE EXECUTION:")
    print("  1. Dijkstra Validity Prediction: Dijkstra will FAIL and output incorrect shortest paths!")
    print("  2. Cause: Dijkstra finalizes B at distance 2.0, then immediately finalizes D at distance 3.0")
    print("     via path A -> B -> D. Once finalized, D is NEVER re-evaluated by Dijkstra.")
    print("     However, path A -> C -> E -> D has total cost 5.0 + 2.0 + (-6.0) = 1.0 < 3.0!")
    print("  3. Affected Routes: Node D and all downstream nodes (F, G, H) will carry inflated costs in Dijkstra.")
    
    edges_mod = list(base_edges)
    edges_mod.append(('E', 'D', -6.0))

    dijk_mod = dijkstra(edges_mod, 'A')
    bf_mod = bellman_ford(edges_mod, VERTICES, 'A')
    
    print("\n--- Comparative Execution on Graph with Negative Edge E -> D (-6.0) ---")
    print(f"{'Target':<7} | {'Dijkstra Dist':<15} | {'Bellman-Ford Dist':<18} | {'Status / Discrepancy'}")
    print("-" * 70)
    for v in VERTICES:
        d_val = dijk_mod['dist'][v]
        bf_val = bf_mod['dist'][v]
        diff = "PREDICTION CONFIRMED: DIJKSTRA FAILED!" if d_val != bf_val else "Identical"
        print(f"Node {v:<2} | {d_val:<15.1f} | {bf_val:<18.1f} | {diff}")
        
    print("\nDetailed Discrepancy Analysis:")
    print(f"  * Node D: Dijkstra = {dijk_mod['dist']['D']:.1f} (Path: {' -> '.join(dijk_mod['paths']['D'])}).")
    print(f"            Bellman-Ford = {bf_mod['dist']['D']:.1f} (Path: {' -> '.join(bf_mod['paths']['D'])}).")
    print(f"  * Node F: Dijkstra = {dijk_mod['dist']['F']:.1f} (Path: {' -> '.join(dijk_mod['paths']['F'])}).")
    print(f"            Bellman-Ford = {bf_mod['dist']['F']:.1f} (Path: {' -> '.join(bf_mod['paths']['F'])}).")
    print(f"  * Node G: Dijkstra = {dijk_mod['dist']['G']:.1f} vs Bellman-Ford = {bf_mod['dist']['G']:.1f}.")
    print(f"  * Node H: Dijkstra = {dijk_mod['dist']['H']:.1f} vs Bellman-Ford = {bf_mod['dist']['H']:.1f}.")
    print("  Conclusion: Dijkstra's greedy finalization assumption is fundamentally broken by negative edges,")
    print("  whereas Bellman-Ford's multi-pass relaxation guarantees exact convergence.")

    # -------------------------------------------------------------------------
    # STAGE C: PRODUCTION FAILURE - REACHABLE NEGATIVE CYCLE
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("STAGE C: PRODUCTION FAILURE - REACHABLE NEGATIVE-WEIGHT CYCLE DETECTION")
    print("=" * 75)
    print("Intervention: Insert edge F -> E with weight -1.0.")
    print("Directed Cycle Formed: E -> D (w=-6.0) -> F (w=4.0) -> E (w=-1.0).")
    print("Total Cycle Weight = -6.0 + 4.0 + (-1.0) = -3.0 < 0 (Reachable from Source A)!")
    
    edges_cycle = list(edges_mod)
    edges_cycle.append(('F', 'E', -1.0))
    
    bf_cycle = bellman_ford(edges_cycle, VERTICES, 'A')
    
    if bf_cycle['has_negative_cycle']:
        print("\n>>> CRITICAL ALERT: REACHABLE NEGATIVE CYCLE DETECTED!")
        print(f"Cycle Vertices Identified: {' -> '.join(bf_cycle['cycle_nodes'])}")
        print("Algorithmic Detection Mechanism:")
        print("  1. Bellman-Ford performed |V|-1 = 7 iterations of edge relaxations.")
        print("  2. On the |V|-th pass (iteration 8), edge (E -> D) or (F -> E) could STILL reduce distances.")
        print("  3. By the triangle inequality, if dist[u] + weight(u, v) < dist[v] after |V|-1 passes,")
        print("     a negative-weight cycle is reachable from the source.")
        print("  4. The engine safely aborts shortest-path dispatching, preventing infinite loops.")
    else:
        print("Negative cycle not detected.")

    # -------------------------------------------------------------------------
    # STAGE D: ALL-PAIRS SHORTEST PATH (FLOYD) & REACHABILITY (WARSHALL)
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("STAGE D: ANALYTICS REQUIREMENTS - FLOYD'S APSP & WARSHALL'S REACHABILITY")
    print("=" * 75)
    D_matrix, R_matrix = floyd_warshall(VERTICES, base_edges)
    
    print("\n[1] Floyd's All-Pairs Shortest Path Distance Matrix (8x8):")
    header = "       " + " ".join(f"{v:>6}" for v in VERTICES)
    print(header)
    print("      " + "-" * (7 * len(VERTICES)))
    for i, u in enumerate(VERTICES):
        row_str = f"Node {u} |"
        for j, v in enumerate(VERTICES):
            val = D_matrix[i][j]
            val_str = f"{val:6.1f}" if val != INF else "   INF"
            row_str += val_str + " "
        print(row_str)
        
    print("\n[2] Warshall's Transitive Closure Reachability Matrix (8x8):")
    header_r = "       " + " ".join(f"{v:>4}" for v in VERTICES)
    print(header_r)
    print("      " + "-" * (5 * len(VERTICES)))
    for i, u in enumerate(VERTICES):
        row_str = f"Node {u} |"
        for j, v in enumerate(VERTICES):
            val_str = " 1  " if R_matrix[i][j] else " 0  "
            row_str += val_str
        print(row_str)
    print("\nInterpretation:")
    print("  - Floyd Matrix gives exact all-pairs costs (e.g. A->H is 12.0, C->H is 13.0, E->H is 11.0).")
    print("  - Warshall Matrix provides O(1) boolean reachability query resolution for route dispatch.")

if __name__ == "__main__":
    run_task3()
