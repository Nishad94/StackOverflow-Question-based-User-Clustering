from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('stackoverflow')

f = open('SOoutput.txt', 'r')
user_dict_list = f.read().split('===')

cnt = 0
for itm in user_dict_list:
	if itm:
		a = itm.split('<<<')
		user_id = a[0]
		questions = a[1]
		questions = questions[:-3]
		if len(questions) > 5:
			session.execute("INSERT INTO stackdata(id,questions) VALUES(%s,%s)", (int(user_id), questions))
			cnt += 1
			print cnt
