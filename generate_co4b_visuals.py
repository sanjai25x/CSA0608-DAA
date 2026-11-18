"""
================================================================================
SIMATS ENGINEERING - DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
CO4 ASSIGNMENT 4B - VISUAL GRAPHICS & SCREENSHOT GENERATOR
Author: SANJAI S (Reg. No: 192511018)
================================================================================
Generates high-resolution visualization figures and charts for Tasks 1 to 6
and saves them directly into the respective Source_Code/Task_X/ directories.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = r"C:\Users\SANJAI\.gemini\antigravity\scratch\CSA0608-DAA\CO4_Assignment_4B"

def generate_task1_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_1", "task1_word_wrap_analysis.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: Line Width vs Penalty and Line Count
    widths = [20, 25, 30]
    penalties = [1100, 505, 819]
    line_counts = [8, 6, 5]
    
    color = '#1f77b4'
    ax1.set_title("Word Wrap DP: Line Width vs Layout Penalty", fontsize=12, fontweight='bold', pad=10)
    ax1.set_xlabel("Maximum Line Width (M)", fontsize=11)
    ax1.set_ylabel("Minimum Total Penalty (Cubic Slack)", color=color, fontsize=11)
    bars = ax1.bar([str(w) for w in widths], penalties, color=['#2b5c8f', '#2ca02c', '#d62728'], width=0.45, alpha=0.85)
    ax1.tick_params(axis='y', labelcolor=color)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 20, f"{int(yval)}", ha='center', va='bottom', fontweight='bold')
    
    ax1_twin = ax1.twinx()
    color2 = '#ff7f0e'
    ax1_twin.set_ylabel("Total Number of Lines", color=color2, fontsize=11)
    ax1_twin.plot([str(w) for w in widths], line_counts, color=color2, marker='o', linewidth=2.5, markersize=8)
    ax1_twin.tick_params(axis='y', labelcolor=color2)
    for i, txt in enumerate(line_counts):
        ax1_twin.annotate(f"{txt} lines", ([str(w) for w in widths][i], txt), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color=color2)
    ax1.grid(True, linestyle='--', alpha=0.4)

    # Right: Line-by-Line Slack Breakdown for Base Case (M=26)
    lines_base = ["L1: Buffering and layout", "L2: management require", "L3: rigorous dynamic", "L4: programming to balance", "L5: aesthetic readability"]
    slack_base = [6, 8, 10, 4, 5]
    penalty_base = [216, 512, 1000, 64, 0]
    
    y_pos = np.arange(len(lines_base))
    ax2.set_title("Base Word Wrap (M=26): Unused Spaces & Penalties", fontsize=12, fontweight='bold', pad=10)
    ax2.barh(y_pos, slack_base, color='#4575b4', alpha=0.8, label='Unused Spaces (Chars)')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(lines_base, fontsize=9)
    ax2.invert_yaxis()
    ax2.set_xlabel("Unused Space (Characters)", fontsize=11)
    
    for i, v in enumerate(slack_base):
        pen_str = f"Slack: {v} | Pen: {penalty_base[i]}" if i < 4 else f"Slack: {v} | Pen: 0 (Final)"
        ax2.text(v + 0.2, i, pen_str, va='center', fontsize=9, fontweight='bold')
    ax2.set_xlim(0, 14)
    ax2.grid(True, linestyle='--', alpha=0.4)
    ax2.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

def generate_task2_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_2", "task2_knapsack_comparison.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Normal Fractional Knapsack Packing
    items = ["PKG-A", "PKG-B", "PKG-C", "PKG-D", "PKG-E"]
    ratios = [6.0, 5.0, 4.0, 3.0, 2.0]
    fractions = [1.0, 1.0, 1.0, 0.0, 0.0]
    
    ax1.set_title("Task 2.1: Greedy Fractional Packing (Capacity = 60 kg)", fontsize=12, fontweight='bold', pad=10)
    bars1 = ax1.bar(items, ratios, color=['#1b9e77', '#1b9e77', '#1b9e77', '#d95f02', '#d95f02'], alpha=0.85)
    ax1.set_ylabel("Value-to-Weight Ratio ($/kg)", fontsize=11)
    ax1.set_xlabel("Freight Item Catalog (Sorted by Density)", fontsize=11)
    ax1.axhline(y=4.0, color='r', linestyle='--', label='Cutoff Ratio (Greedy Threshold = 4.0 $/kg)')
    
    for i, bar in enumerate(bars1):
        status = "LOADED (100%)" if fractions[i] == 1.0 else "EXCLUDED"
        ax1.text(bar.get_x() + bar.get_width()/2.0, bar.get_height() + 0.15, f"{status}\n({bar.get_height():.1f} $/kg)", ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax1.set_ylim(0, 7.5)
    ax1.grid(True, linestyle='--', alpha=0.4)
    ax1.legend(loc='upper right')

    # Right: Adversarial 0/1 Counterexample (Greedy Trap vs DP)
    strategies = ["Greedy 0/1 Heuristic\n(Committed Item-1 first)", "Dynamic Programming 0/1\n(Global Optimum)"]
    values = [160.0, 220.0]
    weights = [30.0, 50.0]
    
    ax2.set_title("Task 2.2: Breaking Greedy Intuition (Capacity = 50 kg)", fontsize=12, fontweight='bold', pad=10)
    bars2 = ax2.bar(strategies, values, color=['#e41a1c', '#377eb8'], width=0.5, alpha=0.85)
    ax2.set_ylabel("Total Value Achieved ($)", fontsize=11)
    
    for bar, wt in zip(bars2, weights):
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f"${yval:.0f}\n(Wt: {wt:.0f} / 50 kg)", ha='center', va='bottom', fontweight='bold', fontsize=10)
        
    ax2.annotate("Suboptimality Gap: $60 (27.3% Loss)\nGreedy trapped by high-ratio Item-1",
                 xy=(0, 160), xytext=(0.1, 190),
                 arrowprops=dict(facecolor='black', shrink=0.08, width=1.5, headwidth=8),
                 fontsize=9, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#ffeda0", ec="black"))
    ax2.set_ylim(0, 260)
    ax2.grid(True, linestyle='--', alpha=0.4)

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

def generate_task3_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_3", "task3_routing_analysis.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Stage A vs Stage B Distance Discrepancy
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    dijk_stage_b = [0.0, 2.0, 5.0, 3.0, 7.0, 7.0, 9.0, 12.0]
    bf_stage_b   = [0.0, 2.0, 5.0, 1.0, 7.0, 5.0, 7.0, 10.0]

    x = np.arange(len(nodes))
    width = 0.35
    
    ax1.set_title("Stage B: Dijkstra Failure vs Bellman-Ford (Edge E->D = -6.0)", fontsize=12, fontweight='bold', pad=10)
    rects1 = ax1.bar(x - width/2, dijk_stage_b, width, label='Dijkstra (Greedy Defect)', color='#d95f02', alpha=0.85)
    rects2 = ax1.bar(x + width/2, bf_stage_b, width, label='Bellman-Ford (Exact Optimum)', color='#2ca02c', alpha=0.85)
    
    ax1.set_xlabel("Target Vertices", fontsize=11)
    ax1.set_ylabel("Shortest Path Distance from Source A", fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(nodes)
    ax1.legend(loc='upper left')
    ax1.grid(True, linestyle='--', alpha=0.4)
    
    # Highlight nodes where Dijkstra failed
    for i in [3, 5, 6, 7]:
        ax1.annotate("FAIL", xy=(x[i] - width/2, dijk_stage_b[i]), xytext=(x[i] - width/2, dijk_stage_b[i] + 1.0),
                     ha='center', fontsize=8, fontweight='bold', color='red')

    # Right: Stage D Floyd All-Pairs Shortest Path Heatmap
    D_floyd = np.array([
        [0.0,  2.0,  5.0,  3.0,  7.0,  7.0,  9.0, 12.0],
        [np.nan, 0.0, np.nan, 1.0, np.nan, 5.0, 7.0, 10.0],
        [np.nan, np.nan, 0.0, np.nan, 2.0, 7.0, 9.0, 12.0],
        [np.nan, np.nan, np.nan, 0.0, np.nan, 4.0, 6.0, 9.0],
        [np.nan, np.nan, np.nan, np.nan, 0.0, 5.0, 7.0, 10.0],
        [np.nan, np.nan, np.nan, np.nan, np.nan, 0.0, 2.0, 5.0],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0, 3.0],
        [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0]
    ])
    
    cax = ax2.imshow(np.nan_to_num(D_floyd, nan=20.0), cmap='viridis_r', interpolation='nearest')
    ax2.set_title("Stage D: Floyd's All-Pairs Shortest Path Distance Matrix", fontsize=12, fontweight='bold', pad=10)
    ax2.set_xticks(np.arange(len(nodes)))
    ax2.set_yticks(np.arange(len(nodes)))
    ax2.set_xticklabels(nodes)
    ax2.set_yticklabels(nodes)
    
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            val = D_floyd[i, j]
            txt = f"{val:.0f}" if not np.isnan(val) else "INF"
            txt_color = "white" if not np.isnan(val) and val > 6 else "black"
            ax2.text(j, i, txt, ha="center", va="center", color=txt_color, fontsize=8, fontweight='bold')
    fig.colorbar(cax, ax=ax2, label="Shortest Distance (Units)")

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

def generate_task4_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_4", "task4_assembly_line_route.png")
    fig, ax = plt.subplots(figsize=(14, 6))

    # Assembly line schematic: Line 1 (y=2), Line 2 (y=1)
    stations = [1, 2, 3, 4, 5, 6]
    a1 = [7, 9, 3, 4, 8, 4]
    a2 = [8, 5, 6, 4, 5, 7]
    route = [1, 2, 1, 2, 2, 1] # Optimal route lines
    
    ax.set_title("Task 4: Dynamic Programming Assembly Line Scheduling Flow (Optimal Route)", fontsize=13, fontweight='bold', pad=15)
    
    # Plot stations
    for s in stations:
        # Line 1 station node
        col1 = '#2ca02c' if route[s - 1] == 1 else '#aec7e8'
        ax.scatter(s, 2, s=900, color=col1, edgecolors='black', linewidth=1.5, zorder=4)
        ax.text(s, 2, f"S1,{s}\n({a1[s-1]})", ha='center', va='center', fontweight='bold', fontsize=8, zorder=5)

        # Line 2 station node
        col2 = '#2ca02c' if route[s - 1] == 2 else '#aec7e8'
        ax.scatter(s, 1, s=900, color=col2, edgecolors='black', linewidth=1.5, zorder=4)
        ax.text(s, 1, f"S2,{s}\n({a2[s-1]})", ha='center', va='center', fontweight='bold', fontsize=8, zorder=5)
        
    # Draw horizontal sequential edges
    for s in range(1, 6):
        ax.plot([s, s+1], [2, 2], color='#cccccc', linestyle='--', linewidth=1.5, zorder=1)
        ax.plot([s, s+1], [1, 1], color='#cccccc', linestyle='--', linewidth=1.5, zorder=1)
        # Cross transfers
        ax.plot([s, s+1], [2, 1], color='#fed9a6', linestyle=':', linewidth=1.2, zorder=1)
        ax.plot([s, s+1], [1, 2], color='#fed9a6', linestyle=':', linewidth=1.2, zorder=1)

    # Highlight optimal route sequence
    route_coords = []
    # Entry
    ax.scatter(0, 2, s=400, color='#ff7f0e', edgecolors='black', zorder=4)
    ax.text(0, 2, "Entry 1\n(e1=2)", ha='center', va='center', fontsize=7, fontweight='bold')
    ax.scatter(0, 1, s=400, color='#aec7e8', edgecolors='black', zorder=4)
    ax.text(0, 1, "Entry 2\n(e2=4)", ha='center', va='center', fontsize=7, fontweight='bold')
    
    # Exit
    ax.scatter(7, 2, s=400, color='#ff7f0e', edgecolors='black', zorder=4)
    ax.text(7, 2, "Exit 1\n(x1=3)", ha='center', va='center', fontsize=7, fontweight='bold')
    ax.scatter(7, 1, s=400, color='#aec7e8', edgecolors='black', zorder=4)
    ax.text(7, 1, "Exit 2\n(x2=2)", ha='center', va='center', fontsize=7, fontweight='bold')
    
    # Trace optimal green path
    opt_pts = [(0, 2), (1, 1), (2, 2), (3, 1), (4, 2), (5, 2), (6, 1), (7, 2)]
    # wait: route is [1, 2, 1, 2, 2, 1] -> station 1 on line 1, station 2 on line 2, etc.
    opt_pts = [(0, 2)] + [(s, 2 if route[s-1]==1 else 1) for s in stations] + [(7, 2)]
    
    for i in range(len(opt_pts) - 1):
        x1_pt, y1_pt = opt_pts[i]
        x2_pt, y2_pt = opt_pts[i+1]
        ax.annotate('', xy=(x2_pt, y2_pt), xytext=(x1_pt, y1_pt),
                    arrowprops=dict(facecolor='#2ca02c', edgecolor='#1b7837', width=3, headwidth=10, shrink=0.15),
                    zorder=3)

    ax.set_xlim(-0.8, 7.8)
    ax.set_ylim(0.4, 2.6)
    ax.set_yticks([1, 2])
    ax.set_yticklabels(["Line 2", "Line 1"], fontsize=12, fontweight='bold')
    ax.set_xticks(range(8))
    ax.set_xticklabels(["Entry", "Station 1", "Station 2", "Station 3", "Station 4", "Station 5", "Station 6", "Exit"], fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.3)
    
    ax.text(3.5, 0.55, "Minimum Total Production Time = 38 Time Units\nGreen Path: Entry -> L1-S1 -> Transfer -> L2-S2 -> Transfer -> L1-S3 -> Transfer -> L2-S4 -> L2-S5 -> Transfer -> L1-S6 -> Exit",
            ha='center', fontsize=10, fontweight='bold', bbox=dict(boxstyle="round,pad=0.5", fc="#e5f5e0", ec="#31a354"))

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

def generate_task5_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_5", "task5_mst_comparison.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Algorithm Comparison on Multiple MST Graph
    algs = ["Kruskal's Algorithm", "Prim's Algorithm", "Borůvka's Algorithm"]
    costs = [19.0, 19.0, 19.0]
    edge_counts = [7, 7, 7]
    
    ax1.set_title("Task 5.2: MST Algorithm Cost Equivalence on Stressed Graph", fontsize=12, fontweight='bold', pad=10)
    bars = ax1.bar(algs, costs, color=['#386cb0', '#f0027f', '#7fc97f'], width=0.45, alpha=0.85)
    ax1.set_ylabel("Total Minimum Spanning Tree Weight", fontsize=11)
    ax1.set_ylim(0, 24)
    for bar in bars:
        ax1.text(bar.get_x() + bar.get_width()/2.0, bar.get_height() + 0.4, f"Cost = {bar.get_height():.1f}\n(7 Edges)", ha='center', va='bottom', fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.4)

    # Right: Edge Selection Discrepancy Breakdown
    krus_edges = ['(D,E)', '(B,C)', '(A,C)', '(F,G)', '(E,F)', '(G,H)', '(B,D)']
    prim_edges = ['(A,B)', '(A,C)', '(B,D)', '(D,E)', '(E,F)', '(F,G)', '(F,H)']
    
    ax2.set_title("Edge Set Divergence (Equal Cost = 19.0)", fontsize=12, fontweight='bold', pad=10)
    ax2.axis('off')
    
    table_data = [
        ["Attribute / Metric", "Kruskal's Algorithm", "Prim's Algorithm", "Borůvka's Algorithm"],
        ["Next Safe Edge", "Lightest globally non-cyclical", "Lightest cross-cut from tree", "Cheapest incident per component"],
        ["Tie-Breaker Used", "Global input edge list order", "Priority queue insertion order", "Component contraction ID"],
        ["Cycle A-B-C Choice", "(B-C: 2.0) and (A-C: 2.0)", "(A-B: 2.0) and (A-C: 2.0)", "(B-C: 2.0) and (A-C: 2.0)"],
        ["Node H Tie Choice", "(G-H: 4.0)", "(F-H: 4.0)", "(G-H: 4.0)"],
        ["Identical Edge Set?", "Baseline Match", "DIVERGENT (Valid)", "Matches Kruskal"],
        ["Total Weight", "19.0 (Exact)", "19.0 (Exact)", "19.0 (Exact)"]
    ]
    table = ax2.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.8)
    
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#2b5c8f')
            cell.set_text_props(color='white', fontweight='bold')
        elif row in [3, 4, 5]:
            cell.set_facecolor('#fff7bc')
        else:
            cell.set_facecolor('#f7f7f7' if row % 2 == 0 else '#ffffff')

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

def generate_task6_visual():
    path = os.path.join(BASE_DIR, "Source_Code", "Task_6", "task6_tsp_state_growth.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: State Space Growth Curve (N = 4 to 10)
    n_vals = [4, 5, 6, 7, 8, 9, 10]
    dp_states = [19, 57, 171, 493, 1359, 3601, 9235]
    brute_force_perms = [6, 24, 120, 720, 5040, 40320, 362880]

    ax1.set_title("Task 6.5: TSP State-Space Growth (Held-Karp vs Brute Force)", fontsize=12, fontweight='bold', pad=10)
    ax1.plot(n_vals, dp_states, marker='s', color='#2ca02c', linewidth=2.5, label='Held-Karp DP States: O(N^2 * 2^N)')
    ax1.plot(n_vals, brute_force_perms, marker='o', color='#d62728', linestyle='--', linewidth=2.5, label='Exhaustive Brute Force: (N-1)!')
    ax1.set_yscale('log')
    ax1.set_xlabel("Number of Locations (N)", fontsize=11)
    ax1.set_ylabel("Evaluations / States (Log Scale)", fontsize=11)
    ax1.grid(True, which="both", ls="--", alpha=0.4)
    ax1.legend(loc='upper left')
    
    for i, (nv, sv) in enumerate(zip(n_vals, dp_states)):
        if nv in [4, 7, 10]:
            ax1.annotate(f"{sv:,}", (nv, sv), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='#2ca02c')

    # Right: Optimal 7-Node Last-Mile Delivery Route
    # 2D coordinates for visual route map
    coords = {
        "Central-Hub": (0, 0),
        "Loc-A": (2, 4),
        "Loc-B": (5, 5),
        "Loc-C": (8, 2),
        "Loc-D": (3, -3),
        "Loc-E": (6, -1),
        "Loc-F": (9, -4)
    }
    
    tour = ["Central-Hub", "Loc-D", "Loc-E", "Loc-F", "Loc-C", "Loc-B", "Loc-A", "Central-Hub"]
    
    ax2.set_title("Task 6.3: Optimal Last-Mile Tour (N=7 Nodes, Cost=75.0 km)", fontsize=12, fontweight='bold', pad=10)
    
    # Plot edges
    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        ax2.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor='#1f77b4', edgecolor='#08519c', width=2.5, headwidth=9, shrink=0.1),
                    zorder=2)
                    
    # Plot nodes
    for name, (x, y) in coords.items():
        is_hub = (name == "Central-Hub")
        col = '#d62728' if is_hub else '#2ca02c'
        ax2.scatter(x, y, s=500 if is_hub else 350, color=col, edgecolors='black', linewidth=1.5, zorder=3)
        ax2.text(x, y + 0.6, name, ha='center', va='bottom', fontweight='bold', fontsize=9)

    ax2.set_xlim(-1.5, 10.5)
    ax2.set_ylim(-5.5, 6.5)
    ax2.grid(True, linestyle='--', alpha=0.4)
    ax2.set_xlabel("East-West Coordinate (km)", fontsize=11)
    ax2.set_ylabel("North-South Coordinate (km)", fontsize=11)

    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
    print(f"Generated: {path}")

if __name__ == "__main__":
    generate_task1_visual()
    generate_task2_visual()
    generate_task3_visual()
    generate_task4_visual()
    generate_task5_visual()
    generate_task6_visual()
    print("All CO4 Assignment 4B visuals generated successfully!")
