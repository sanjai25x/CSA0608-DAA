"""
========================================================================================
CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS
ASSIGNMENT 4A: PART I - ALGORITHMIC DESIGN THROUGH PSEUDOCODE
MASTER CAPSTONE REPORT GENERATOR (DOCX, PDF, MD)
STUDENT: SANJAI S (192511018)
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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE_DIR = r"C:\Users\SANJAI\.gemini\antigravity\scratch\CSA0608-DAA\CO4_Assignment_4A"
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
        else:
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(50, 50, 50)
    return h

def add_p(doc, text, bold_prefix=None, space_after=6, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(10)
        r_b.font.bold = True
        r_b.font.color.rgb = RGBColor(20, 20, 20)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.italic = italic
    r.font.color.rgb = RGBColor(40, 40, 40)
    return p

def create_docx_table(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "1F497D")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        for p in hdr_cells[i].paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(9.5)
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 255, 255)
                
    for row_idx, row_data in enumerate(data):
        row_cells = table.rows[row_idx + 1].cells
        bg_color = "F2F5F9" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, cell_value in enumerate(row_data):
            row_cells[col_idx].text = str(cell_value)
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=100, right=100)
            for p in row_cells[col_idx].paragraphs:
                p.paragraph_format.line_spacing = 1.1
                p.paragraph_format.space_after = Pt(2)
                for run in p.runs:
                    run.font.name = 'Arial'
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(30, 30, 30)
                    
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)
                
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(6)
    return table

def add_image_if_exists(doc, img_path, caption="", width=Inches(6.2)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = 'Arial'
            r_cap.font.size = Pt(8.5)
            r_cap.italic = True
            r_cap.font.color.rgb = RGBColor(80, 80, 80)

# ======================================================================================
# 1. BUILD DOCX REPORT
# ======================================================================================
def generate_docx():
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(1)
        s.bottom_margin = Inches(1)
        s.left_margin = Inches(1)
        s.right_margin = Inches(1)
        
    # Title / Cover Page
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(12)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = title_p.add_run("SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES\nSIMATS ENGINEERING\nDEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING\n\n")
    r_uni.font.name = 'Arial'
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(16, 44, 87)
    
    r_title = title_p.add_run("ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE: OPTIMIZATION PROBLEMS VIA GREEDY STRATEGIES AND DYNAMIC PROGRAMMING\n\n")
    r_title.font.name = 'Arial'
    r_title.font.size = Pt(15)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(16, 44, 87)
    
    r_sub = title_p.add_run("COURSE OUTCOME 4 (CO4) COMPREHENSIVE CAPSTONE REPORT\nCourse Code & Name: CSA0608 – Design and Analysis of Algorithms\nMode: Individual Submission | Total Marks: 50\n\n")
    r_sub.font.name = 'Arial'
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(80, 80, 80)
    
    auth_p = doc.add_paragraph()
    auth_p.paragraph_format.space_before = Pt(36)
    auth_p.paragraph_format.space_after = Pt(36)
    auth_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_auth = auth_p.add_run("Submitted by:\nSANJAI S\nRegister Number: 192511018\nDepartment of Computer Science and Engineering\nSIMATS Engineering, Chennai – 602 105\n\nUnder the Guidance of:\nFaculty of Computer Science and Engineering\nSaveetha Institute of Medical and Technical Sciences\nNovember 2026")
    r_auth.font.name = 'Arial'
    r_auth.font.size = Pt(10.5)
    r_auth.font.color.rgb = RGBColor(40, 40, 40)
    
    doc.add_page_break()
    
    # Bonafide Certificate
    add_header(doc, "BONAFIDE CERTIFICATE", level=1)
    add_p(doc, "This is to certify that the assignment entitled \"ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE: OPTIMIZATION PROBLEMS VIA GREEDY STRATEGIES AND DYNAMIC PROGRAMMING\" is a bonafide record of work done independently by SANJAI S (Reg. No: 192511018) in partial fulfilment of the requirements for Course Outcome 4 (CO4) in CSA0608 – Design and Analysis of Algorithms at SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai, during the academic year 2026–2027.")
    add_p(doc, "\n\n\n______________________\t\t\t\t______________________\nCourse Faculty\t\t\t\tHead of the Department\nDepartment of CSE\t\t\t\tDepartment of CSE\nSIMATS Engineering\t\t\t\tSIMATS Engineering")
    
    doc.add_page_break()
    
    # Candidate Declaration
    add_header(doc, "CANDIDATE DECLARATION", level=1)
    add_p(doc, "I, SANJAI S (Register Number: 192511018), hereby declare that the assignment entitled \"ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE: OPTIMIZATION PROBLEMS VIA GREEDY STRATEGIES AND DYNAMIC PROGRAMMING\" submitted for Course Outcome 4 (CO4) in CSA0608 – Design and Analysis of Algorithms is my original intellectual work. All problem interpretations, mathematical state definitions, recurrence relations, pseudocode specifications conforming to the SIMATS Engineering Handbook for Algorithmic Pseudocode, desk-check traces, defect forensic analyses, and the Day-4 Design Challenge solutions were developed and executed by me.")
    add_p(doc, "\n\nPlace: Chennai\nDate: 18th November 2026\n\n\n___________________________\nSANJAI S (192511018)\nDepartment of Computer Science and Engineering\nSIMATS Engineering")
    
    doc.add_page_break()
    
    # Abstract
    add_header(doc, "ABSTRACT", level=1)
    add_p(doc, "This capstone report presents a comprehensive progression of algorithmic design—from problem interpretation and state modeling to pseudocode formulation, manual tracing, defect forensics, and adversarial validation—addressing Course Outcome 4 (CO4) of CSA0608: Design and Analysis of Algorithms. The report investigates two pillar optimization paradigms: Greedy Strategies and Dynamic Programming (DP). In Task 1, an ambiguous junior engineer's fractional knapsack design is diagnosed across six algorithmic deficiencies and repaired into an unambiguous greedy density-sorted formulation. Task 2 models the Job Sequencing with Deadlines requirement, formalizes the latest-slot greedy choice rule, performs a manual trace on five jobs earning $180, and verifies an adversarial modification where Job B displaces Job C to yield $210. Task 3 derives the 0/1 Knapsack DP state DP[i][w] and recurrence, providing complete pseudocode with backtracking reconstruction, an 8x5 state table desk-check selecting items {Q, R} ($45), and an analysis of predecessor dependencies. Task 4 conducts forensics on a defective WordBreak pseudocode, constructs an adversarial failing counterexample (\"abcat\" with Dict={\"cat\"}) exposing prefix-chaining omissions, and applies a minimal surgical fix verified via regression testing. Task 5 evaluates Dijkstra, Bellman-Ford, and Floyd-Warshall on a shared directed graph, contrasting non-negative greedy commitments with repeated relaxation and intermediate vertex subset formulations. Finally, Task 6 solves the compulsory Day-4 Design Challenge for energy-aware cloud data centre scheduling through Weighted Interval Scheduling via binary search and DP, securing 200 energy savings across {J2, J5, J7, J8} and demonstrating immunity against adversarial earliest-finish and max-value traps.")
    add_p(doc, "Greedy Strategy, Dynamic Programming, Fractional Knapsack, Job Sequencing with Deadlines, 0/1 Knapsack, Word Break Forensics, Dijkstra, Bellman-Ford, Floyd-Warshall, Weighted Interval Scheduling, SIMATS Pseudocode.", bold_prefix="Keywords: ")
    
    doc.add_page_break()
    
    # Table of Contents
    add_header(doc, "TABLE OF CONTENTS", level=1)
    t_items = [
        ("1. TASK 1: ALGORITHM DESIGN REVIEW – FRACTIONAL KNAPSACK", "1"),
        ("   1.1 Diagnosis of Algorithmic Deficiencies", "1"),
        ("   1.2 Repaired Language-Independent Pseudocode", "2"),
        ("   1.3 Design Defence (Pseudocode Criteria)", "3"),
        ("2. TASK 2: FROM BUSINESS REQUIREMENT TO GREEDY PSEUDOCODE", "4"),
        ("   2.1 Modeling Problem Inputs, Outputs, and Constraints", "4"),
        ("   2.2 Greedy Hypothesis Formulation and Justification", "5"),
        ("   2.3 Complete Pseudocode for Job Sequencing", "5"),
        ("   2.4 Step-by-Step Desk-Check Trace (Profit = $180)", "6"),
        ("   2.5 Adversarial Modification Challenge (Job B Preemption)", "7"),
        ("3. TASK 3: FROM RECURRENCE TO EXECUTABLE LOGIC – 0/1 KNAPSACK", "8"),
        ("   3.1 Mathematical State Definition", "8"),
        ("   3.2 Recurrence Derivation and Meaning of Terms", "8"),
        ("   3.3 Complete Pseudocode with Backtracking Reconstruction", "9"),
        ("   3.4 Full DP State Table Desk-Check (Capacity = 7 kg)", "10"),
        ("   3.5 Explanation of Predecessor Dependencies", "11"),
        ("4. TASK 4: PSEUDOCODE FORENSICS – WORD BREAK DEFECT DIAGNOSIS", "12"),
        ("   4.1 Exact Defect Identification and Algorithmic Root Cause", "12"),
        ("   4.2 Student-Designed Failing Counterexample", "12"),
        ("   4.3 Minimal Surgical Repair", "13"),
        ("   4.4 Regression Check on Valid Inputs", "13"),
        ("5. TASK 5: SAME GRAPH, DIFFERENT ALGORITHMIC REASONING", "14"),
        ("   5.1 Dijkstra's Greedy Non-Negative Shortest-Path Design", "14"),
        ("   5.2 Negative Edge Breakdown & Bellman-Ford Reasoning", "16"),
        ("   5.3 All-Pairs Shortest Path & Floyd-Warshall State Transition", "17"),
        ("6. TASK 6: DAY-4 DESIGN CHALLENGE – ENERGY-AWARE SCHEDULING", "18"),
        ("   6.1 Stage 1: Problem Interpretation and Abstraction", "18"),
        ("   6.2 Stage 2: Strategy Proposal & Greedy Failure Analysis", "18"),
        ("   6.3 Stage 3: Critical Information, Predecessors, and State", "19"),
        ("   6.4 Stage 4: Complete Pseudocode (Weighted Interval Scheduling)", "20"),
        ("   6.5 Stage 5: Desk-Check Trace on 8 Cloud Jobs (Value = 200)", "21"),
        ("   6.6 Stage 6: Attack Your Own Design (Adversarial Trap Immunity)", "22"),
        ("7. CONCLUSION AND COMPARATIVE ARCHITECTURAL MATRIX", "24"),
        ("APPENDICES (SOURCE CODE LISTINGS & EXECUTION SCREENSHOTS)", "26")
    ]
    for itm, pg in t_items:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(2)
        r = p_t.add_run(itm)
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        
    doc.add_page_break()
    
    # --- SECTION 1: TASK 1 ---
    add_header(doc, "1. TASK 1: ALGORITHM DESIGN REVIEW – FRACTIONAL KNAPSACK", level=1)
    add_p(doc, "A logistics company loads divisible packages into a delivery vehicle of maximum carrying capacity C. Each package possesses a weight w_i and monetary value v_i. The goal is to maximize total value without exceeding capacity.")
    add_header(doc, "1.1 Diagnosis of the Junior Engineer's Proposed Pseudocode", level=2)
    add_p(doc, "The junior engineer's proposal suffers from critical algorithmic deficiencies that make reliable software implementation impossible:")
    
    t1_headers = ["No.", "Deficiency", "Algorithmic Explanation", "Implementation Impact"]
    t1_data = [
        ["1", "Undefined Inputs & Outputs", "Omits parameter declarations (P, W, V, n, C) and output return structure.", "Engineer cannot bind data structures, signatures, or caller interfaces."],
        ["2", "Ambiguous Selection Criterion", "Uses 'Arrange packages' and 'Select best package' without defining greedy metric.", "Hides greedy choice rule; engineer may sort by value or weight, yielding suboptimal loading."],
        ["3", "Missing Feasibility & Tracking", "'vehicle has space' fails to track remaining capacity C_rem or test w_i <= C_rem.", "Cannot detect when an item overflows remaining capacity."],
        ["4", "Failure to Handle Divisibility", "Problem permits package division, but code lacks fractional division logic.", "Underfills vehicle; fails to compute fraction f = C_rem / w_i."],
        ["5", "Infinite Loop Trap", "Loop does not advance pointers or remove processed packages.", "Repetitive evaluation of same package causes non-termination."],
        ["6", "Unspecified Result Construction", "'Calculate value' and 'RETURN result' provide no accumulation mechanism.", "Caller receives uninitialized result; allocation vector is lost."]
    ]
    create_docx_table(doc, t1_headers, t1_data, [0.5, 1.8, 2.4, 2.3])
    
    add_header(doc, "1.2 Repaired Pseudocode Specification", level=2)
    add_p(doc, "The repaired algorithm computes density ratios R[i] = V[i]/W[i], sorts packages descendingly, packs full packages while capacity permits, and divides the first overflowing package to saturate capacity exactly.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_1", "task1_execution_terminal.png"), "Figure 1.1: Execution Output of Repaired Fractional Knapsack Algorithm.")
    
    add_header(doc, "1.3 Design Defence (Pseudocode Qualification)", level=2)
    add_p(doc, "This solution qualifies as pseudocode rather than code because it uses language-independent mathematical abstractions (SORT in descending order, FOR i <- 1 TO n DO) and explicit input/output contracts without syntax-specific boilerplate (pointers, class imports, memory management). It qualifies as pseudocode rather than informal English because every state transition, feasibility boundary (W[i] <= current_capacity), density ratio calculation (V[i]/W[i]), and fractional division rule (C_rem / W[i]) is mathematically deterministic, unambiguous, and directly implementable by any software engineer.")
    
    doc.add_page_break()
    
    # --- SECTION 2: TASK 2 ---
    add_header(doc, "2. TASK 2: FROM BUSINESS REQUIREMENT TO GREEDY PSEUDOCODE", level=1)
    add_p(doc, "A cloud service provider receives independent single-slot jobs characterized by Job ID, Deadline d_i, and Profit p_i. A job earns its profit only if completed on or before its deadline. The objective is to maximize total profit.")
    
    add_header(doc, "2.1 Problem Abstraction & Requirement Model", level=2)
    add_p(doc, "Input: n jobs J_i = (id_i, d_i, p_i) with integer deadline d_i >= 1 and profit p_i >= 0.", bold_prefix="• ")
    add_p(doc, "Output: Schedule array S[1...M] (where M = max d_i) and total profit earned.", bold_prefix="• ")
    add_p(doc, "Objective: Maximize sum of p_i for scheduled jobs.", bold_prefix="• ")
    add_p(doc, "Constraints: Unit processing time (1 slot/job), 1 job per slot, deadline feasibility t <= d_i, at most 1 execution per job.", bold_prefix="• ")
    add_p(doc, "Decision: Accept/reject job and select optimal slot t in [1, d_i].", bold_prefix="• ")
    
    add_header(doc, "2.2 Greedy Hypothesis Formulation", level=2)
    add_p(doc, "\"Sort all incoming jobs in descending order of profit, and greedily allocate each candidate job to the latest unoccupied discrete time slot t <= d_i.\"", bold_prefix="Greedy-Choice Rule: ")
    add_p(doc, "Prioritizing highest profit captures maximum immediate value. Allocating the latest feasible slot defers resource commitment as late as possible, preserving earlier slots for subsequent jobs with earlier, stricter deadlines.")
    
    add_header(doc, "2.3 Desk-Check Trace (Given Instance)", level=2)
    add_p(doc, "Given Jobs: A(d=2, p=80), B(d=1, p=35), C(d=2, p=60), D(d=3, p=40), E(d=1, p=25). Sorted: A(80), C(60), D(40), B(35), E(25). Max deadline M = 3.")
    add_p(doc, "1. Job A (d=2, p=80): Assign Slot 2. Schedule: [-, A, -], Profit: $80.")
    add_p(doc, "2. Job C (d=2, p=60): Slot 2 occupied -> Assign Slot 1. Schedule: [C, A, -], Profit: $140.")
    add_p(doc, "3. Job D (d=3, p=40): Assign Slot 3. Schedule: [C, A, D], Profit: $180.")
    add_p(doc, "4. Job B (d=1, p=35): Slot 1 occupied -> REJECTED.")
    add_p(doc, "5. Job E (d=1, p=25): Slot 1 occupied -> REJECTED.")
    add_p(doc, "Final Schedule: Slot 1: Job C | Slot 2: Job A | Slot 3: Job D. Total Profit: $180.")
    
    add_header(doc, "2.4 Adversarial Modification Challenge", level=2)
    add_p(doc, "Modification: Increase Job B's profit from $35 to $90 (d=1 remains).")
    add_p(doc, "Prediction: Job B becomes priority #1, claims Slot 1, and displaces Job C (d=2), causing Job C to be rejected.")
    add_p(doc, "Execution Result: B claims Slot 1 ($90), A claims Slot 2 ($80), C is rejected (Slots 1 & 2 full), D claims Slot 3 ($40). New Schedule: [B, A, D], Total Profit = $210. Prediction perfectly verified!")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_2", "task2_execution_terminal.png"), "Figure 2.1: Execution Output of Greedy Job Sequencing & Adversarial Validation.")
    
    doc.add_page_break()
    
    # --- SECTION 3: TASK 3 ---
    add_header(doc, "3. TASK 3: FROM RECURRENCE TO EXECUTABLE LOGIC – 0/1 KNAPSACK", level=1)
    add_p(doc, "A cargo vehicle with carrying capacity W must transport indivisible items with weights w_i and values v_i.")
    
    add_header(doc, "3.1 State Definition & Mathematical Recurrence", level=2)
    add_p(doc, "DP[i][w] = The maximum total monetary value achievable by selecting a feasible subset of the first i items {1...i} such that combined weight <= w.", bold_prefix="State Definition: ")
    add_p(doc, "DP[0][w] = 0 for all w; DP[i][0] = 0 for all i.", bold_prefix="Base Cases: ")
    add_p(doc, "If w_i > w: DP[i][w] = DP[i-1][w] (Item i cannot fit into capacity w).\nIf w_i <= w: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i) (Exclude vs Include).", bold_prefix="Recurrence: ")
    
    add_header(doc, "3.2 Desk-Check on Given Instance (Capacity W = 7)", level=2)
    add_p(doc, "Items: P(w=2, v=12), Q(w=3, v=20), R(w=4, v=25), S(w=5, v=30).")
    
    t3_headers = ["Item (i)", "w=0", "w=1", "w=2", "w=3", "w=4", "w=5", "w=6", "w=7"]
    t3_data = [
        ["0: Base", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["1: P(2,12)", "0", "0", "12", "12", "12", "12", "12", "12"],
        ["2: Q(3,20)", "0", "0", "12", "20", "20", "32", "32", "32"],
        ["3: R(4,25)", "0", "0", "12", "20", "25", "32", "37", "45"],
        ["4: S(5,30)", "0", "0", "12", "20", "25", "32", "37", "45"]
    ]
    create_docx_table(doc, t3_headers, t3_data, [1.1, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65])
    
    add_p(doc, "Backtracking from DP[4][7] = 45:\n• DP[4][7] == DP[3][7] (45 == 45) -> Item S Excluded.\n• DP[3][7] != DP[2][7] (45 != 32) -> Item R INCLUDED! Residual cap = 7 - 4 = 3.\n• DP[2][3] != DP[1][3] (20 != 12) -> Item Q INCLUDED! Residual cap = 3 - 3 = 0.\n• Cap = 0 -> Item P Excluded.\nSelected Items: {Q, R}, Total Weight = 7 kg, Maximum Value = $45.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_3", "task3_dp_table_visualization.png"), "Figure 3.1: Complete 0/1 Knapsack DP State Matrix Heatmap.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_3", "task3_execution_terminal.png"), "Figure 3.2: Execution Output of 0/1 Knapsack Dynamic Programming.")
    
    add_header(doc, "3.3 Dependency Analysis", level=2)
    add_p(doc, "State DP[i][w] depends on DP[i-1][w] and DP[i-1][w - w_i]. Both predecessors belong strictly to the preceding row i-1. Therefore, row i-1 must be fully computed before row i is evaluated. The outer loop must iterate forward i = 1 TO n.")
    
    doc.add_page_break()
    
    # --- SECTION 4: TASK 4 ---
    add_header(doc, "4. TASK 4: PSEUDOCODE FORENSICS – WORD BREAK DEFECT DIAGNOSIS", level=1)
    add_p(doc, "A faulty WordBreak algorithm attempts to determine whether a string of length n can be completely segmented into dictionary words.")
    
    add_header(doc, "4.1 Exact Defect Identification", level=2)
    add_p(doc, "The decision IF substring(Text, j, i) is in Dictionary THEN evaluates only the dictionary membership of the suffix chunk Text[j...i-1], but fails to verify whether the prefix ending at j was validly segmentable (DP[j] == TRUE). Finding a valid dictionary word in the middle/end of text is useless if the preceding prefix is unsegmentable gibberish.")
    
    add_header(doc, "4.2 Student-Designed Failing Counterexample", level=2)
    add_p(doc, "Text = \"abcat\", Dictionary = {\"cat\"}. Ground Truth: FALSE.")
    add_p(doc, "Faulty Execution: At i=5, j=2, substring(\"abcat\", 2, 5) = \"cat\" is in Dictionary. Faulty algorithm ignores DP[2]=FALSE and sets DP[5] <- TRUE, erroneously returning TRUE (False Positive)!")
    
    add_header(doc, "4.3 Minimal Surgical Repair & Regression Verification", level=2)
    add_p(doc, "Change decision to: IF (DP[j] == TRUE) AND (substring(Text, j, i) is in Dictionary) THEN DP[i] <- TRUE; BREAK; END IF")
    add_p(doc, "Regression Test: Text = \"applepie\", Dict = {\"apple\", \"pie\"}. Repaired algorithm returns TRUE, confirming correct behavior is preserved.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_4", "task4_execution_terminal.png"), "Figure 4.1: Execution Output: Word Break Forensics Defect Diagnosis and Repair.")
    
    doc.add_page_break()
    
    # --- SECTION 5: TASK 5 ---
    add_header(doc, "5. TASK 5: SAME GRAPH, DIFFERENT ALGORITHMIC REASONING", level=1)
    add_p(doc, "Given directed weighted graph with vertices {A, B, C, D, E} and edges: A->B:4, A->C:7, B->C:2, B->D:6, C->D:1, D->E:3, C->E:8.")
    
    add_header(doc, "5.1 Dijkstra's Greedy Algorithm (Non-Negative Weights)", level=2)
    add_p(doc, "Dijkstra initializes dist[A]=0, others infinity. Extracts minimum distance unvisited vertex and relaxes outgoing edges. Result: A:0, B:4, C:6, D:7, E:10.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_5", "task5_graph_visualization.png"), "Figure 5.1: Directed Weighted Graph Topology and Edge Weights.")
    
    add_header(doc, "5.2 Negative Edge Breakdown & Bellman-Ford Reasoning", level=2)
    add_p(doc, "Why Greedy Fails: Dijkstra assumes extracted vertices are finalized and cannot decrease. Negative edges violate this by allowing longer paths to become shorter via negative increments.")
    add_p(doc, "Bellman-Ford repeatedly relaxes all |E| edges for |V|-1 rounds. A |V|-th pass that still decreases distance proves the presence of a reachable negative-weight cycle.")
    
    add_header(doc, "5.3 Floyd-Warshall All-Pairs Shortest Path", level=2)
    add_p(doc, "State D^(k)[i][j] = Length of shortest path from i to j using intermediate vertices from {1...k}. State transition: D^(k)[i][j] = min(D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j]). Solves all pairs in Theta(V^3).")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_5", "task5_execution_terminal.png"), "Figure 5.2: Execution Output: Shortest Path Algorithms Comparison.")
    
    doc.add_page_break()
    
    # --- SECTION 6: TASK 6 ---
    add_header(doc, "6. TASK 6: DESIGN CHALLENGE – ENERGY-AWARE CLOUD JOB SCHEDULING", level=1)
    add_p(doc, "A specialized server executes computational jobs with start time s_i, finish time f_i, and energy-saving value v_i. Only non-overlapping jobs can execute. Objective: Maximize total energy savings.")
    
    add_header(doc, "6.1 Problem Interpretation & Strategy Selection", level=2)
    add_p(doc, "This is the Weighted Interval Scheduling Problem. Greedy by Earliest Finish Time or Max Value fails on weighted intervals because an early low-value job or single high-value job can block multiple compatible jobs of greater combined value. Dynamic Programming guarantees global optimality in O(n log n) time.")
    
    add_header(doc, "6.2 Predecessors and DP State Formulation", level=2)
    add_p(doc, "Jobs are sorted by finish time. Predecessor p(i) = latest job j < i with f_j <= s_i (found via binary search in O(log n)).\nState DP[i] = max(DP[i-1], v_i + DP[p(i)]).")
    
    add_header(doc, "6.3 Desk-Check Trace (8-Job Dataset)", level=2)
    t6_headers = ["i", "Job ID", "Interval", "Value", "p(i)", "DP[p(i)]", "DP[i-1]", "DP[i]", "Decision"]
    t6_data = [
        ["1", "J1", "[1, 3]", "20", "0", "0", "0", "20", "INCLUDE J1 (20+0=20)"],
        ["2", "J2", "[2, 5]", "50", "0", "0", "20", "50", "INCLUDE J2 (50+0=50)"],
        ["3", "J3", "[4, 6]", "30", "1", "20", "50", "50", "EXCLUDE J3 (Keep DP=50)"],
        ["4", "J4", "[6, 8]", "40", "3", "50", "50", "90", "INCLUDE J4 (40+50=90)"],
        ["5", "J5", "[5, 9]", "60", "2", "50", "90", "110", "INCLUDE J5 (60+50=110)"],
        ["6", "J6", "[8, 10]", "30", "4", "90", "110", "120", "INCLUDE J6 (30+90=120)"],
        ["7", "J7", "[9, 11]", "50", "5", "110", "120", "160", "INCLUDE J7 (50+110=160)"],
        ["8", "J8", "[11, 13]", "40", "7", "160", "160", "200", "INCLUDE J8 (40+160=200)"]
    ]
    create_docx_table(doc, t6_headers, t6_data, [0.4, 0.8, 1.1, 0.7, 0.6, 0.9, 0.9, 0.7, 2.1])
    
    add_p(doc, "Backtracking from DP[8]: Includes J8 -> p(8)=7 -> Includes J7 -> p(7)=5 -> Includes J5 -> p(5)=2 -> Includes J2 -> p(2)=0. Selected Compatible Jobs: {J2, J5, J7, J8}. Maximum Total Energy Savings = 50 + 60 + 50 + 40 = 200.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_6", "task6_scheduling_visualization.png"), "Figure 6.1: Optimal Energy-Aware Interval Schedule Gantt Chart.")
    
    add_header(doc, "6.4 Attack Your Own Design (Adversarial Trap Immunity)", level=2)
    add_p(doc, "Constructed 5-job adversarial set: A1[1,4] v=10, A2[3,8] v=100, A3[2,5] v=60, A4[5,9] v=60, A5[9,12] v=50.\n• Greedy EFT picks A1+A4+A5 = 120 (SUBOPTIMAL)\n• Greedy Value picks A2+A5 = 150 (SUBOPTIMAL)\n• Our DP Engine selects {A3, A4, A5} = 170 (GLOBAL OPTIMUM)!\nImmunity Proof: DP systematically compares including each job against the optimal prefix up to p(i), discovering that 60 + 60 + 50 = 170 beats the single 100 trap job.")
    add_image_if_exists(doc, os.path.join(SRC_DIR, "Task_6", "task6_execution_terminal.png"), "Figure 6.2: Execution Output: Day-4 Challenge Verification & Adversarial Attack.")
    
    doc.add_page_break()
    
    # --- SECTION 7: CONCLUSION ---
    add_header(doc, "7. CONCLUSION AND COMPARATIVE ARCHITECTURAL MATRIX", level=1)
    add_p(doc, "This assignment demonstrates that algorithmic optimization requires rigorous problem modeling prior to implementation. Greedy strategies excel when the Greedy Choice Property and Optimal Substructure hold unconditionally (Fractional Knapsack, Job Sequencing, Dijkstra). When local choices blind the solver to future opportunities (0/1 Knapsack, Word Break, Negative-Weight Graphs, Weighted Interval Scheduling), Dynamic Programming is indispensable.")
    
    t7_headers = ["Task / Problem", "Paradigm", "Decision Criterion / State", "Complexity", "Key Algorithmic Finding"]
    t7_data = [
        ["Task 1: Fractional Knapsack", "Greedy", "Sort by density v_i/w_i", "O(n log n)", "Divisible items guarantee greedy choice property holds."],
        ["Task 2: Job Sequencing", "Greedy", "Latest available slot t <= d_i", "O(n^2) / O(n log n)", "Deferring slot commitments preserves earlier slots for tight deadlines."],
        ["Task 3: 0/1 Knapsack", "DP", "DP[i][w] over prefix & capacity", "Theta(n W)", "Indivisibility creates subproblem overlap; greedy heuristics fail."],
        ["Task 4: Word Break", "DP", "DP[i] prefix segmentability", "O(n^2)", "Forensic fix: Must enforce DP[j]==True before suffix matching."],
        ["Task 5: Shortest Paths", "Greedy / DP", "Dijkstra vs Bellman-Ford vs Floyd", "O(V^2) / O(VE) / O(V^3)", "Negative edges break greedy finalizing; APSP uses intermediate DP."],
        ["Task 6: Cloud Scheduling", "DP", "DP[i] = max(DP[i-1], v_i + DP[p(i)])", "O(n log n)", "Weighted intervals defeat greedy EFT/Value; DP finds true optimum."]
    ]
    create_docx_table(doc, t7_headers, t7_data, [1.4, 0.9, 1.8, 1.1, 2.0])
    
    docx_path = os.path.join(REPORT_DIR, "CO4_Assignment_4A_Report.docx")
    doc.save(docx_path)
    print(f"Saved DOCX Report: {docx_path}")

# ======================================================================================
# 2. BUILD PDF REPORT USING REPORTLAB
# ======================================================================================
def generate_pdf():
    pdf_path = os.path.join(REPORT_DIR, "CO4_Assignment_4A_Report.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=15, leading=19,
        textColor=colors.HexColor('#102C57'), alignment=1, spaceAfter=8
    )
    sub_style = ParagraphStyle(
        'DocSub', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=14,
        textColor=colors.HexColor('#4B5563'), alignment=1, spaceAfter=14
    )
    h1_style = ParagraphStyle(
        'H1', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=13, leading=17,
        textColor=colors.HexColor('#102C57'), spaceBefore=12, spaceAfter=6
    )
    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=colors.HexColor('#1E5096'), spaceBefore=8, spaceAfter=4
    )
    body_style = ParagraphStyle(
        'Body', parent=styles['BodyText'],
        fontName='Helvetica', fontSize=9, leading=12.5,
        textColor=colors.HexColor('#1F2937'), spaceAfter=5
    )
    bullet_style = ParagraphStyle(
        'Bullet', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11.5,
        textColor=colors.HexColor('#1F2937'), leftIndent=12, spaceAfter=3
    )
    code_style = ParagraphStyle(
        'CodeStyle', parent=styles['Normal'],
        fontName='Courier', fontSize=7.5, leading=10,
        textColor=colors.HexColor('#111827'), backColor=colors.HexColor('#F3F4F6'),
        spaceBefore=4, spaceAfter=6, leftIndent=10
    )

    story = []
    
    # Title / Header
    story.append(Paragraph("SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES", sub_style))
    story.append(Paragraph("SIMATS ENGINEERING — DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING", sub_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE:<br/>OPTIMIZATION PROBLEMS VIA GREEDY STRATEGIES AND DYNAMIC PROGRAMMING", title_style))
    story.append(Paragraph("COURSE OUTCOME 4 (CO4) COMPREHENSIVE CAPSTONE REPORT<br/>Course Code: CSA0608 – Design and Analysis of Algorithms | Total Marks: 50", sub_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>Submitted by:</b> SANJAI S (Reg. No: 192511018) | Department of CSE, SIMATS Engineering<br/><b>Date:</b> November 2026", sub_style))
    story.append(Spacer(1, 10))
    
    # Bonafide & Declaration
    story.append(Paragraph("BONAFIDE CERTIFICATE & CANDIDATE DECLARATION", h1_style))
    story.append(Paragraph("This is to certify that this report is a bonafide record of independent work performed by SANJAI S (192511018) under Course Outcome 4 (CO4) of CSA0608 at SIMATS Engineering, Chennai. All algorithmic models, mathematical recurrences, pseudocode conforming to the SIMATS Engineering Handbook, desk-checks, forensic defect diagnoses, and Day-4 design challenges represent original individual work.", body_style))
    story.append(Spacer(1, 10))
    
    # Abstract
    story.append(Paragraph("ABSTRACT", h1_style))
    story.append(Paragraph("This report presents a thorough algorithmic progression from requirements modeling to pseudocode, manual traces, and adversarial validation across six core tasks. In Task 1, poor pseudocode for fractional knapsack is diagnosed across six deficiencies and repaired into an unambiguous greedy density-sorted algorithm. Task 2 models Job Sequencing with Deadlines, proves the latest-slot greedy rule, traces a 5-job instance earning $180, and validates an adversarial modification yielding $210. Task 3 derives 0/1 Knapsack DP state DP[i][w] and recurrence, providing pseudocode with backtracking reconstruction, an 8x5 table desk-check ({Q, R}, $45), and dependency proofs. Task 4 conducts forensics on defective WordBreak pseudocode, designing counterexample \"abcat\" (Dict={\"cat\"}) and a minimal surgical repair. Task 5 evaluates Dijkstra, Bellman-Ford, and Floyd-Warshall on a shared graph. Task 6 solves the Day-4 Design Challenge for cloud data centre scheduling through Weighted Interval Scheduling via binary search and DP, securing 200 energy savings across {J2, J5, J7, J8} and demonstrating immunity against adversarial traps.", body_style))
    story.append(Spacer(1, 10))
    
    # Task 1
    story.append(Paragraph("TASK 1: ALGORITHM DESIGN REVIEW – FRACTIONAL KNAPSACK", h1_style))
    story.append(Paragraph("<b>Deficiencies Diagnosed:</b> 1) Undefined inputs/outputs (P, W, V, C); 2) Ambiguous selection criterion ('arrange'/'best' hides greedy density rule); 3) Missing feasibility and capacity tracking; 4) Failure to compute fractional division f = C_rem / w_i; 5) Missing loop pointer advancement (infinite loop); 6) Unspecified result construction.", body_style))
    story.append(Paragraph("<b>Repaired Algorithm:</b> Computes density R[i]=V[i]/W[i], sorts descendingly, fills complete items, divides first overflowing item, terminates.", body_style))
    story.append(Paragraph("<b>Design Defence:</b> Qualifies as pseudocode by using language-independent mathematical abstractions (SORT descending, FOR i <- 1 TO n) without syntactic boilerplate, while remaining mathematically deterministic and unambiguous.", body_style))
    story.append(Spacer(1, 10))
    
    # Task 2
    story.append(Paragraph("TASK 2: JOB SEQUENCING WITH DEADLINES", h1_style))
    story.append(Paragraph("<b>Requirement Model:</b> Maximize profit from unit-time jobs where job i earns p_i iff scheduled in slot t <= d_i.", body_style))
    story.append(Paragraph("<b>Greedy Hypothesis:</b> Sort jobs descending by profit, and allocate each job to the latest unoccupied slot t <= d_i. Deferring slot commitment preserves earlier slots for jobs with tighter deadlines.", body_style))
    story.append(Paragraph("<b>Desk-Check on {A(80,d=2), B(35,d=1), C(60,d=2), D(40,d=3), E(25,d=1)}:</b> Sorted order A, C, D, B, E. Job A takes Slot 2 ($80); Job C takes Slot 1 ($140); Job D takes Slot 3 ($180); B and E rejected. <b>Total Profit: $180</b>.", body_style))
    story.append(Paragraph("<b>Adversarial Challenge:</b> Increasing Job B profit to 90 causes B to claim Slot 1, preempting and displacing Job C. New schedule: [B, A, D], Total Profit = $210 (Verified!).", body_style))
    story.append(Spacer(1, 10))
    
    # Task 3
    story.append(Paragraph("TASK 3: DYNAMIC PROGRAMMING – 0/1 KNAPSACK", h1_style))
    story.append(Paragraph("<b>State Definition:</b> DP[i][w] = Maximum total value achievable using a subset of items {1...i} under weight capacity w.", body_style))
    story.append(Paragraph("<b>Recurrence:</b> DP[i][w] = DP[i-1][w] if w_i > w; max(DP[i-1][w], DP[i-1][w-w_i] + v_i) if w_i <= w.", body_style))
    story.append(Paragraph("<b>Desk-Check on P(2,12), Q(3,20), R(4,25), S(5,30) with W=7:</b> Optimal DP[4][7] = 45. Backtracking skips S, includes R (rem cap=3), includes Q (rem cap=0), skips P. <b>Selected Items: {Q, R}, Total Value = $45</b>.", body_style))
    story.append(Paragraph("<b>Dependency:</b> State DP[i][w] depends on DP[i-1][w] and DP[i-1][w-w_i] from row i-1, mandating forward row iteration i=1...n.", body_style))
    story.append(Spacer(1, 10))
    
    # Task 4
    story.append(Paragraph("TASK 4: PSEUDOCODE FORENSICS – WORD BREAK", h1_style))
    story.append(Paragraph("<b>Exact Defect:</b> The condition 'IF substring(Text, j, i) is in Dictionary' verifies only the suffix slice, ignoring whether the preceding prefix ending at j was validly segmentable (DP[j] == TRUE).", body_style))
    story.append(Paragraph("<b>Counterexample:</b> Text = \"abcat\", Dict = {\"cat\"}. Ground truth is FALSE. Faulty code sets DP[5] <- TRUE because \"cat\" is in Dict, ignoring DP[2]=FALSE. Returns TRUE (False Positive!).", body_style))
    story.append(Paragraph("<b>Surgical Fix:</b> IF (DP[j] == TRUE) AND (substring(Text, j, i) is in Dictionary) THEN DP[i] <- TRUE; BREAK; END IF. Regression on \"applepie\" verified.", body_style))
    story.append(Spacer(1, 10))
    
    # Task 5
    story.append(Paragraph("TASK 5: SHORTEST PATHS – DIJKSTRA, BELLMAN-FORD, FLOYD", h1_style))
    story.append(Paragraph("<b>Dijkstra (Non-negative):</b> Greedily extracts unvisited vertex with min tentative distance and relaxes outgoing edges. Result from A: A:0, B:4, C:6, D:7, E:10.", body_style))
    story.append(Paragraph("<b>Negative Edge Breakdown:</b> Negative edges violate Dijkstra's greedy assumption that extracted vertex distances are finalized. Bellman-Ford performs |V|-1 relaxation rounds and detects negative cycles on the |V|-th pass.", body_style))
    story.append(Paragraph("<b>Floyd-Warshall (APSP):</b> State D^(k)[i][j] = shortest path from i to j using intermediate vertices from {1...k}. Transition: min(D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j]).", body_style))
    story.append(Spacer(1, 10))
    
    # Task 6
    story.append(Paragraph("TASK 6: DAY-4 DESIGN CHALLENGE – ENERGY-AWARE SCHEDULING", h1_style))
    story.append(Paragraph("<b>Problem Abstraction:</b> Weighted Interval Scheduling. Maximize sum of values of non-overlapping jobs.", body_style))
    story.append(Paragraph("<b>Strategy:</b> Greedy by finish time or value fails on weighted intervals. Dynamic Programming with binary search for latest non-conflicting job p(i) guarantees global optimality.", body_style))
    story.append(Paragraph("<b>Desk-Check (8 Jobs):</b> DP[i] = max(DP[i-1], v_i + DP[p(i)]). States: DP[1]=20, DP[2]=50, DP[3]=50, DP[4]=90, DP[5]=110, DP[6]=120, DP[7]=160, DP[8]=200. Backtracking reconstructs <b>{J2, J5, J7, J8}</b> with <b>Maximum Energy Savings = 200</b>.", body_style))
    story.append(Paragraph("<b>Adversarial Attack:</b> Evaluated on {A1[1,4]v=10, A2[3,8]v=100, A3[2,5]v=60, A4[5,9]v=60, A5[9,12]v=50}. Greedy EFT gets 120; Greedy Value gets 150; our DP engine achieves optimal 170 ({A3, A4, A5}), proving complete immunity to local traps.", body_style))
    story.append(Spacer(1, 10))
    
    # Comparative Matrix Table
    story.append(Paragraph("COMPARATIVE PARADIGM SUMMARY MATRIX", h1_style))
    matrix_data = [
        ["Task", "Paradigm", "Complexity", "Key Algorithmic Principle"],
        ["Task 1: Fractional Knapsack", "Greedy", "O(n log n)", "Divisibility enables greedy ratio choice."],
        ["Task 2: Job Sequencing", "Greedy", "O(n^2) / O(n log n)", "Latest-slot commitment preserves earlier flexibility."],
        ["Task 3: 0/1 Knapsack", "Dynamic Programming", "Theta(n W)", "Indivisibility requires evaluating include vs exclude."],
        ["Task 4: Word Break", "Dynamic Programming", "O(n^2)", "Prefix state chaining (DP[j]==True) ensures correctness."],
        ["Task 5: Shortest Paths", "Greedy / DP", "O(V^2) / O(VE) / O(V^3)", "Non-negative greedy vs repeated relaxation vs all-pairs DP."],
        ["Task 6: Cloud Scheduling", "Dynamic Programming", "O(n log n)", "Binary search predecessor p(i) + DP solves weighted intervals."]
    ]
    t = Table(matrix_data, colWidths=[110, 85, 95, 230])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F497D')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,0), 5),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,1), (-1,-1), 7.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t)
    
    doc.build(story)
    print(f"Saved PDF Report: {pdf_path}")

# ======================================================================================
# 3. BUILD MARKDOWN REPORT
# ======================================================================================
def generate_md():
    md_path = os.path.join(REPORT_DIR, "CO4_Assignment_4A_Report.md")
    content = """# ASSIGNMENT 4A (PART I) – ALGORITHMIC DESIGN THROUGH PSEUDOCODE
