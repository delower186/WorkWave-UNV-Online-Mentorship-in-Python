"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""

# list
mylist = ["apple", "banana", "cherry", "apple"]

# # Accessing item
# print(mylist[1])
# # Adding item
# mylist.append("melon")
# print(mylist)
# # remove
# mylist.remove("apple")
# print(mylist)
# append(), clear(), count(), len(), extend(), pop(), remove()


# tuple
mytuple = ("apple", "banana", "cherry")

# # Accessing item
# print(mytuple[0])
# # Adding Item
# tupleList = list(mytuple)
# tupleList.append("melon")
# conTuple = tuple(tupleList)
# print(conTuple)
#
# #remove item
# tupleList = list(mytuple)
# tupleList.remove("apple")
# conTuple = tuple(tupleList)
# print(conTuple)
# count()
print(mytuple.count("apple"))

# set
myset = {"apple", "banana", "cherry"}

# #Accessing item
# print("hello" in myset)
#
# # Adding item
# myset.add("hello")
# print(myset)
#
# # Removing item
# myset.remove("apple")
# print(myset)
# add(), clear(), pop(), remove()



# dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# # Accessing Item
# print(thisdict.get("brand"))
#
# # Adding item
# thisdict['color'] = "white"
# print(thisdict)
#
# # Removing item
# thisdict.pop("model")
# print(thisdict)

#print(thisdict["brand"])

# clear(), get(), items(), pop(), keys(), values()


def get_name():
    return "delower"

print(get_name())

class human:
    def get_name(self):
        return "delower"