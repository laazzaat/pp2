#example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#example 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#example 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#example 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#example 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#example 6
tuple1 = ("abc", 34, True, 40, "male")

#example 7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#tuple class

#example 8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access
#example 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#example 2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#example 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#example 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#example 5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#example 6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#example 7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#join
#example 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#example 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#loop
#example 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#example 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#example 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#methods
#example 1
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

#unpack
#example 1
fruits = ("apple", "banana", "cherry")

#example 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#example 3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#example 4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#update
#example 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#example 2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#example 3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#example 4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#example 5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists