# file listing elves and their calories
with open("input.txt") as file:
    food = file.readlines()


def sortFruit(fruit: list):
    elves_list = {}
    current_elf = 1
    current_elf_cal = 0
    for current_fruit in fruit:
        try:
            current_elf_cal = current_elf_cal + int(current_fruit)
        except ValueError:
            elves_list[current_elf] = current_elf_cal
            current_elf = current_elf + 1
            current_elf_cal = 0
            continue
    elves_list[current_elf] = current_elf_cal
    return elves_list


def getHighestCal(elf_list: dict):
    max_elf = max(elf_list, key=elf_list.get)
    value = elf_list[max_elf]
    del elf_list[max_elf]
    return value


def getTopNumber(elf_list: dict, top_number: int):
    top_list = 0
    for i in range(top_number):
        top_list = top_list + getHighestCal(elf_list)
    return "The top {} elves are carrying {} calories".format(top_number, top_list)


ELF_LIST = sortFruit(food)
print(getTopNumber(ELF_LIST, 3))
