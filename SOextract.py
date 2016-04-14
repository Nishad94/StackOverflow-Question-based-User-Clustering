from stackexchange import Site, StackOverflow
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cluster import Cluster
import time
cluster = Cluster()
session = cluster.connect('stackoverflow')

f = open('finalUSERS.txt', 'r')
idlist = f.read().split(',')

combinedStats = []

i=1

with open('SOoutput.txt','a') as op:
	for id in idlist:
		user_stat = {}
		so = Site(StackOverflow)
		user = so.user(id)
		total_questions = user.questions.fetch()
		user_stat['userID'] = id
		questions_text = []
		for q in total_questions:
			questions_text.append(unicode(q).split("'")[1])
		user_stat['questions'] = questions_text
		combinedStats.append(user_stat)
		combined_questions = " ".join(questions_text)
		'''op.write('==='.encode('utf-8') + str(id).encode('utf-8') + ' '.encode('utf-8') + '<<< '.encode('utf-8') + combined_questions.encode('utf-8') + ' >>>'.encode('utf-8'))'''
		time.sleep(3)
		session.execute("INSERT INTO stackdata(id,questions) VALUES(%s,%s)", (int(id), combined_questions.encode('utf-8')))
		print 'finished inserting ' + str(i)
		i=i+1