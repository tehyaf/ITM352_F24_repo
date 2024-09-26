myLists = [
    [1,2,"a", (1,2,3), True, [3,2,"z"], [5,6,7]], #6 elts "The list has at least 5 but at most 10 elements"
    [1,2,"a"], #3 elts "The list has fewer than 5 elements"
    [1,2,"a", (1,2,3), True, [3,2,"z"], [5,6,7,8,9]], #6 elts "The list has more than 11 elements"
]

myList = myLists[2]
if(len(myList) < 5):
    print("The list has fewer than 5 elements")
elif( 5 <= len(myList) <= 10):
    print("The list has at least 5 but at most 10 elements")
else:
    print("The list has more than 10 elements")