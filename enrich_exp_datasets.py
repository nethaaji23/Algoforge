import json, sys
sys.stdout.reconfigure(encoding='utf-8')

exp_path = 'C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/experience_questions.json'
exp_full_path = 'C:/Users/netha/.gemini/antigravity/scratch/algoforge_hyper_glitch/AlgoForge_Experience_Mode_Question_Bank.json'

with open(exp_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Add rich datasets to coding questions
coding_datasets = {
    "EXP-SORT-04": [
        {"id": "TC #01", "input": "[4, 2, 1, 3]", "expected": "[1, 2, 3, 4]"},
        {"id": "TC #02", "input": "[5, 1, 1, 2, 0, 0]", "expected": "[0, 0, 1, 1, 2, 5]"},
        {"id": "TC #03", "input": "[10, -1, 3, 8, 2]", "expected": "[-1, 2, 3, 8, 10]"},
        {"id": "TC #04", "input": "[1]", "expected": "[1]"},
        {"id": "TC #05", "input": "[3, 3, 3]", "expected": "[3, 3, 3]"}
    ],
    "EXP-SEARCH-04": [
        {"id": "TC #01", "input": "arr=[10, 20, 30, 40, 50], target=30", "expected": "2"},
        {"id": "TC #02", "input": "arr=[10, 20, 30, 40, 50], target=99", "expected": "-1"},
        {"id": "TC #03", "input": "arr=[5], target=5", "expected": "0"},
        {"id": "TC #04", "input": "arr=[1, 3, 5, 7, 9, 11], target=7", "expected": "3"},
        {"id": "TC #05", "input": "arr=[2, 4, 6, 8, 10], target=2", "expected": "0"}
    ],
    "EXP-GRAPH-04": [
        {"id": "TC #01", "input": "adj=[[1, 2], [0, 2, 3], [0, 1], [1]], node=1", "expected": "3"},
        {"id": "TC #02", "input": "adj=[[], [0], [1]], node=0", "expected": "0"},
        {"id": "TC #03", "input": "adj=[[1,2,3,4], [0], [0], [0], [0]], node=0", "expected": "4"},
        {"id": "TC #04", "input": "adj=[[1], [0]], node=1", "expected": "1"},
        {"id": "TC #05", "input": "adj=[[2], [], [0]], node=2", "expected": "1"}
    ],
    "EXP-TREE-04": [
        {"id": "TC #01", "input": "root=[20, 10, 30, 5, 15]", "expected": "5"},
        {"id": "TC #02", "input": "root=[50, 40, 60, 30]", "expected": "30"},
        {"id": "TC #03", "input": "root=[100]", "expected": "100"},
        {"id": "TC #04", "input": "root=[8, 3, 10, 1, 6, 14]", "expected": "1"},
        {"id": "TC #05", "input": "root=[25, 12, 36, 8, 19]", "expected": "8"}
    ],
    "EXP-AVL-04": [
        {"id": "TC #01", "input": "left_height=3, right_height=1", "expected": "2"},
        {"id": "TC #02", "input": "left_height=2, right_height=2", "expected": "0"},
        {"id": "TC #03", "input": "left_height=1, right_height=3", "expected": "-2"},
        {"id": "TC #04", "input": "left_height=0, right_height=1", "expected": "-1"},
        {"id": "TC #05", "input": "left_height=4, right_height=2", "expected": "2"}
    ],
    "EXP-HEAP-04": [
        {"id": "TC #01", "input": "parent=2, left=5, right=8", "expected": "true"},
        {"id": "TC #02", "input": "parent=10, left=4, right=12", "expected": "false"},
        {"id": "TC #03", "input": "parent=1, left=1, right=3", "expected": "true"},
        {"id": "TC #04", "input": "parent=7, left=9, right=6", "expected": "false"},
        {"id": "TC #05", "input": "parent=3, left=4, right=5", "expected": "true"}
    ]
}

for q in questions:
    if q["id"] in coding_datasets:
        q["testcases"] = coding_datasets[q["id"]]

with open(exp_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

with open(exp_full_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Successfully enriched {len(questions)} questions in {exp_path} and {exp_full_path}!")
