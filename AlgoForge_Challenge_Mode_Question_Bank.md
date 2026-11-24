# AlgoForge - Challenge Mode Assessment Question Bank
**Project Name**: AlgoForge - Interactive Algorithm & Data Structure Platform
**Course**: Analysis and Design of Data Structures & Algorithms (ADSA)
**Mode**: Challenge Mode (Timed Assessment & Competitive Examination Arena)
**Total Questions**: 20 (10 Coding Problems + 10 Advanced MCQs)
**Target Audience**: Advanced Students, Exam Candidates, Competitive Coders
**Sources**: GeeksforGeeks, HackerRank, Codeforces, LeetCode

---

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
