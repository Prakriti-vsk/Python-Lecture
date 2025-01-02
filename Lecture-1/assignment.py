#Assignment Marksheet

a=(input('Enter your full name: '))

b=int(input('Class:'))

c='Mathematics', 'Science', 'English', 'Social Studies', 'Computer Science'

print('Subjects:',c)

d='enter your marks here :'

e1=int(input('Mathematics:'))
e2=int(input('Science:'))
e3=int(input('English:'))
e4=int(input('Social Studies:'))
e5=int(input('Computer Science:'))

f=e1+e2+e3+e4+e5
print('Total Marks:',f)

percentage=(423/500*100)
print('Percentage Obtained',percentage,'%')
if percentage >= 90:
    print('Grade: A+')
elif percentage >= 80:
    print('Grade: A')
elif percentage >= 70:
    print('Grade: B+')
elif percentage >= 60:
    print('Grade: B')
elif percentage >= 50:
    print('Grade: C+')
elif percentage >= 40:
    print('Grade: C')
else:
    print('Grade: Fail')








