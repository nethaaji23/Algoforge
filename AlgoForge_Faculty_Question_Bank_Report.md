# AlgoForge - Comprehensive ADSA Question Bank Report
**Presented to**: Course Faculty / Evaluation Committee
**Course**: Analysis and Design of Data Structures & Algorithms (ADSA)
**Platform Name**: AlgoForge Interactive Algorithm Learning & Assessment Engine
**Total Dataset Questions**: 44 Questions (24 Experience Mode + 20 Challenge Mode)
**Question Bank Sources**: GeeksforGeeks, HackerRank, Codeforces, LeetCode

---

## 📑 Executive Summary

This document presents the complete, verified question bank dataset integrated into the **AlgoForge** platform. The question bank is stratified into two operational modes designed for different learning stages:

1. **Experience Mode Question Bank (24 Questions)**:
   - **Purpose**: Practice, continuous classroom assessment, line-by-line step-by-step visual execution.
   - **Difficulty**: Accessible practice level across 6 core ADSA domains.
   - **Domains Covered**: Sorting, Searching, Graphs, Trees & BST, AVL Trees, Heaps & Priority Queues.
   - **Question Types**: MCQs, Output Prediction, Algorithm Tracing, and Short Accessible Coding.

2. **Challenge Mode Question Bank (20 Questions)**:
   - **Purpose**: Timed continuous assessment examinations, mid-term testing, competitive programming arena.
   - **Difficulty**: Moderate to competitive examination level.
   - **Domains Covered**: Advanced Sorting, Rotated Searching, Graph Traversal (BFS/DFS), BST Invariants, Tree Heights, and Complexity Bounds.
   - **Question Types**: Full Python Coding Challenges (with 3-testcase automated verification matrices) and Advanced Conceptual MCQs.

---

# PART I: EXPERIENCE MODE QUESTION BANK

## 📊 Question Bank Topic Matrix

| Topic | Question Count | Question Types Included | Primary External Sources |
| :--- | :---: | :--- | :--- |
| **Sorting** | 4 | MCQ, Output Prediction, Tracing, Coding | GeeksforGeeks, HackerRank, LeetCode |
| **Searching** | 4 | MCQ, Output Prediction, Tracing, Coding | Codeforces, HackerRank, LeetCode, GeeksforGeeks |
| **Graphs** | 4 | MCQ, Output Prediction, Tracing, Coding | GeeksforGeeks, Codeforces, HackerRank, LeetCode |
| **Trees & BST** | 4 | MCQ, Output Prediction, Tracing, Coding | GeeksforGeeks, HackerRank, LeetCode |
| **AVL Trees** | 4 | MCQ, Output Prediction, Tracing, Coding | GeeksforGeeks, HackerRank, Codeforces, LeetCode |
| **Heaps & Priority Queues** | 4 | MCQ, Output Prediction, Tracing, Coding | GeeksforGeeks, HackerRank, Codeforces, LeetCode |

---

## 📝 Detailed Question Catalog (Experience Mode)

### Question 1: BUBBLE SORT BEST CASE COMPLEXITY
- **Question ID**: EXP-SORT-01
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Sorting (Time Complexity)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
What is the Time Complexity of Bubble Sort with a boolean swapped flag when the input array is already sorted in ascending order?

#### 🔘 Options
A. O(n) - Linear Time  ✔ [CORRECT]
B. O(n²) - Quadratic Time
C. O(n log n) - Linearithmic Time
D. O(1) - Constant Time

**Correct Answer**: **Option A** (O(n) - Linear Time)

#### 💡 Explanation & Pedagogical Step
> When the array is already sorted, no adjacent swaps occur during the first pass, allowing the early break flag to exit in O(n) time.

---

### Question 2: SELECTION SORT FIRST PASS OUTPUT
- **Question ID**: EXP-SORT-02
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Sorting (Pass Execution)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: N = 5 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Given array [29, 10, 14, 37, 13], what is the array state after 1 complete pass of Selection Sort (ascending order)?

#### 🔘 Options
A. [10, 29, 14, 37, 13]  ✔ [CORRECT]
B. [10, 14, 29, 37, 13]
C. [13, 10, 14, 29, 37]
D. [29, 10, 14, 13, 37]

**Correct Answer**: **Option A** ([10, 29, 14, 37, 13])

#### 💡 Explanation & Pedagogical Step
> Selection Sort scans the entire array for the minimum element (10) and swaps it with the first element (29).

---

### Question 3: INSERTION SORT KEY SHIFTING
- **Question ID**: EXP-SORT-03
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Sorting (Algorithm Tracing)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: N = 5 | **Time Limit**: 0.40 SEC

#### 📌 Problem Description
Inserting key `12` into sorted subarray [5, 8, 15, 20]. Which elements shift right to make room for `12`?

