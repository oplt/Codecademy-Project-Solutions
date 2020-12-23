#Grading a multiple choice exam is easy. 
# But how much do multiple choice exams tell us about what a student really knows? 
# Dr. Dirac is administering a statistics midterm exam and wants to use Bayes’ Theorem to help him understand the following:
# - Given that a student answered a question correctly, what is the probability that she really knows the material?
# Dr. Dirac knows the following probabilities based on many years of teaching:
# - There is a question on the exam that 60% of students know the correct answer to.
# - Given that a student knows the correct answer, there is still a 15% chance that the student picked the wrong answer.
# - Given that a student does not know the answer, there is still a 20% chance that the student picks the correct answer by guessing.
# Using these probabilities, we can answer the question.

import numpy as np

# In order to use Bayes Theorem, we need to phrase our question as P(A|B). 
# What is A and B in this case?
# P(A) = P(knows the material)
# P(B) = P(answers correctly)
# P(A|B) = P(knows the material | answers correctly)

# What is the probability that the student knows the material?
# P(knows the material) = 0.60

# Given that the student knows the material, what is the probability that she answers correctly?
# P(answers correctly | knows material) = 1 - 0.15

# What is the probability of any student answering correctly?
# P(answers correctly | knows material) * P(knows material) and (+) P(answers correctly| does not know material) *P(does not know material)
# = 0.85 * 0.6 + 0.2 * 0.4 
# = 0.59

# Using the three probabilities and Bayes’ Theorem, calculate P(knows material | answers correctly)

# P(knows material | answers correctly)= P(A|B) = P(B|A) * P(A) / P(B) = 0.85 * 0.6 / 0.59
p_knows_material_given_answers_correctly = 0.85 * 0.6 / 0.59
print(p_knows_material_given_answers_correctly)