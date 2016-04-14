import re

p = re.compile('/users/[0-9]+/\w+')

with open('userID.txt','a') as op:
	for line in open('page6.html'):
		line = line.strip()
		t = re.findall(p,line)
		if t :
			t = t[0]
			t = t[7:]
			first_slash = t.find('/')
			t = t[:first_slash]
			op.write(t+'\n')