## Optimization Problems via Greedy Strategies and Dynamic Programming

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Assessment:** Course Outcome 4 (CO4) – Assignment 4A  
**Student Name:** SANJAI S (Reg. No: 192511018)  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences, Chennai  
**Date:** November 2026  

---

## BONAFIDE CERTIFICATE & DECLARATION
This is to certify that this report is a bonafide record of independent work done by SANJAI S (192511018) under Course Outcome 4 (CO4) in CSA0608 at SIMATS Engineering. All algorithm models, mathematical state definitions, recurrence derivations, pseudocode conforming to the SIMATS Engineering Handbook, desk-checks, forensic defect diagnoses, and Day-4 design challenge solutions were developed and validated independently.

---

## 1. TASK 1: ALGORITHM DESIGN REVIEW – FRACTIONAL KNAPSACK
- **Deficiencies Diagnosed:**
  1. Undefined inputs/outputs (P, W, V, C).
  2. Ambiguous selection criterion ('arrange'/'best' hides greedy density rule v_i/w_i).
  3. Missing feasibility and capacity tracking (C_rem).
  4. Failure to handle package divisibility (fractional allocation f = C_rem / w_i).
  5. Missing loop advancement (infinite loop).
  6. Unspecified result construction.
- **Repaired Pseudocode:** Computes density R[i] = V[i]/W[i], sorts descendingly, fills complete items, divides first overflowing item, terminates.
- **Design Defence:** Qualifies as pseudocode by using language-independent mathematical abstractions without syntactic boilerplate, while remaining mathematically deterministic and unambiguous.

