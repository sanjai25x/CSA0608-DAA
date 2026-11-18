"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
CO4 ASSIGNMENT 4B: MASTER CAPSTONE REPORT GENERATOR (DOCX, PDF, MD)
STUDENT: SANJAI S (192511018)
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
SIMATS ENGINEERING, SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES
========================================================================================
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = r"C:\Users\SANJAI\.gemini\antigravity\scratch\CSA0608-DAA\CO4_Assignment_4B"
REPORT_DIR = os.path.join(BASE_DIR, "Report")
SRC_DIR = os.path.join(BASE_DIR, "Source_Code")
os.makedirs(REPORT_DIR, exist_ok=True)

# Helper styling for python-docx
def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def add_header(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(6)
    for run in h.runs:
        run.font.name = 'Arial'
        if level == 1:
            run.font.size = Pt(15)
            run.font.bold = True
            run.font.color.rgb = RGBColor(16, 44, 87)
        elif level == 2:
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 80, 150)
        elif level == 3:
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(50, 50, 50)
    return h

def add_body_p(doc, text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(20, 20, 20)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.italic = italic
    r.font.color.rgb = RGBColor(40, 40, 40)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F4F6F9")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 30, 30)

def add_styled_table(doc, headers, data, col_widths=None):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Header
    for c_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h_text)
        run.font.name = 'Arial'
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
    # Rows
    for r_idx, row in enumerate(data):
        bg = "FFFFFF" if r_idx % 2 == 0 else "F2F5F9"
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(str(val))
            run.font.name = 'Arial'
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(30, 30, 30)
    if col_widths:
        for row in tbl.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width

print("Starting DOCX Generation...")
doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# -----------------------------------------------------------------------------
# DOCX TITLE / COVER PAGE
# -----------------------------------------------------------------------------
p_title_pre = doc.add_paragraph()
p_title_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_title_pre.add_run("SIMATS ENGINEERING\nSAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES\n")
r.font.name = 'Arial'
r.font.size = Pt(13)
r.font.bold = True
r.font.color.rgb = RGBColor(16, 44, 87)

r_dept = p_title_pre.add_run("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\n")
r_dept.font.name = 'Arial'
r_dept.font.size = Pt(11)
r_dept.font.bold = True
r_dept.font.color.rgb = RGBColor(60, 60, 60)

p_rule = doc.add_paragraph()
p_rule.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_line = p_rule.add_run("―" * 55)
r_line.font.color.rgb = RGBColor(180, 180, 180)

p_main = doc.add_paragraph()
p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_main.paragraph_format.space_before = Pt(18)
p_main.paragraph_format.space_after = Pt(8)
r_crs = p_main.add_run("CSA0608 – DESIGN AND ANALYSIS OF ALGORITHMS\n")
r_crs.font.name = 'Arial'
r_crs.font.size = Pt(14)
r_crs.font.bold = True
r_crs.font.color.rgb = RGBColor(16, 44, 87)

r_sub = p_main.add_run("COURSE OUTCOME 4 – ASSIGNMENT 4B\n")
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(16)
r_sub.font.bold = True
r_sub.font.color.rgb = RGBColor(180, 40, 40)

r_desc = p_main.add_run("PART II: ALGORITHM ENGINEERING — IMPLEMENT, TEST, DEBUG & OPTIMISE\n"
                        "Dynamic Programming & Greedy Strategies for Complex Engineering Systems")
r_desc.font.name = 'Arial'
r_desc.font.size = Pt(11)
r_desc.font.italic = True
r_desc.font.color.rgb = RGBColor(80, 80, 80)

p_box = doc.add_table(rows=1, cols=1)
p_box.alignment = WD_TABLE_ALIGNMENT.CENTER
c_box = p_box.cell(0, 0)
set_cell_background(c_box, "EBF1F5")
set_cell_margins(c_box, top=140, bottom=140, left=200, right=200)
p_meta = c_box.paragraphs[0]
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_meta.paragraph_format.line_spacing = 1.3
r_meta = p_meta.add_run(
    "CANDIDATE DETAILS\n"
    "Student Name: SANJAI S\n"
    "Register Number: 192511018\n"
    "Department: Computer Science and Engineering\n"
    "Academic Year: 2026–2027 | Total Marks: 50 | Nature: Individual Submission"
)
r_meta.font.name = 'Arial'
r_meta.font.size = Pt(10)
r_meta.font.bold = True
r_meta.font.color.rgb = RGBColor(20, 40, 70)

doc.add_page_break()

# -----------------------------------------------------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------------------------------------------------
add_header(doc, "EXECUTIVE SUMMARY", level=1)
add_body_p(doc, 
    "This laboratory report presents the complete algorithm engineering, empirical validation, "
    "adversarial debugging, and architectural trade-off analysis for CO4 Assignment 4B (Part II: Algorithm Engineering) "
    "under course CSA0608 – Design and Analysis of Algorithms. Building directly upon the design specifications "
    "formulated in Part I, this work rigorously tests six distinct real-world optimization prototypes across Dynamic "
    "Programming (DP) and Greedy paradigms:")
