# WAP to create dictionary with details of four students name,age,roll no and search by roll no
d = dict()
for i in range(4):
    roll = int(input('Enter the roll number: '))
    name = input('Enter the name: ')
    age = int(input('Enter the age: '))
    d[roll] = (name, age)
rollno = int(input('Enter roll number to search: '))
for i in d:
    if i == rollno:
        a = d[i]
        print('\nrollno\tname\tage')
        print(i, end='\t')
        for j in a:
            print(j, end='\t')
        break
else:
    print('the roll you entered is not found')
