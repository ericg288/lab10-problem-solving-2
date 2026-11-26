# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
# For EACH problem, work out your problem-solving OUTLINE first - STEP ONE: RESTATE THE PROBLEM,
# Try a small example by hand, and sketch your approach - STEP TWO: CREATE A SMALL EXAMPLE
# STEP THREE: CREATE A PLAN
# DO NOT RENAME THE FUNCTIONS 


def eval_rpn(tokens):
    # Step 1: Read a math expression in postfix form and calculate the answer by storing numbers in a stack
    # Step 2: For each token: if operator, pop b then a, push a op b; else push int(token)
    # Step 3: Return the only item left in the stack

    stack = []                                                # Empty list, waiting for the operators
    operators = {"+", "-", "*", "/"}                          # The valid list of operators

    for token in tokens:                                      # For each token in the list of tokens
        for token in tokens:
            if token in operators:                            # Operator: combines the top two numbers on the stack
                b = stack.pop()                               
                a = stack.pop()
                if token == "+":                              # Compute a op b and push the result back onto the stack
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))                      # Convert the string into an integer, and push it back into the stack

    return stack[0]                                           # Only the final answer remains in the stack


def decode_string(s):
    # Step 1: Expand a string like k[encoded] by repeating encoded k times, INCLUDING NESTED BRACKETS 
    # Step 2: For "3[a2[c]]", at the first [ save ("", 3), at the second [ save ("a", 2), then each ] pops and gives "acc" and then "accaccacc"
    # Step 3: Walk through all characters, build up the number and current text, push (text, count) on [, and on ] pop and set current = previous_text + current * count


    stack = []                                                                    # Stack remembers the text and repeat-count from outside each "["
    current = ""                                                                  # Text built so far at the CURRENT nesting level
    num = 0                                                                       # Repeat-count being read (can have several digits, like "12")

    for ch in s:
        if ch.isdigit():                                                          # Digit: adds it to the number being read
            num = num * 10 + int(ch)

        elif ch == "[":                                                           # Opening bracket: save outside context, then start fresh inside
            stack.append((current, num))
            current = ""
            num = 0

        elif ch == "]":                                                           # Closing bracket: repeat the inside text and attach it to the outside text
            prev_text, k = stack.pop()
            current = prev_text + current * k
                
        else:                                                                     # Letter: now adds it to the current text
            current += ch

    return current


def daily_temperatures(temps):
    # Step 1: For each day, find out how many days it'll be until the temperature gets warmer, or 0 if the weather doesn't warm up
    # Step 2: For [30, 40, 50, 60], day 0 waits until day 1 (1 day), day 1 until day 2 (1 day), day 2 until day 3 (1 day), and day 3 never gets a warmer day (0)
    # Step 3: Keep a stack of day indexes still waiting, and when today is warmer than the day on top, pop it and record the gap in days

    result = [0] * len(temps)                                     # Default answer is 0 (no warmer day found)
    stack = []                                                    # Stack holds indexes of days that it spends waiting for a warmer day                           

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:                     # Today is warmer than the waiting day on top, so the wait is over
            j = stack.pop()
            result[j] = i - j

        stack.append(i)                                           # Now waits for the warmer day

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Step 1: Count the number of "islands" in a 2D grid of 1s (land) and 0s (water). An island is a group of connected 1s (horizontally or vertically).
    # Step 2: For ["11000", "11000", "00100", "00011"], the top-left 2x2 block is one island, the single middle 1 is another, and the bottom-right pair is a third, so the answer is 3
    # Step 3: Scan every cell, and when you find an unvisited '1', count 1 island and use a stack to visit and mark all the connected land cells. 

    if not grid:
        return 0                                        # Empty grid has no islands

    rows, cols = len(grid), len(grid[0])

    visited = set()                                     # Cells whe've already counted as an island
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:          # New, unvisited land: this is a new island
                count += 1
                visited.add((r, c))

                stack = [(r, c)]                                     # Stack of land cells whose neighbors we still need to check

                while stack:
                    x, y = stack.pop()

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):        # Check up, down, left, right
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < rows and 0 <= ny < cols                # Stay inside the grid, only land, and only if not visited yet
                                and grid[nx][ny] == "1"
                                and (nx, ny) not in visited):
                            visited.add((nx, ny))
                            stack.append((nx, ny))

    return count


if __name__ == "__main__":
    main()