#### 🔘 Options
A. Elements 15 and 20 shift right  ✔ [CORRECT]
B. Only element 20 shifts right
C. Elements 5, 8, 15, and 20 all shift right
D. No elements shift

**Correct Answer**: **Option A** (Elements 15 and 20 shift right)

#### 💡 Explanation & Pedagogical Step
> Elements greater than key 12 (i.e. 15 and 20) shift one position right to make room for inserting 12.

---

### Question 4: SORT A SMALL ARRAY (EASY)
- **Question ID**: EXP-SORT-04
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Sorting (Array Sorting)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 100 | **Time Limit**: 0.50 SEC

#### 📌 Problem Description
Write a function `sortSmallArray(arr)` that sorts a list of numbers in ascending order using Bubble Sort or Selection Sort.

#### 💻 Code Starter / Snippet
`python
def sortSmallArray(arr):
    # TODO: Sort array in ascending order
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(sortSmallArray([4, 2, 5, 1]))
`

#### 💡 Explanation & Pedagogical Step
> Iterate through the array and swap adjacent elements if a[j] > a[j+1]. Return the sorted array.

---

### Question 5: LINEAR VS BINARY SEARCH PREREQUISITES
- **Question ID**: EXP-SEARCH-01
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Searching (Prerequisites)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Why can Linear Search be executed on an unsorted array, while Binary Search cannot?

#### 🔘 Options
A. Linear search checks elements sequentially without relying on sorted order  ✔ [CORRECT]
B. Binary search requires linked lists
C. Linear search requires prime numbers
D. Binary search only works on arrays of size 10

**Correct Answer**: **Option A** (Linear search checks elements sequentially without relying on sorted order)

#### 💡 Explanation & Pedagogical Step
> Linear search checks each element sequentially, whereas binary search halves the search space based on monotonic sorted order.

---

### Question 6: BINARY SEARCH MID INDEX TRACE
- **Question ID**: EXP-SEARCH-02
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Searching (Mid Index Calculation)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: N = 6 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Searching for target = 7 in sorted array [1, 3, 5, 7, 9, 11]. What is the first mid index and mid value inspected?

#### 🔘 Options
A. mid index = 2 (mid value = 5)  ✔ [CORRECT]
B. mid index = 3 (mid value = 7)
C. mid index = 1 (mid value = 3)
D. mid index = 4 (mid value = 9)

**Correct Answer**: **Option A** (mid index = 2 (mid value = 5))

#### 💡 Explanation & Pedagogical Step
> low = 0, high = 5. mid = (0 + 5) // 2 = 2. arr[2] = 5. Since 5 < 7, search moves to right half.

---

### Question 7: BINARY SEARCH TOTAL COMPARISONS
- **Question ID**: EXP-SEARCH-03
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Searching (Iteration Count)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: N = 10 | **Time Limit**: 0.40 SEC

#### 📌 Problem Description
How many total mid comparisons are needed to find target = 91 in sorted array [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]?

#### 🔘 Options
A. 4 total comparisons  ✔ [CORRECT]
B. 10 total comparisons
C. 1 comparison
D. 7 comparisons

**Correct Answer**: **Option A** (4 total comparisons)

#### 💡 Explanation & Pedagogical Step
> Iteration 1: mid=4 (16) -> Iteration 2: mid=7 (56) -> Iteration 3: mid=8 (72) -> Iteration 4: mid=9 (91 Match!). Total 4 comparisons.

---

### Question 8: FIND ELEMENT INDEX (EASY)
- **Question ID**: EXP-SEARCH-04
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Searching (Linear Search)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 500 | **Time Limit**: 0.40 SEC

#### 📌 Problem Description
Write a function `findTargetIndex(arr, target)` that returns the 0-based index of target in array, or -1 if target is not found.

#### 💻 Code Starter / Snippet
`python
def findTargetIndex(arr, target):
    # TODO: Return index of target or -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(findTargetIndex([15, 42, 8, 99, 23], 99))
`

#### 💡 Explanation & Pedagogical Step
> Iterate through arr with loop index i. If arr[i] == target, return i. If loop completes, return -1.

---

### Question 9: BFS LEVEL-BY-LEVEL EXPLORATION
- **Question ID**: EXP-GRAPH-01
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Graphs (BFS Traversal)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Which graph traversal strategy visits all direct neighbors of a node before visiting nodes two steps away?

#### 🔘 Options
A. Breadth-First Search (BFS)  ✔ [CORRECT]
B. Depth-First Search (DFS)
C. Preorder Traversal
D. Postorder Traversal

**Correct Answer**: **Option A** (Breadth-First Search (BFS))

#### 💡 Explanation & Pedagogical Step
> BFS explores graph nodes level-by-level using a FIFO Queue.

---

