# The probability that some person have the disease A is 1%
# consequently, the probability of someone not having it is 99%
prob_disease = 0.01
prob_not_disease = 1 - prob_disease

# A T test to detect the disease is not 100% precise, detecting the disease
# in a person that is not sick and not detecting it in sick people

# The test detects the disease in sick people in 90% of the cases
# and it does not detect it on sick people in 10% of the cases
prob_pos_test_and_disease = 0.9
prob_neg_test_and_disease = 0.1

# The test detects the disease in a not sick person in 5% of the cases
# and it does not detect the disease in a person that is not sick in 95% of the cases
prob_pos_test_and_not_disease = 0.05
prob_neg_test_and_not_disease = 0.95

# True positive: chance that one person have the disease and the test result is positive
prob_true_positive = prob_disease * prob_pos_test_and_disease
# True negative: chance that one person does not have the disease and test result is negative
prob_true_negative = prob_not_disease * prob_neg_test_and_not_disease
# False positive: chance that one person does not have the disease and test result is positive
prob_false_positive = prob_not_disease * prob_pos_test_and_not_disease
# False negative: chance that one person have the disease and test result is negative
prob_false_negative = prob_disease * prob_neg_test_and_disease

# I took the test and the result is positive. What is the chance that i have the disease?
# Bayes Theorem: P(D|A) = (P(A|D) * P(D)) / (P(A|D) * P(D) + P(A|¬D) * P(¬D))
# P(D|A) = Probability of disease given a positive test. This is what we want to calculate
# P(A|D) = Probability of positive test given that you have the disease -> 90%
# P(D) = Probability that one person have the disease -> 1%
# P(A|¬D) = Probabiliy of a positive test given that you are not sick -> 5%
# P(¬D) = Probability that one person does not have the disease -> 99%
# Now we will simplify the variables so that the equation does not gets too extense
P_A_D = prob_pos_test_and_disease 
P_D = prob_disease 
P_A_ND = prob_pos_test_and_not_disease 
P_ND = prob_not_disease 
prob_disease_given_positive = (P_A_D * P_D) / (P_A_D * P_D + P_A_ND * P_ND)
print(prob_disease_given_positive)
