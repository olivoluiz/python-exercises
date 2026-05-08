name = input('Student name: ')
grade1 = float(input('First grade: '))
grade2 = float(input('Second grade: '))
average = (grade1 + grade2) / 2
print(f'{name} average: {average}')
if average >= 7:
print('Approved')
else:
print('Failed')
