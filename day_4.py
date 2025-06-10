# Day 4

# ---------- Part 1 ----------

with open("day_4_data.txt", "r") as f:
    data = f.read().strip().split("\n")

def check_forward_horizontal(text, i, j):
    if j+3 < len(text[i]):
        if text[i][j:j+4] == "XMAS":
            return True
    return False

def check_backward_horizontal(text, i, j):
    if j-3 >= 0:
        substring = text[i][j] + text[i][j-1] + text[i][j-2] + text[i][j-3]
        if substring == "XMAS":
            return True
    return False

def check_down_vertical(text, i, j):
    if i+3 < len(text):
        substring = (text[i][j] +
                     text[i+1][j] +
                     text[i+2][j] +
                     text[i+3][j])
        if substring == "XMAS":
            return True
    return False

def check_up_vertical(text, i, j):
    if i-3 >= 0:
        substring = (text[i][j] +
                     text[i-1][j] +
                     text[i-2][j] +
                     text[i-3][j])
        if substring == "XMAS":
            return True
    return False

def check_down_right_diagonal(text, i, j):
    if i+3 < len(text) and j+3 < len(text[i]):
        substring = (text[i][j] +
                     text[i+1][j+1] +
                     text[i+2][j+2] +
                     text[i+3][j+3])
        if substring == "XMAS":
            return True
    return False

def check_down_left_diagonal(text, i, j):
    if i+3 < len(text) and j-3 >= 0:
        substring = (text[i][j] +
                     text[i+1][j-1] +
                     text[i+2][j-2] +
                     text[i+3][j-3])
        if substring == "XMAS":
            return True
    return False

def check_up_right_diagonal(text, i, j):
    if i-3 >= 0 and j+3 < len(text[i]):
        substring = (text[i][j] +
                     text[i-1][j+1] +
                     text[i-2][j+2] +
                     text[i-3][j+3])
        if substring == "XMAS":
            return True
    return False

def check_up_left_diagonal(text, i, j):
    if i-3 >= 0 and j-3 >= 0:
        substring = (text[i][j] +
                     text[i-1][j-1] +
                     text[i-2][j-2] +
                     text[i-3][j-3])
        if substring == "XMAS":
            return True
    return False

def count_xmas(data):
    xmas_count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if check_forward_horizontal(data, i, j):
                xmas_count += 1
            if check_backward_horizontal(data, i, j):
                xmas_count += 1
            if check_down_vertical(data, i, j):
                xmas_count += 1
            if check_up_vertical(data, i, j):
                xmas_count += 1
            if check_down_right_diagonal(data, i, j):
                xmas_count += 1
            if check_down_left_diagonal(data, i, j):
                xmas_count += 1
            if check_up_right_diagonal(data, i, j):
                xmas_count += 1
            if check_up_left_diagonal(data, i, j):
                xmas_count += 1
    return xmas_count

print("Count is:", count_xmas(data))


# ---------- Part 2 ----------

def check_x_right(text, i, j):
    substring = (text[i][j] +
                    text[i+1][j+1] +
                    text[i+2][j+2])
    if substring == "MAS" or substring == "SAM":
        return True
    return False

def check_x_left(text, i, j):
    substring = (text[i][j] +
                    text[i+1][j-1] +
                    text[i+2][j-2])
    if substring == "MAS" or substring == "SAM":
            return True
    return False

def count_mas(data):
    mas_count = 0
    for i in range(len(data)-2):
        for j in range(len(data[i])-2):
            if check_x_right(data, i, j) and check_x_left(data, i, j+2):
                mas_count+=1
    return mas_count


print("Count is:", count_mas(data))