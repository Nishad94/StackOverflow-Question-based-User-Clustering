from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cluster import Cluster
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from sklearn.cluster import KMeans
import re
import nltk


cluster = Cluster()
session = cluster.connect('stackoverflow')

results = session.execute("select * from stackdata")

userIDS = []
questions = []
cluster_id = []

for r in results:
	userIDS.append(r.id)
	questions.append(r.questions)

stopwords = nltk.corpus.stopwords.words('english')

# load nltk's SnowballStemmer as variabled 'stemmer'

stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token) and len(token) >= 3:
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

totalvocab_stemmed = []
for i in questions:
    allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
    '''print allwords_stemmed'''
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.9, max_features=200000,
                                 min_df=0.01, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

tfidf_matrix = tfidf_vectorizer.fit_transform(questions) #fit the vectorizer to synopses

'''print(tfidf_matrix.shape)'''

terms = tfidf_vectorizer.get_feature_names()

dist = 1 - cosine_similarity(tfidf_matrix)


num_clusters = 5

km = KMeans(n_clusters=num_clusters)

km.fit(tfidf_matrix)

clusters = km.labels_.tolist()

for i in range(5):
	idx = 0
	print 'Cluster ID : ' + str(i+1) 
	print 'Stack Overflow User IDs in this cluster: '
	for c in clusters:
		if c == i:
			print userIDS[idx],
		idx += 1
	print '\n'
	print("Most significant terms in Cluster: " +  str(i+1))
	#sort cluster centers by proximity to centroid
	order_centroids = km.cluster_centers_.argsort()[:, ::-1] 
	    
	for ind in order_centroids[i, :13]: #replace 6 with n words per cluster
	    # Find term corresponding to the term id
	    print terms[ind], 

	print '\n\n'

cluster_count = [0,0,0,0,0]
for i in clusters:
	cluster_count[i] += 1

import plotly.plotly as py
import plotly.graph_objs as go
import plotly

data = [
    go.Bar(
        x=['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5'],
        y=cluster_count
    )
]
plot_url = plotly.offline.plot(data, filename='basic-bar')