add_body_p(doc, "1. Task 1 – Word Wrap Document Layout Engine: Dynamic programming model with cubic penalty function, intermediate prefix state exposure, multi-width regression analysis, and boundary guards.")
add_body_p(doc, "2. Task 2 – Greedy vs Dynamic Programming Knapsack: Comparative evaluation of Fractional Knapsack (Greedy O(n log n)) against 0/1 Knapsack (DP O(nW)), complete with a student-designed adversarial counterexample exposing the greedy commitment trap and real-time FPTAS trade-offs.")
add_body_p(doc, "3. Task 3 – Network Routing Engine Under Adverse Conditions: Multi-protocol routing engine combining Dijkstra's SSSP, Bellman-Ford negative edge/cycle detection, Floyd's All-Pairs Shortest Path, and Warshall's Transitive Closure reachability.")
add_body_p(doc, "4. Task 4 – Smart Manufacturing Assembly Line Scheduling: Linear-time DP optimization engine for twin parallel production lines, decision exposure tables, transfer cost spikes, machine slowdown disruptions, and 3-line generalization.")
add_body_p(doc, "5. Task 5 – Three Greedy Engineers, One Network (MST Triad): Comparative engineering implementation of Kruskal's, Prim's, and Boruvka's algorithms, including non-unique weight stress testing demonstrating divergent valid MSTs and cloud deployment selections.")
add_body_p(doc, "6. Task 6 – Last-Mile Delivery Route Optimisation (Held-Karp TSP): Bitmask dynamic programming formulation for distribution logistics, brute-force validation (N=5), empirical state-space combinatorial explosion benchmark (N=4..10), 200-node approximation analysis, and technical reflection.")

# -----------------------------------------------------------------------------
# TASK 1
# -----------------------------------------------------------------------------
add_header(doc, "TASK 1: BUILD AND VALIDATE A DYNAMIC PROGRAMMING SOLUTION", level=1)
add_header(doc, "Word Wrap as a Document-Layout Engine (8 Marks)", level=2)

add_body_p(doc, 
    "A document-processing engine must wrap a stream of words into lines of maximum width M such that aesthetic readability "
    "is maximized. Unused spaces at the end of interior lines create an unsightly visual gap penalized as S^3 = (M - used_length)^3. "
    "The final line carries zero penalty as paragraph terminators naturally terminate with residual slack.")

add_header(doc, "1.1 Mathematical Formulation & DP Recurrence", level=3)
add_body_p(doc, 
    "Let words be indexed 1..n with lengths l_1..l_n. Placing words i..j on a single line consumes length "
    "L(i, j) = sum_{k=i}^j l_k + (j - i). The cost P(i, j) is defined as (M - L(i, j))^3 for j < n, 0 for j = n, and infinity if L(i, j) > M. "
    "The minimum layout penalty for words 1..j satisfies the optimal substructure recurrence:")
add_code_block(doc, 
    "DP[0] = 0\n"
    "DP[j] = min_{1 <= i <= j} { DP[i - 1] + P(i, j) }\n"
    "Choice Pointer: parent[j] = argmin_{1 <= i <= j} { DP[i - 1] + P(i, j) }"
)

add_header(doc, "1.2 Pseudocode (SIMATS Engineering Standard)", level=3)
with open(os.path.join(SRC_DIR, "Task_1", "task1_pseudocode.md"), 'r', encoding='utf-8') as f:
    pseudo_1 = f.read()
add_code_block(doc, pseudo_1)

add_header(doc, "1.3 Execution Results & Intermediate DP State Exposure", level=3)
add_body_p(doc, 
    "The engine was executed with line width M = 26 on the test document text: "
    "'Buffering and layout management require rigorous dynamic programming to balance aesthetic readability' (12 words). "
    "The program output the exact optimal lines, unused spaces, and line penalties:")

task1_table_data = [
    ["L1", "Buffering and layout", "6 chars", "216 (6^3)"],
    ["L2", "management require", "8 chars", "512 (8^3)"],
    ["L3", "rigorous dynamic", "10 chars", "1000 (10^3)"],
    ["L4", "programming to balance", "4 chars", "64 (4^3)"],
    ["L5", "aesthetic readability", "5 chars", "0 (Final Line)"]
]
add_styled_table(doc, ["Line", "Words Formatted on Line", "Unused Slack", "Line Penalty"], task1_table_data)
add_body_p(doc, "Total Minimum Layout Penalty: 1,792. Total Lines: 5.")

# Embed Figure 1
t1_img = os.path.join(SRC_DIR, "Task_1", "task1_word_wrap_analysis.png")
if os.path.exists(t1_img):
    doc.add_paragraph().alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture(t1_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 1: Word Wrap DP Performance, Multi-Width Comparison & Slack Breakdown.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "1.4 Multi-Width Requirement Change & Boundary Testing", level=3)
add_body_p(doc, 
    "Requirement Change Experiment: The layout engine was executed across three distinct line widths: M=20, M=25, and M=30. "
    "Predictions were recorded prior to execution:")
add_body_p(doc, "• At M = 20: Narrow width forced lines to accommodate 1-2 words. Predicted high cubic penalty. Actual: 1,100 penalty (8 lines).")
add_body_p(doc, "• At M = 25: Moderate width allowed 3-4 words per line with tight spacing. Predicted substantial penalty decrease. Actual: 505 penalty (6 lines).")
add_body_p(doc, "• At M = 30: Wider margins accommodated 4-6 words. Predicted further line compaction. Actual: 819 penalty (5 lines). Notice that while line count dropped from 6 to 5, the penalty rose from 505 to 819 because one line incurred slack 8 (8^3 = 512). This exposes the non-linear sensitivity of cubic penalty functions!")
add_body_p(doc, "Defensive Boundary Testing: A word whose length exactly equals M (15 chars) incurred exactly 0 penalty (0^3 = 0). When an oversized word (49 chars > M=20) was supplied, the engine defensively raised a ValueError before state computation, preventing index corruption.")

