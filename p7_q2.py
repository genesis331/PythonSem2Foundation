# Practical 7
# Q2

list1 = [53, 85, 42, 53, 4, 1, 4]
list2 = [5, 61, 8, 2, 5]
# Prints the lists
print("List 1:", list1)
print("List 2:", list2)
# Prints the sum of elements in list1
print("The sum of elements in list1 is", sum(list1))
# Removes 1 from list1
list1.remove(1)
# Prints list1 again
print("After removing number 1, list1 is", list1)
# Deletes the third element in list2 and prints the deleted element
print("The deleted third element in the list2 is", list2.pop(2))
# Counts and prints the number of times 5 appears in list2
print("The number 5 appears %d times in list2" % list2.count(5))
# Concatenates and sorts list1 and list2
list3 = sorted(list1 + list2)
# Prints the concatenated and sorted list
print("List3 is", list3)
