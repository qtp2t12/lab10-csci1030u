# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.

import operator
def eval_rpn(tokens):
# Outline 
# 1. Create an empty stack to store numbers.
# 2. Loop through each token in the input.
# 3. If the token is a number, convert it to an integer.
# 4. Add the number to the stack.
# 5. If the token is an operator, pop two numbers.
# 6. Perform the operation using the two numbers.
# 7. Push the result back onto the stack.
# 8. After processing all tokens, return the final result.
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)
    }
    stack = []
    for token in tokens:
        if token in ops:
            right = stack.pop()
            left = stack.pop()
            stack.append(ops[token](left, right))
        else:
            stack.append(int(token))
    return stack.pop()
    


def decode_string(s):
 #Create an empty stack to remember previous strings.
# 2. Create variables for the current string and repeat count.
# 3. Loop through each character in the input.
# 4. If it's a digit, build the repeat count.
# 5. If it's '[', save the current string and count.
# 6. Reset the current string and count.
# 7. If it's ']', pop the saved information.
# 8. Repeat the current string and combine it with the previous string.
# 9. Otherwise, add the character to the current string.
# 10. Return the completed decoded string.
    stack = []
    current_string = ""
    repeat_count = 0
    for char in s:
        if char.isdigit():
            repeat_count = repeat_count * 10 + int(char)
        elif char == "[":
            stack.append((current_string, repeat_count))
            current_string = ""
            repeat_count = 0
        elif char == "]":
            previous_string, count = stack.pop()
            current_string = previous_string + current_string * count
        else:
            current_string += char
    return current_string


def daily_temperatures(temps):
# Outline:
# 1. Create a result list filled with zeros.
# 2. Create an empty stack to store day indices.
# 3. Loop through each temperature.
# 4. Compare it with previous days in the stack.
# 5. If warmer, calculate the days between them.
# 6. Remove the previous day from the stack.
# 7. Add the current day to the stack.
# 8. Return the result list.
    result = [0] * len(temps)
    stack = []
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day
        stack.append(i)
    return result


def num_islands(grid):   # Part 4 - stretch (optional)
# Outline:
# 1. Create a set to track visited cells.
# 2. Create a counter for the islands.
# 3. Loop through each cell in the grid.
# 4. If land is found and not visited, count an island.
# 5. Use a stack to explore connected land.
# 6. Mark each connected land cell as visited.
# 7. Continue until all cells are checked.
# 8. Return the total number of islands.
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                stack = [(r, c)]
                visited.add((r, c))
                while stack:
                    row, col = stack.pop()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                stack.append((nr, nc))
    return islands



def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
