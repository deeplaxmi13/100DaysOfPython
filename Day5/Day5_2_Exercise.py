'''
You are oging to write a program that calculates the highest score from a List of scores

eg: student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important: you are not allowed to use max or  min functions. The output words must match the example ie
The highest score in the class is x

Example Input:
78 65 89 86 55 91 64 89

Example Output:
The highest score in the class is 91
'''



print("Welcome to the Highest Score Calculator")
student_scores = input("Input a list of scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(f"ENtered scores are: {student_scores}")

highestScore = -1

for score in student_scores:
    if score > highestScore:
        highestScore = score

print(f"The highest score in the class is {highestScore}")




'''
min(student_scores) - will give you the minimum score in the list

max(student_scores) - will give you the highest score in the list
'''