thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant"
# # The values will remain the same:
# print(thistuple)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" # This will raise an error
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

