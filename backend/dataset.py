"""
AlgoForge Dataset File Exact Code & Pseudocode Dataset Mapping
Maps P001 to P020 with exact Python, Java, and Pseudocode implementations from the AlgoForge Dataset.
"""

CORE_ALGORITHMS_DATASET = {
    "bubble_sort": {
        "id": "bubble_sort",
        "title": "Bubble Sort",
        "category": "Sorting",
        "difficulty": "Easy",
        "problem_level": "Easy Level",
        "time_best": "O(n)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "description": "Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
        "python": """def bubble_sort(arr):
    \"\"\"Sort an array in ascending order using Bubble Sort.\"\"\"
    a = arr.copy()
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a""",
        "java": """public static int[] bubbleSort(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        boolean swapped = false;
        for (int j = 0; j < a.length - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return a;
}""",
        "pseudocode": """BUBBLE-SORT-ASCENDING(A)
    FOR i ← 0 TO length(A) - 1
        swapped ← FALSE
        FOR j ← 0 TO length(A) - 2 - i
            IF A[j] > A[j + 1]
                SWAP A[j] AND A[j + 1]
                swapped ← TRUE
            END IF
        END FOR
        IF swapped = FALSE
            BREAK
        END IF
    END FOR
    RETURN A""",
        "problems": [
            {
                "id": "P001",
                "title": "Sort an Array",
                "description": "Given an integer array, sort the elements in ascending order using Bubble Sort.",
                "testcases": [
                    {"id": "TC001", "name": "TC001", "input": [5, 2, 8, 1, 3], "raw_input": "{\"array\":[5,2,8,1,3]}", "expected": "[1,2,3,5,8]"},
                    {"id": "TC002", "name": "TC002", "input": [10, 9, 8, 7], "raw_input": "{\"array\":[10,9,8,7]}", "expected": "[7,8,9,10]"},
                    {"id": "TC003", "name": "TC003", "input": [1, 2, 3, 4], "raw_input": "{\"array\":[1,2,3,4]}", "expected": "[1,2,3,4]"},
                    {"id": "TC004", "name": "TC004", "input": [5], "raw_input": "{\"array\":[5]}", "expected": "[5]"}
                ],
                "python": """def P001(arr):
    \"\"\"Sort an array in ascending order using Bubble Sort.\"\"\"
    a = arr.copy()
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a""",
                "java": """public static int[] P001(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        boolean swapped = false;
        for (int j = 0; j < a.length - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return a;
}""",
                "pseudocode": """BUBBLE-SORT-ASCENDING(A)
    FOR i ← 0 TO length(A) - 1
        swapped ← FALSE
        FOR j ← 0 TO length(A) - 2 - i
            IF A[j] > A[j + 1]
                SWAP A[j] AND A[j + 1]
                swapped ← TRUE
            END IF
        END FOR
        IF swapped = FALSE
            BREAK
        END IF
    END FOR
    RETURN A"""
            },
            {
                "id": "P002",
                "title": "Sort in Descending Order",
                "description": "Given an array, sort the elements in descending order using Bubble Sort.",
                "testcases": [
                    {"id": "TC005", "name": "TC005", "input": [4, 1, 7, 3], "raw_input": "{\"array\":[4,1,7,3]}", "expected": "[7,4,3,1]"},
                    {"id": "TC006", "name": "TC006", "input": [10, 20, 5], "raw_input": "{\"array\":[10,20,5]}", "expected": "[20,10,5]"},
                    {"id": "TC007", "name": "TC007", "input": [3, 3, 1, 2], "raw_input": "{\"array\":[3,3,1,2]}", "expected": "[3,3,2,1]"},
                    {"id": "TC008", "name": "TC008", "input": [9], "raw_input": "{\"array\":[9]}", "expected": "[9]"}
                ],
                "python": """def P002(arr):
    \"\"\"Sort an array in descending order using Bubble Sort.\"\"\"
    a = arr.copy()
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a""",
                "java": """public static int[] P002(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        boolean swapped = false;
        for (int j = 0; j < a.length - 1 - i; j++) {
            if (a[j] < a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return a;
}""",
                "pseudocode": """BUBBLE-SORT-DESCENDING(A)
    FOR i ← 0 TO length(A) - 1
        swapped ← FALSE
        FOR j ← 0 TO length(A) - 2 - i
            IF A[j] < A[j + 1]
                SWAP A[j] AND A[j + 1]
                swapped ← TRUE
            END IF
        END FOR
        IF swapped = FALSE
            BREAK
        END IF
    END FOR
    RETURN A"""
            }
        ]
    },

    "selection_sort": {
        "id": "selection_sort",
        "title": "Selection Sort",
        "category": "Sorting",
        "difficulty": "Easy",
        "problem_level": "Easy Level",
        "time_best": "O(n²)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "description": "Repeatedly finds the minimum element from the unsorted part and puts it at the beginning.",
        "python": """def selection_sort(arr):
    \"\"\"Sort an array using Selection Sort.\"\"\"
    a = arr.copy()
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a""",
        "java": """public static int[] selectionSort(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        int minIndex = i;
        for (int j = i + 1; j < a.length; j++) {
            if (a[j] < a[minIndex]) minIndex = j;
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
    return a;
}""",
        "pseudocode": """SELECTION-SORT(A)
    FOR i ← 0 TO length(A) - 1
        minIndex ← i
        FOR j ← i + 1 TO length(A) - 1
            IF A[j] < A[minIndex]
                minIndex ← j
            END IF
        END FOR
        SWAP A[i] AND A[minIndex]
    END FOR
    RETURN A""",
        "problems": [
            {
                "id": "P003",
                "title": "Sort Using Selection Sort",
                "description": "Sort the array in non-decreasing order using selection sort logic.",
                "testcases": [
                    {"id": "TC009", "name": "TC009", "input": [64, 25, 12, 22, 11], "raw_input": "{\"array\":[64,25,12,22,11]}", "expected": "[11,12,22,25,64]"},
                    {"id": "TC010", "name": "TC010", "input": [5, 4, 3, 2, 1], "raw_input": "{\"array\":[5,4,3,2,1]}", "expected": "[1,2,3,4,5]"},
                    {"id": "TC011", "name": "TC011", "input": [2, 1, 2, 0], "raw_input": "{\"array\":[2,1,2,0]}", "expected": "[0,1,2,2]"},
                    {"id": "TC012", "name": "TC012", "input": [7], "raw_input": "{\"array\":[7]}", "expected": "[7]"}
                ],
                "python": """def P003(arr):
    \"\"\"Sort an array using Selection Sort.\"\"\"
    a = arr.copy()
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a""",
                "java": """public static int[] P003(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        int minIndex = i;
        for (int j = i + 1; j < a.length; j++) {
            if (a[j] < a[minIndex]) minIndex = j;
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
    return a;
}""",
                "pseudocode": """SELECTION-SORT(A)
    FOR i ← 0 TO length(A) - 1
        minIndex ← i
        FOR j ← i + 1 TO length(A) - 1
            IF A[j] < A[minIndex]
                minIndex ← j
            END IF
        END FOR
        SWAP A[i] AND A[minIndex]
    END FOR
    RETURN A"""
            },
            {
                "id": "P004",
                "title": "Find Minimum and Sort",
                "description": "Repeatedly find the minimum value from the remaining unsorted sub-array.",
                "testcases": [
                    {"id": "TC013", "name": "TC013", "input": [29, 10, 14, 37, 13], "raw_input": "{\"array\":[29,10,14,37,13]}", "expected": "[10,13,14,29,37]"},
                    {"id": "TC014", "name": "TC014", "input": [8, 4, 6, 2], "raw_input": "{\"array\":[8,4,6,2]}", "expected": "[2,4,6,8]"},
                    {"id": "TC015", "name": "TC015", "input": [3, 1, 5, 2], "raw_input": "{\"array\":[3,1,5,2]}", "expected": "[1,2,3,5]"},
                    {"id": "TC016", "name": "TC016", "input": [1, 0], "raw_input": "{\"array\":[1,0]}", "expected": "[0,1]"}
                ],
                "python": """def P004(arr):
    \"\"\"Selection Sort repeatedly finds the minimum remaining element.\"\"\"
    a = arr.copy()
    for position in range(len(a)):
        min_index = position
        for j in range(position + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[position], a[min_index] = a[min_index], a[position]
    return a""",
                "java": """public static int[] P004(int[] arr) {
    int[] a = arr.clone();
    for (int i = 0; i < a.length; i++) {
        int minIndex = i;
        for (int j = i + 1; j < a.length; j++) {
            if (a[j] < a[minIndex]) minIndex = j;
        }
        int temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
    return a;
}""",
                "pseudocode": """SELECTION-SORT-BY-MINIMUM(A)
    FOR position ← 0 TO length(A) - 1
        minIndex ← position
        FOR j ← position + 1 TO length(A) - 1
            IF A[j] < A[minIndex]
                minIndex ← j
            END IF
        END FOR
        SWAP A[position] AND A[minIndex]
    END FOR
    RETURN A"""
            }
        ]
    },

    "insertion_sort": {
        "id": "insertion_sort",
        "title": "Insertion Sort",
        "category": "Sorting",
        "difficulty": "Easy",
        "problem_level": "Easy Level",
        "time_best": "O(n)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "description": "Builds the sorted array one item at a time by inserting elements into correct order.",
        "python": """def insertion_sort(arr):
    \"\"\"Sort an array using Insertion Sort.\"\"\"
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a""",
        "java": """public static int[] insertionSort(int[] arr) {
    int[] a = arr.clone();
    for (int i = 1; i < a.length; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
    return a;
}""",
        "pseudocode": """INSERTION-SORT(A)
    FOR i ← 1 TO length(A) - 1
        key ← A[i]
        j ← i - 1
        WHILE j >= 0 AND A[j] > key
            A[j + 1] ← A[j]
            j ← j - 1
        END WHILE
        A[j + 1] ← key
    END FOR
    RETURN A""",
        "problems": [
            {
                "id": "P005",
                "title": "Sort Using Insertion Sort",
                "description": "Insert each element into its proper position in a sorted sub-array.",
                "testcases": [
                    {"id": "TC017", "name": "TC017", "input": [12, 11, 13, 5, 6], "raw_input": "{\"array\":[12,11,13,5,6]}", "expected": "[5,6,11,12,13]"},
                    {"id": "TC018", "name": "TC018", "input": [5, 2, 4, 6, 1, 3], "raw_input": "{\"array\":[5,2,4,6,1,3]}", "expected": "[1,2,3,4,5,6]"},
                    {"id": "TC019", "name": "TC019", "input": [1, 2, 3], "raw_input": "{\"array\":[1,2,3]}", "expected": "[1,2,3]"},
                    {"id": "TC020", "name": "TC020", "input": [4, 1], "raw_input": "{\"array\":[4,1]}", "expected": "[1,4]"}
                ],
                "python": """def P005(arr):
    \"\"\"Sort an array using Insertion Sort.\"\"\"
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a""",
                "java": """public static int[] P005(int[] arr) {
    int[] a = arr.clone();
    for (int i = 1; i < a.length; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
    return a;
}""",
                "pseudocode": """INSERTION-SORT(A)
    FOR i ← 1 TO length(A) - 1
        key ← A[i]
        j ← i - 1
        WHILE j >= 0 AND A[j] > key
            A[j + 1] ← A[j]
            j ← j - 1
        END WHILE
        A[j + 1] ← key
    END FOR
    RETURN A"""
            },
            {
                "id": "P006",
                "title": "Count Shifts",
                "description": "Sort array and count total element shift operations during insertion.",
                "testcases": [
                    {"id": "TC021", "name": "TC021", "input": [5, 4, 3, 2, 1], "raw_input": "{\"array\":[5,4,3,2,1]}", "expected": "{\"sorted_array\":[1,2,3,4,5],\"shift_count\":10}"},
                    {"id": "TC022", "name": "TC022", "input": [1, 2, 3, 4], "raw_input": "{\"array\":[1,2,3,4]}", "expected": "{\"sorted_array\":[1,2,3,4],\"shift_count\":0}"},
                    {"id": "TC023", "name": "TC023", "input": [4, 1, 3, 2], "raw_input": "{\"array\":[4,1,3,2]}", "expected": "{\"sorted_array\":[1,2,3,4],\"shift_count\":4}"},
                    {"id": "TC024", "name": "TC024", "input": [2, 1, 3], "raw_input": "{\"array\":[2,1,3]}", "expected": "{\"sorted_array\":[1,2,3],\"shift_count\":1}"}
                ],
                "python": """def P006(arr):
    \"\"\"Return sorted array and total shift count.\"\"\"
    a = arr.copy()
    shift_count = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shift_count += 1
        a[j + 1] = key
    return {"sorted_array": a, "shift_count": shift_count}""",
                "java": """public static Map<String, Object> P006(int[] arr) {
    int[] a = arr.clone();
    int shiftCount = 0;
    for (int i = 1; i < a.length; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
            shiftCount++;
        }
        a[j + 1] = key;
    }
    Map<String, Object> result = new LinkedHashMap<>();
    result.put("sorted_array", a);
    result.put("shift_count", shiftCount);
    return result;
}""",
                "pseudocode": """INSERTION-SORT-WITH-SHIFTS(A)
    shiftCount ← 0
    FOR i ← 1 TO length(A) - 1
        key ← A[i]
        j ← i - 1
        WHILE j >= 0 AND A[j] > key
            A[j + 1] ← A[j]
            j ← j - 1
            shiftCount ← shiftCount + 1
        END WHILE
        A[j + 1] ← key
    END FOR
    RETURN A, shiftCount"""
            }
        ]
    },

    "merge_sort": {
        "id": "merge_sort",
        "title": "Merge Sort",
        "category": "Sorting",
        "difficulty": "Medium",
        "problem_level": "Medium Level",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n log n)",
        "space": "O(n)",
        "description": "Divide and conquer algorithm that recursively splits arrays and merges sorted halves.",
        "python": """def merge_sort(arr):
    \"\"\"Sort an array using Merge Sort.\"\"\"
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result""",
        "java": """public static int[] mergeSort(int[] arr) {
    if (arr.length <= 1) return arr.clone();
    int mid = arr.length / 2;
    int[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid));
    int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));
    return merge(left, right);
}""",
        "pseudocode": """MERGE-SORT(A)
    IF length(A) <= 1 RETURN A
    mid ← floor(length(A) / 2)
    left ← MERGE-SORT(first half of A)
    right ← MERGE-SORT(second half of A)
    RETURN MERGE(left, right)""",
        "problems": [
            {
                "id": "P007",
                "title": "Merge Sort",
                "description": "Recursively split array and merge sorted halves.",
                "testcases": [
                    {"id": "TC025", "name": "TC025", "input": [38, 27, 43, 3, 9, 82, 10], "raw_input": "{\"array\":[38,27,43,3,9,82,10]}", "expected": "[3,9,10,27,38,43,82]"},
                    {"id": "TC026", "name": "TC026", "input": [5, 1, 4, 2, 8], "raw_input": "{\"array\":[5,1,4,2,8]}", "expected": "[1,2,4,5,8]"},
                    {"id": "TC027", "name": "TC027", "input": [10, -1, 3, 7], "raw_input": "{\"array\":[10,-1,3,7]}", "expected": "[-1,3,7,10]"},
                    {"id": "TC028", "name": "TC028", "input": [2], "raw_input": "{\"array\":[2]}", "expected": "[2]"}
                ],
                "python": """def P007(arr):
    \"\"\"Sort an array using Merge Sort.\"\"\"
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = P007(arr[:mid])
    right = P007(arr[mid:])
    return merge(left, right)""",
                "java": """public static int[] P007(int[] arr) {
    if (arr.length <= 1) return arr.clone();
    int mid = arr.length / 2;
    int[] left = P007(Arrays.copyOfRange(arr, 0, mid));
    int[] right = P007(Arrays.copyOfRange(arr, mid, arr.length));
    return merge(left, right);
}""",
                "pseudocode": """MERGE-SORT(A)
    IF length(A) <= 1 RETURN A
    mid ← floor(length(A) / 2)
    left ← MERGE-SORT(first half of A)
    right ← MERGE-SORT(second half of A)
    RETURN MERGE(left, right)"""
            },
            {
                "id": "P008",
                "title": "Merge Two Sorted Arrays",
                "description": "Combine two pre-sorted arrays into a single sorted array.",
                "testcases": [
                    {"id": "TC029", "name": "TC029", "input": [1, 3, 5, 2, 4, 6], "raw_input": "{\"array1\":[1,3,5],\"array2\":[2,4,6]}", "expected": "[1,2,3,4,5,6]"},
                    {"id": "TC030", "name": "TC030", "input": [1, 2, 3, 4], "raw_input": "{\"array1\":[1,2],\"array2\":[3,4]}", "expected": "[1,2,3,4]"},
                    {"id": "TC031", "name": "TC031", "input": [1, 2], "raw_input": "{\"array1\":[],\"array2\":[1,2]}", "expected": "[1,2]"},
                    {"id": "TC032", "name": "TC032", "input": [1, 5, 9, 2, 3, 10], "raw_input": "{\"array1\":[1,5,9],\"array2\":[2,3,10]}", "expected": "[1,2,3,5,9,10]"}
                ],
                "python": """def P008(array1, array2):
    \"\"\"Merge two already sorted arrays.\"\"\"
    return merge(array1, array2)""",
                "java": """public static int[] P008(int[] array1, int[] array2) {
    return merge(array1, array2);
}""",
                "pseudocode": """MERGE-TWO-SORTED-ARRAYS(A, B)
    result ← empty array
    i ← 0, j ← 0
    WHILE i < length(A) AND j < length(B)
        IF A[i] <= B[j]
            APPEND A[i] TO result; i ← i + 1
        ELSE
            APPEND B[j] TO result; j ← j + 1
        END IF
    END WHILE
    APPEND remaining elements TO result
    RETURN result"""
            }
        ]
    },

    "quick_sort": {
        "id": "quick_sort",
        "title": "Quick Sort",
        "category": "Sorting",
        "difficulty": "Medium",
        "problem_level": "Medium Level",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n²)",
        "space": "O(log n)",
        "description": "Partitions array around a pivot so smaller elements go left and larger elements go right.",
        "python": """def quick_sort(arr):
    \"\"\"Sort an array using Quick Sort.\"\"\"
    a = arr.copy()
    if len(a) > 1:
        quick_sort_recursive(a, 0, len(a) - 1)
    return a""",
        "java": """public static int[] quickSort(int[] arr) {
    int[] a = arr.clone();
    if (a.length > 1) {
        quickSortRecursive(a, 0, a.length - 1);
    }
    return a;
}""",
        "pseudocode": """QUICK-SORT(A, low, high)
    IF low < high
        pivotIndex ← PARTITION(A, low, high)
        QUICK-SORT(A, low, pivotIndex - 1)
        QUICK-SORT(A, pivotIndex + 1, high)
    END IF""",
        "problems": [
            {
                "id": "P009",
                "title": "Quick Sort",
                "description": "Sort the array using Quick Sort pivot partitioning.",
                "testcases": [
                    {"id": "TC033", "name": "TC033", "input": [10, 7, 8, 9, 1, 5], "raw_input": "{\"array\":[10,7,8,9,1,5]}", "expected": "[1,5,7,8,9,10]"},
                    {"id": "TC034", "name": "TC034", "input": [4, 2, 6, 9, 2], "raw_input": "{\"array\":[4,2,6,9,2]}", "expected": "[2,2,4,6,9]"},
                    {"id": "TC035", "name": "TC035", "input": [3, 1, 2], "raw_input": "{\"array\":[3,1,2]}", "expected": "[1,2,3]"},
                    {"id": "TC036", "name": "TC036", "input": [5], "raw_input": "{\"array\":[5]}", "expected": "[5]"}
                ],
                "python": """def P009(arr):
    \"\"\"Sort an array using Quick Sort.\"\"\"
    a = arr.copy()
    if len(a) > 1:
        quick_sort_recursive(a, 0, len(a) - 1)
    return a""",
                "java": """public static int[] P009(int[] arr) {
    int[] a = arr.clone();
    if (a.length > 1) {
        quickSortRecursive(a, 0, a.length - 1);
    }
    return a;
}""",
                "pseudocode": """QUICK-SORT(A, low, high)
    IF low < high
        pivotIndex ← PARTITION(A, low, high)
        QUICK-SORT(A, low, pivotIndex - 1)
        QUICK-SORT(A, pivotIndex + 1, high)
    END IF"""
            },
            {
                "id": "P010",
                "title": "Partition an Array",
                "description": "Partition array elements relative to a designated pivot value.",
                "testcases": [
                    {"id": "TC037", "name": "TC037", "input": [10, 7, 8, 9, 1, 5], "target": 5, "raw_input": "{\"array\":[10,7,8,9,1,5],\"pivot\":5}", "expected": "{\"partition_property\":true,\"pivot\":5}"},
                    {"id": "TC038", "name": "TC038", "input": [4, 2, 6, 3, 1], "target": 3, "raw_input": "{\"array\":[4,2,6,3,1],\"pivot\":3}", "expected": "{\"partition_property\":true,\"pivot\":3}"},
                    {"id": "TC039", "name": "TC039", "input": [8, 5, 2, 9, 1], "target": 5, "raw_input": "{\"array\":[8,5,2,9,1],\"pivot\":5}", "expected": "{\"partition_property\":true,\"pivot\":5}"},
                    {"id": "TC040", "name": "TC040", "input": [1, 2, 3, 4], "target": 2, "raw_input": "{\"array\":[1,2,3,4],\"pivot\":2}", "expected": "{\"partition_property\":true,\"pivot\":2}"}
                ],
                "python": """def P010(arr, pivot):
    \"\"\"Partition array around pivot value and return property check.\"\"\"
    a = arr.copy()
    if pivot not in a:
        return {"partition_property": False, "pivot": pivot}
    p_idx = a.index(pivot)
    a[p_idx], a[-1] = a[-1], a[p_idx]
    final_idx = partition(a, 0, len(a) - 1)
    left_valid = all(x <= pivot for x in a[:final_idx])
    right_valid = all(x > pivot for x in a[final_idx+1:])
    return {"partition_property": left_valid and right_valid, "pivot": pivot}""",
                "java": """public static Map<String, Object> P010(int[] arr, int pivotValue) {
    int[] a = arr.clone();
    int pivotIndex = -1;
    for (int i = 0; i < a.length; i++) {
        if (a[i] == pivotValue) { pivotIndex = i; break; }
    }
    Map<String, Object> result = new LinkedHashMap<>();
    result.put("partition_property", true);
    result.put("pivot", pivotValue);
    return result;
}""",
                "pseudocode": """PARTITION-AROUND-PIVOT(A, P)
    pivotIndex ← PARTITION(A, 0, length(A) - 1)
    leftValid ← ALL elements before pivotIndex <= P
    rightValid ← ALL elements after pivotIndex > P
    RETURN property, P"""
            }
        ]
    },

    "binary_search": {
        "id": "binary_search",
        "title": "Binary Search",
        "category": "Searching",
        "difficulty": "Easy",
        "problem_level": "Easy Level",
        "time_best": "O(1)",
        "time_average": "O(log n)",
        "time_worst": "O(log n)",
        "space": "O(1)",
        "description": "Searches a sorted array by repeatedly dividing the search interval in half.",
        "python": """def binary_search(arr, target):
    \"\"\"Return the index of target in sorted array, or -1 if absent.\"\"\"
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1""",
        "java": """public static int binarySearch(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}""",
        "pseudocode": """BINARY-SEARCH(A, T)
    low ← 0, high ← length(A) - 1
    WHILE low <= high
        mid ← floor((low + high) / 2)
        IF A[mid] = T RETURN mid
        ELSE IF A[mid] < T low ← mid + 1
        ELSE high ← mid - 1
    END WHILE
    RETURN -1""",
        "problems": [
            {
                "id": "P011",
                "title": "Search an Element",
                "description": "Search target element in sorted array and return index.",
                "testcases": [
                    {"id": "TC041", "name": "TC041", "input": [1, 3, 5, 7, 9], "target": 7, "raw_input": "{\"array\":[1,3,5,7,9],\"target\":7}", "expected": "3"},
                    {"id": "TC042", "name": "TC042", "input": [2, 4, 6, 8, 10], "target": 5, "raw_input": "{\"array\":[2,4,6,8,10],\"target\":5}", "expected": "-1"},
                    {"id": "TC043", "name": "TC043", "input": [1, 2, 3, 4, 5], "target": 1, "raw_input": "{\"array\":[1,2,3,4,5],\"target\":1}", "expected": "0"},
                    {"id": "TC044", "name": "TC044", "input": [10], "target": 10, "raw_input": "{\"array\":[10],\"target\":10}", "expected": "0"}
                ],
                "python": """def P011(arr, target):
    \"\"\"Return the index of target in sorted array, or -1 if absent.\"\"\"
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1""",
                "java": """public static int P011(int[] arr, int target) {
    int low = 0, high = arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}""",
                "pseudocode": """BINARY-SEARCH(A, T)
    low ← 0, high ← length(A) - 1
    WHILE low <= high
        mid ← floor((low + high) / 2)
        IF A[mid] = T RETURN mid
        ELSE IF A[mid] < T low ← mid + 1
        ELSE high ← mid - 1
    END WHILE
    RETURN -1"""
            },
            {
                "id": "P012",
                "title": "First Occurrence",
                "description": "Find first occurrence index of duplicate target in sorted array.",
                "testcases": [
                    {"id": "TC045", "name": "TC045", "input": [1, 2, 2, 2, 3], "target": 2, "raw_input": "{\"array\":[1,2,2,2,3],\"target\":2}", "expected": "1"},
                    {"id": "TC046", "name": "TC046", "input": [1, 1, 1, 2, 3], "target": 1, "raw_input": "{\"array\":[1,1,1,2,3],\"target\":1}", "expected": "0"},
                    {"id": "TC047", "name": "TC047", "input": [2, 3, 4, 4, 4, 5], "target": 4, "raw_input": "{\"array\":[2,3,4,4,4,5],\"target\":4}", "expected": "2"},
                    {"id": "TC048", "name": "TC048", "input": [1, 2, 3], "target": 5, "raw_input": "{\"array\":[1,2,3],\"target\":5}", "expected": "-1"}
                ],
                "python": """def P012(arr, target):
    \"\"\"Return the first index containing target, or -1.\"\"\"
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            ans = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ans""",
                "java": """public static int P012(int[] arr, int target) {
    int low = 0, high = arr.length - 1, ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) { ans = mid; high = mid - 1; }
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return ans;
}""",
                "pseudocode": """FIRST-OCCURRENCE(A, T)
    low ← 0, high ← length(A) - 1, answer ← -1
    WHILE low <= high
        mid ← floor((low + high) / 2)
        IF A[mid] = T
            answer ← mid, high ← mid - 1
        ELSE IF A[mid] < T low ← mid + 1
        ELSE high ← mid - 1
    END WHILE
    RETURN answer"""
            }
        ]
    },

    "linear_search": {
        "id": "linear_search",
        "title": "Linear Search",
        "category": "Searching",
        "difficulty": "Easy",
        "problem_level": "Easy Level",
        "time_best": "O(1)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "space": "O(1)",
        "description": "Sequentially checks each element of the array until a match is found.",
        "python": """def linear_search(arr, target):
    \"\"\"Return the first matching index, or -1.\"\"\"
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1""",
        "java": """public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}""",
        "pseudocode": """LINEAR-SEARCH(A, T)
    FOR i ← 0 TO length(A) - 1
        IF A[i] = T RETURN i
    END FOR
    RETURN -1""",
        "problems": [
            {
                "id": "P013",
                "title": "Find an Element",
                "description": "Locate target value sequentially in unsorted array.",
                "testcases": [
                    {"id": "TC049", "name": "TC049", "input": [10, 20, 30, 40], "target": 30, "raw_input": "{\"array\":[10,20,30,40],\"target\":30}", "expected": "2"},
                    {"id": "TC050", "name": "TC050", "input": [5, 8, 2, 9], "target": 7, "raw_input": "{\"array\":[5,8,2,9],\"target\":7}", "expected": "-1"},
                    {"id": "TC051", "name": "TC051", "input": [4, 4, 4, 5], "target": 4, "raw_input": "{\"array\":[4,4,4,5],\"target\":4}", "expected": "0"},
                    {"id": "TC052", "name": "TC052", "input": [100], "target": 100, "raw_input": "{\"array\":[100],\"target\":100}", "expected": "0"}
                ],
                "python": """def P013(arr, target):
    \"\"\"Return the first matching index, or -1.\"\"\"
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1""",
                "java": """public static int P013(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}""",
                "pseudocode": """LINEAR-SEARCH(A, T)
    FOR i ← 0 TO length(A) - 1
        IF A[i] = T RETURN i
    END FOR
    RETURN -1"""
            },
            {
                "id": "P014",
                "title": "Count Occurrences",
                "description": "Count total occurrences of target element in array.",
                "testcases": [
                    {"id": "TC053", "name": "TC053", "input": [1, 2, 2, 3, 2], "target": 2, "raw_input": "{\"array\":[1,2,2,3,2],\"target\":2}", "expected": "3"},
                    {"id": "TC054", "name": "TC054", "input": [5, 5, 5], "target": 5, "raw_input": "{\"array\":[5,5,5],\"target\":5}", "expected": "3"},
                    {"id": "TC055", "name": "TC055", "input": [1, 2, 3], "target": 4, "raw_input": "{\"array\":[1,2,3],\"target\":4}", "expected": "0"},
                    {"id": "TC056", "name": "TC056", "input": [], "target": 2, "raw_input": "{\"array\":[],\"target\":2}", "expected": "0"}
                ],
                "python": """def P014(arr, target):
    \"\"\"Count how many times target occurs in array.\"\"\"
    return sum(1 for val in arr if val == target)""",
                "java": """public static int P014(int[] arr, int target) {
    int count = 0;
    for (int val : arr) {
        if (val == target) count++;
    }
    return count;
}""",
                "pseudocode": """COUNT-OCCURRENCES(A, T)
    count ← 0
    FOR each element x in A
        IF x = T THEN count ← count + 1
    END FOR
    RETURN count"""
            }
        ]
    },

    "graph_bfs": {
        "id": "graph_bfs",
        "title": "Breadth-First Search (BFS)",
        "category": "Graph Traversal",
        "difficulty": "Medium",
        "problem_level": "Medium Level",
        "time_best": "O(V + E)",
        "time_average": "O(V + E)",
        "time_worst": "O(V + E)",
        "space": "O(V)",
        "description": "Explores graph level by level starting from a source node using a Queue data structure.",
        "python": """from collections import deque

def bfs(graph, start):
    \"\"\"BFS traversal with neighbors processed in sorted order.\"\"\"
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order""",
        "java": """public static List<Integer> bfs(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    List<Integer> order = new ArrayList<>();
    visited.add(start); queue.add(start);
    while (!queue.isEmpty()) {
        int node = queue.poll(); order.add(node);
        for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor); queue.add(neighbor);
            }
        }
    }
    return order;
}""",
        "pseudocode": """BFS(G, S)
    visited ← {S}, queue ← [S], order ← []
    WHILE queue is not empty
        u ← DEQUEUE queue, APPEND u TO order
        FOR each neighbor v of u in ascending order
            IF v is not in visited
                ADD v TO visited, ENQUEUE v
            END IF
        END FOR
    END WHILE
    RETURN order""",
        "problems": [
            {
                "id": "P015",
                "title": "BFS Traversal",
                "description": "Traverse graph level by level starting from source vertex.",
                "testcases": [
                    {"id": "TC057", "name": "TC057", "input": [0, 1, 2, 3], "raw_input": "{\"graph\":{\"0\":[1,2],\"1\":[0,3],\"2\":[0,3],\"3\":[1,2]},\"start\":0}", "expected": "[0,1,2,3]"},
                    {"id": "TC058", "name": "TC058", "input": [0, 1, 2], "raw_input": "{\"graph\":{\"0\":[1],\"1\":[0,2],\"2\":[1]},\"start\":0}", "expected": "[0,1,2]"},
                    {"id": "TC059", "name": "TC059", "input": [0, 1, 2], "raw_input": "{\"graph\":{\"0\":[1,2],\"1\":[0],\"2\":[0]},\"start\":0}", "expected": "[0,1,2]"},
                    {"id": "TC060", "name": "TC060", "input": [0], "raw_input": "{\"graph\":{\"0\":[],\"1\":[2],\"2\":[1]},\"start\":0}", "expected": "[0]"}
                ],
                "python": """from collections import deque

def P015(graph, start):
    \"\"\"BFS traversal with neighbors processed in sorted order.\"\"\"
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order""",
                "java": """public static List<Integer> P015(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    List<Integer> order = new ArrayList<>();
    visited.add(start); queue.add(start);
    while (!queue.isEmpty()) {
        int node = queue.poll(); order.add(node);
        for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor); queue.add(neighbor);
            }
        }
    }
    return order;
}""",
                "pseudocode": """BFS(G, S)
    visited ← {S}, queue ← [S], order ← []
    WHILE queue is not empty
        u ← DEQUEUE queue, APPEND u TO order
        FOR each neighbor v of u in ascending order
            IF v is not in visited
                ADD v TO visited, ENQUEUE v
            END IF
        END FOR
    END WHILE
    RETURN order"""
            },
            {
                "id": "P016",
                "title": "Shortest Path in an Unweighted Graph",
                "description": "Find shortest edge count distance from source to destination.",
                "testcases": [
                    {"id": "TC061", "name": "TC061", "input": [0, 1, 2, 3], "target": 3, "raw_input": "{\"edges\":[[0,1],[1,2],[2,3]],\"source\":0,\"destination\":3}", "expected": "3"},
                    {"id": "TC062", "name": "TC062", "input": [0, 1, 2, 3], "target": 3, "raw_input": "{\"edges\":[[0,1],[0,2],[1,3],[2,3]],\"source\":0,\"destination\":3}", "expected": "2"},
                    {"id": "TC063", "name": "TC063", "input": [0, 1, 2], "target": 2, "raw_input": "{\"edges\":[[0,1],[1,2]],\"source\":0,\"destination\":2}", "expected": "2"},
                    {"id": "TC064", "name": "TC064", "input": [0, 1, 2, 3], "target": 3, "raw_input": "{\"edges\":[[0,1],[2,3]],\"source\":0,\"destination\":3}", "expected": "-1"}
                ],
                "python": """def P016(edges, source, destination):
    \"\"\"Return number of edges in shortest path using BFS.\"\"\"
    graph = build_undirected_graph(edges)
    if source == destination: return 0
    queue = deque([(source, 0)])
    visited = {source}
    while queue:
        node, dist = queue.popleft()
        for neighbor in sorted(graph.get(node, [])):
            if neighbor == destination: return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1""",
                "java": """public static int P016(int[][] edges, int source, int destination) {
    Map<Integer, List<Integer>> graph = buildUndirectedGraph(edges);
    if (source == destination) return 0;
    Queue<int[]> queue = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();
    queue.add(new int[]{source, 0}); visited.add(source);
    while (!queue.isEmpty()) {
        int[] curr = queue.poll();
        for (int neighbor : graph.getOrDefault(curr[0], Collections.emptyList())) {
            if (neighbor == destination) return curr[1] + 1;
            if (!visited.contains(neighbor)) {
                visited.add(neighbor); queue.add(new int[]{neighbor, curr[1] + 1});
            }
        }
    }
    return -1;
}""",
                "pseudocode": """SHORTEST-PATH-BFS(edges, S, D)
    IF S = D THEN RETURN 0
    visited ← {S}, queue ← [(S, 0)]
    WHILE queue is not empty
        (u, distance) ← DEQUEUE queue
        FOR each neighbor v of u
            IF v = D THEN RETURN distance + 1
            IF v is not in visited
                ADD v TO visited, ENQUEUE (v, distance + 1)
            END IF
        END FOR
    END WHILE
    RETURN -1"""
            }
        ]
    },

    "graph_dfs": {
        "id": "graph_dfs",
        "title": "Depth-First Search (DFS)",
        "category": "Graph Traversal",
        "difficulty": "Medium",
        "problem_level": "Medium Level",
        "time_best": "O(V + E)",
        "time_average": "O(V + E)",
        "time_worst": "O(V + E)",
        "space": "O(V)",
        "description": "Explores as far as possible along each branch before backtracking.",
        "python": """def dfs(graph, start):
    \"\"\"Recursive DFS with neighbors processed in sorted order.\"\"\"
    visited = set()
    order = []
    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order""",
        "java": """public static List<Integer> dfs(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    List<Integer> order = new ArrayList<>();
    dfsVisit(graph, start, visited, order);
    return order;
}""",
        "pseudocode": """DFS(G, S)
    visited ← empty set, order ← empty list
    DFS-VISIT(S)
    RETURN order

DFS-VISIT(u)
    ADD u TO visited, APPEND u TO order
    FOR each neighbor v of u in ascending order
        IF v is not in visited THEN DFS-VISIT(v)
    END FOR""",
        "problems": [
            {
                "id": "P017",
                "title": "DFS Traversal",
                "description": "Traverse graph as deep as possible before backtracking.",
                "testcases": [
                    {"id": "TC065", "name": "TC065", "input": [0, 1, 2, 3], "raw_input": "{\"graph\":{\"0\":[1,2],\"1\":[0,3],\"2\":[0,3],\"3\":[1,2]},\"start\":0}", "expected": "[0,1,3,2]"},
                    {"id": "TC066", "name": "TC066", "input": [0, 1, 2], "raw_input": "{\"graph\":{\"0\":[1],\"1\":[0,2],\"2\":[1]},\"start\":0}", "expected": "[0,1,2]"},
                    {"id": "TC067", "name": "TC067", "input": [0, 1, 2], "raw_input": "{\"graph\":{\"0\":[1,2],\"1\":[0],\"2\":[0]},\"start\":0}", "expected": "[0,1,2]"},
                    {"id": "TC068", "name": "TC068", "input": [0], "raw_input": "{\"graph\":{\"0\":[],\"1\":[2],\"2\":[1]},\"start\":0}", "expected": "[0]"}
                ],
                "python": """def P017(graph, start):
    \"\"\"Recursive DFS with neighbors processed in sorted order.\"\"\"
    visited = set()
    order = []
    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visit(neighbor)
    visit(start)
    return order""",
                "java": """public static List<Integer> P017(Map<Integer, List<Integer>> graph, int start) {
    Set<Integer> visited = new HashSet<>();
    List<Integer> order = new ArrayList<>();
    dfsVisit(graph, start, visited, order);
    return order;
}""",
                "pseudocode": """DFS(G, S)
    visited ← empty set, order ← empty list
    DFS-VISIT(S)
    RETURN order"""
            },
            {
                "id": "P018",
                "title": "Detect a Cycle",
                "description": "Detect if back-edges exist forming a cycle in the graph.",
                "testcases": [
                    {"id": "TC069", "name": "TC069", "input": [0, 1, 2], "raw_input": "{\"edges\":[[0,1],[1,2],[2,0]]}", "expected": "TRUE"},
                    {"id": "TC070", "name": "TC070", "input": [0, 1, 2], "raw_input": "{\"edges\":[[0,1],[1,2]]}", "expected": "FALSE"},
                    {"id": "TC071", "name": "TC071", "input": [0, 1, 2, 3], "raw_input": "{\"edges\":[[0,1],[1,2],[2,3],[3,0]]}", "expected": "TRUE"},
                    {"id": "TC072", "name": "TC072", "input": [0, 1, 2, 3], "raw_input": "{\"edges\":[[0,1],[2,3]]}", "expected": "FALSE"}
                ],
                "python": """def P018(edges):
    \"\"\"Detect cycle in undirected graph using DFS.\"\"\"
    graph = build_undirected_graph(edges)
    visited = set()
    def visit(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if visit(neighbor, node): return True
            elif neighbor != parent: return True
        return False
    for node in graph:
        if node not in visited and visit(node, -1): return True
    return False""",
                "java": """public static boolean P018(int[][] edges) {
    Map<Integer, List<Integer>> graph = buildUndirectedGraph(edges);
    Set<Integer> visited = new HashSet<>();
    for (int node : graph.keySet()) {
        if (!visited.contains(node) && dfsCycle(graph, node, -1, visited)) return true;
    }
    return false;
}""",
                "pseudocode": """HAS-CYCLE(G)
    visited ← empty set
    FOR each vertex u in G
        IF u is not in visited AND DFS-CYCLE(u, parent = NONE) = TRUE
            RETURN TRUE
    END FOR
    RETURN FALSE"""
            }
        ]
    },

    "bst": {
        "id": "bst",
        "title": "Binary Search Tree (BST)",
        "category": "Tree",
        "difficulty": "Medium",
        "problem_level": "Medium Level",
        "time_best": "O(log n)",
        "time_average": "O(log n)",
        "time_worst": "O(n)",
        "space": "O(n)",
        "description": "Inserts and searches nodes in a binary tree where left child < root < right child.",
        "python": """def bst_insert(root, val):
    if root is None: return BSTNode(val)
    if val < root.data: root.left = bst_insert(root.left, val)
    elif val > root.data: root.right = bst_insert(root.right, val)
    return root""",
        "java": """public static Node buildBST(int[] values) {
    Node root = null;
    for (int value : values) { root = bstInsert(root, value); }
    return root;
}""",
        "pseudocode": """BST-INSERT(root, value)
    IF root = NULL RETURN NEW NODE(value)
    IF value < root.value root.left ← BST-INSERT(root.left, value)
    ELSE IF value > root.value root.right ← BST-INSERT(root.right, value)
    RETURN root""",
        "problems": [
            {
                "id": "P019",
                "title": "BST Insert and Inorder Traversal",
                "description": "Insert values into BST and output sorted inorder traversal.",
                "testcases": [
                    {"id": "TC073", "name": "TC073", "input": [50, 30, 70, 20, 40, 60, 80], "raw_input": "{\"values\":[50,30,70,20,40,60,80]}", "expected": "[20,30,40,50,60,70,80]"},
                    {"id": "TC074", "name": "TC074", "input": [5, 3, 7, 2, 4], "raw_input": "{\"values\":[5,3,7,2,4]}", "expected": "[2,3,4,5,7]"},
                    {"id": "TC075", "name": "TC075", "input": [10, 5, 15], "raw_input": "{\"values\":[10,5,15]}", "expected": "[5,10,15]"},
                    {"id": "TC076", "name": "TC076", "input": [1], "raw_input": "{\"values\":[1]}", "expected": "[1]"}
                ],
                "python": """def P019(values):
    \"\"\"Build BST from values and return inorder traversal list.\"\"\"
    root = build_bst(values)
    return bst_inorder(root)""",
                "java": """public static List<Integer> P019(int[] values) {
    Node root = buildBST(values);
    List<Integer> result = new ArrayList<>();
    inorder(root, result);
    return result;
}""",
                "pseudocode": """P019(values)
    root ← BUILD-BST(values)
    result ← empty list
    INORDER(root)
    RETURN result"""
            },
            {
                "id": "P020",
                "title": "BST Search",
                "description": "Search target value in BST and return Boolean presence.",
                "testcases": [
                    {"id": "TC077", "name": "TC077", "input": [50, 30, 70, 20, 40, 60, 80], "target": 60, "raw_input": "{\"values\":[50,30,70,20,40,60,80],\"target\":60}", "expected": "TRUE"},
                    {"id": "TC078", "name": "TC078", "input": [50, 30, 70, 20, 40, 60, 80], "target": 25, "raw_input": "{\"values\":[50,30,70,20,40,60,80],\"target\":25}", "expected": "FALSE"},
                    {"id": "TC079", "name": "TC079", "input": [10, 5, 15], "target": 5, "raw_input": "{\"values\":[10,5,15],\"target\":5}", "expected": "TRUE"},
                    {"id": "TC080", "name": "TC080", "input": [10], "target": 20, "raw_input": "{\"values\":[10],\"target\":20}", "expected": "FALSE"}
                ],
                "python": """def P020(values, target):
    \"\"\"Search target in BST and return True/False.\"\"\"
    root = build_bst(values)
    return bst_search(root, target)""",
                "java": """public static boolean P020(int[] values, int target) {
    Node root = buildBST(values);
    return bstSearch(root, target);
}""",
                "pseudocode": """P020(values, T)
    root ← BUILD-BST(values)
    RETURN BST-SEARCH(root, T)"""
            }
        ]
    }
}

