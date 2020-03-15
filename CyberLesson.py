print('**************************************')
print('*Cybersecurity Super Secret Gradebook*')
print('**************************************')
print('Reminder: Each Homework assignment is worth of 10 points \n and Testout is worth 25 points')

class Person():
  name = input('What is their name? \n')
  toGrade = input('What grade did they get in testout? \n')
  if (int(toGrade) > 25):
    toGrade = 0
    print('Cheater detected: Points have been deducted')
  hw1Grade = input('What did they get on the first homework assignment? \n')
  if (int(hw1Grade) > 10):
    print('Cheater detected: Points have been deducted')
    hw1Grade = 0
  overallGrade = ((int(toGrade) + int(hw1Grade)) / 35) * 100

def addStudent(student1):
  print(student1.name+ '\t\t\t\t' + student1.toGrade + '\t\t\t\t\t' + student1.hw1Grade + '\t\t\t\t' + str(student1.overallGrade) + '%')

billy = Person()
sierra = Person()

print('Name:       Testout Grade:     HW Assignment #1:      Overall Grade:')
print('____________________________________________________________________')
addStudent(billy)
addStudent(sierra)



