#python Lists- data structure




fruits = ["orange","apple","pear"]

fruitToEat = fruits[0]
print(fruitToEat)

fruitToAvoid = fruits[-1]
print(fruitToAvoid)

states_of_america = ["Delaware","Pennsylvania","Texas"]


print(states_of_america[0])


#Assignment
states_of_america[1] = "Pencilvania"
print(states_of_america)


#append

states_of_america.append("Angelland")
print(states_of_america)

'''
List functions are:
1. append
2. extends(iterable)
3. insert(i,x)
4. remove(x)
5. pop([i])
6. clear()
7. index(x[,start[,end]])
8. count(x)
9. sort(*,key= None, reverse = False)
10. reverse()
11. copy()
'''


states_of_america.extend(["New York","Jack Bauer Island"])
print(states_of_america)