### Question 10: DFS TRAVERSAL STACK TRACE
- **Question ID**: EXP-GRAPH-02
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Graphs (DFS Trace)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: V = 4 | **Time Limit**: 0.40 SEC

#### 📌 Problem Description
Graph adjacency: 0 -> [1, 2], 1 -> [3], 2 -> [], 3 -> []. Starting from node 0, what is the DFS traversal order (visiting first neighbor first)?

#### 🔘 Options
A. 0, 1, 3, 2  ✔ [CORRECT]
B. 0, 1, 2, 3
C. 0, 2, 1, 3
D. 3, 1, 2, 0

**Correct Answer**: **Option A** (0, 1, 3, 2)

#### 💡 Explanation & Pedagogical Step
> DFS goes deep: visits 0 -> visits 1 -> visits 3 (leaf) -> backtracks to 0 -> visits 2. Order: 0, 1, 3, 2.

---

### Question 11: UNWEIGHTED SHORTEST DISTANCE WITH BFS
- **Question ID**: EXP-GRAPH-03
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Graphs (Shortest Path)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: UNWEIGHTED GRAPH | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
In an unweighted graph, what is the shortest distance (number of edges) from node A to node D if paths are A-B-C-D (3 edges) and A-E-D (2 edges)?

#### 🔘 Options
A. 2 edges (via path A-E-D)  ✔ [CORRECT]
B. 3 edges (via path A-B-C-D)
C. 1 edge
D. 4 edges

**Correct Answer**: **Option A** (2 edges (via path A-E-D))

#### 💡 Explanation & Pedagogical Step
> BFS guarantees finding the shortest path in terms of edge count in unweighted graphs. Path A-E-D takes 2 edges.

---

### Question 12: COUNT NEIGHBORS OF A NODE (EASY)
- **Question ID**: EXP-GRAPH-04
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Graphs (Adjacency List)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: V ≤ 100 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Write a function `countNeighbors(graph, node)` that returns the number of direct neighbors connected to `node` in an adjacency list dictionary.

#### 💻 Code Starter / Snippet
`python
def countNeighbors(graph, node):
    # TODO: Return length of graph[node]
    return len(graph.get(node, []))

print(countNeighbors({0: [1, 2, 3], 1: [0], 2: [0]}, 0))
`

#### 💡 Explanation & Pedagogical Step
> Return `len(graph.get(node, []))`.

---

### Question 13: BST NODE VALUE INVARIANT
- **Question ID**: EXP-TREE-01
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Trees (BST Invariant)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
In a Binary Search Tree (BST), which statement is true for any node with key K?

#### 🔘 Options
A. All keys in Left Subtree < K and all keys in Right Subtree > K  ✔ [CORRECT]
B. All keys in Left Subtree > K
C. Left child key must equal Right child key
D. Tree height must always be 1

**Correct Answer**: **Option A** (All keys in Left Subtree < K and all keys in Right Subtree > K)

#### 💡 Explanation & Pedagogical Step
> BST property requires left subtree keys < K and right subtree keys > K for every node in the tree.

---

### Question 14: BST INORDER OUTPUT PREDICTION
- **Question ID**: EXP-TREE-02
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Trees (Inorder Traversal)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: N = 5 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
What is the output sequence of performing Inorder traversal on a BST containing inserted values [50, 30, 70, 20, 40]?

#### 🔘 Options
A. [20, 30, 40, 50, 70]  ✔ [CORRECT]
B. [50, 30, 20, 40, 70]
C. [70, 50, 40, 30, 20]
D. [20, 40, 30, 70, 50]

**Correct Answer**: **Option A** ([20, 30, 40, 50, 70])

#### 💡 Explanation & Pedagogical Step
> Inorder traversal (Left, Root, Right) on a BST always visits nodes in sorted ascending order.

---

### Question 15: BST INSERTION PATH TRACE
- **Question ID**: EXP-TREE-03
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Trees (BST Insertion Path)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: N = 4 | **Time Limit**: 0.40 SEC

#### 📌 Problem Description
Inserting key 35 into a BST with root 50, left child 30, right child 70, and 30's right child 40. Where does 35 attach?

#### 🔘 Options
A. As the left child of node 40  ✔ [CORRECT]
B. As the right child of node 40
C. As the left child of node 70
D. As the left child of root 50

**Correct Answer**: **Option A** (As the left child of node 40)

#### 💡 Explanation & Pedagogical Step
> 35 < 50 (go left to 30), 35 > 30 (go right to 40), 35 < 40 (attach as left child of 40).

---

### Question 16: FIND MINIMUM VALUE IN BST (EASY)
- **Question ID**: EXP-TREE-04
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Trees (BST Minimum)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 100 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Write a function `findMinBST(tree)` that returns the smallest key in a BST (the leftmost node value).

