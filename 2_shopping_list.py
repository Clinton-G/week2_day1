#   Task 1 & 2:

decision = input("Would you Like to Add Anything to the Shopping List? ")
shop = []
while decision != 'no':
    print('Shopping List Contains:', shop)
    item = input("What Would You Like to Add? ")
    shop.append(item)
    print(shop)
    decision = input("Would you Like to Add Anything Else to the Shopping List? ")
if decision == 'no':
    remove = input('Would You Like to Remove Anything? ')
while remove != 'no':
    remove = input('What Would You Like to Remove?: ')
    shop.remove(item)
    print(shop)
    remove = input("Would You Like to Remove Anything Else?: ")
if remove == 'no':
    print("Have a Good Trip, Shopping List:", shop)