# -----------------------------------------------------------------------------
# TASK 2
# -----------------------------------------------------------------------------
add_header(doc, "TASK 2: GREEDY vs DYNAMIC PROGRAMMING", level=1)
add_header(doc, "Build It, Break It, Explain It (9 Marks)", level=2)

add_body_p(doc, 
    "Logistical dispatch platforms face the classic resource allocation dilemma: packing freight of weight w_i and value v_i "
    "into a vehicle of capacity W. We implement Solution A (Greedy Fractional Knapsack) and Solution B (0/1 Knapsack DP).")

add_header(doc, "2.1 Solution Implementations & Normal Case Execution", level=3)
add_body_p(doc, 
    "In the normal divisible freight scenario (Capacity W = 60 kg), items are sorted by value-to-weight ratio v_i / w_i. "
    "Greedy strategy commits PKG-A (wt:10, val:60, ratio:6.0), PKG-B (wt:20, val:100, ratio:5.0), and PKG-C (wt:30, val:120, ratio:4.0). "
    "This achieves the exact global optimum of $280.00 with 100% capacity utilization.")

add_header(doc, "2.2 Breaking the Greedy Intuition: Adversarial Counterexample", level=3)
add_body_p(doc, 
    "When items are strictly indivisible (0/1 constraint), greedy density heuristics fail catastrophically. "
    "We designed the following adversarial test instance with Capacity W = 50 kg:")
task2_adv_data = [
    ["ITEM-1", "10 kg", "$60.00", "6.00 $/kg", "Committed 1st by Greedy", "EXCLUDED by DP"],
    ["ITEM-2", "20 kg", "$100.00", "5.00 $/kg", "Committed 2nd by Greedy", "SELECTED by DP"],
    ["ITEM-3", "30 kg", "$120.00", "4.00 $/kg", "REJECTED (No space)", "SELECTED by DP"]
]
add_styled_table(doc, ["Item ID", "Weight", "Value", "Density Ratio", "Greedy 0/1 Action", "DP 0/1 Action"], task2_adv_data)

add_body_p(doc, 
    "Identification of the First Greedy Commitment Trap: Greedy observes ITEM-1 has the highest ratio (6.00 $/kg) and irrevocably "
    "commits it. This leaves 40 kg remaining. Next, Greedy takes ITEM-2 (20 kg, $100), leaving 20 kg remaining. "
    "Greedy now encounters ITEM-3 (30 kg), which cannot fit! Greedy terminates with {ITEM-1, ITEM-2} yielding $160.00. "
    "However, Dynamic Programming evaluates the full combinatorial state space and selects {ITEM-2, ITEM-3}, achieving $220.00! "
    "The greedy trap was the initial commitment to ITEM-1, which caused an awkward residual capacity and resulted in a 27.3% suboptimality gap ($60 loss)!")

# Embed Figure 2
t2_img = os.path.join(SRC_DIR, "Task_2", "task2_knapsack_comparison.png")
if os.path.exists(t2_img):
    doc.add_picture(t2_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 2: Fractional Greedy Packing vs 0/1 Knapsack Adversarial Counterexample.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "2.3 Engineering Comparison & Changed Requirement (FPTAS)", level=3)
task2_comp_data = [
    ["Theoretical Time", "O(n log n)", "Theta(n * W) pseudo-polynomial"],
    ["Computational Work", "19 sorting/scan comparisons", "153 table state evaluations"],
    ["Auxiliary Memory", "O(1) auxiliary (656 bytes)", "Theta(n * W) table (1,944 bytes)"],
    ["Solution Quality", "Exact for Fractional; Bounded for 0/1", "Guaranteed Global Optimum (0/1)"],
    ["Decision Latency", "< 0.05 milliseconds", "Scales with capacity W"]
]
add_styled_table(doc, ["Engineering Dimension", "Solution A (Greedy Heuristic)", "Solution B (Dynamic Programming)"], task2_comp_data)
add_body_p(doc, 
    "Management Mandate Response: When management requires decision delivery within milliseconds and accepts near-optimal results, "
    "pure DP is discarded because high capacity W (e.g. W = 100,000) causes memory thrashing and exceeds latency SLAs. "
    "Instead, we deploy a Modified Greedy Heuristic (taking max of Greedy-0/1 and single largest value item), guaranteeing a 2-approximation "
    "(>= 50% optimal) in O(n log n) sub-millisecond time, or a Fully Polynomial Time Approximation Scheme (FPTAS) scaling values by K = eps * V_max / n.")

# -----------------------------------------------------------------------------
# TASK 3
# -----------------------------------------------------------------------------
add_header(doc, "TASK 3: ROUTING ENGINE UNDER CHANGING NETWORK CONDITIONS", level=1)
add_header(doc, "Dijkstra + Bellman-Ford + Floyd + Warshall (10 Marks)", level=2)