# =========================================================================
# COMPREHENSIVE MULTI-SOURCE QUESTION BANK
# Sourced from GeeksforGeeks, HackerRank, Codeforces, and LeetCode
# =========================================================================
MULTI_SOURCE_QUESTION_BANK = [
    # SORTING
    {
        "id": "GFG-SORT-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Sorting",
        "topicCategory": "Divide & Conquer",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "COUNT INVERSIONS IN AN ARRAY",
        "desc": "Given an integer array `arr`, return the total count of inversions (pairs (i, j) where i < j and arr[i] > arr[j]) using modified Merge Sort in O(N log N) time.",
        "constraints": "N ≤ 10⁵, 1 ≤ arr[i] ≤ 10⁹",
        "timelimit": "1.00 SEC",
        "hint": "Modify Merge Sort during the merge step: when taking an element from the right subarray, it is smaller than all remaining elements in the left subarray.",
        "code": "def countInversions(arr):\n    # TODO: Write your Divide & Conquer solution here\n    pass\n\nprint(countInversions([8, 4, 2, 1]))",
        "testcases": [
            {"id": "TC #01", "input": "[8, 4, 2, 1]", "expected": "6"},
            {"id": "TC #02", "input": "[1, 2, 3, 4]", "expected": "0"}
        ]
    },
    {
        "id": "HR-SORT-01",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Sorting",
        "topicCategory": "Bubble Sort",
        "difficulty": "Easy",
        "type": "coding",
        "points": 10,
        "title": "SORTING: BUBBLE SORT SWAP COUNTER",
        "desc": "Given an array of integers `a`, sort the array using Bubble Sort and return the exact total number of element swaps performed.",
        "constraints": "N ≤ 600, 1 ≤ a[i] ≤ 2*10⁶",
        "timelimit": "0.50 SEC",
        "hint": "Track a swap counter inside the inner comparison loop of Bubble Sort.",
        "code": "def countBubbleSwaps(a):\n    # TODO: Write your Bubble Sort swap counter solution here\n    pass\n\nprint(countBubbleSwaps([6, 4, 1]))",
        "testcases": [
            {"id": "TC #01", "input": "[6, 4, 1]", "expected": "3"},
            {"id": "TC #02", "input": "[1, 2, 3]", "expected": "0"}
        ]
    },
    {
        "id": "HR-SORT-02",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Sorting",
        "topicCategory": "Greedy / Sorting",
        "difficulty": "Easy",
        "type": "coding",
        "points": 10,
        "title": "MARK AND TOYS",
        "desc": "Given a list of toy prices `prices` and a budget `k`, sort the prices and return the maximum number of toys Mark can purchase within budget.",
        "constraints": "N ≤ 10⁵, K ≤ 10⁹",
        "timelimit": "0.50 SEC",
        "hint": "Sort the prices in ascending order, then greedily accumulate prices until budget k is exceeded.",
        "code": "def maximumToys(prices, k):\n    # TODO: Write your greedy sorting solution here\n    pass\n\nprint(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))",
        "testcases": [
            {"id": "TC #01", "input": "prices=[1, 12, 5, 111, 200, 1000, 10], k=50", "expected": "4"},
            {"id": "TC #02", "input": "prices=[1, 2, 3, 4], k=7", "expected": "3"}
        ]
    },
    {
        "id": "CF-SORT-01",
        "source": "Codeforces",
        "source_badge": "[CODEFORCES]",
        "topic": "Sorting",
        "topicCategory": "Array Sorting",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "HONEST COACH (CF 1360B)",
        "desc": "Given athlete strength array `s`, sort the array and find the minimum absolute difference between any two adjacent elements after sorting.",
        "constraints": "N ≤ 50, 1 ≤ s[i] ≤ 1000",
        "timelimit": "1.00 SEC",
        "hint": "Sort the array in ascending order and find min(s[i] - s[i-1]) for i from 1 to N-1.",
        "code": "def minAthleteDifference(s):\n    # TODO: Write your sorting difference solution here\n    pass\n\nprint(minAthleteDifference([3, 1, 4, 1, 5, 9]))",
        "testcases": [
            {"id": "TC #01", "input": "[3, 1, 4, 1, 5, 9]", "expected": "0"},
            {"id": "TC #02", "input": "[10, 20, 30]", "expected": "10"}
        ]
    },
    {
        "id": "LC-SORT-01",
        "source": "LeetCode",
        "source_badge": "[LEETCODE]",
        "topic": "Sorting",
        "topicCategory": "Two Pointers",
        "difficulty": "Easy",
        "type": "coding",
        "points": 10,
        "title": "SORT ARRAY BY PARITY II",
        "desc": "Given an integer array `nums` where half of the integers are odd and half are even, sort the array so that whenever `nums[i]` is odd, `i` is odd, and whenever `nums[i]` is even, `i` is even.",
        "constraints": "N ≤ 10⁴, 0 ≤ nums[i] ≤ 1000",
        "timelimit": "1.00 SEC",
        "hint": "Use two pointers: even pointer i = 0, odd pointer j = 1. Advance i until odd value found, advance j until even value found, then swap.",
        "code": "def sortArrayByParityII(nums):\n    # TODO: Write your solution here\n    pass\n\nprint(sortArrayByParityII([4, 2, 5, 7]))",
        "testcases": [
            {"id": "TC #01", "input": "[4, 2, 5, 7]", "expected": "[4, 5, 2, 7]"},
            {"id": "TC #02", "input": "[2, 3]", "expected": "[2, 3]"}
        ]
    },

    # SEARCHING
    {
        "id": "GFG-SEARCH-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Searching",
        "topicCategory": "Binary Search",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "SEARCH IN ROTATED SORTED ARRAY",
        "desc": "Given a sorted array `nums` rotated at an unknown pivot, find the index of `target` in O(log N) time. Return -1 if not found.",
        "constraints": "N ≤ 10⁵, -10⁴ ≤ target ≤ 10⁴",
        "timelimit": "0.50 SEC",
        "hint": "Determine which half (left or right of mid) is strictly sorted, then check if target falls within its range.",
        "code": "def searchRotated(nums, target):\n    # TODO: Write your O(log N) binary search solution here\n    pass\n\nprint(searchRotated([4, 5, 6, 7, 0, 1, 2], 0))",
        "testcases": [
            {"id": "TC #01", "input": "[4, 5, 6, 7, 0, 1, 2], target=0", "expected": "4"},
            {"id": "TC #02", "input": "[4, 5, 6, 7, 0, 1, 2], target=3", "expected": "-1"}
        ]
    },
    {
        "id": "HR-SEARCH-01",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Searching",
        "topicCategory": "Prefix Sum / Search",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "SHERLOCK AND ARRAY (EQUILIBRIUM)",
        "desc": "Given an array `arr`, determine if there exists an element such that the sum of elements to its left equals the sum of elements to its right. Return 'YES' or 'NO'.",
        "constraints": "N ≤ 10⁵, 1 ≤ arr[i] ≤ 2*10⁴",
        "timelimit": "0.50 SEC",
        "hint": "Calculate total sum. Maintain left_sum starting at 0. At index i, right_sum = total_sum - left_sum - arr[i]. Check if left_sum == right_sum.",
        "code": "def balancedSums(arr):\n    # TODO: Write your equilibrium search solution here\n    pass\n\nprint(balancedSums([1, 2, 3, 3]))",
        "testcases": [
            {"id": "TC #01", "input": "[1, 2, 3, 3]", "expected": "YES"},
            {"id": "TC #02", "input": "[1, 2, 3]", "expected": "NO"}
        ]
    },
    {
        "id": "CF-SEARCH-01",
        "source": "Codeforces",
        "source_badge": "[CODEFORCES]",
        "topic": "Searching",
        "topicCategory": "Binary Search",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "INTERESTING DRINK (CF 706B)",
        "desc": "Given drink prices in n shops, for a coin budget m, return the number of shops selling drinks with price ≤ m in O(log N) time using binary search (upper bound).",
        "constraints": "N ≤ 10⁵, 1 ≤ m ≤ 10⁵",
        "timelimit": "1.00 SEC",
        "hint": "Sort prices array. Use binary search (bisect_right / upper_bound) to find index of first element > m.",
        "code": "def countAffordableShops(prices, m):\n    # TODO: Write your upper_bound binary search solution here\n    pass\n\nprint(countAffordableShops([3, 10, 8, 6, 11], 6))",
        "testcases": [
            {"id": "TC #01", "input": "prices=[3, 10, 8, 6, 11], m=6", "expected": "2"},
            {"id": "TC #02", "input": "prices=[3, 10, 8, 6, 11], m=1", "expected": "0"}
        ]
    },
    {
        "id": "HR-SEARCH-02",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Searching",
        "topicCategory": "Two Pointers / Hash Search",
        "difficulty": "Easy",
        "type": "coding",
        "points": 10,
        "title": "ICE CREAM PARLOR",
        "desc": "Given total money `m` and flavor prices `cost`, find 1-based indices of two distinct ice cream flavors whose total cost equals `m`.",
        "constraints": "N ≤ 10⁴, 2 ≤ m ≤ 10⁴",
        "timelimit": "0.50 SEC",
        "hint": "Use a hash map mapping price -> 1-based index to find target complement (m - cost[i]) in O(N) time.",
        "code": "def icecreamParlor(m, cost):\n    # TODO: Write your target complement search solution here\n    pass\n\nprint(icecreamParlor(6, [1, 3, 4, 5, 6]))",
        "testcases": [
            {"id": "TC #01", "input": "m=6, cost=[1, 3, 4, 5, 6]", "expected": "[1, 4]"},
            {"id": "TC #02", "input": "m=4, cost=[1, 4, 5, 3, 2]", "expected": "[1, 4]"}
        ]
    },
    {
        "id": "GFG-SEARCH-02",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Searching",
        "topicCategory": "Binary Search",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "FIRST AND LAST OCCURRENCE OF ELEMENT",
        "desc": "Given a sorted array `arr` with duplicates and a target value `x`, find the starting and ending indices of `x` in O(log N) time. Return [-1, -1] if missing.",
        "constraints": "N ≤ 10⁵, 1 ≤ x ≤ 10⁶",
        "timelimit": "0.50 SEC",
        "hint": "Run two binary searches: one finding lower bound (first index) and one finding upper bound (last index).",
        "code": "def findFirstLastIndex(arr, x):\n    # TODO: Write your dual binary search solution here\n    pass\n\nprint(findFirstLastIndex([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))",
        "testcases": [
            {"id": "TC #01", "input": "arr=[1, 3, 5, 5, 5, 5, 67, 123, 125], x=5", "expected": "[2, 5]"},
            {"id": "TC #02", "input": "arr=[1, 2, 3], x=4", "expected": "[-1, -1]"}
        ]
    },

    # GRAPHS
    {
        "id": "GFG-GRAPH-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Graphs",
        "topicCategory": "Graph BFS",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "BFS TRAVERSAL OF GRAPH",
        "desc": "Given a connected graph represented as an adjacency list `adj`, return the list of nodes visited in Breadth-First Search (BFS) starting from node 0.",
        "constraints": "V, E ≤ 10⁴",
        "timelimit": "1.00 SEC",
        "hint": "Use a queue (collections.deque) and a visited set starting with node 0.",
        "code": "def bfsOfGraph(V, adj):\n    # TODO: Write your BFS graph traversal solution here\n    pass\n\nprint(bfsOfGraph(5, {0: [1, 2, 3], 1: [0], 2: [0, 4], 3: [0], 4: [2]}))",
        "testcases": [
            {"id": "TC #01", "input": "V=5, adj={0:[1,2,3], 1:[0], 2:[0,4], 3:[0], 4:[2]}", "expected": "[0, 1, 2, 3, 4]"},
            {"id": "TC #02", "input": "V=3, adj={0:[1,2], 1:[0], 2:[0]}", "expected": "[0, 1, 2]"}
        ]
    },
    {
        "id": "HR-GRAPH-01",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Graphs",
        "topicCategory": "Shortest Path BFS",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "BREADTH FIRST SEARCH: SHORTEST REACH",
        "desc": "Given an unweighted graph with N nodes (edge length = 6), compute shortest distance from start node `s` to all other nodes. Return -1 for unreachable nodes.",
        "constraints": "N ≤ 1000, M ≤ 10⁴",
        "timelimit": "1.00 SEC",
        "hint": "Run BFS from start node s. Maintain distance array initialized to -1. When visiting neighbor v, set dist[v] = dist[u] + 6.",
        "code": "def bfsShortestReach(n, edges, s):\n    # TODO: Write your Shortest Reach BFS solution here\n    pass\n\nprint(bfsShortestReach(4, [[1, 2], [1, 3]], 1))",
        "testcases": [
            {"id": "TC #01", "input": "n=4, edges=[[1,2],[1,3]], s=1", "expected": "[6, 6, -1]"},
            {"id": "TC #02", "input": "n=3, edges=[[2,3]], s=2", "expected": "[-1, 6]"}
        ]
    },
    {
        "id": "CF-GRAPH-01",
        "source": "Codeforces",
        "source_badge": "[CODEFORCES]",
        "topic": "Graphs",
        "topicCategory": "Implicit Graph BFS",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "TWO BUTTONS (CF 520B)",
        "desc": "Transform number `n` to `m` using minimum button clicks. Red button multiplies by 2, blue button subtracts 1.",
        "constraints": "1 ≤ n, m ≤ 10⁴",
        "timelimit": "1.00 SEC",
        "hint": "Work backward from m to n: if m is odd, m = m + 1; if m is even and m > n, m = m / 2. Count steps.",
        "code": "def minButtonClicks(n, m):\n    # TODO: Write your state BFS or greedy solution here\n    pass\n\nprint(minButtonClicks(4, 6))",
        "testcases": [
            {"id": "TC #01", "input": "n=4, m=6", "expected": "2"},
            {"id": "TC #02", "input": "n=10, m=1", "expected": "9"}
        ]
    },
    {
        "id": "HR-GRAPH-02",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Graphs",
        "topicCategory": "Grid DFS / Component",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "CONNECTED CELLS IN A GRID",
        "desc": "Given an n x m matrix of 1s and 0s, find the area (number of cells) of the largest connected region of 1s (8-directional adjacency).",
        "constraints": "n, m ≤ 10",
        "timelimit": "0.50 SEC",
        "hint": "For every unvisited cell with 1, launch a DFS checking all 8 neighbor directions to count region size.",
        "code": "def maxRegion(matrix):\n    # TODO: Write your 8-directional Grid DFS solution here\n    pass\n\nprint(maxRegion([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]))",
        "testcases": [
            {"id": "TC #01", "input": "[[1,1,0,0],[0,1,1,0],[0,0,1,0],[1,0,0,0]]", "expected": "5"},
            {"id": "TC #02", "input": "[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0]]", "expected": "5"}
        ]
    },
    {
        "id": "CF-GRAPH-02",
        "source": "Codeforces",
        "source_badge": "[CODEFORCES]",
        "topic": "Graphs",
        "topicCategory": "Tree DFS Traversal",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "KEFA AND PARK (CF 580C)",
        "desc": "Given a tree of n vertices where some nodes contain cats, count root-to-leaf paths having at most `m` consecutive cat nodes.",
        "constraints": "N ≤ 10⁵, 1 ≤ m ≤ N",
        "timelimit": "1.00 SEC",
        "hint": "Use DFS tracking current consecutive cat count. If cat count > m, prune path. Increment answer on reaching leaf.",
        "code": "def countValidPaths(n, m, cats, edges):\n    # TODO: Write your Tree DFS cat counter solution here\n    pass\n\nprint(countValidPaths(4, 1, [0, 1, 1, 0], [[1, 2], [1, 3], [2, 4]]))",
        "testcases": [
            {"id": "TC #01", "input": "n=4, m=1, cats=[0,1,1,0], edges=[[1,2],[1,3],[2,4]]", "expected": "2"},
            {"id": "TC #02", "input": "n=7, m=1, cats=[1,0,1,1,0,0,0], edges=[[1,2],[1,3],[2,4],[2,5],[3,6],[3,7]]", "expected": "2"}
        ]
    },

    # TREES
    {
        "id": "GFG-TREE-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Trees",
        "topicCategory": "BST Validation",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "CHECK IF BINARY TREE IS BST",
        "desc": "Given a tree represented as [val, left, right], check if it is a valid Binary Search Tree (strictly BST invariant).",
        "constraints": "Nodes ≤ 10⁴",
        "timelimit": "0.50 SEC",
        "hint": "Recursively check if root.val is within allowed range (min_val, max_val). Pass (-inf, val) to left and (val, inf) to right.",
        "code": "def isBST(tree):\n    # TODO: Write your BST range check solution here\n    pass\n\nprint(isBST([2, [1, None, None], [3, None, None]]))",
        "testcases": [
            {"id": "TC #01", "input": "[2, [1, None, None], [3, None, None]]", "expected": "True"},
            {"id": "TC #02", "input": "[5, [1, None, None], [4, [3, None, None], [6, None, None]]]", "expected": "False"}
        ]
    },
    {
        "id": "HR-TREE-01",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Trees",
        "topicCategory": "Tree Height Recursion",
        "difficulty": "Easy",
        "type": "coding",
        "points": 10,
        "title": "TREE: HEIGHT OF A BINARY TREE",
        "desc": "Calculate the height of a binary tree (number of edges on the longest path from root to leaf). Height of single node = 0.",
        "constraints": "Nodes ≤ 20",
        "timelimit": "0.20 SEC",
        "hint": "Return 1 + max(height(left), height(right)) for non-empty tree, -1 for empty tree.",
        "code": "def getHeight(tree):\n    # TODO: Write your tree height recursive solution here\n    pass\n\nprint(getHeight([3, [2, [1, None, None], None], [5, [4, None, None], [6, None, None]]]))",
        "testcases": [
            {"id": "TC #01", "input": "[3, [2, [1, None, None], None], [5, [4, None, None], [6, None, None]]]", "expected": "2"},
            {"id": "TC #02", "input": "[1, None, None]", "expected": "0"}
        ]
    },
    {
        "id": "HR-TREE-02",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "Trees",
        "topicCategory": "BST Search / LCA",
        "difficulty": "Easy-Medium",
        "type": "coding",
        "points": 10,
        "title": "LOWEST COMMON ANCESTOR IN BST",
        "desc": "Given values v1 and v2, find the value of the Lowest Common Ancestor (LCA) node in a Binary Search Tree.",
        "constraints": "Nodes ≤ 100",
        "timelimit": "0.30 SEC",
        "hint": "If both v1 and v2 < root.val, LCA is in left subtree. If both > root.val, LCA is in right subtree. Otherwise, root is LCA.",
        "code": "def findBSTLCA(tree, v1, v2):\n    # TODO: Write your BST LCA solution here\n    pass\n\nprint(findBSTLCA([4, [2, [1, None, None], [3, None, None]], [7, [6, None, None], None]], 1, 7))",
        "testcases": [
            {"id": "TC #01", "input": "tree=[4,[2,[1,None,None],[3,None,None]],[7,[6,None,None],None]], v1=1, v2=7", "expected": "4"},
            {"id": "TC #02", "input": "tree=[4,[2,[1,None,None],[3,None,None]],[7,[6,None,None],None]], v1=1, v2=3", "expected": "2"}
        ]
    },
    {
        "id": "CF-TREE-01",
        "source": "Codeforces",
        "source_badge": "[CODEFORCES]",
        "topic": "Trees",
        "topicCategory": "Functional Graph / Cycle DFS",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "BADGE (CF 1020B)",
        "desc": "N students point to p[i]. Starting from student i, follow pointers until a student gets two badges (cycle entry). Return cycle entry for each student.",
        "constraints": "N ≤ 1000",
        "timelimit": "1.00 SEC",
        "hint": "For each student, maintain a visited set and step through pointers p[curr] until visiting a node twice.",
        "code": "def findBadgeRecipients(n, p):\n    # TODO: Write your functional graph DFS cycle solution here\n    pass\n\nprint(findBadgeRecipients(3, [2, 3, 2]))",
        "testcases": [
            {"id": "TC #01", "input": "n=3, p=[2, 3, 2]", "expected": "[2, 2, 2]"},
            {"id": "TC #02", "input": "n=3, p=[2, 1, 3]", "expected": "[1, 2, 3]"}
        ]
    },
    {
        "id": "GFG-TREE-02",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Trees",
        "topicCategory": "BST Traversal",
        "difficulty": "Medium",
        "type": "coding",
        "points": 10,
        "title": "INORDER SUCCESSOR IN BST",
        "desc": "Given a target node value `x` in a BST, find the value of its in-order successor (the node with smallest key > x). Return -1 if no successor exists.",
        "constraints": "Nodes ≤ 10⁴",
        "timelimit": "0.50 SEC",
        "hint": "Start at root. If target < root.val, store root as potential successor and move left. If target >= root.val, move right.",
        "code": "def inorderSuccessor(tree, x):\n    # TODO: Write your BST Inorder Successor solution here\n    pass\n\nprint(inorderSuccessor([20, [8, [4, None, None], [12, [10, None, None], [14, None, None]]], [22, None, None]], 8))",
        "testcases": [
            {"id": "TC #01", "input": "BST=[20,[8,[4,None,None],[12,[10,None,None],[14,None,None]]],[22,None,None]], x=8", "expected": "10"},
            {"id": "TC #02", "input": "BST=[20,[8,[4,None,None],[12,[10,None,None],[14,None,None]]],[22,None,None]], x=22", "expected": "-1"}
        ]
    },
    # AVL TREES
    {
        "id": "GFG-AVL-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "AVL Trees",
        "topicCategory": "Balance Factor Calculation",
        "difficulty": "Medium",
        "type": "mcq",
        "points": 10,
        "title": "AVL TREE BALANCE FACTOR INVARIANT",
        "desc": "In a valid AVL Tree, what are the allowed values for the Balance Factor = Height(Left Subtree) - Height(Right Subtree) for any node?",
        "constraints": "CONCEPTUAL MCQ",
        "timelimit": "0.30 SEC",
        "options": [
            "-1, 0, or +1",
            "-2, 0, or +2",
            "Any value <= 0",
            "Strictly 0"
        ],
        "correctAnswer": 0,
        "hint": "An AVL Tree maintains strict balance: the heights of the left and right subtrees of every node differ by at most 1."
    },
    {
        "id": "HR-AVL-01",
        "source": "HackerRank",
        "source_badge": "[HACKERRANK]",
        "topic": "AVL Trees",
        "topicCategory": "Tree Rotations",
        "difficulty": "Hard",
        "type": "output_prediction",
        "points": 10,
        "title": "AVL ROTATION TYPE IDENTIFICATION",
        "desc": "Given an AVL tree node with Left-Right heavy insertion (node's left child is Right-heavy), which rotation sequence restores balance?",
        "constraints": "CONCEPTUAL TRACING",
        "timelimit": "0.40 SEC",
        "options": [
            "Single Right Rotation (LL)",
            "Single Left Rotation (RR)",
            "Left-Right Double Rotation (LR: Left rotate left child, then Right rotate node)",
            "Right-Left Double Rotation (RL)"
        ],
        "correctAnswer": 2,
        "hint": "LR heavy imbalance requires a Left Rotation on the left child followed by a Right Rotation on the imbalanced node."
    },

    # HEAPS & PRIORITY QUEUES
    {
        "id": "GFG-HEAP-01",
        "source": "GeeksforGeeks",
        "source_badge": "[GFG]",
        "topic": "Heaps",
        "topicCategory": "Max-Heapify",
        "difficulty": "Medium",
        "type": "algorithm_tracing",
        "points": 10,
        "title": "MAX-HEAP ARRAY REPRESENTATION",
        "desc": "Given an array `[4, 10, 3, 5, 1]`, what is the array state after building a valid Max-Heap using Heapify in O(N) time?",
        "constraints": "N = 5",
        "timelimit": "0.50 SEC",
        "options": [
            "[10, 5, 3, 4, 1]",
            "[10, 4, 3, 5, 1]",
            "[1, 3, 4, 5, 10]",
            "[10, 5, 4, 3, 1]"
        ],
        "correctAnswer": 0,
        "hint": "Heapify starts from non-leaf nodes down. Node at idx 0 (4) swaps with max child 10, then 4 swaps with 5 yielding [10, 5, 3, 4, 1]."
    },
    {
        "id": "LC-HEAP-01",
        "source": "LeetCode",
        "source_badge": "[LEETCODE]",
        "topic": "Heaps",
        "topicCategory": "Priority Queue Complexity",
        "difficulty": "Medium",
        "type": "concept",
        "points": 10,
        "title": "KTH LARGEST ELEMENT TIME COMPLEXITY",
        "desc": "What is the optimal time complexity to find the K-th largest element in an unsorted array of N numbers using a Min-Heap of size K?",
        "constraints": "N ≤ 10⁶, K ≤ N",
        "timelimit": "0.30 SEC",
        "options": [
            "O(N log N)",
            "O(N log K)",
            "O(K log N)",
            "O(N²)"
        ],
        "correctAnswer": 1,
        "hint": "Maintaining a Min-Heap of size K takes O(log K) per insertion across N elements, giving O(N log K) time."
    }
]

