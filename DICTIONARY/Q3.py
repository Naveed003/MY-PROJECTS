# WAP to create dictionary contain the details of employees with name as keys and age and salary as values.WAP to print employees info as record
d = dict()
n = int(input('enter number of employees: '))
for i in range(n):
    name = input('Enter the name: ')
    age = input('Enter the age: ')
    salary = int(input('Enter the salary: '))
    d[name] = (age, salary)
print('name\tage\tsalary')
for i in d:
    print('\n')
    a = d[i]
    print(i, end='\t')
    for j in a:
        print(j, end='\t')