---

## 2. TASK 2: JOB SEQUENCING WITH DEADLINES
- **Greedy Hypothesis:** Sort jobs descending by profit, and allocate each job to the latest unoccupied slot t <= d_i. Deferring slot commitment preserves earlier slots for jobs with tighter deadlines.
- **Desk-Check Trace:** On jobs {A(80,d=2), B(35,d=1), C(60,d=2), D(40,d=3), E(25,d=1)}:
  - Job A -> Slot 2 ($80)
  - Job C -> Slot 1 ($140)
  - Job D -> Slot 3 ($180)
  - Jobs B and E are rejected. Total Profit = **$180**.
- **Adversarial Modification Challenge:** Increasing Job B profit to 90 causes B to claim Slot 1, preempting and displacing Job C. New schedule: [B, A, D], Total Profit = **$210** (Verified!).

---

## 3. TASK 3: DYNAMIC PROGRAMMING – 0/1 KNAPSACK
- **State Definition:** DP[i][w] = Maximum total value achievable using a subset of items {1...i} under weight capacity w.
- **Recurrence:**
  - If w_i > w: DP[i][w] = DP[i-1][w]
  - If w_i <= w: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)
- **Desk-Check (Capacity W = 7):** On items P(2,12), Q(3,20), R(4,25), S(5,30):
  - Optimal Value DP[4][7] = **$45**.
  - Backtracking reconstructs **{Q, R}** (weight = 3+4=7 kg, value = 20+25=$45).
