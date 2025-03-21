from collections import deque

def find_shortest_sequence(code: str, keypad_type="numeric"):
    # Define the keypads
    numeric_keypad = {
        (0, 0): "7", (0, 1): "8", (0, 2): "9",
        (1, 0): "4", (1, 1): "5", (1, 2): "6",
        (2, 0): "1", (2, 1): "2", (2, 2): "3",
                     (3, 1): "0", (3, 2): "A"
    }
    numeric_keypad_reversed = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "1": (2, 0), "2": (2, 1), "3": (2, 2),
                     "0": (3, 1), "A": (3, 2)
    }

    directional_keypad = {
                     (0, 1): "^", (0, 2): "A",
        (1, 0): "<", (1, 1): "v", (1, 2): ">"
    }

    directional_keypad_reversed = {
                     "^": (0, 1), "A": (0, 2),
        "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }

    # Define the starting positions
    if keypad_type == "numeric":
        start_pos = (3, 2)
    else:
        start_pos = (0, 2)

    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    def get_position(key):
        if keypad_type == "numeric":
            return numeric_keypad_reversed[key]
        elif keypad_type == "directional":
            return directional_keypad_reversed[key]
        else:
            raise ValueError(f"Invalid keypad type: {keypad_type}")

    def bfs(start, target):
        queue = deque([(start, [])])
        visited = {start: 0}  # Keep track of distance to each position
        all_paths = []
        min_length = float('inf')

        while queue:
            current_pos, path = queue.popleft()
            current_dist = len(path)

            # If we found a path and it's longer than min_length, we can stop
            if current_dist > min_length:
                continue

            if current_pos == target:
                min_length = current_dist
                all_paths.append(path)
                continue

            for direction, (di, dj) in directions.items():
                ni, nj = current_pos[0] + di, current_pos[1] + dj
                new_pos = (ni, nj)

                # Check if position is valid based on keypad type
                valid_pos = (new_pos in numeric_keypad if keypad_type == "numeric" else new_pos in directional_keypad)

                if valid_pos:
                    new_dist = current_dist + 1
                    # Add new position if unvisited or if we found an equally short path
                    if new_pos not in visited or visited[new_pos] >= new_dist:
                        visited[new_pos] = new_dist
                        queue.append((new_pos, path + [direction]))

        return all_paths

    all_sequences = [[]]  # Start with empty sequence
    current_pos = start_pos

    for char in code:
        target_pos = get_position(char)
        paths = bfs(current_pos, target_pos)

        # Create new sequences for all possible combinations
        new_sequences = []
        for existing_seq in all_sequences:
            for path in paths:
                new_sequences.append(existing_seq + path + ["A"])

        all_sequences = new_sequences
        current_pos = target_pos

    return all_sequences

codes = ["789A", "968A", "286A", "349A", "170A"]
# codes = ["029A", "980A", "179A", "456A", "379A"]
results = []
for code in codes:
    length_set = set()
    lev1 = find_shortest_sequence(code, keypad_type="numeric")
    for l1 in lev1:
        lev2 = find_shortest_sequence(l1, keypad_type="directional")
        for l2 in lev2:
            lev3 = find_shortest_sequence(l2, keypad_type="directional")
            for l3 in lev3:
                length_set.add(len(l3))
    c = int(code[:-1])
    min_len = min(length_set)
    results.append((min_len, c))

sum_result = 0
for result in results:
    sum_result += result[0] * result[1]
assert sum_result == 176650
