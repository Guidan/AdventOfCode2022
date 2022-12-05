with open("input.txt") as file:
    sections = [line.strip() for line in file]


def createNumList(section: str):
    range_limits = section.split('-')
    num_list = [number for number in range(int(range_limits[0]), int(range_limits[1])+1)]
    return num_list


def isOverlapped(first: list[int], second: list[int]):
    intersect = list(set(first) & set(second))
    intersect.sort()
    if intersect == first or intersect == second:
        return True
    else:
        return False


def isOverlappedPartial(first: list[int], second: list[int]):
    intersect = list(set(first) & set(second))
    if len(intersect) > 0:
        return True
    else:
        return False


def findOverlaps(sections_list: list[str]):
    number_of_overlaps = 0
    number_of_partial_overlaps = 0
    for section in sections_list:
        elves = section.split(',')
        if isOverlapped(createNumList(elves[0]), createNumList(elves[1])):
            number_of_overlaps = number_of_overlaps + 1
        if isOverlappedPartial(createNumList(elves[0]), createNumList(elves[1])):
            number_of_partial_overlaps = number_of_partial_overlaps + 1
    return number_of_overlaps, number_of_partial_overlaps


print(findOverlaps(sections))