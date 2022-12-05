STACK_DATA = {
    1: ['B', 'G', 'S', 'C'],
    2: ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
    3: ['M', 'Q', 'S'],
    4: ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
    5: ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
    6: ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
    7: ['T', 'J', 'P', 'B', 'W'],
    8: ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
    9: ['N', 'S', 'H', 'B', 'P', 'F']
}

with open("inputed.txt") as file:
    instructions = [line.strip() for line in file]


def executeInstruction(instruction: str, stack: dict):
    instructions_list = instruction.split()
    amount = int(instructions_list[1])
    from_row = int(instructions_list[3])
    to_row = int(instructions_list[5])
    for i in range(amount):
        if len(stack[from_row]) == 0:
            break
        top = stack[from_row][-1]
        stack[from_row].pop(-1)
        stack[to_row].append(top)
    return stack


def crateMover9001(instruction: str, stack: dict):
    instructions_list = instruction.split()
    amount = int(instructions_list[1])
    from_row = int(instructions_list[3])
    to_row = int(instructions_list[5])
    if amount > len(stack[from_row]):
        amount = len(stack[from_row])
    stack_index = int(amount * -1)
    section = stack[from_row][stack_index:]
    stack[from_row] = stack[from_row][:stack_index]
    for box in section:
        stack[to_row].append(box)
    return stack


def getTopLetter(instructions: list, stack: dict):
    for instruction in instructions:
        # part 1
        # stack = executeInstruction(instruction, stack)
        # part 2
        stack = crateMover9001(instruction, stack)
    print(stack)


getTopLetter(instructions, STACK_DATA)
