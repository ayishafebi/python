list1 = list(map(int, input("Enter first list of integers: ").split()))
list2 = list(map(int, input("Enter second list of integers: ").split()))

# a) Check whether the lists are exactly the same
if len (list1) == len(list2):
    print("a) The lists have the same values.")
else:
    print("a) The lists do not have the same values.")

# b) Check whether the lists contain the same values
if set(list1) == set(list2):
    print("b) the  lists contain the same values.")
else:
    print("b) the lists do not contain the sum values.")

# c) Find values occurring in both lists
common = set(list1) & set(list2)
print("c) Values occurring in both lists:", common)

