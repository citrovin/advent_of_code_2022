# read data from input
with open("./input.txt") as file:
    input = file.read()
    file.close()

# get the values for every elf
elves_str = input.rsplit('\n\n')
cal_elves_str = [i.split('\n') for i in elves_str]
cal_elves_str[-1].pop() # remove last item 
cal_elves_int = []
for i in cal_elves_str:
    cal_elf = [int(j) for j in i]
    cal_elves_int.append(cal_elf)

cal_count=[sum(i) for i in cal_elves_int]
first=(cal_count.index(max(cal_count)), max(cal_count))
cal_count.remove(first[1])

second=(cal_count.index(max(cal_count)), max(cal_count))
cal_count.remove(second[1])

third=(cal_count.index(max(cal_count)), max(cal_count))
total=first[1]+second[1]+third[1]

print(f'Elf {first[0]} has the most nutritional food | Maximum amount of calories: {first[1]}')
print(f'Elf {second[0]} has the most nutritional food | Maximum amount of calories: {second[1]}')
print(f'Elf {third[0]} has the most nutritional food | Maximum amount of calories: {third[1]}')
print(f'Total calories: {total}')