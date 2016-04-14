num_set = {0,}

with open('finalUSERS.txt', 'w') as f:
	for line in open('userID.txt'):
		num = line.strip()
		num_set.add(int(num))
	for n in num_set:
		f.write(str(n)+',')
		