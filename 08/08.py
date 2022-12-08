with open("input.txt") as file:
    tree_map = [line.strip() for line in file]


def getFirstTallTree(tree_list: list, tree_height: int):
    for index, tree in enumerate(tree_list):
        if tree >= tree_height:
            return index+1
    return len(tree_list)


def calcTreeScore(tree_map: list, row: int, col: int):
    tree = int(tree_map[row][col])
    # if number is on edge, it's score is 0
    if row == 0 or row == len(tree_map) - 1 or col == 0 or col == len(tree_map[row])-1:
        return 0
    else:
        # build lists for trees in each direction
        east = list(map(int, [*tree_map[row][col+1:]]))
        west = list(map(int, [*tree_map[row][:col]]))
        west.reverse()
        north = []
        south = []
        for check_row in tree_map[row + 1:]:
            south.append(int(check_row[col]))
        for check_row in tree_map[:row]:
            north.insert(0, int(check_row[col]))
        north_score = getFirstTallTree(north, tree)
        south_score = getFirstTallTree(south, tree)
        east_score = getFirstTallTree(east, tree)
        west_score = getFirstTallTree(west, tree)
        return north_score * south_score * east_score * west_score


def isVisible(map: list, row: int, col: int):
    tree = int(map[row][col])
    if int(max(map[row][:col])) < tree or int(max(map[row][col+1:])) < tree:
        return True
    else:
        # find max height above and below current tree
        tallest_north = float('-inf')
        tallest_south = float('-inf')
        for check_row in map[row+1:]:
            if int(check_row[col]) > tallest_south:
                tallest_south = int(check_row[col])
        for check_row in map[:row]:
            if int(check_row[col]) > tallest_north:
                tallest_north = int(check_row[col])
        if tallest_north < tree or tallest_south < tree:
            return True
        else:
            return False


def countVisibleTrees(map: list):
    visible_trees = 0
    for index_r, row in enumerate(map):
        if index_r == 0 or index_r == len(map)-1:
            visible_trees += len(row)
        else:
            for index_c, column in enumerate(row):
                if index_c == 0 or index_c == len(row)-1:
                    visible_trees += 1
                else:
                    if isVisible(map, index_r, index_c):
                        visible_trees += 1
    return visible_trees


def scoreAllTrees(map: list):
    highest_score = 0
    for index_r, row in enumerate(map):
        if index_r == 0 or index_r == len(map) - 1:
            continue
        for index_c, column in enumerate(row):
            if index_c == 0 or index_c == len(row) - 1:
                continue
            tree_score = calcTreeScore(map, index_r, index_c)
            if tree_score > highest_score:
                highest_score = tree_score
    return highest_score


print(countVisibleTrees(tree_map))
print(scoreAllTrees(tree_map))