#### 💻 Code Starter / Snippet
`python
def findMinBST(tree):
    # TODO: Traverse left child to find min value
    curr = tree
    while curr and isinstance(curr, list) and curr[1] is not None:
        curr = curr[1]
    return curr[0] if isinstance(curr, list) else curr

print(findMinBST([50, [30, [20, None, None], [40, None, None]], [70, None, None]]))
`

#### 💡 Explanation & Pedagogical Step
> Start at root. Keep moving to left child until left child is None. Return that node's value.

---

### Question 17: AVL BALANCE FACTOR FORMULA
- **Question ID**: EXP-AVL-01
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: AVL Trees (Balance Factor)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
How is the Balance Factor (BF) of an AVL tree node calculated?

#### 🔘 Options
A. BF = Height(Left Subtree) - Height(Right Subtree)  ✔ [CORRECT]
B. BF = Height(Root) * 2
C. BF = Number of Left Nodes + Number of Right Nodes
D. BF = Left Child Value - Right Child Value

**Correct Answer**: **Option A** (BF = Height(Left Subtree) - Height(Right Subtree))

#### 💡 Explanation & Pedagogical Step
> Balance factor is Height(Left) - Height(Right), which must equal -1, 0, or +1 in a valid AVL tree.

---

### Question 18: SINGLE RIGHT ROTATION (LL IMPALANCE)
- **Question ID**: EXP-AVL-02
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: AVL Trees (Single Rotation)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL TRACING | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
Inserting keys 30, 20, 10 in order into an AVL tree creates an LL heavy imbalance at node 30. After a single Right Rotation, which node becomes the new root?

#### 🔘 Options
A. Node 20  ✔ [CORRECT]
B. Node 10
C. Node 30
D. Node 15

**Correct Answer**: **Option A** (Node 20)

#### 💡 Explanation & Pedagogical Step
> Right rotating at node 30 pulls node 20 up to root, with 10 as left child and 30 as right child.

---

### Question 19: AVL REBALANCING TRIGGER
- **Question ID**: EXP-AVL-03
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: AVL Trees (Rebalancing Trigger)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL TRACING | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
If adding a key causes a node's Balance Factor to become +2, what action must the AVL tree perform?

#### 🔘 Options
A. Perform tree rotation(s) to restore balance factor to {-1, 0, +1}  ✔ [CORRECT]
B. Delete the root node
C. Convert tree into a Linked List
D. Do nothing

**Correct Answer**: **Option A** (Perform tree rotation(s) to restore balance factor to {-1, 0, +1})

#### 💡 Explanation & Pedagogical Step
> Any node with Balance Factor +2 or -2 violates the AVL balance invariant and triggers tree rotation(s).

---

### Question 20: CALCULATE BALANCE FACTOR (EASY)
- **Question ID**: EXP-AVL-04
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: AVL Trees (Balance Factor Calculation)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL EASY | **Time Limit**: 0.20 SEC

#### 📌 Problem Description
Write a function `getBalanceFactor(left_height, right_height)` that returns `left_height - right_height`.

#### 💻 Code Starter / Snippet
`python
def getBalanceFactor(left_height, right_height):
    # TODO: Return left_height - right_height
    return left_height - right_height

print(getBalanceFactor(3, 2))
`

#### 💡 Explanation & Pedagogical Step
> Return `left_height - right_height`.

---

### Question 21: MIN-HEAP ROOT INVARIANT
- **Question ID**: EXP-HEAP-01
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Heaps (Min-Heap Invariant)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
What is always true about the element stored at index 0 (root) of a valid Min-Heap?

#### 🔘 Options
A. It is the minimum element in the entire heap  ✔ [CORRECT]
B. It is the maximum element in the entire heap
C. It is the median element
D. It is always 0

**Correct Answer**: **Option A** (It is the minimum element in the entire heap)

#### 💡 Explanation & Pedagogical Step
> In a Min-Heap, parent <= children everywhere, making index 0 the global minimum value.

---

### Question 22: MIN-HEAP INSERTION (SIFT-UP)
- **Question ID**: EXP-HEAP-02
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Heaps (Sift-Up Insertion)
- **Question Type**: OUTPUT_PREDICTION | **Points**: 10 PTS
- **Constraints**: N = 4 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
In a Min-Heap [10, 20, 30], key 5 is inserted at the end. After sifting up to restore heap order, what is the array state?

#### 🔘 Options
A. [5, 10, 30, 20]  ✔ [CORRECT]
B. [10, 20, 30, 5]
C. [5, 20, 10, 30]
D. [30, 20, 10, 5]

**Correct Answer**: **Option A** ([5, 10, 30, 20])

