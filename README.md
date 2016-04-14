StackOverflow Question-based User Clustering

Program that clusters SO users on the basis of the questions asked by each by each individual. The clustering used is K-means clustering.

The workflow is as follows:
1. Extract user ids from Stack Overflow urls.
2. Use PyStackExchange API to extract all questions of each user.
3. Use NLTK for stemming and tokenizing the questions.
4. Create a Tf-Idf vector matrix, treating each set of questions of a user as a seperate document.
5. Run K-means on the above tf-idf matrix and obtain clusters.
6. Display top keywords in each cluster and corresponding cluster users.
