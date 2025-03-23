# Write a program that takes a student's score (0-100) and prints their grade:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

score = float(input("Enter the student's score (0-100): "))

if score >=90 and score <=100:
    print("Grade: A")
elif score >= 80 and score <=89:
    print("Grade: B")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 60 and score <= 69:
    print("Grade: D")
elif score < 60:
    print("Grade: F")
else:
    print("Invalid score! Please enter a number between 0 and 100.")
