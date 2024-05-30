grades = [95, 55, 10, 65, 75, 85]
average = sum(grades) / 6
print('The Average Grade is:', round(average))
# print(round(average))


#   Task 2:

max_grade = max(grades)
print('The Highest Grade is:', max_grade)


min_grade = min(grades)
print('The Lowest Grade is:', min_grade)


#   Task 3:


# for 'eachgrade' in list 'grade'
for grade in grades:
    if grade >= 90:
        print('a')
    elif grade >= 80:
        print('b')
    elif grade >= 70:
        pass
    elif grade >=60:
        pass
    else:
        pass

