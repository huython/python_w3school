thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
