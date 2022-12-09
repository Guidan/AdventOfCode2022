/* REXX */
input =.stream~new("input.txt")
food = input~makearray(line)
elf_cals.0 = 0
curr_elf = 1
elf_cals.1 = 0

do fruit over food
    if fruit = "" then do 
        curr_elf = curr_elf + 1
        elf_cals.curr_elf = 0
    end
    else do 
        elf_cals.curr_elf = elf_cals.curr_elf + fruit
    end
end
elf_cals.0 = curr_elf

most_cals = max()
say "The Elf with the most Calories is: "most_cals

exit 0

max:
    max = 0
    do i=1 to elf_cals.0
        if elf_cals.i > max then max = elf_cals.i
    end
return max
