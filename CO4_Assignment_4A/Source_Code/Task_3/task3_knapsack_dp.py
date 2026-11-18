"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
TASK 3: DYNAMIC PROGRAMMING - 0/1 KNAPSACK
STUDENT: SANJAI S (192511018)
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

class Item:
    def __init__(self, item_id, weight, value):
        self.item_id = item_id
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item({self.item_id}, w={self.weight}, v={self.value})"


def knapsack_01_dp(items, capacity):
    """
    0/1 Knapsack Dynamic Programming with Backtracking Reconstruction.
    Conforms to SIMATS Engineering Handbook for Algorithmic Pseudocode.
    
    State Definition:
    DP[i][w] = Maximum value achievable using a subset of items {1..i}
               under weight constraint w.
               
    Recurrence:
    DP[i][w] = DP[i-1][w]                                    if w_i > w
    DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)       if w_i <= w
    
    Time Complexity: Theta(n * W)
    Space Complexity: Theta(n * W)
    """
    n = len(items)
    # DP Table of dimensions (n + 1) x (capacity + 1)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Bottom-Up Dynamic Programming Formulation
    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            if item.weight > w:
                DP[i][w] = DP[i - 1][w]
            else:
                exclude_val = DP[i - 1][w]
                include_val = DP[i - 1][w - item.weight] + item.value
                DP[i][w] = max(exclude_val, include_val)
                
    optimal_value = DP[n][capacity]
    
    # Backtracking Reconstruction of Selected Items
    selected_items = []
    curr_w = capacity
    for i in range(n, 0, -1):
        item = items[i - 1]
        # If value is different from cell above, item i was included!
        if DP[i][curr_w] != DP[i - 1][curr_w]:
            selected_items.append(item)
            curr_w -= item.weight
            
    selected_items.reverse()
    return optimal_value, selected_items, DP


def run_task3_demo():
    print("=" * 80)
    print("TASK 3: DYNAMIC PROGRAMMING - 0/1 KNAPSACK (DESK-CHECK)")
    print("=" * 80)
    
    test_items = [
        Item("P", weight=2, value=12),
        Item("Q", weight=3, value=20),
        Item("R", weight=4, value=25),
        Item("S", weight=5, value=30)
    ]
    capacity = 7
    
    print(f"Vehicle Capacity: {capacity} kg")
    print("Cargo Items:")
    for it in test_items:
        print(f"  Item {it.item_id}: Weight = {it.weight} kg, Value = ${it.value}")
        
    opt_val, selected, dp_table = knapsack_01_dp(test_items, capacity)
    
    print("\n--- Complete 0/1 Knapsack DP State Table (DP[i][w]) ---")
    headers = ["Item / w"] + [f"w={w}" for w in range(capacity + 1)]
    header_line = " | ".join(f"{h:>8}" for h in headers)
    print(header_line)
    print("-" * len(header_line))
    
    labels = ["Base (0)"] + [f"{it.item_id}(w={it.weight},v={it.value})" for it in test_items]
    for i in range(len(dp_table)):
        row_str = f"{labels[i]:>8} | " + " | ".join(f"{dp_table[i][w]:>8}" for w in range(capacity + 1))
        print(row_str)
        
    print("-" * len(header_line))
    print(f"\nMaximum Obtainable Value : ${opt_val}")
    print(f"Reconstructed Selected Items : {[it.item_id for it in selected]}")
    total_w = sum(it.weight for it in selected)
    total_v = sum(it.value for it in selected)
    print(f"Selected Items Weight Sum   : {total_w} kg (<= {capacity} kg)")
    print(f"Selected Items Value Sum    : ${total_v}")
    
    print("\n[SUCCESS] Task 3 Verification Complete.")
    return opt_val, selected, dp_table

if __name__ == "__main__":
    run_task3_demo()
