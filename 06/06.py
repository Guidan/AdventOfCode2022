with open("input.txt") as file:
    signal = file.readline()


def isUnique(string: str) -> bool:
    return len(set(string)) == len(string)


def cycleSignal(signal, length: int):
    total_char = 0
    for index, letter in enumerate(signal):
        if isUnique(signal[index:index+length]):
            print(signal[index:index+length])
            total_char = index+length
            break
    return total_char


print(cycleSignal(signal, 4))
