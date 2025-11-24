from functools import lru_cache

build_options = {
    'T': {'duration': 5, 'unit_profit': 1500},
    'P': {'duration': 4, 'unit_profit': 1000},
    'C': {'duration': 10, 'unit_profit': 2000}
}

def solve(total_time):
    @lru_cache(None)
    def compute(time_used):
        max_profit = 0
        combinations = set()
        possible_choice = False

        for build_type, config in build_options.items():
            duration = config['duration']
            unit_profit = config['unit_profit']

            if time_used + duration <= total_time:
                possible_choice = True
                current_profit = (total_time - (time_used + duration)) * unit_profit
                sub_profit, sub_combinations = compute(time_used + duration)
                total_profit = current_profit + sub_profit

                for combo in sub_combinations:
                    if build_type == 'T':
                        new_combo = (combo[0] + 1, combo[1], combo[2])
                    elif build_type == 'P':
                        new_combo = (combo[0], combo[1] + 1, combo[2])
                    else:
                        new_combo = (combo[0], combo[1], combo[2] + 1)

                    if total_profit > max_profit:
                        max_profit = total_profit
                        combinations = {new_combo}
                    elif total_profit == max_profit:
                        combinations.add(new_combo)

        if not possible_choice:
            return 0, {(0, 0, 0)}

        return max_profit, frozenset(combinations)

    best_profit, all_solutions = compute(0)
    return best_profit, sorted(all_solutions)

if __name__ == "__main__":
    test_inputs = [7, 8, 13]
    for t in test_inputs:
        profit, solutions = solve(t)
        print(f"Input Time Unit: {t}")
        print(f"Earnings: ${profit}")
        for idx, sol in enumerate(solutions, 1):
            print(f"Solution {idx}: T: {sol[0]} P: {sol[1]} C: {sol[2]}")
        print()
