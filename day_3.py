# Day 3

# ---------- Part 1 ----------

with open("day_3_data.txt", "r") as f:
    data = f.readlines()

total = 0
for s in data:
    for i in  range(len(s)):
        if s[i:i+4] == "mul(":
            args = s[i+4:].split(")")[0].split(",")
            if len(args) == 2:
                try:
                    total += int(args[0]) * int(args[1])
                except:
                    pass

print("Total is:", total)


# ---------- Part 2 ----------

with open("day_3_data.txt", "r") as f:
    data = f.readlines()

do = True
total = 0

for s in data:
    for i in range(len(s)):
        if s[i:i+7] == "don't()":
            do = False
        if s[i:i+4] == "do()":
            do = True

        if do:
            if s[i:i+4] == "mul(":
                args = s[i+4:].split(")")[0].split(",")
                if len(args) == 2:
                    try:
                        total += int(args[0]) * int(args[1])
                    except:
                        pass

print("Total is:", total)