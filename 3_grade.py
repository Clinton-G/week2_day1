#given a list of grades, this function will calc. avg. grade
#add a function that finds the highest, and the lowest grade in the list
#create a list that grades an assignment into a, b, c, d, f. add funtciton to sort the grade list in order from a-f

#Task 1: Code a function to calculate the average grade. 
#Task 2: Implement a function to find the highest and lowest grade. 
#Task 3 (BONUS): Create a feature that categorizes grades into letter grades (A, B, C, etc.).



#   Task 1:

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




