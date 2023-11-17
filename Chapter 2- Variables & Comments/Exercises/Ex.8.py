English = int(input("Enter your marks in English = "))
Science = int(input("Enter your marks in Science = "))
History = int(input("Enter your marks in History = "))
Maths = int(input("Enter your marks in Maths = "))
PE = int(input("Enter your marks in PE = "))

marks_obtained = English + Science + History + Maths + PE
total_marks = 500
average = (marks_obtained) / 5
percentage = ((marks_obtained)/total_marks)*100

print("The total marks are = ", marks_obtained)
print("The average is = ", average)
print("The total percentage is = ", percentage)