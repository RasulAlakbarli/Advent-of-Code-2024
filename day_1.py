# Day 1

left_nums = []
right_nums = []

with open('day_1_data.txt', 'r') as f:
    for line in f.readlines():
        left_nums.append(int(line.strip().split('   ')[0]))
        right_nums.append(int(line.strip().split('   ')[1]))

left_nums.sort()
right_nums.sort()

# ---------- Part 1 ----------

total_sum = 0

for l,r in zip(left_nums, right_nums):
    total_sum += abs(l - r)

print("Answer is:",total_sum)


# ---------- Part 2 ----------

total_sum = 0

for l in left_nums:
    freq = right_nums.count(l)
    total_sum += l*freq

print("Answer is:",total_sum)