#### 💡 Explanation & Pedagogical Step
> 5 is added at end [10, 20, 30, 5]. Sift up: 5 swaps with 20 -> [10, 5, 30, 20], 5 swaps with 10 -> [5, 10, 30, 20].

---

### Question 23: MAX-HEAP EXTRACT-MAX STEP
- **Question ID**: EXP-HEAP-03
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Heaps (Extract Max)
- **Question Type**: ALGORITHM_TRACING | **Points**: 10 PTS
- **Constraints**: N = 5 | **Time Limit**: 0.30 SEC

#### 📌 Problem Description
When extracting the maximum value from a Max-Heap [90, 80, 70, 40, 30], which element is moved to the root before heapifying down?

#### 🔘 Options
A. The last element (30)  ✔ [CORRECT]
B. The second element (80)
C. Element 40
D. Number 0

**Correct Answer**: **Option A** (The last element (30))

#### 💡 Explanation & Pedagogical Step
> Extract-Max replaces root 90 with the last leaf element (30), shrinks size by 1, and calls Heapify-Down on root.

---

### Question 24: CHECK MIN-HEAP PROPERTY FOR 3 NODES (EASY)
- **Question ID**: EXP-HEAP-04
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Heaps (Min-Heap Check)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL EASY | **Time Limit**: 0.20 SEC

#### 📌 Problem Description
Write a function `isMinHeap3(parent, left_child, right_child)` that returns True if parent <= left_child and parent <= right_child.

#### 💻 Code Starter / Snippet
`python
def isMinHeap3(parent, left_child, right_child):
    # TODO: Return True if parent <= left and parent <= right
    return parent <= left_child and parent <= right_child

print(isMinHeap3(5, 10, 15))
`

#### 💡 Explanation & Pedagogical Step
> Return `parent <= left_child and parent <= right_child`.

---


---

# PART II: CHALLENGE MODE QUESTION BANK

## 📊 Question Bank Topic Matrix

| Topic | Coding Problems | Conceptual MCQs | Total Questions | Sourced Platforms |
| :--- | :---: | :---: | :---: | :--- |
| **Sorting** | 3 | 3 | 6 | GeeksforGeeks, HackerRank, Codeforces |
| **Searching** | 2 | 2 | 4 | GeeksforGeeks, Codeforces, LeetCode |
| **Graphs** | 2 | 2 | 4 | GeeksforGeeks, Codeforces |
| **Trees & BST** | 3 | 3 | 6 | GeeksforGeeks, HackerRank, LeetCode |
| **Total** | **10** | **10** | **20** | **Multi-Source Standard** |

---

## 📝 Detailed Question Catalog (Challenge Mode)

### Question 1: COUNT INVERSIONS IN AN ARRAY
- **Question ID**: Q1
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Sorting (Divide & Conquer)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 10⁵, 1 ≤ arr[i] ≤ 10⁹ | **Time Limit**: 1.00 SEC

#### 📌 Problem Statement
Given an integer array `arr`, return the total count of inversions (pairs (i, j) where i < j and arr[i] > arr[j]) using Divide & Conquer in O(N log N) time.

#### 💻 Starter Template / Solution Interface
`python
def countInversions(arr):
    # TODO: Write your Divide & Conquer solution here
    pass

print(countInversions([8, 4, 2, 1]))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | [8, 4, 2, 1] | 6 |
| TC #02 | [1, 2, 3, 4] | 0 |
| TC #03 | [2, 4, 1, 3, 5] | 3 |

#### 💡 Concept Reference Hint
> Modify Merge Sort during the merge phase: when taking an element from the right subarray, it is smaller than all remaining elements in the left subarray.

---

### Question 2: SORTING: BUBBLE SORT SWAP COUNTER
- **Question ID**: Q2
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Sorting (Array Sorting)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 2 ≤ N ≤ 600, 1 ≤ a[i] ≤ 2 × 10⁶ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Given an array of integers, sort the array in ascending order using Bubble Sort and calculate the total number of element swaps required.

#### 💻 Starter Template / Solution Interface
`python
def countBubbleSwaps(a):
    # TODO: Write your Bubble Sort swap counter solution here
    pass

print(countBubbleSwaps([6, 4, 1]))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | [6, 4, 1] | 3 |
| TC #02 | [1, 2, 3] | 0 |
| TC #03 | [3, 2, 1] | 3 |

#### 💡 Concept Reference Hint
> Track swap operations inside the inner loop whenever a[j] > a[j+1]. Return the total swap count.

---

### Question 3: MARK AND TOYS
- **Question ID**: Q3
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Sorting (Greedy Sorting)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ N ≤ 10⁵, 1 ≤ k ≤ 10⁹ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Mark has a budget $k$. Given an array of toy prices, determine the maximum number of toys he can buy.

