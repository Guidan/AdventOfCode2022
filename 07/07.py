import json

with open("input.txt") as file:
    commands = [line.strip() for line in file]


def buildDirectory(commands):
    filesystem = {
        "/": {
            "type": "dir",
            "size": 0,
            "content": []
        }
    }
    cwd = []
    for line in commands:
        line_list = line.split()
        if line_list[0] == "$":
            if line_list[1] == "cd":
                if line_list[2] == "..":
                    del cwd[-1]
                elif line_list[2] == "/":
                    continue
                else:
                    cwd.append(line_list[2])
            else:
                continue
        else:
            if len(cwd) == 0:
                key = getCWD(cwd) + line_list[1]
            else:
                key = getCWD(cwd) + "/" + line_list[1]
            if line_list[0].isnumeric():
                size = int(line_list[0])
                file = {
                        "type": "file",
                        "size": size,
                        "content": None
                }
                filesystem[key] = file
                filesystem[getCWD(cwd)]["content"].append(key)
            else:
                folder = {
                    "type": "dir",
                    "size": 0,
                    "content": []
                }
                filesystem[key] = folder
                filesystem[getCWD(cwd)]["content"].append(key)
    return filesystem


def getCWD(cwd: list):
    if len(cwd) == 0:
        return "/"
    return "/"+("/".join(cwd))


def updateFileSize(filesystem: dict):
    filesystem = dict(sorted(filesystem.items(), key=lambda item: (item[0].count("/"), len(item[0])), reverse=True))
    for key, node in filesystem.items():
        if node["type"] == "dir":
            for data in node["content"]:
                node["size"] += filesystem[data]["size"]


def getTotalSize(filesystem: dict):
    total_size = 0
    for key, node in filesystem.items():
        if node["type"] == "dir":
            if node["size"] <= 100000:
                total_size += node["size"]
    return total_size


def clearSpace(filesystem: dict, total_space: int):
    space_to_clear = 30000000 - (total_space - filesystem["/"]["size"])
    smallest_folder_size = total_space
    for key, node in filesystem.items():
        if node["type"] == "dir":
            if space_to_clear <= node["size"] < smallest_folder_size:
                smallest_folder_size = node["size"]
    return smallest_folder_size


filesystem = buildDirectory(commands)
updateFileSize(filesystem)
print(json.dumps(filesystem, indent=4, sort_keys=True))
# part 1
print(getTotalSize(filesystem))
# part 2
print(clearSpace(filesystem, 70000000))
