'''student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
   total_height+=height
number_of_student = 0
for student in student_heights:
    number_of_student+=1
print(round(total_height / number_of_student))'''
'''
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print("highest score is " + str(highest_score))'''
'''
total_sum = 0
for number in range(2, 101, 2):
    total_sum+=number
print(total_sum)

for number in range(1, 101):
    if number%15 == 0:
        print("fizz buzz")
    elif number%5 == 0:
        print("buzz")
    elif number%3 == 0:
        print("fizz")
    else:
        print(number)
'''