#### 💻 Starter Template / Solution Interface
`python
def maximumToys(prices, k):
    # TODO: Write your greedy sorting solution here
    pass

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | prices=[1, 12, 5, 111, 200, 1000, 10], k=50 | 4 |
| TC #02 | prices=[1, 2, 3, 4], k=7 | 3 |

#### 💡 Concept Reference Hint
> Sort the toy prices in ascending order, then greedily accumulate prices until the budget $k$ is exceeded.

---

### Question 4: SEARCH IN ROTATED SORTED ARRAY
- **Question ID**: Q4
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Searching (Binary Search)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ N ≤ 10⁴, -10⁴ ≤ target ≤ 10⁴ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Given a rotated sorted array `nums` and a target `target`, return the 0-based index of target, or -1 if not present, in O(log N) time.

#### 💻 Starter Template / Solution Interface
`python
def searchRotated(nums, target):
    # TODO: Write your O(log N) binary search solution here
    pass

print(searchRotated([4, 5, 6, 7, 0, 1, 2], 0))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | nums=[4, 5, 6, 7, 0, 1, 2], target=0 | 4 |
| TC #02 | nums=[4, 5, 6, 7, 0, 1, 2], target=3 | -1 |

#### 💡 Concept Reference Hint
> At least one half of the array (left to mid OR mid to right) is always sorted. Determine which half is sorted and check if target lies within that range.

---

### Question 5: INTERESTING DRINK (CF 706B)
- **Question ID**: Q5
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Searching (Binary Search)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ N ≤ 10⁵, 1 ≤ m ≤ 10⁹ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Given shop drink prices, find the number of shops Vasya can afford for budget $m$ using upper_bound Binary Search in O(log N) time.

#### 💻 Starter Template / Solution Interface
`python
def countAffordableShops(prices, m):
    # TODO: Write your upper_bound binary search solution here
    pass

print(countAffordableShops([3, 10, 8, 6, 11], 6))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | prices=[3, 10, 8, 6, 11], m=6 | 2 |
| TC #02 | prices=[3, 10, 8, 6, 11], m=1 | 0 |

#### 💡 Concept Reference Hint
> Sort the price list once. For each query budget m, use binary search (bisect_right) to count prices ≤ m.

---

### Question 6: BFS TRAVERSAL OF GRAPH
- **Question ID**: Q6
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Graphs (Graph Traversal)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ V ≤ 10⁴, 0 ≤ E ≤ 10⁴ | **Time Limit**: 0.80 SEC

#### 📌 Problem Statement
Given a connected undirected graph with V vertices (0-indexed) and adjacency list `adj`, return the list of nodes visited in BFS order starting from node 0.

#### 💻 Starter Template / Solution Interface
`python
def bfsOfGraph(V, adj):
    # TODO: Write your BFS graph traversal solution here
    pass

print(bfsOfGraph(5, {0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]}))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | V=5, adj={0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]} | [0, 1, 2, 3, 4] |
| TC #02 | V=3, adj={0: [1, 2], 1: [0], 2: [0]} | [0, 1, 2] |

#### 💡 Concept Reference Hint
> Use a FIFO queue and a visited set. Enqueue node 0 first, then iteratively dequeue and explore unvisited neighbors.

---

### Question 7: TWO BUTTONS (CF 520B)
- **Question ID**: Q7
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Graphs (Implicit Graph BFS)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ n, m ≤ 10⁴ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Vasya has number $n$. Button 1 multiplies by 2; Button 2 subtracts 1. Determine minimum button presses to reach $m$.

#### 💻 Starter Template / Solution Interface
`python
def minButtonClicks(n, m):
    # TODO: Write your state BFS or greedy solution here
    pass

print(minButtonClicks(4, 6))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | n=4, m=6 | 2 |
| TC #02 | n=10, m=1 | 9 |

#### 💡 Concept Reference Hint
> Work backwards from m to n: if m is odd, add 1; if m is even and m > n, divide by 2. Count step operations.

---

### Question 8: CHECK IF BINARY TREE IS BST
- **Question ID**: Q8
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Trees (Binary Search Tree)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 10⁴, -10⁹ ≤ val ≤ 10⁹ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Given a binary tree, determine whether it satisfies the valid Binary Search Tree (BST) invariants (Left < Node < Right for all subtrees).

#### 💻 Starter Template / Solution Interface
`python
def isBST(tree):
    # TODO: Write your BST range check solution here
    pass

print(isBST([2, [1, None, None], [3, None, None]]))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | tree=[2, [1, None, None], [3, None, None]] | True |
| TC #02 | tree=[2, [3, None, None], [1, None, None]] | False |

#### 💡 Concept Reference Hint
> Pass valid ranges `(min_val, max_val)` recursively down the tree. For node `val`, check `min_val < val < max_val`.

---

