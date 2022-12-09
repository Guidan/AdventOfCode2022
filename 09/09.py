from numpy import sign

with open("input.txt") as file:
    instructions = [(line.strip()).split() for line in file]


def moveHead(moves, rope_length):
    rope_segments = [[0, 0] for _ in range(rope_length)]
    # use set to prevent duplicates
    visited = set()
    for move in moves:
        direction, steps = move
        for num_steps in range(0, int(steps)):
            # move head in x or y direction
            rope_segments[0][0] += {"U": 1, "D": -1}.get(direction, 0)
            rope_segments[0][1] += {"R": 1, "L": -1}.get(direction, 0)
            for curr_seg in range(1, len(rope_segments)):
                ydist = rope_segments[curr_seg-1][0] - rope_segments[curr_seg][0]
                xdist = rope_segments[curr_seg-1][1] - rope_segments[curr_seg][1]
                # pythagorean stuff to see if segments are far enough away to pull alone with head
                if ydist**2 + xdist**2 > 2:
                    rope_segments[curr_seg][0] += sign(ydist)
                    rope_segments[curr_seg][1] += sign(xdist)
            visited.add(str(rope_segments[-1]))
    return len(visited)


# part 1
print(moveHead(instructions, 2))
# part 2
print(moveHead(instructions, 10))