add_body_p(doc, 
    "We architect a production-grade routing engine on a weighted directed network consisting of 8 vertices {A, B, C, D, E, F, G, H} "
    "and 13 directed edges, testing normal operations, negative weight edge anomalies, negative cycle production failures, and all-pairs analytics.")

add_header(doc, "3.1 Stage A – Normal Routing (Dijkstra SSSP)", level=3)
add_body_p(doc, "Source vertex A was executed using Dijkstra's algorithm. Vertices were finalized in greedy distance order:")
add_body_p(doc, "Finalization Sequence: A(0.0) -> B(2.0) -> D(3.0) -> C(5.0) -> E(7.0) -> F(7.0) -> G(9.0) -> H(12.0).")
task3_stage_a = [
    ["Node A", "0.0", "None", "A"],
    ["Node B", "2.0", "A", "A -> B"],
    ["Node C", "5.0", "A", "A -> C"],
    ["Node D", "3.0", "B", "A -> B -> D"],
    ["Node E", "7.0", "C", "A -> C -> E"],
    ["Node F", "7.0", "D", "A -> B -> D -> F"],
    ["Node G", "9.0", "D", "A -> B -> D -> G"],
    ["Node H", "12.0", "G", "A -> B -> D -> G -> H"]
]
add_styled_table(doc, ["Target Vertex", "Shortest Distance", "Predecessor", "Reconstructed Path"], task3_stage_a)

add_header(doc, "3.2 Stage B – Negative Edge Insertion & Prediction Verification", level=3)
add_body_p(doc, 
    "Intervention: We introduced edge E -> D with negative weight -6.0. The graph remains strictly acyclic. "
    "Prediction: Dijkstra will FAIL. It finalizes D at distance 3.0 via A -> B -> D before evaluating E (dist 7.0). "
    "Because D is already finalized, Dijkstra will never re-evaluate D via A -> C -> E -> D (cost 5 + 2 - 6 = 1.0 < 3.0). "
    "Consequently, downstream nodes F, G, H will also have inflated distances.")
task3_stage_b = [
    ["Node D", "3.0 (A -> B -> D)", "1.0 (A -> C -> E -> D)", "PREDICTION CONFIRMED: DIJKSTRA FAILED"],
    ["Node F", "7.0 (A -> B -> D -> F)", "5.0 (A -> C -> E -> D -> F)", "PREDICTION CONFIRMED: DIJKSTRA FAILED"],
    ["Node G", "9.0", "7.0", "PREDICTION CONFIRMED: DIJKSTRA FAILED"],
    ["Node H", "12.0", "10.0", "PREDICTION CONFIRMED: DIJKSTRA FAILED"]
]
add_styled_table(doc, ["Vertex", "Dijkstra Reported Cost", "Bellman-Ford Exact Cost", "Validation Status"], task3_stage_b)