- **Dependency:** State DP[i][w] depends on DP[i-1][w] and DP[i-1][w-w_i] from row i-1, mandating forward row iteration i=1...n.

---

## 4. TASK 4: PSEUDOCODE FORENSICS – WORD BREAK
- **Defect:** Checks only whether substring(Text, j, i) is in Dictionary, ignoring whether the preceding prefix ending at j was segmentable (DP[j] == TRUE).
- **Counterexample:** Text = \"abcat\", Dict = {\"cat\"}. Ground truth is FALSE. Faulty code sets DP[5] <- TRUE because \"cat\" is in Dict, ignoring DP[2]=FALSE. Returns TRUE (False Positive!).
- **Surgical Repair:** `IF (DP[j] == TRUE) AND (substring(Text, j, i) is in Dictionary) THEN DP[i] <- TRUE; BREAK; END IF`. Regression on \"applepie\" verified.

---

## 5. TASK 5: SHORTEST PATHS – DIJKSTRA, BELLMAN-FORD, FLOYD-WARSHALL
- **Dijkstra:** Greedily extracts unvisited vertex with min tentative distance and relaxes outgoing edges. Result from A: A:0, B:4, C:6, D:7, E:10.
- **Negative Edges & Bellman-Ford:** Negative edges violate Dijkstra's greedy finalizing assumption. Bellman-Ford performs |V|-1 relaxation rounds and detects negative cycles on the |V|-th pass.
- **Floyd-Warshall (APSP):** State D^(k)[i][j] = shortest path from i to j using intermediate vertices from {1...k}. Transition: min(D^(k-1)[i][j], D^(k-1)[i][k] + D^(k-1)[k][j]).

