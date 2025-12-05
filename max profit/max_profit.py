build_options = {
    'T': {'duration': 5, 'unit_profit': 1500},
    'P': {'duration': 4, 'unit_profit': 1000},
    'C': {'duration': 10, 'unit_profit': 2000}
}

def solve(total_time):   
    dp = [(0, {(0, 0, 0)})] * (total_time + 1)
    
    for t in range(total_time - 1, -1, -1):
        max_profit = 0
        combinations = {(0, 0, 0)}

        for build_type, config in build_options.items():
            duration = config['duration']
            unit_profit = config['unit_profit']
            finish_time = t + duration

            if finish_time < total_time:                
                current_profit = (total_time - finish_time) * unit_profit
                sub_profit, sub_combinations = dp[finish_time]
                total_profit = current_profit + sub_profit

                if total_profit > max_profit:
                    max_profit = total_profit
                    combinations = set()
                    for combo in sub_combinations:
                        if build_type == 'T':
                            combinations.add((combo[0] + 1, combo[1], combo[2]))
                        elif build_type == 'P':
                            combinations.add((combo[0], combo[1] + 1, combo[2]))
                        else:
                            combinations.add((combo[0], combo[1], combo[2] + 1))
                elif total_profit == max_profit:
                    for combo in sub_combinations:
                        if build_type == 'T':
                            combinations.add((combo[0] + 1, combo[1], combo[2]))
                        elif build_type == 'P':
                            combinations.add((combo[0], combo[1] + 1, combo[2]))
                        else:
                            combinations.add((combo[0], combo[1], combo[2] + 1))
        
        dp[t] = (max_profit, frozenset(combinations))

    best_profit, all_solutions = dp[0]
    return best_profit, sorted(list(all_solutions))

if __name__ == "__main__":
    test_inputs = [7,8,13,49]
    for t in test_inputs:
        profit, solutions = solve(t)
        print(f"Input Time Unit: {t}")
        print(f"Earnings: ${profit}")
        for idx, sol in enumerate(solutions, 1):
            print(f"Solution {idx}: T: {sol[0]} P: {sol[1]} C: {sol[2]}")
        print()
