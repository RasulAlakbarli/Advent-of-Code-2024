# Day 5

# ---------- Part 1 ----------

# Read data and divide into rules and pages
data = open("day_5_data.txt").read().splitlines()

rules = []
pages = []

for line in data:
    if "|" in line:
        rules.append([int(line.split("|")[0]), int(line.split("|")[1])])
    elif line == "":
        continue
    else:
        pages.append(list(map(int, line.split(","))))


# Create a set with unique pages
unique_pages = set()

for element in pages:
	for page in element:
		unique_pages.add(int(page))
		
# Create a lookup table to easily detect faults  
lookup = { page: set() for page in unique_pages }

for page in unique_pages:
	for rule in rules:
		if page == rule[0]:
			lookup[page].add(rule[1])
			
# Scan through all pages
mid = []

for page in pages:
	pass_ = False
	approve = True
	# Iterating through elements
	for i in range(len(page)):
		# Checking each sublist
		if not pass_:
			for element in page[:i]:
				if element in lookup[page[i]]:
					pass_ = True
					approve = False
					break
		else: 
			# print("Fault detected:", element, page[i])
			break
	if approve:
		mid.append(page[len(page)//2])
		# print("Approved")

out = sum(mid)

print("\n\n\n Part 1 result is: ", out)


# ---------- Part 2 ----------

mid = []

for page in pages:
	faulty = False
	# Iterating through elements
	for i in range(len(page)):
		# Checking each sublist
		for element_i in range(len(page[:i])):
			element = page[element_i]
			if element in lookup[page[i]]:
				# print("Swapping: ", page[element_i], page[i])
				page[element_i], page[i] = page[i], page[element_i]
				faulty = True
	if faulty:
		mid.append(page[len(page)//2])
		
out = sum(mid)

print("\n\n\n Part 2 result is: ", out)