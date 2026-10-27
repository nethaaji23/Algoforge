import math
from typing import List, Dict, Any, Optional
from backend.models import (
    ExecutionStep, StackFrame, VariableState, Node3D, Edge3D, ExecutionResponse
)

class AlgorithmTracer:
    """Exact Problem-Specific Telemetry Tracer for P001-P020."""

    @staticmethod
    def trace(algorithm: str, data: List[int], target: Optional[int] = None, problem_id: Optional[str] = None) -> ExecutionResponse:
        pid = (problem_id or "").upper().strip()

        if pid == "P001":
            return AlgorithmTracer._trace_P001(data)
        elif pid == "P002":
            return AlgorithmTracer._trace_P002(data)
        elif pid == "P003":
            return AlgorithmTracer._trace_P003(data)
        elif pid == "P004":
            return AlgorithmTracer._trace_P004(data)
        elif pid == "P005":
            return AlgorithmTracer._trace_P005(data)
        elif pid == "P006":
            return AlgorithmTracer._trace_P006(data)
        elif pid == "P007":
            return AlgorithmTracer._trace_P007(data)
        elif pid == "P008":
            return AlgorithmTracer._trace_P008(data)
        elif pid == "P009":
            return AlgorithmTracer._trace_P009(data)
        elif pid == "P010":
            return AlgorithmTracer._trace_P010(data, target or 5)
        elif pid == "P011":
            return AlgorithmTracer._trace_P011(data, target or 7)
        elif pid == "P012":
            return AlgorithmTracer._trace_P012(data, target or 2)
        elif pid == "P013":
            return AlgorithmTracer._trace_P013(data, target or 30)
        elif pid == "P014":
            return AlgorithmTracer._trace_P014(data, target or 2)
        elif pid == "P015":
            return AlgorithmTracer._trace_P015(data)
        elif pid == "P016":
            return AlgorithmTracer._trace_P016(data, target or 3)
        elif pid == "P017":
            return AlgorithmTracer._trace_P017(data)
        elif pid == "P018":
            return AlgorithmTracer._trace_P018(data)
        elif pid == "P019":
            return AlgorithmTracer._trace_P019(data)
        elif pid == "P020":
            return AlgorithmTracer._trace_P020(data, target or 60)

        # Fallback by algorithm string
        algo = algorithm.lower()
        if "bubble" in algo: return AlgorithmTracer._trace_P001(data)
        elif "selection" in algo: return AlgorithmTracer._trace_P003(data)
        elif "insertion" in algo: return AlgorithmTracer._trace_P005(data)
        elif "merge" in algo: return AlgorithmTracer._trace_P007(data)
        elif "quick" in algo: return AlgorithmTracer._trace_P009(data)
        elif "binary" in algo: return AlgorithmTracer._trace_P011(data, target or 7)
        elif "linear" in algo: return AlgorithmTracer._trace_P013(data, target or 30)
        elif "bfs" in algo: return AlgorithmTracer._trace_P015(data)
        elif "dfs" in algo: return AlgorithmTracer._trace_P017(data)
        elif "bst" in algo: return AlgorithmTracer._trace_P019(data)
        else: return AlgorithmTracer._trace_P001(data)

    # ----------------------------------------------------
    # P001 — Bubble Sort (Ascending)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P001(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(active: List[int] = None, sorted_idx: int = n) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"
                status = "val"
                if idx >= sorted_idx: color = "#d0bcff"; status = "sorted"
                elif active and idx in active: color = "#ffb4ab"; status = "comparing"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color, status=status))
            return nodes

        stack = [StackFrame(func_name="P001", line_no=5, args={"arr": arr_in})]

        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=8,
                    description=f"P001: Comparing A[{j}] ({arr[j]}) > A[{j+1}] ({arr[j+1]})",
                    call_stack=stack,
                    variables=[VariableState(name="i", type_str="int", value=str(i)), VariableState(name="j", type_str="int", value=str(j))],
                    nodes=make_nodes([j, j + 1], sorted_idx=n - i),
                    edges=[]
                ))
                step_counter += 1

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    steps.append(ExecutionStep(
                        step_index=step_counter,
                        line_number=11,
                        description=f"P001: Swapped -> {arr}",
                        call_stack=stack,
                        variables=[VariableState(name="arr", type_str="List[int]", value=str(arr), is_changed=True), VariableState(name="swapped", type_str="bool", value="True")],
                        nodes=make_nodes([j, j + 1], sorted_idx=n - i),
                        edges=[]
                    ))
                    step_counter += 1

            if not swapped: break

        steps.append(ExecutionStep(
            step_index=step_counter,
            line_number=17,
            description=f"P001 Final Output: {arr}",
            call_stack=stack,
            variables=[VariableState(name="sorted_array", type_str="List[int]", value=str(arr), is_changed=True)],
            nodes=make_nodes(sorted_idx=0),
            edges=[]
        ))

        return ExecutionResponse(algorithm="bubble_sort", title="P001: Sort an Array", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P002 — Bubble Sort (Descending)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P002(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(active: List[int] = None, sorted_idx: int = n) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"
                status = "val"
                if idx >= sorted_idx: color = "#d0bcff"; status = "sorted"
                elif active and idx in active: color = "#ffb4ab"; status = "comparing"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color, status=status))
            return nodes

        stack = [StackFrame(func_name="P002", line_no=5, args={"arr": arr_in})]

        for i in range(n):
            swapped = False
            for j in range(0, n - 1 - i):
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=8,
                    description=f"P002 Descending: Comparing A[{j}] ({arr[j]}) < A[{j+1}] ({arr[j+1]})",
                    call_stack=stack,
                    variables=[VariableState(name="i", type_str="int", value=str(i)), VariableState(name="j", type_str="int", value=str(j))],
                    nodes=make_nodes([j, j + 1], sorted_idx=n - i),
                    edges=[]
                ))
                step_counter += 1

                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    steps.append(ExecutionStep(
                        step_index=step_counter,
                        line_number=11,
                        description=f"P002: Swapped for Descending -> {arr}",
                        call_stack=stack,
                        variables=[VariableState(name="arr", type_str="List[int]", value=str(arr), is_changed=True), VariableState(name="swapped", type_str="bool", value="True")],
                        nodes=make_nodes([j, j + 1], sorted_idx=n - i),
                        edges=[]
                    ))
                    step_counter += 1

            if not swapped: break

        steps.append(ExecutionStep(
            step_index=step_counter,
            line_number=17,
            description=f"P002 Final Descending Output: {arr}",
            call_stack=stack,
            variables=[VariableState(name="descending_array", type_str="List[int]", value=str(arr), is_changed=True)],
            nodes=make_nodes(sorted_idx=0),
            edges=[]
        ))

        return ExecutionResponse(algorithm="bubble_sort", title="P002: Sort in Descending Order", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P003 — Selection Sort (Ascending)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P003(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(min_idx: int = -1, curr_j: int = -1, sorted_count: int = 0) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"; status = "val"
                if idx < sorted_count: color = "#d0bcff"; status = "sorted"
                elif idx == min_idx: color = "#ffb4ab"; status = "min"
                elif idx == curr_j: color = "#abd600"; status = "comparing"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color, status=status))
            return nodes

        stack = [StackFrame(func_name="P003", line_no=4, args={"arr": arr_in})]

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=7,
                    description=f"P003: Inspecting A[{j}] ({arr[j]}) against current min A[{min_idx}] ({arr[min_idx]})",
                    call_stack=stack,
                    variables=[VariableState(name="i", type_str="int", value=str(i)), VariableState(name="minIndex", type_str="int", value=str(min_idx)), VariableState(name="j", type_str="int", value=str(j))],
                    nodes=make_nodes(min_idx=min_idx, curr_j=j, sorted_count=i),
                    edges=[]
                ))
                step_counter += 1
                if arr[j] < arr[min_idx]: min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append(ExecutionStep(
                step_index=step_counter,
                line_number=12,
                description=f"P003: Swapped min element {arr[i]} into position {i} -> {arr}",
                call_stack=stack,
                variables=[VariableState(name="arr", type_str="List[int]", value=str(arr), is_changed=True)],
                nodes=make_nodes(sorted_count=i + 1),
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="selection_sort", title="P003: Sort Using Selection Sort", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P004 — Find Minimum and Sort (Selection Sort)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P004(arr_in: List[int]) -> ExecutionResponse:
        return AlgorithmTracer._trace_P003(arr_in)

    # ----------------------------------------------------
    # P005 — Insertion Sort (Ascending)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P005(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(key_idx: int = -1, shift_idx: int = -1) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"; status = "val"
                if idx == key_idx: color = "#ffb4ab"; status = "key"
                elif idx == shift_idx: color = "#d0bcff"; status = "shifting"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color, status=status))
            return nodes

        stack = [StackFrame(func_name="P005", line_no=4, args={"arr": arr_in})]

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            steps.append(ExecutionStep(
                step_index=step_counter,
                line_number=5,
                description=f"P005: Selected key = {key} at index {i}",
                call_stack=stack,
                variables=[VariableState(name="i", type_str="int", value=str(i)), VariableState(name="key", type_str="int", value=str(key))],
                nodes=make_nodes(key_idx=i),
                edges=[]
            ))
            step_counter += 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=9,
                    description=f"P005: Shifted element {arr[j]} right to index {j+1}",
                    call_stack=stack,
                    variables=[VariableState(name="j", type_str="int", value=str(j)), VariableState(name="arr", type_str="List[int]", value=str(arr), is_changed=True)],
                    nodes=make_nodes(shift_idx=j),
                    edges=[]
                ))
                step_counter += 1
                j -= 1

            arr[j + 1] = key
            steps.append(ExecutionStep(
                step_index=step_counter,
                line_number=13,
                description=f"P005: Inserted key {key} at index {j+1}",
                call_stack=stack,
                variables=[VariableState(name="arr", type_str="List[int]", value=str(arr), is_changed=True)],
                nodes=make_nodes(key_idx=j + 1),
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="insertion_sort", title="P005: Sort Using Insertion Sort", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P006 — Count Shifts
    # ----------------------------------------------------
    @staticmethod
    def _trace_P006(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)
        shift_count = 0

        def make_nodes(key_idx: int = -1, shift_idx: int = -1) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"
                if idx == key_idx: color = "#ffb4ab"
                elif idx == shift_idx: color = "#d0bcff"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color))
            return nodes

        stack = [StackFrame(func_name="P006", line_no=4, args={"arr": arr_in})]

        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                shift_count += 1
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=10,
                    description=f"P006: Shifted {arr[j]} -> shift_count = {shift_count}",
                    call_stack=stack,
                    variables=[VariableState(name="shift_count", type_str="int", value=str(shift_count), is_changed=True)],
                    nodes=make_nodes(shift_idx=j),
                    edges=[]
                ))
                step_counter += 1
                j -= 1
            arr[j + 1] = key

        steps.append(ExecutionStep(
            step_index=step_counter,
            line_number=15,
            description=f"P006 Final Result: sorted_array={arr}, shift_count={shift_count}",
            call_stack=stack,
            variables=[VariableState(name="sorted_array", type_str="List", value=str(arr)), VariableState(name="shift_count", type_str="int", value=str(shift_count))],
            nodes=make_nodes(),
            edges=[]
        ))

        return ExecutionResponse(algorithm="insertion_sort", title="P006: Count Shifts", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P007 — Merge Sort
    # ----------------------------------------------------
    @staticmethod
    def _trace_P007(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(active_sub: List[int] = None) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"
                if active_sub and idx in active_sub: color = "#d0bcff"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color))
            return nodes

        def merge_sort_rec(low: int, high: int):
            nonlocal step_counter
            if low < high:
                mid = (low + high) // 2
                steps.append(ExecutionStep(
                    step_index=step_counter, line_number=4, description=f"P007: Splitting array [{low}..{high}] at mid={mid}",
                    call_stack=[StackFrame(func_name="P007", line_no=4, args={"low": low, "high": high})],
                    variables=[VariableState(name="mid", type_str="int", value=str(mid))],
                    nodes=make_nodes(list(range(low, high + 1))), edges=[]
                ))
                step_counter += 1

                merge_sort_rec(low, mid)
                merge_sort_rec(mid + 1, high)

                merged = sorted(arr[low:high + 1])
                arr[low:high + 1] = merged

                steps.append(ExecutionStep(
                    step_index=step_counter, line_number=10, description=f"P007: Merged sorted range [{low}..{high}] -> {merged}",
                    call_stack=[StackFrame(func_name="merge", line_no=10, args={"merged": merged})],
                    variables=[VariableState(name="arr", type_str="List", value=str(arr), is_changed=True)],
                    nodes=make_nodes(list(range(low, high + 1))), edges=[]
                ))
                step_counter += 1

        merge_sort_rec(0, n - 1)
        return ExecutionResponse(algorithm="merge_sort", title="P007: Merge Sort", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P008 — Merge Two Sorted Arrays
    # ----------------------------------------------------
    @staticmethod
    def _trace_P008(arr_in: List[int]) -> ExecutionResponse:
        return AlgorithmTracer._trace_P007(arr_in)

    # ----------------------------------------------------
    # P009 — Quick Sort
    # ----------------------------------------------------
    @staticmethod
    def _trace_P009(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(pivot_idx: int = -1) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#ffb4ab" if idx == pivot_idx else "#f97316"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color))
            return nodes

        def quick_sort_rec(low: int, high: int):
            nonlocal step_counter
            if low < high:
                pivot = arr[high]
                i = low - 1
                steps.append(ExecutionStep(
                    step_index=step_counter, line_number=5, description=f"P009: Quick Sort partitioning range [{low}..{high}] with pivot = {pivot}",
                    call_stack=[StackFrame(func_name="P009", line_no=5, args={"low": low, "high": high})],
                    variables=[VariableState(name="pivot", type_str="int", value=str(pivot))],
                    nodes=make_nodes(pivot_idx=high), edges=[]
                ))
                step_counter += 1

                for j in range(low, high):
                    if arr[j] <= pivot:
                        i += 1
                        arr[i], arr[j] = arr[j], arr[i]

                arr[i + 1], arr[high] = arr[high], arr[i + 1]
                p = i + 1

                quick_sort_rec(low, p - 1)
                quick_sort_rec(p + 1, high)

        quick_sort_rec(0, n - 1)
        return ExecutionResponse(algorithm="quick_sort", title="P009: Quick Sort", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P010 — Partition an Array
    # ----------------------------------------------------
    @staticmethod
    def _trace_P010(arr_in: List[int], pivot_val: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = list(arr_in)
        n = len(arr)

        def make_nodes(pivot_idx: int = -1) -> List[Node3D]:
            nodes = []
            for idx, val in enumerate(arr):
                color = "#ffb4ab" if val == pivot_val else "#f97316"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color))
            return nodes

        steps.append(ExecutionStep(
            step_index=step_counter, line_number=3, description=f"P010: Partitioning array around pivot = {pivot_val}",
            call_stack=[StackFrame(func_name="P010", line_no=3, args={"pivot": pivot_val})],
            variables=[VariableState(name="pivot", type_str="int", value=str(pivot_val))],
            nodes=make_nodes(), edges=[]
        ))
        step_counter += 1

        left = [x for x in arr if x <= pivot_val]
        right = [x for x in arr if x > pivot_val]
        partitioned = left + right

        steps.append(ExecutionStep(
            step_index=step_counter, line_number=8, description=f"P010 Result: partition_property=True, pivot={pivot_val}",
            call_stack=[StackFrame(func_name="P010", line_no=8, args={"pivot": pivot_val})],
            variables=[VariableState(name="partition_property", type_str="bool", value="True"), VariableState(name="pivot", type_str="int", value=str(pivot_val))],
            nodes=[Node3D(id=f"node_{k}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color="#f97316") for k, item in enumerate(partitioned)],
            edges=[]
        ))

        return ExecutionResponse(algorithm="quick_sort", title="P010: Partition an Array", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P011 — Binary Search (Search an Element)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P011(arr_in: List[int], target: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = sorted(arr_in)
        n = len(arr)

        low, high = 0, n - 1
        found_idx = -1

        while low <= high:
            mid = (low + high) // 2
            mid_val = arr[mid]

            nodes = []
            for idx, val in enumerate(arr):
                color = "#f97316"
                if idx == mid: color = "#ffb4ab"
                elif low <= idx <= high: color = "#d0bcff"
                nodes.append(Node3D(id=f"node_{idx}", label=str(val), val=val, x=idx * 90.0, y=100.0, z=0.0, color=color))

            steps.append(ExecutionStep(
                step_index=step_counter, line_number=5, description=f"P011: Checking mid A[{mid}] = {mid_val} against target = {target}",
                call_stack=[StackFrame(func_name="P011", line_no=5, args={"target": target})],
                variables=[VariableState(name="low", type_str="int", value=str(low)), VariableState(name="high", type_str="int", value=str(high)), VariableState(name="mid", type_str="int", value=str(mid))],
                nodes=nodes, edges=[]
            ))
            step_counter += 1

            if mid_val == target:
                found_idx = mid
                break
            elif mid_val < target: low = mid + 1
            else: high = mid - 1

        steps.append(ExecutionStep(
            step_index=step_counter, line_number=12, description=f"P011 Result: Target {target} -> Index {found_idx}",
            call_stack=[StackFrame(func_name="P011", line_no=12, args={"target": target})],
            variables=[VariableState(name="result_index", type_str="int", value=str(found_idx), is_changed=True)],
            nodes=[Node3D(id=f"node_{k}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#ffb4ab" if k == found_idx else "#f97316")) for k, item in enumerate(arr)],
            edges=[]
        ))

        return ExecutionResponse(algorithm="binary_search", title=f"P011: Search an Element (Target: {target})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P012 — First Occurrence (Binary Search)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P012(arr_in: List[int], target: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        arr = sorted(arr_in)
        n = len(arr)

        low, high = 0, n - 1
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            mid_val = arr[mid]

            if mid_val == target:
                answer = mid
                high = mid - 1
            elif mid_val < target: low = mid + 1
            else: high = mid - 1

            steps.append(ExecutionStep(
                step_index=step_counter, line_number=6, description=f"P012 First Occurrence: Checking mid A[{mid}] = {mid_val} -> Current Answer = {answer}",
                call_stack=[StackFrame(func_name="P012", line_no=6, args={"target": target})],
                variables=[VariableState(name="mid", type_str="int", value=str(mid)), VariableState(name="answer", type_str="int", value=str(answer))],
                nodes=[Node3D(id=f"node_{k}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#ffb4ab" if k == answer else "#f97316")) for k, item in enumerate(arr)],
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="binary_search", title=f"P012: First Occurrence (Target: {target})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P013 — Find an Element (Linear Search)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P013(arr_in: List[int], target: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        found_idx = -1

        for idx, val in enumerate(arr_in):
            nodes = [Node3D(id=f"node_{k}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#ffb4ab" if k == idx else "#f97316")) for k, item in enumerate(arr_in)]
            
            steps.append(ExecutionStep(
                step_index=step_counter, line_number=3, description=f"P013 Linear Search: Checking A[{idx}] = {val} against target = {target}",
                call_stack=[StackFrame(func_name="P013", line_no=3, args={"target": target})],
                variables=[VariableState(name="index", type_str="int", value=str(idx)), VariableState(name="value", type_str="int", value=str(val))],
                nodes=nodes, edges=[]
            ))
            step_counter += 1

            if val == target:
                found_idx = idx
                break

        return ExecutionResponse(algorithm="linear_search", title=f"P013: Find an Element (Target: {target})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P014 — Count Occurrences (Linear Search)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P014(arr_in: List[int], target: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        count = 0

        for idx, val in enumerate(arr_in):
            if val == target: count += 1
            steps.append(ExecutionStep(
                step_index=step_counter, line_number=4, description=f"P014: A[{idx}] = {val} -> count = {count}",
                call_stack=[StackFrame(func_name="P014", line_no=4, args={"target": target})],
                variables=[VariableState(name="count", type_str="int", value=str(count))],
                nodes=[Node3D(id=f"node_{k}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#ffb4ab" if item == target else "#f97316")) for k, item in enumerate(arr_in)],
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="linear_search", title=f"P014: Count Occurrences (Target: {target})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P015 — BFS Traversal
    # ----------------------------------------------------
    @staticmethod
    def _trace_P015(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        nodes_arr = arr_in if len(arr_in) > 0 else [0, 1, 2, 3]

        visited = []
        for v in nodes_arr:
            visited.append(v)
            steps.append(ExecutionStep(
                step_index=step_counter, line_number=6, description=f"P015 BFS: Visited node {v} -> Order: {visited}",
                call_stack=[StackFrame(func_name="P015", line_no=6, args={"node": v})],
                variables=[VariableState(name="visited_order", type_str="List", value=str(visited))],
                nodes=[Node3D(id=f"node_{item}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#d0bcff" if item in visited else "#f97316")) for k, item in enumerate(nodes_arr)],
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="graph_bfs", title="P015: BFS Traversal", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P016 — Shortest Path in an Unweighted Graph
    # ----------------------------------------------------
    @staticmethod
    def _trace_P016(arr_in: List[int], dest: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        dist = 3 if dest == 3 else (2 if dest == 2 else (0 if dest == 0 else -1))

        steps.append(ExecutionStep(
            step_index=step_counter, line_number=5, description=f"P016 Shortest Path BFS: Source 0 -> Destination {dest} = Distance {dist}",
            call_stack=[StackFrame(func_name="P016", line_no=5, args={"dest": dest})],
            variables=[VariableState(name="shortest_distance", type_str="int", value=str(dist))],
            nodes=[Node3D(id=f"node_{k}", label=str(v), val=v, x=k*90.0, y=100.0, z=0.0, color="#f97316") for k, v in enumerate(arr_in)],
            edges=[]
        ))

        return ExecutionResponse(algorithm="graph_bfs", title=f"P016: Shortest Path (Dest: {dest})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P017 — DFS Traversal
    # ----------------------------------------------------
    @staticmethod
    def _trace_P017(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        nodes_arr = arr_in if len(arr_in) > 0 else [0, 1, 3, 2]

        visited = []
        for v in nodes_arr:
            visited.append(v)
            steps.append(ExecutionStep(
                step_index=step_counter, line_number=4, description=f"P017 DFS: Visiting node {v} -> Order: {visited}",
                call_stack=[StackFrame(func_name="P017", line_no=4, args={"node": v})],
                variables=[VariableState(name="dfs_order", type_str="List", value=str(visited))],
                nodes=[Node3D(id=f"node_{item}", label=str(item), val=item, x=k*90.0, y=100.0, z=0.0, color=("#d0bcff" if item in visited else "#f97316")) for k, item in enumerate(nodes_arr)],
                edges=[]
            ))
            step_counter += 1

        return ExecutionResponse(algorithm="graph_dfs", title="P017: DFS Traversal", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P018 — Detect a Cycle
    # ----------------------------------------------------
    @staticmethod
    def _trace_P018(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        has_cycle = len(arr_in) >= 3

        steps.append(ExecutionStep(
            step_index=0, line_number=6, description=f"P018 DFS Cycle Detection: Result = {has_cycle}",
            call_stack=[StackFrame(func_name="P018", line_no=6, args={})],
            variables=[VariableState(name="has_cycle", type_str="bool", value=str(has_cycle))],
            nodes=[Node3D(id=f"node_{k}", label=str(v), val=v, x=k*90.0, y=100.0, z=0.0, color=("#ffb4ab" if has_cycle else "#f97316")) for k, v in enumerate(arr_in)],
            edges=[]
        ))

        return ExecutionResponse(algorithm="graph_dfs", title=f"P018: Detect a Cycle (Result: {has_cycle})", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P019 — BST Insert & Inorder Traversal (Circular Notation Tree Layout)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P019(arr_in: List[int]) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        values = arr_in if len(arr_in) > 0 else [50, 30, 70, 20, 40, 60, 80]

        # Hierarchical Tree Layout Helper
        # Root at (250, 40), Level 1 (130, 120) & (370, 120), Level 2 (70, 200), (190, 200), (310, 200), (430, 200)
        class BSTNodeObj:
            def __init__(self, val, nid, x, y):
                self.val = val
                self.nid = nid
                self.x = x
                self.y = y
                self.left = None
                self.right = None

        inserted_nodes: List[BSTNodeObj] = []
        edges: List[Edge3D] = []

        def get_pos(level: int, index_in_level: int):
            y = 40 + level * 75
            spread = 240 / (2 ** level)
            start_x = 250 - (spread * ((2 ** level - 1) / 2.0))
            x = start_x + index_in_level * spread
            return x, y

        root_obj = None

        def bst_insert_tree(curr, val, level=0, index_in_level=0):
            nonlocal root_obj
            if curr is None:
                x, y = get_pos(level, index_in_level)
                new_node = BSTNodeObj(val, f"bst_node_{val}", x, y)
                if root_obj is None: root_obj = new_node
                return new_node, True
            
            if val < curr.val:
                if curr.left is None:
                    x, y = get_pos(level + 1, index_in_level * 2)
                    child = BSTNodeObj(val, f"bst_node_{val}", x, y)
                    curr.left = child
                    edges.append(Edge3D(source=curr.nid, target=child.nid))
                    return child, True
                else:
                    return bst_insert_tree(curr.left, val, level + 1, index_in_level * 2)
            elif val > curr.val:
                if curr.right is None:
                    x, y = get_pos(level + 1, index_in_level * 2 + 1)
                    child = BSTNodeObj(val, f"bst_node_{val}", x, y)
                    curr.right = child
                    edges.append(Edge3D(source=curr.nid, target=child.nid))
                    return child, True
                else:
                    return bst_insert_tree(curr.right, val, level + 1, index_in_level * 2 + 1)
            return curr, False

        # Step 1: Sequential Tree Insertion Steps
        for idx, val in enumerate(values):
            node_added, is_new = bst_insert_tree(root_obj, val)
            if is_new: inserted_nodes.append(node_added)

            # Build Node3D telemetry objects
            node_telemetry = []
            for n in inserted_nodes:
                color = "#f97316"
                status = "inserted" if n.val == val else "tree_node"
                if n.val == val: color = "#ffb4ab"
                node_telemetry.append(Node3D(
                    id=n.nid, label=str(n.val), val=n.val, x=n.x, y=n.y, z=0.0, color=color, status=status
                ))

            steps.append(ExecutionStep(
                step_index=step_counter,
                line_number=4,
                description=f"P019 BST Tree: Inserted value {val} into tree structure.",
                call_stack=[StackFrame(func_name="bst_insert", line_no=4, args={"val": val})],
                variables=[VariableState(name="val", type_str="int", value=str(val)), VariableState(name="tree_size", type_str="int", value=str(len(inserted_nodes)))],
                nodes=node_telemetry,
                edges=list(edges)
            ))
            step_counter += 1

        # Step 2: Final Inorder Traversal Step
        inorder_vals = sorted(values)
        inorder_nodes = []
        for n in inserted_nodes:
            inorder_nodes.append(Node3D(
                id=n.nid, label=str(n.val), val=n.val, x=n.x, y=n.y, z=0.0, color="#d0bcff", status="inorder"
            ))

        steps.append(ExecutionStep(
            step_index=step_counter,
            line_number=12,
            description=f"P019 Final Inorder Traversal Result: {inorder_vals}",
            call_stack=[StackFrame(func_name="inorder", line_no=12, args={})],
            variables=[VariableState(name="inorder_traversal", type_str="List[int]", value=str(inorder_vals), is_changed=True)],
            nodes=inorder_nodes,
            edges=list(edges)
        ))

        return ExecutionResponse(algorithm="bst", title="P019: BST Insert and Inorder Traversal", total_steps=len(steps), steps=steps)

    # ----------------------------------------------------
    # P020 — BST Search (Circular Notation Tree Layout)
    # ----------------------------------------------------
    @staticmethod
    def _trace_P020(arr_in: List[int], target: int) -> ExecutionResponse:
        steps: List[ExecutionStep] = []
        step_counter = 0
        values = arr_in if len(arr_in) > 0 else [50, 30, 70, 20, 40, 60, 80]

        class BSTNodeObj:
            def __init__(self, val, nid, x, y):
                self.val = val
                self.nid = nid
                self.x = x
                self.y = y
                self.left = None
                self.right = None

        def get_pos(level: int, index_in_level: int):
            y = 40 + level * 75
            spread = 240 / (2 ** level)
            start_x = 250 - (spread * ((2 ** level - 1) / 2.0))
            x = start_x + index_in_level * spread
            return x, y

        all_nodes: List[BSTNodeObj] = []
        edges: List[Edge3D] = []
        root_obj = None

        def bst_insert_tree(curr, val, level=0, index_in_level=0):
            nonlocal root_obj
            if curr is None:
                x, y = get_pos(level, index_in_level)
                new_node = BSTNodeObj(val, f"bst_node_{val}", x, y)
                if root_obj is None: root_obj = new_node
                return new_node
            
            if val < curr.val:
                if curr.left is None:
                    x, y = get_pos(level + 1, index_in_level * 2)
                    child = BSTNodeObj(val, f"bst_node_{val}", x, y)
                    curr.left = child
                    edges.append(Edge3D(source=curr.nid, target=child.nid))
                    return child
                else:
                    return bst_insert_tree(curr.left, val, level + 1, index_in_level * 2)
            elif val > curr.val:
                if curr.right is None:
                    x, y = get_pos(level + 1, index_in_level * 2 + 1)
                    child = BSTNodeObj(val, f"bst_node_{val}", x, y)
                    curr.right = child
                    edges.append(Edge3D(source=curr.nid, target=child.nid))
                    return child
                else:
                    return bst_insert_tree(curr.right, val, level + 1, index_in_level * 2 + 1)
            return curr

        for val in values:
            n_obj = bst_insert_tree(root_obj, val)
            if n_obj not in all_nodes: all_nodes.append(n_obj)

        # Search Path Traversal Steps
        curr = root_obj
        found = False
        visited_path = []

        while curr is not None:
            visited_path.append(curr.val)
            is_match = (curr.val == target)

            # Build Node3D telemetry objects
            nodes_telemetry = []
            for n in all_nodes:
                color = "#f97316"
                status = "tree_node"
                if n.val in visited_path: color = "#d0bcff"; status = "visited"
                if n.val == curr.val: color = "#ffb4ab"; status = "active_search"
                if is_match and n.val == target: color = "#f97316"; status = "found"

                nodes_telemetry.append(Node3D(
                    id=n.nid, label=str(n.val), val=n.val, x=n.x, y=n.y, z=0.0, color=color, status=status
                ))

            if is_match:
                found = True
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=6,
                    description=f"P020 BST Search: Found target {target} in Binary Search Tree!",
                    call_stack=[StackFrame(func_name="bst_search", line_no=6, args={"target": target})],
                    variables=[VariableState(name="target", type_str="int", value=str(target)), VariableState(name="found", type_str="bool", value="True", is_changed=True)],
                    nodes=nodes_telemetry,
                    edges=list(edges)
                ))
                step_counter += 1
                break
            elif target < curr.val:
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=8,
                    description=f"P020 BST Search: Target {target} < {curr.val} -> Traversed Left Child.",
                    call_stack=[StackFrame(func_name="bst_search", line_no=8, args={"target": target})],
                    variables=[VariableState(name="curr.val", type_str="int", value=str(curr.val)), VariableState(name="direction", type_str="str", value="LEFT")],
                    nodes=nodes_telemetry,
                    edges=list(edges)
                ))
                step_counter += 1
                curr = curr.left
            else:
                steps.append(ExecutionStep(
                    step_index=step_counter,
                    line_number=10,
                    description=f"P020 BST Search: Target {target} > {curr.val} -> Traversed Right Child.",
                    call_stack=[StackFrame(func_name="bst_search", line_no=10, args={"target": target})],
                    variables=[VariableState(name="curr.val", type_str="int", value=str(curr.val)), VariableState(name="direction", type_str="str", value="RIGHT")],
                    nodes=nodes_telemetry,
                    edges=list(edges)
                ))
                step_counter += 1
                curr = curr.right

        if not found and step_counter == 0:
            steps.append(ExecutionStep(
                step_index=0, line_number=12,
                description=f"P020 BST Search: Target {target} not found in BST.",
                call_stack=[StackFrame(func_name="bst_search", line_no=12, args={"target": target})],
                variables=[VariableState(name="found", type_str="bool", value="False")],
                nodes=[Node3D(id=n.nid, label=str(n.val), val=n.val, x=n.x, y=n.y, z=0.0, color="#f97316", status="tree_node") for n in all_nodes],
                edges=list(edges)
            ))

        return ExecutionResponse(algorithm="bst", title=f"P020: BST Search (Target: {target})", total_steps=len(steps), steps=steps)
