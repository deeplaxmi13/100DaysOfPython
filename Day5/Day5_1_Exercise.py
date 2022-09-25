'''
you are going to write a program that calculates the average student height from a list of heights.

eg:
student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

eg: 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights

1146/7 = 163.71428571428572

Average height rounded to the nearest while number = 164



'''


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

totalHeight = 0
noOfStudents=0

for height in student_heights:
    totalHeight += height
    noOfStudents += 1

average = round(totalHeight/noOfStudents)
print(f"Average height is {average}")

'''
totalHeight = sum(student_heights)
numberOfStudents = len(student_heights)
averageHeight = round(totalHeight/numberOfStudents)
'''