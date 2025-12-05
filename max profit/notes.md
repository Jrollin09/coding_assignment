# Logical Errors and Improvements in Max Profit Algorithm

## 1. Missing "Stop Early" Option (CRITICAL - FIXED)

### Description
The initial implementation attempted to build a property whenever there was sufficient time remaining. It did not consider the option of *not* building anything and stopping at the current state.

### Consequence
This caused the algorithm to miss valid solutions where stopping early returned the same profit as building a "zero-profit" structure (one that finishes exactly at the deadline).
- **Example (Time Unit 49):** It found `T:9 P:1 C:0` but missed `T:9 P:0 C:0`. Both have $324000 profit.

### Fix
The `combinations` set in `compute` (currently, the iterative loop) is initialized with `{(0, 0, 0)}` instead of an empty set. This ensures the current state is always a candidate.
- **Reference:** `max_profit.py` [Line 8], [Line 12]

## 2. Zero-Profit Building Inclusion (LOGIC CHANGE - FIXED)

### Description
The algorithm originally allowed building a structure if `finish_time <= total_time`. This meant a building finishing exactly at `total_time` contributed 0 profit but was still included in the solution count.

### Consequence
Solutions included redundant buildings that added no value.
- **Example:** `T:9 P:1 C:0` vs `T:9 P:0 C:0`. The `P` in the first solution added 0 profit.

### Fix
Changed the condition to `finish_time < total_time`. Now, a building is only constructed if it finishes *before* the deadline, ensuring it contributes at least some profit.
- **Reference:** `max_profit.py` [Line 19]

## 3. Recursion Depth Limit (PERFORMANCE - FIXED)

### Description
For extremely large `total_time` (e.g., > 4000), the recursive approach would hit Python's recursion depth limit.

### Fix
Refactored the solution to use **Iterative Dynamic Programming**.
- **Benefit:** Can handle arbitrarily large inputs (limited only by memory/time, not stack depth).
- **Benefit:** Improved performance by removing function call overhead.
- **Reference:** `max_profit.py` [Line 10]

