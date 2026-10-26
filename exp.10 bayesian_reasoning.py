# Bayesian Reasoning

disease = float(input("Enter probability of disease: "))
positive = float(input("Enter probability of positive test if diseased: "))
false_positive = float(input("Enter false positive probability: "))

numerator = positive * disease

denominator = numerator + false_positive * (1 - disease)

result = numerator / denominator

print("Probability of disease after positive test:", result)
print("Percentage:", result * 100, "%")