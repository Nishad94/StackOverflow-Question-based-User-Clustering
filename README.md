<h1>StackOverflow Question-based User Clustering</h1>

Program that clusters SO users on the basis of the questions asked by each by each individual. The clustering used is K-means clustering available in the Scikit-learn library.

The workflow is as follows:
- Extract user ids from Stack Overflow urls.
- Use PyStackExchange API to extract all questions of each user.
- Use NLTK for stemming and tokenizing the questions.
- Create a Tf-Idf vector matrix, treating each set of questions of a user as a seperate document.
- Run K-means on the above tf-idf matrix and obtain clusters.
- Display top keywords in each cluster and corresponding cluster users.