### Question 9: TREE: HEIGHT OF A BINARY TREE
- **Question ID**: Q9
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Trees (Binary Tree)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: 1 ≤ N ≤ 20 | **Time Limit**: 0.40 SEC

#### 📌 Problem Statement
Return the height of a binary tree (number of edges on the longest path from root to a leaf node).

#### 💻 Starter Template / Solution Interface
`python
def getHeight(tree):
    # TODO: Write your tree height recursive solution here
    pass

print(getHeight([3, [2, [1, None, None], None], [5, [4, None, None], [6, None, None]]]))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | tree=[3, [2, [1, None, None], None], [5, [4, None, None], [6, None, None]]] | 2 |
| TC #02 | tree=[1, None, None] | 0 |

#### 💡 Concept Reference Hint
> Height of empty tree is -1. Recursively return `1 + max(height(left), height(right))`.

---

### Question 10: INORDER SUCCESSOR IN BST
- **Question ID**: Q10
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Trees (BST Traversal)
- **Question Type**: CODING | **Points**: 10 PTS
- **Constraints**: N ≤ 10⁴, 1 ≤ val ≤ 10⁵ | **Time Limit**: 0.50 SEC

#### 📌 Problem Statement
Given a BST root and node $X$, find the node with the smallest value greater than $X$'s value in O(h) time.

#### 💻 Starter Template / Solution Interface
`python
def inorderSuccessor(tree, x):
    # TODO: Write your BST Inorder Successor solution here
    pass

