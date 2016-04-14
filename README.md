<h1>StackOverflow Question-based User Clustering</h1>

Using the Python driver for the Stackexchange API, questions are fetched for each user and stored in the database. On the basis of these questions, users are clustered into multiple groups using K-Means clustering available in the Scikit-learn Python library. The top keywords are displayed for each cluster. Each cluster thus defines a particular software domain wherein all users are active, and thus significant information about each user can be mined.

The workflow is as follows:
- Extract user ids from Stack Overflow urls.
- Use PyStackExchange API to extract all questions of each user.
- Use NLTK for stemming and tokenizing the questions.
- Create a Tf-Idf vector matrix, treating each set of questions of a user as a seperate document.
- Run K-means on the above tf-idf matrix and obtain clusters.
- Display top keywords in each cluster and corresponding cluster users.