# Embed Figure 3
t3_img = os.path.join(SRC_DIR, "Task_3", "task3_routing_analysis.png")
if os.path.exists(t3_img):
    doc.add_picture(t3_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 3: Dijkstra Failure vs Bellman-Ford Accuracy and Floyd's APSP Heatmap.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "3.3 Stage C – Negative Cycle Detection & Stage D Analytics", level=3)
add_body_p(doc, 
    "Production Failure Handling: Directed edge F -> E (-1.0) was inserted, forming cycle E -> D(w=-6.0) -> F(w=4.0) -> E(w=-1.0) "
    "with cycle sum -3.0 < 0. Bellman-Ford performed |V|-1 = 7 passes, and on the 8th pass detected that distances could still be relaxed. "
    "The engine safely raised an alarm, traced the cycle vertices E -> D -> F -> E, and aborted dispatch to prevent infinite looping.")
add_body_p(doc, 
    "Stage D Analytics: Floyd's algorithm computed the complete 8x8 APSP matrix in Theta(|V|^3) time, and Warshall's algorithm computed "
    "the transitive closure boolean reachability matrix, enabling O(1) pairwise route queries.")

# -----------------------------------------------------------------------------
# TASK 4
# -----------------------------------------------------------------------------
add_header(doc, "TASK 4: SMART MANUFACTURING OPTIMISATION", level=1)
add_header(doc, "Assembly Line Scheduling Dynamic Programming (7 Marks)", level=2)

add_body_p(doc, 
    "A manufacturing facility operates two parallel assembly lines (Line 1 and Line 2) across 6 sequential processing stations. "
    "We formulate a linear-time DP engine to minimize total manufacturing time and trace station decisions.")

add_header(doc, "4.1 Optimization Engine & Decision Exposure", level=3)
add_body_p(doc, 
    "Using factory parameters e_1=2, e_2=4, x_1=3, x_2=2, station processing vectors a_1=[7,9,3,4,8,4], a_2=[8,5,6,4,5,7], "
    "and transfer vectors t_1=[2,3,1,3,4], t_2=[2,1,2,2,1], the DP produced the optimal route with minimum time = 38 units:")
add_body_p(doc, "Optimal Route: Entry -> Line 1-St 1 -> Transfer -> Line 2-St 2 -> Transfer -> Line 1-St 3 -> Transfer -> Line 2-St 4 -> Line 2-St 5 -> Transfer -> Line 1-St 6 -> Exit.")

task4_trace_data = [
    ["St 2", "18", "23", "STAY (Line 1)", "17", "16", "TRANSFER (from Line 1)"],
    ["St 3", "21", "20", "TRANSFER (from Line 2)", "22", "27", "STAY (Line 2)"],
    ["St 4", "24", "28", "STAY (Line 1)", "26", "25", "TRANSFER (from Line 1)"],
    ["St 5", "32", "35", "STAY (Line 1)", "30", "32", "STAY (Line 2)"],
    ["St 6", "36", "35", "TRANSFER (from Line 2)", "37", "43", "STAY (Line 2)"]
]
add_styled_table(doc, ["Station", "L1 Stay", "L1 Trans", "L1 Selection", "L2 Stay", "L2 Trans", "L2 Selection"], task4_trace_data)

# Embed Figure 4
t4_img = os.path.join(SRC_DIR, "Task_4", "task4_assembly_line_route.png")
if os.path.exists(t4_img):
    doc.add_picture(t4_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 4: Dynamic Programming Assembly Line Scheduling Flow & Optimal Route.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "4.2 Predictions, Disruptions & Extension to 3 Lines", level=3)
add_body_p(doc, 
    "Transfer Cost Spike: Transfer penalty t1[0] was increased from 2 to 25. As predicted, the engine completely avoided "
    "transferring at Station 1, remaining on Line 1 for Stations 1, 2, and 3, increasing total time to 39 units.")
add_body_p(doc, 
    "Machine Slowdown Challenge: Line 2 Station 5 suffered mechanical degradation (processing time surged from 5 to 22). "
    "The engine detected this bottleneck and automatically diverted production to Line 1 at Station 5 (a1[4]=8), maintaining global optimality.")
add_body_p(doc, 
    "Engineering Extension to 3 Assembly Lines: To scale to lines L1, L2, L3, the state vector generalizes to DP[3][n+1]. "
    "Transition recurrence becomes f_i[j] = min_{1 <= k <= 3} (f_k[j-1] + t_{k,i}[j-1]) + a_i[j-1], where t_{k,i} = 0 when k=i. "
    "Complexity scales gracefully to O(M^2 * n) operations, maintaining linear scalability with respect to station count.")

# -----------------------------------------------------------------------------
# TASK 5
# -----------------------------------------------------------------------------
add_header(doc, "TASK 5: THREE GREEDY ENGINEERS, ONE NETWORK", level=1)
add_header(doc, "Kruskal + Prim + Boruvka (7 Marks)", level=2)

add_body_p(doc, 
    "Three fundamental greedy Minimum Spanning Tree (MST) algorithms were implemented on the same 8-vertex, 13-edge network:")
add_body_p(doc, "• Kruskal's Algorithm: Global edge sorting + Disjoint Set Union (DSU) with path compression and union by rank.")
add_body_p(doc, "• Prim's Algorithm: Cut property + Min-Priority Queue growing a single tree component from source vertex A.")
add_body_p(doc, "• Boruvka's Algorithm: Component contraction where each connected component simultaneously finds its cheapest incident edge.")

add_header(doc, "5.1 Stress Testing: Non-Unique Edge Weights & Divergent MSTs", level=3)
add_body_p(doc, 
    "We stressed the network by introducing edge weight ties (cycle A-B-C with weight 2.0, and dual connections to H of weight 4.0). "
    "The algorithms produced the following results:")
task5_mst_data = [
    ["Kruskal's Algorithm", "19.0", "(D-E:1), (B-C:2), (A-C:2), (F-G:2), (E-F:3), (G-H:4), (B-D:5)"],
    ["Prim's Algorithm", "19.0", "(A-B:2), (A-C:2), (B-D:5), (D-E:1), (E-F:3), (F-G:2), (F-H:4)"],
    ["Borůvka's Algorithm", "19.0", "(B-C:2), (A-C:2), (D-E:1), (F-G:2), (G-H:4), (B-D:5), (E-F:3)"]
]
add_styled_table(doc, ["Algorithm", "Total MST Cost", "Selected Edge Set (7 Edges)"], task5_mst_data)
add_body_p(doc, 
    "Can algorithms return different edge sets while all being correct? YES! Kruskal selected (B-C:2) and (G-H:4), while Prim selected "
    "(A-B:2) and (F-H:4). Because both edge sets form valid acyclic spanning trees and achieve the exact same minimum weight (19.0), "
    "both are mathematically optimal. Tie-breaking mechanisms (global sort order vs priority queue insertion vs component IDs) explain the divergence.")

# Embed Figure 5
t5_img = os.path.join(SRC_DIR, "Task_5", "task5_mst_comparison.png")
if os.path.exists(t5_img):
    doc.add_picture(t5_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 5: MST Algorithm Equivalence and Divergent Edge Set Verification.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "5.2 Industry Architecture Deployment Decisions", level=3)
task5_deploy_data = [
    ["Sparse Network (E ~ V)", "Kruskal (or Prim-PQ)", "Kruskal sorts in O(E log V) with near O(1) DSU operations; minimal memory overhead."],
    ["Dense Network (E ~ V^2)", "Prim (Adjacency Matrix)", "Prim with matrix runs in O(V^2), eliminating heap overhead and cache misses entirely."],
    ["Distributed Cloud Cluster", "Borůvka's Algorithm", "Components find cheapest edges in parallel; ideal for MapReduce/Spark distributed graphs."]
]
add_styled_table(doc, ["Target Environment", "Recommended Algorithm", "Architectural & Hardware Justification"], task5_deploy_data)

# -----------------------------------------------------------------------------
# TASK 6
# -----------------------------------------------------------------------------
add_header(doc, "TASK 6: LAST-MILE DELIVERY ROUTE OPTIMISATION", level=1)
add_header(doc, "Travelling Salesperson Problem Using Dynamic Programming (9 Marks)", level=2)

add_body_p(doc, 
    "A central distribution hub serves customer locations. The delivery vehicle must visit every location exactly once and return "
    "to the hub with minimum travel cost (NP-hard TSP). We implement the Held-Karp Bitmask Dynamic Programming algorithm.")

add_header(doc, "6.1 State Formulation & Brute Force Validation", level=3)
add_body_p(doc, 
    "Why Current Location Alone Fails: A partial state (j) cannot determine which locations remain unvisited. To maintain validity, "
    "the state MUST retain both the current location j and the subset of visited locations S. "
    "Recurrence: DP[S][j] = min_{k in S \\ {j}} (DP[S \\ {j}][k] + C[k][j]), with base case DP[{0}][0] = 0.")
add_body_p(doc, 
    "Validation (N = 5 nodes): On an instance with 1 Hub + 4 Delivery Locations, Brute Force evaluated all 4! = 24 permutations, "
    "finding optimal tour Central-Hub -> Loc-A -> Loc-B -> Loc-C -> Loc-D -> Central-Hub with cost 58.0 km. "
    "Held-Karp DP evaluated 57 states and produced the EXACT SAME optimal cost (58.0 km) and identical tour, rigorously confirming correctness.")
add_body_p(doc, 
    "Prototype Execution (N = 7 nodes): Evaluated on Central-Hub + 6 locations. Optimal tour: "
    "Central-Hub -> Loc-D -> Loc-E -> Loc-F -> Loc-C -> Loc-B -> Loc-A -> Central-Hub. Minimum travel cost = 75.0 km.")

# Embed Figure 6
t6_img = os.path.join(SRC_DIR, "Task_6", "task6_tsp_state_growth.png")
if os.path.exists(t6_img):
    doc.add_picture(t6_img, width=Inches(6.2))
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cap = p_cap.add_run("Figure 6: TSP State-Space Growth (Held-Karp vs Brute Force) & Optimal Tour Map.")
    r_cap.font.name = 'Arial'; r_cap.font.size = Pt(8.5); r_cap.font.italic = True

add_header(doc, "6.2 Empirical State-Space Growth Benchmark", level=3)
task6_growth_data = [
    ["N = 4", "19 states", "0.016 ms", "1,592 bytes", "6 perms"],
    ["N = 5", "57 states", "0.022 ms", "3,384 bytes", "24 perms"],
    ["N = 6", "171 states", "0.043 ms", "7,224 bytes", "120 perms"],
    ["N = 7", "493 states", "0.124 ms", "15,416 bytes", "720 perms"],
    ["N = 8", "1,359 states", "0.232 ms", "32,920 bytes", "5,040 perms"],
    ["N = 9", "3,601 states", "0.605 ms", "69,752 bytes", "40,320 perms"],
    ["N = 10", "9,235 states", "1.495 ms", "148,120 bytes", "362,880 perms"]
]
add_styled_table(doc, ["Locations (N)", "DP States Evaluated", "Execution Time", "DP Table Memory", "Brute Force Perms"], task6_growth_data)

add_header(doc, "6.3 Scaling to 200 Locations & Technical Reflection", level=3)
add_body_p(doc, 
    "Why Exact DP Fails for N = 200: The state space contains 2^200 ≈ 1.6 * 10^60 subsets, exceeding the atoms in the solar system. "
    "Management relaxed optimality to near-optimal satisficing. We propose Nearest Neighbor + 2-Opt local search heuristics and Christofides' "
    "1.5-approximation, trading ~2% suboptimality for instant 2-second route generation.")

add_body_p(doc, 
    "Technical Reflection (Mandated <= 150 Words):\n"
    "\"Dynamic Programming achieves dramatic efficiency gains over brute force by memoizing overlapping subproblems, reducing TSP from "
    "O(N!) to O(N^2 * 2^N). However, DP scalability is strictly bounded by its state-space representation. For TSP, the Markovian property "
    "fails without retaining the unvisited customer set; hence, the state requires a subset S. Because the power set grows exponentially as 2^N, "
    "our empirical benchmarks show memory and operations doubling with every increment in N. While polynomial DP succeeds for problems with "
    "linear states like Assembly Line Scheduling (O(N)) or Word Wrap (O(N^2)), it cannot overcome the fundamental combinatorial explosion of "
    "NP-hard problems with subset-based states. DP optimizes overlapping subproblem traversal, but it does not alter the underlying exponential "
    "dimensionality of the state space itself.\"", bold_prefix="Student Technical Reflection: ", italic=True)

# -----------------------------------------------------------------------------
# CONCLUSION & ENGINEERING LEARNINGS
# -----------------------------------------------------------------------------
add_header(doc, "CONCLUSION & ENGINEERING SYNTHESIS", level=1)
add_body_p(doc, 
    "CO4 Assignment 4B successfully validates the core principles of Algorithm Engineering across Dynamic Programming and Greedy strategies. "
    "Key engineering insights established through empirical testing include:")
add_body_p(doc, "1. Greedy Choice Limits: Greedy algorithms deliver optimal speed O(n log n) when the matroid greedy choice property holds (Fractional Knapsack, MST), but fail when irrevocable commitments lock out better combinatorial combinations (0/1 Knapsack, negative edge Dijkstra).")
add_body_p(doc, "2. Dynamic Programming Universality: DP guarantees global mathematical optimality by memoizing overlapping subproblems, but its real-world scalability depends entirely on state dimensionality (O(n) for assembly lines vs O(n^2 2^n) for TSP).")
add_body_p(doc, "3. Defensive Engineering: Production routing systems must anticipate failure states, incorporating cycle detection (Bellman-Ford) and boundary guards before executing optimization engines.")

# Save DOCX
docx_path = os.path.join(REPORT_DIR, "CO4_Assignment_4B_Report.docx")
doc.save(docx_path)
print(f"Generated DOCX: {docx_path}")

# -----------------------------------------------------------------------------
# PDF GENERATION (REPORTLAB)
# -----------------------------------------------------------------------------
print("Starting PDF Generation via ReportLab...")
pdf_path = os.path.join(REPORT_DIR, "CO4_Assignment_4B_Report.pdf")
pdf_doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)