print(inorderSuccessor([20, [8, [4, None, None], [12, [10, None, None], [14, None, None]]], [22, None, None]], 8))
`

#### 🧪 Test Suite Matrix
| Test Case ID | Input Data | Expected Output |
| :--- | :--- | :--- |
| TC #01 | tree=[20, [8, ...]], x=8 | 10 |
| TC #02 | tree=[20, [8, ...]], x=14 | 20 |

#### 💡 Concept Reference Hint
> Traverse from root: if root.val > X.val, save root as candidate successor and move left; else move right.

---

### Question 11: MERGE SORT COMPLEXITY ANALYSIS
- **Question ID**: Q11
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Sorting (Algorithm Analysis)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
What is the tight worst-case Time Complexity and Space Complexity of standard Merge Sort on an array of size N?

#### 🔘 Multiple Choice Options
A. Time: O(N²), Space: O(1)
B. Time: O(N log N), Space: O(N)  ✔ [CORRECT]
C. Time: O(N log N), Space: O(1)
D. Time: O(N²), Space: O(N)

**Correct Answer**: **Option B** (Time: O(N log N), Space: O(N))

#### 💡 Concept Reference Hint
> Merge Sort recursively divides array into halves (O(log N) depth) and allocates an auxiliary array of size N to merge elements.

---

### Question 12: QUICK SORT WORST-CASE BEHAVIOR
- **Question ID**: Q12
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Sorting (Algorithm Analysis)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
Under which condition does standard Quick Sort exhibit its worst-case time complexity of O(N²)?

#### 🔘 Multiple Choice Options
A. Array is already sorted and the first or last element is chosen as the pivot  ✔ [CORRECT]
B. Pivot is always chosen as the exact median element of the subarray
C. Array elements are distinct and uniformly distributed in random order
D. Randomized pivot selection strategy is applied

**Correct Answer**: **Option A** (Array is already sorted and the first or last element is chosen as the pivot)

#### 💡 Concept Reference Hint
> Selecting extreme elements as pivot in a sorted array creates extremely unbalanced partitions of size 0 and N-1.

---

### Question 13: BINARY SEARCH PREREQUISITES
- **Question ID**: Q13
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Searching (Algorithm Prerequisites)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
What is the mandatory prerequisite condition required to execute Binary Search on a sequence in O(log N) time?

#### 🔘 Multiple Choice Options
A. The array elements must all be distinct prime numbers
B. The sequence must be stored in a linked list structure
C. The sequence must be sorted in monotonic order (ascending or descending)  ✔ [CORRECT]
D. The total array size must be an exact power of 2

**Correct Answer**: **Option C** (The sequence must be sorted in monotonic order (ascending or descending))

#### 💡 Concept Reference Hint
> Binary search relies on monotonic ordering to eliminate half the remaining elements at each step.

---

### Question 14: INTEGER OVERFLOW IN BINARY SEARCH
- **Question ID**: Q14
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Searching (Implementation Safety)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
In production code, why is `mid = low + (high - low) / 2` preferred over `mid = (low + high) / 2`?

#### 🔘 Multiple Choice Options
A. It executes twice as fast at hardware instruction level
B. It prevents integer overflow when (low + high) exceeds maximum 32-bit integer capacity  ✔ [CORRECT]
C. It automatically handles floating-point inputs
D. It avoids L1 cache misses in modern processors

**Correct Answer**: **Option B** (It prevents integer overflow when (low + high) exceeds maximum 32-bit integer capacity)

#### 💡 Concept Reference Hint
> If low + high exceeds INT_MAX (2,147,483,647), it overflows to a negative number causing out-of-bounds indexing.

---

### Question 15: BFS VS DFS GRAPH DATA STRUCTURES
- **Question ID**: Q15
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Graphs (Data Structures)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
Which data structures are fundamentally used to implement Breadth-First Search (BFS) and Depth-First Search (DFS) graph traversals respectively?

#### 🔘 Multiple Choice Options
A. BFS uses Stack; DFS uses Queue
B. BFS uses Queue (FIFO); DFS uses Stack (LIFO / Recursion)  ✔ [CORRECT]
C. BFS uses Priority Queue; DFS uses Hash Table
D. BFS uses Array; DFS uses Binary Heap

**Correct Answer**: **Option B** (BFS uses Queue (FIFO); DFS uses Stack (LIFO / Recursion))

#### 💡 Concept Reference Hint
> BFS explores level-by-level using a Queue (FIFO); DFS explores as deep as possible using a Stack (LIFO).

---

### Question 16: SHORTEST PATH IN UNWEIGHTED GRAPHS
- **Question ID**: Q16
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Graphs (Shortest Path)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
Which algorithm guarantees finding the shortest path from a single source in an unweighted graph in O(V + E) time?

#### 🔘 Multiple Choice Options
A. Dijkstra's Algorithm
B. Floyd-Warshall Algorithm
C. Breadth-First Search (BFS)  ✔ [CORRECT]
D. Bellman-Ford Algorithm

**Correct Answer**: **Option C** (Breadth-First Search (BFS))

#### 💡 Concept Reference Hint
> In unweighted graphs, BFS visits nodes in increasing order of distance from source, guaranteeing shortest path in O(V + E).

---

### Question 17: BST SEARCH WORST-CASE COMPLEXITY
- **Question ID**: Q17
- **Source**: HackerRank [HACKERRANK]
- **Topic & Category**: Trees (Tree Complexity)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
What is the worst-case time complexity of searching for a value in an unbalanced (skewed) Binary Search Tree of N nodes?

#### 🔘 Multiple Choice Options
A. O(1)
B. O(log N)
C. O(N)  ✔ [CORRECT]
D. O(N log N)

**Correct Answer**: **Option C** (O(N))

#### 💡 Concept Reference Hint
> A skewed BST degrades into a single linked list of depth N, requiring O(N) operations in worst case.

---

### Question 18: INORDER TRAVERSAL PROPERTY OF BST
- **Question ID**: Q18
- **Source**: GeeksforGeeks [GFG]
- **Topic & Category**: Trees (Tree Traversal)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
Performing an Inorder traversal (Left, Root, Right) on a valid Binary Search Tree produces which output sequence?

#### 🔘 Multiple Choice Options
A. Elements in strictly reverse order
B. Elements in sorted ascending order  ✔ [CORRECT]
C. Random unsorted order
D. Elements grouped by node depth

**Correct Answer**: **Option B** (Elements in sorted ascending order)

#### 💡 Concept Reference Hint
> By BST definition, all left children < root < right children. Inorder traversal visits left first, then root, then right, yielding sorted order.

---

### Question 19: BALANCED BINARY TREE HEIGHT
- **Question ID**: Q19
- **Source**: LeetCode [LEETCODE]
- **Topic & Category**: Trees (Tree Height)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
What is the height of a self-balancing binary search tree (such as AVL or Red-Black Tree) containing N nodes?

#### 🔘 Multiple Choice Options
A. O(N)
B. O(log N)  ✔ [CORRECT]
C. O(N²)
D. O(1)

**Correct Answer**: **Option B** (O(log N))

#### 💡 Concept Reference Hint
> Self-balancing binary trees maintain height h = O(log N) through node rotation operations.

---

### Question 20: STABLE SORTING ALGORITHM IDENTIFICATION
- **Question ID**: Q20
- **Source**: Codeforces [CODEFORCES]
- **Topic & Category**: Sorting (Algorithm Stability)
- **Question Type**: MCQ | **Points**: 10 PTS
- **Constraints**: CONCEPTUAL MCQ | **Time Limit**: 0.30 SEC

#### 📌 Problem Statement
Which of the following sorting algorithms is inherently STABLE (preserves the original relative order of equal keys)?

#### 🔘 Multiple Choice Options
A. Quick Sort (in-place)
B. Heap Sort
C. Merge Sort  ✔ [CORRECT]
D. Selection Sort

**Correct Answer**: **Option C** (Merge Sort)

#### 💡 Concept Reference Hint
> Merge Sort maintains relative order of equal elements during the merge operation (`left[i] <= right[j]`).

---
