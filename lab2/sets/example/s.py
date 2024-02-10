#python sets

#example 1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#example 2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#apple ignored

#example 3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#true and 1 are the same

#example 4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#false and 0 also duplicates

#example 5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#example 6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#example 7
set1 = {"abc", 34, True, 40, "male"}

#example 8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#set type

#example 9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#access set items
#example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#add set items
#example 1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#example 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#example 3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove
#example 1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#example 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#example 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#example 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#example 5
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#loop
#example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join
#example 1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#example 2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#example 3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#example 4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#example 5
#keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#example 6
#will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#example 7
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
#true and 1 the same

#set methods
'''
add()	     Adds an element to the set
clear()	     Removes all the elements from the set
copy()	     Returns a copy of the set
difference() Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	 Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	 Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	     Removes an element from the set
remove()	 Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	     Return a set containing the union of sets
update()	 Update the set with the union of this set and others
'''
#example 1
#example 2
#example 3
#example 4
#example 5
#example 6
#example 7
#example 8
#example 9
#example 10
#example 11