styles = getSampleStyleSheet()
style_title = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, leading=20, textColor=colors.HexColor('#102C57'), alignment=1, spaceAfter=8)
style_sub = ParagraphStyle('SubStyle', parent=styles['Normal'], fontSize=11, leading=14, textColor=colors.HexColor('#B42828'), alignment=1, spaceAfter=14)
style_h1 = ParagraphStyle('H1Style', parent=styles['Heading1'], fontSize=13, leading=16, textColor=colors.HexColor('#102C57'), spaceBefore=12, spaceAfter=6)
style_h2 = ParagraphStyle('H2Style', parent=styles['Heading2'], fontSize=11, leading=14, textColor=colors.HexColor('#1E5096'), spaceBefore=8, spaceAfter=4)
style_body = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#222222'), spaceAfter=5)
style_code = ParagraphStyle('CodeStyle', parent=styles['Code'], fontSize=7.5, leading=9.5, textColor=colors.HexColor('#1E1E1E'), backColor=colors.HexColor('#F4F6F9'), spaceBefore=4, spaceAfter=6)
style_meta = ParagraphStyle('MetaStyle', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#142846'), alignment=1)

story = []

# Title & Metadata
story.append(Paragraph("<b>SIMATS ENGINEERING</b><br/>SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES", style_title))
story.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING</b>", style_meta))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>CSA0608 – DESIGN AND ANALYSIS OF ALGORITHMS</b><br/>COURSE OUTCOME 4 – ASSIGNMENT 4B (PART II)<br/><b>ALGORITHM ENGINEERING: IMPLEMENT, TEST, DEBUG & OPTIMISE</b>", style_sub))

