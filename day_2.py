# Day 2

# ---------- Part 1 ----------

safe_count = 0
with open("day_2_data.txt", 'r') as f:
    for line in f.readlines():
        safe = True
        line = line.strip().split()
        l = [int(i) for i in line]

        is_increasing = True
        safe = True
        differences = [l[i+1] - l[i] for i in range(len(l)-1)]

        if differences[0] < 0:
            is_increasing = False

        if is_increasing:
            for difference in differences:
                if 1 <= difference <= 3:
                    safe = True
                else:
                    safe = False
                    break

        else:
            for difference in differences:
                if -3 <= difference <= -1:
                    safe = True
                else:
                    safe = False
                    break
        if safe:
            safe_count+=1

print(safe_count)


# ---------- Part 2 ----------

safe_count = 0

with open("day_2_data.txt", 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        l = [int(i) for i in line]

        # Skip reports with less than 2 numbers
        if len(l) < 2:
            continue

        # Compute differences between consecutive levels
        differences = [l[i + 1] - l[i] for i in range(len(l) - 1)]

        # Determine if the sequence is increasing or decreasing
        is_increasing = all(d > 0 for d in differences)
        is_decreasing = all(d < 0 for d in differences)

        # If the sequence is already safe, count it
        if (is_increasing or is_decreasing) and all(1 <= abs(d) <= 3 for d in differences):
            safe_count += 1
            continue

        # Try removing one element at a time and check if the sequence becomes safe
        found_fix = False
        for i in range(len(l)):
            modified_l = l[:i] + l[i+1:]  # Remove one element
            modified_differences = [modified_l[j + 1] - modified_l[j] for j in range(len(modified_l) - 1)]

            # Check if modified sequence is either strictly increasing or decreasing and follows the difference rule
            if modified_differences:
                is_inc = all(d > 0 for d in modified_differences)
                is_dec = all(d < 0 for d in modified_differences)
                if (is_inc or is_dec) and all(1 <= abs(d) <= 3 for d in modified_differences):
                    found_fix = True
                    break  # No need to check further

        if found_fix:
            safe_count += 1

print("Total Safe Reports:", safe_count)
