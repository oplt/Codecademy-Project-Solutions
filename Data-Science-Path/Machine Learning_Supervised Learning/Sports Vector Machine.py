# Support Vector Machines are powerful machine learning models that can make complex decision boundaries. 
# An SVM’s decision boundary can twist and curve to accommodate the training data.
# In this project, we will use an SVM trained using a baseball dataset to find the decision boundary of the strike zone.
# The strike zone can be thought of as a decision boundary that determines whether or not a pitch is a strike or a ball. 
# There is a strict definition of the strike zone: however, in practice, it will vary depending on the umpire or the player at bat.
# Let’s use our knowledge of SVMs to find the real strike zone of several baseball players.

import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()

# print aaron_judge.columns
print(aaron_judge.columns)

# check the different values the description feature
print(aaron_judge.description.unique())

# Look at the unique values stored in the type
print(aaron_judge.type.unique())

# very row’s type feature is either an 'S' for a strike, a 'B' for a ball, or an 'X' for neither (for example, an 'X' could be a hit or an out)..
# change every 'S' to a 1 and every 'B' to a 0
aaron_judge.type = aaron_judge.type.map({'S':1, 'B':0})
print(aaron_judge.type)

# plate_x measures how far left or right the pitch is from the center of home plate. 
# If plate_x = 0, that means the pitch was directly in the middle of the home plate.
print(aaron_judge['plate_x'])
print(aaron_judge['plate_z'])

# We now have the three columns we want to work with: 'plate_x', 'plate_z', and 'type'.
# Let’s remove every row that has a NaN in any of those columns.
aaron_judge = aaron_judge.dropna(subset = ['plate_x', 'plate_z', 'type'])

# Call plt.scatter()
plt.scatter(x = aaron_judge['plate_x'], y = aaron_judge['plate_z'], c = aaron_judge['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
plt.show()

# split the data into a training set and a validation set
training_set, validation_set = train_test_split(aaron_judge, random_state = 1)

# create a classifier
classifier =SVC(kernel = 'rbf')

# Call classifier‘s .fit() method.
classifier.fit(training_set[["plate_x", "plate_z"]], training_set.type)

# visualize the SVM:
def make_meshgrid(ax, h=.02):
    # x_min, x_max = x.min() - 1, x.max() + 1
    # y_min, y_max = y.min() - 1, y.max() + 1
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out


def draw_boundary(ax, clf):

    xx, yy = make_meshgrid(ax)
    return plot_contours(ax, clf, xx, yy,cmap=plt.cm.coolwarm, alpha=0.5)


draw_boundary(ax, classifier)
plt.show()

# find the accuracy
print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type))

#Try to find a configuration of gamma and C that greatly improves the accuracy. 
# You may want to use nested for loops

largest = {"value": 0, "gamma": 1, "C": 1}
for gamma in range(1,5):
    for C in range(1,5):
        classifier =SVC(kernel = 'rbf', gamma = gamma, C = C)
        classifier.fit(training_set[["plate_x", "plate_z"]], training_set.type)
        score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type)
        if(score > largest["value"]):
            largest["value"]= score
            largest["gamma"]= gamma
            largest["C"]= C
print(largest)


draw_boundary(ax, classifier)
plt.show()

# Finally, let’s see how different players’ strike zones change. Aaron Judge is the tallest player in the MLB. 
# Jose Altuve is the shortest player. Instead of using the aaron_judge variable, use jose_altuve.
# To make this easier, you
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()
# print(aaron_judge.columns)
# print(aaron_judge.description.unique())
# print(aaron_judge.type.unique())

def find_strike_zone(player):
    player.type = player.type.map({'S':1, 'B':0})
    player = player.dropna(subset = ['plate_x', 'plate_z', 'type'])
    plt.scatter(x = player['plate_x'], y = player['plate_z'], c = player['type'], cmap = plt.cm.coolwarm, alpha = 0.25)
    training_set, validation_set = train_test_split(player, random_state = 1)
    classifier =SVC(kernel = 'rbf')
    classifier.fit(training_set[["plate_x", "plate_z"]], training_set.type)
    score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type)
    print(score)
    draw_boundary(ax, classifier)
    plt.show()

find_strike_zone(aaron_judge)
find_strike_zone(jose_altuve)
find_strike_zone(david_ortiz)