meta_text = (
    "<b>STUDENT:</b> SANJAI S (Reg. No: 192511018)<br/>"
    "<b>DEPARTMENT:</b> Computer Science and Engineering | <b>TOTAL MARKS:</b> 50<br/>"
    "<b>NATURE:</b> Individual Capstone Laboratory Assignment"
)
meta_table = Table([[Paragraph(meta_text, style_meta)]], colWidths=[500])
meta_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EBF1F5')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#102C57')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
]))
story.append(meta_table)
story.append(Spacer(1, 14))

# Executive Summary
story.append(Paragraph("<b>EXECUTIVE SUMMARY</b>", style_h1))
story.append(Paragraph(
    "This laboratory report presents the complete algorithm engineering, empirical validation, adversarial debugging, "
    "and architectural trade-off analysis for CO4 Assignment 4B. Building on Part I pseudocode designs, six production-grade "
    "prototypes were implemented, tested, and analyzed covering Word Wrap DP, Fractional vs 0/1 Knapsack, Routing under Adverse "
    "Conditions, Assembly Line Scheduling, Greedy MST Algorithms, and Last-Mile TSP Route Optimization.", style_body))

# Task 1
story.append(Paragraph("<b>TASK 1: WORD WRAP AS A DOCUMENT-LAYOUT ENGINE (8 MARKS)</b>", style_h1))
story.append(Paragraph("<b>Mathematical Model:</b> Non-final line penalty is cubic slack S^3 = (M - used_length)^3. Final line carries 0 penalty. DP recurrence: DP[j] = min_{1<=i<=j} (DP[i-1] + P(i, j)).", style_body))
t1_table_pdf = Table([["Line", "Formatted Text", "Slack", "Penalty"]] + task1_table_data, colWidths=[35, 260, 65, 120])
t1_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t1_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t1_img):
    story.append(RLImage(t1_img, width=480, height=205))
    story.append(Spacer(1, 8))

# Task 2
story.append(Paragraph("<b>TASK 2: GREEDY vs DYNAMIC PROGRAMMING KNAPSACK (9 MARKS)</b>", style_h1))
story.append(Paragraph(
    "<b>Adversarial 0/1 Counterexample:</b> Capacity W = 50 kg. Greedy commits ITEM-1 (wt:10, val:60, ratio:6.0) then ITEM-2 (wt:20, val:100, ratio:5.0), "
    "leaving 20 kg residual space which rejects ITEM-3 (wt:30, val:120). Greedy yields $160.00. Optimal DP selects {ITEM-2, ITEM-3} yielding $220.00 (27.3% gap). "
    "Greedy commitment trap conclusively proven.", style_body))
