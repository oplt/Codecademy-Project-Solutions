# In this project, you will use scikit-learn’s Naive Bayes implementation on several different datasets. 
# By reporting the accuracy of the classifier, we can find which datasets are harder to distinguish. 
# For example, how difficult do you think it is to distinguish the difference between emails about hockey and emails about soccer? 
# How hard is it to tell the difference between emails about hockey and emails about tech? In this project, we’ll find out exactly how difficult those two tasks are.

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()

# check the different categories
print(emails.target_names)

# We’re interested in seeing how effective our Naive Bayes classifier is at telling the difference between a baseball email and a hockey email. 
# We can select the categories of articles we want from fetch_20newsgroups by adding the parameter categories.
emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])

# Print the email at index 5 in the list
print(emails.data[5])

# Print the label of the email at index 5
print(emails.target[5])

# split our data into training and test sets
train_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'train', shuffle = True, random_state = 108)
test_emails  = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'test', shuffle = True, random_state = 108)

# We want to transform these emails into lists of word counts
counter = CountVectorizer()

# We need to tell counter what possible words can exist in our emails. 
# counter has a .fit() a function that takes a list of all your data.
counter.fit(test_emails.data + train_emails.data)

# We can now make a list of the counts of our words in our training set.
# Create a variable named train_counts. 
# Set it equal to counter‘s transform function using train_emails.data as a parameter
train_counts = counter.transform(train_emails.data)

# make a variable named test_counts
test_counts = counter.transform(test_emails.data)

# make a Naive Bayes classifier that we can train and test on
classifier = MultinomialNB()

# Call classifier‘s .fit() function.
classifier.fit(train_counts, train_emails.target)

# Test the Naive Bayes Classifier
print(classifier.score(test_counts, test_emails.target))