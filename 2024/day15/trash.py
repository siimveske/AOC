            visit_queue = deque([(new_row, new_col)])
            while visit_queue:
                current_tile_row, current_tile_col = visit_queue.popleft()
                current_tile = grid[current_tile_row][current_tile_col]
                visited.append((current_tile_row, current_tile_col, current_tile)) # mark current tile as visited



                if current_tile == "[": # add closing bracket to-be-visited queue
                    visit_queue.append((current_tile_row, current_tile_col+1))
                elif current_tile == "]":
                    visit_queue.append((current_tile_row, current_tile_col-1))

                current_tile_row, current_tile_col = current_tile_row + delta_row, current_tile_col + delta_col


            if grid[current_tile_row][current_tile_col] == "#":
                continue
            else:
                while visited:
                    current_tile_row, current_tile_col = visited.pop()
                    grid[current_tile_row + delta_row][current_tile_col + delta_col] = "O"
                grid[new_row][new_col] = "@"
                grid[current_row][current_col] = "."
                current_row, current_col = new_row, new_col