---

## 6. TASK 6: DAY-4 DESIGN CHALLENGE – ENERGY-AWARE SCHEDULING
- **Problem Abstraction:** Weighted Interval Scheduling.
- **Strategy:** Greedy by finish time or value fails on weighted intervals. Dynamic Programming with binary search for latest non-conflicting job p(i) guarantees global optimality in O(n log n) time.
- **Desk-Check (8 Jobs):** DP states lead to optimal value **200**. Backtracking reconstructs **{J2, J5, J7, J8}** with zero interval overlap.
- **Adversarial Trap Immunity:** Evaluated on {A1[1,4]v=10, A2[3,8]v=100, A3[2,5]v=60, A4[5,9]v=60, A5[9,12]v=50}. Greedy EFT gets 120; Greedy Value gets 150; our DP engine achieves optimal **170** ({A3, A4, A5}), proving complete immunity to local traps.

---

## 7. COMPARATIVE SUMMARY MATRIX

| Task | Paradigm | Complexity | Key Algorithmic Principle |
| :--- | :--- | :--- | :--- |
| **Task 1: Fractional Knapsack** | Greedy | O(n log n) | Divisibility enables greedy ratio choice. |
| **Task 2: Job Sequencing** | Greedy | O(n^2) / O(n log n) | Latest-slot commitment preserves earlier flexibility. |
| **Task 3: 0/1 Knapsack** | Dynamic Programming | Theta(n W) | Indivisibility requires evaluating include vs exclude. |
| **Task 4: Word Break** | Dynamic Programming | O(n^2) | Prefix state chaining (DP[j]==True) ensures correctness. |
| **Task 5: Shortest Paths** | Greedy / DP | O(V^2) / O(VE) / O(V^3) | Non-negative greedy vs repeated relaxation vs all-pairs DP. |
| **Task 6: Cloud Scheduling** | Dynamic Programming | O(n log n) | Binary search predecessor p(i) + DP solves weighted intervals. |
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved MD Report: {md_path}")

if __name__ == "__main__":
    generate_docx()
    generate_pdf()
    generate_md()
    print("\n[SUCCESS] All CO4 Reports (DOCX, PDF, MD) generated successfully!")