t2_table_pdf = Table([["Item ID", "Weight", "Value", "Density", "Greedy Action", "DP Action"]] + task2_adv_data, colWidths=[55, 50, 50, 65, 130, 130])
t2_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t2_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t2_img):
    story.append(RLImage(t2_img, width=480, height=205))
    story.append(Spacer(1, 8))

# Task 3
story.append(Paragraph("<b>TASK 3: ROUTING ENGINE UNDER CHANGING NETWORK CONDITIONS (10 MARKS)</b>", style_h1))
story.append(Paragraph(
    "<b>Stage B Discrepancy:</b> Negative edge E -> D (-6.0) inserted. Dijkstra finalized D at cost 3.0 via A->B->D and refused to re-evaluate it, "
    "failing on D, F, G, H. Bellman-Ford correctly converged to exact cost 1.0 via A->C->E->D. "
    "<b>Stage C Failure Handling:</b> Edge F -> E (-1.0) formed a reachable negative cycle (cost -3.0). Bellman-Ford's 8th pass detected the cycle and safely aborted.", style_body))
t3_table_pdf = Table([["Vertex", "Dijkstra Reported Cost", "Bellman-Ford Exact Cost", "Validation Status"]] + task3_stage_b, colWidths=[55, 120, 135, 170])
t3_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t3_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t3_img):
    story.append(RLImage(t3_img, width=480, height=205))
    story.append(Spacer(1, 8))

# Task 4
story.append(Paragraph("<b>TASK 4: SMART MANUFACTURING ASSEMBLY LINE SCHEDULING (7 MARKS)</b>", style_h1))
story.append(Paragraph("<b>Optimisation Output:</b> Minimum Production Time = 38 time units across 6 stations. Formatted flow: Entry -> L1-S1 -> Transfer -> L2-S2 -> Transfer -> L1-S3 -> Transfer -> L2-S4 -> L2-S5 -> Transfer -> L1-S6 -> Exit.", style_body))
t4_table_pdf = Table([["Station", "L1 Stay", "L1 Trans", "L1 Selection", "L2 Stay", "L2 Trans", "L2 Selection"]] + task4_trace_data, colWidths=[45, 55, 55, 110, 55, 55, 105])
t4_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7.5),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t4_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t4_img):
    story.append(RLImage(t4_img, width=480, height=205))
    story.append(Spacer(1, 8))

# Task 5
story.append(Paragraph("<b>TASK 5: THREE GREEDY ENGINEERS, ONE NETWORK (7 MARKS)</b>", style_h1))
story.append(Paragraph("<b>Multiple MST Verification:</b> On the stressed network with weight ties, Kruskal, Prim, and Boruvka all achieved the identical minimal total weight of 19.0. Kruskal selected (B-C:2) and (G-H:4), while Prim selected (A-B:2) and (F-H:4), proving that greedy algorithms can return divergent edge sets that are all mathematically correct MSTs.", style_body))
t5_table_pdf = Table([["Algorithm", "Total Cost", "Selected Edge Set"]] + task5_mst_data, colWidths=[110, 60, 310])
t5_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t5_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t5_img):
    story.append(RLImage(t5_img, width=480, height=205))
    story.append(Spacer(1, 8))

# Task 6
story.append(Paragraph("<b>TASK 6: LAST-MILE DELIVERY ROUTE OPTIMISATION - TSP DP (9 MARKS)</b>", style_h1))
story.append(Paragraph("<b>Held-Karp Recurrence:</b> DP[S][j] = min_{k in S\\{j}} (DP[S\\{j}][k] + C[k][j]). Validated against 24 brute-force permutations on N=5 (exact match at 58.0 km). Prototype achieved 75.0 km tour on N=7.", style_body))
t6_table_pdf = Table([["Locations", "DP States", "Execution Time", "Memory", "Brute Force Perms"]] + task6_growth_data, colWidths=[70, 90, 95, 95, 130])
t6_table_pdf.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F4E79')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F9F9F9')]),
]))
story.append(t6_table_pdf)
story.append(Spacer(1, 8))
if os.path.exists(t6_img):
    story.append(RLImage(t6_img, width=480, height=205))
    story.append(Spacer(1, 8))

story.append(Paragraph("<b>Student Technical Reflection (Mandated <= 150 Words):</b>", style_h2))
story.append(Paragraph(
    "<i>\"Dynamic Programming achieves dramatic efficiency gains over brute force by memoizing overlapping subproblems, reducing TSP from "
    "O(N!) to O(N^2 * 2^N). However, DP scalability is strictly bounded by its state-space representation. For TSP, the Markovian property "
    "fails without retaining the unvisited customer set; hence, the state requires a subset S. Because the power set grows exponentially as 2^N, "
    "our empirical benchmarks show memory and operations doubling with every increment in N. While polynomial DP succeeds for problems with "
    "linear states like Assembly Line Scheduling (O(N)) or Word Wrap (O(N^2)), it cannot overcome the fundamental combinatorial explosion of "
    "NP-hard problems with subset-based states. DP optimizes overlapping subproblem traversal, but it does not alter the underlying exponential "
    "dimensionality of the state space itself.\"</i> [121 words - Compliant]", style_body))

pdf_doc.build(story)
print(f"Generated PDF: {pdf_path}")
print("Report compilation complete!")
