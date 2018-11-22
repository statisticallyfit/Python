
# 10.8 deleting elements

# pop modifies original list and returns removed element.
print("USING POP: ")
fruits = ["strawberry", "melon", "apple", "grapefruit", "lemon"]
fruitsOriginal = fruits[:]
print(fruits.pop())
print(fruits)
print(fruits.pop(2))
print(fruits)

# del is keyword like and doesn't show removed element, but modifies list.
print("\n\nUSING DEL: ")
fruits = fruitsOriginal[:]
del fruits[1]
print(fruits)
fruits = fruitsOriginal[:]
del fruits[1:3]
print(fruits)

# remove takes element you want to remove, not index. Modifies list,doesn't return removed one.
print("\n\nUSING REMOVE: ")
fruits = fruitsOriginal[:]
print(fruits.remove("apple"))
print(fruits)



# 10.9 lists and strings
# use list() to convert from string to lsit of chars (not same thing)
print("\n\n", list("banana"))


print("\n", "pining for the fjords".split())
delimiter = "-"
print("\n", delimiter.join("pining for the fjords".split()))
print("\n", ''.join("pining for the fjords".split()))



# 10.12 list args changing
def deleteHead(aList):
    del aList[0]

letters = ["a", "b", "c"]
deleteHead(letters)
print("\n", letters)



def badDelHead(t):
    t = t[1:] # does not change the list in the main program because
    # this is just a copy made (I think that's why)

t4 = [1,2,3]
badDelHead(t4)
print(t4)




def capitalizeAll(sentence):
    words = sentence.split()
    newSentence = ''

    for word in words:
        if word.isalpha():
            newWord = word[0].upper() + word[1:]
            newSentence += ' ' + newWord

    return newSentence[1:] # eliminating space in front


print(capitalizeAll("i like pie and jam with tartinades"), sep="")
print(capitalizeAll("the story teller wove through The CROWEDED street on May 4th of Wednesday"))





# True if all words are uppercase
def onlyUpper(sentence):
    words = sentence.split()
    for word in words:
        if not word.isupper():
            return False
    print("assertion: ", all([word.isupper() for word in words]))
    return True


print(onlyUpper("The peach tart aroma wafted out the window AND INTO the rose-tinted air"))
print(onlyUpper("THE ORANGE ORCHARD GLOWED IN THE EMBER SKY."))





# Aliasing: -------------------------------------------------------------------------

# NOTE: copying means you copy contents and the two lists don't
# note point to the same place in memory. But object copy means
# they do point to samae place in memory.

numbers = [2, 4, 6, 8, 10]
copy = numbers[:]
objcopy = numbers

copy[1] = 3
assert copy == [2, 3, 6, 8, 10] and numbers == [2, 4, 6,8,10]

objcopy[0] = 111
assert objcopy == [111,4,6,8,10] and numbers == [111,4,6,8,10]
numbers[1] = 444
assert objcopy == [111,444,6,8,10] and numbers == [111,444,6,8,10]








# Pass by obj reference Example 1: -----------------------------------------------------


def modifyList(listToModify):
    listToModify.append(7)
    print("inside: ", listToModify)
    listToModify = [1,2,3]
    print("inside: ", listToModify)

### listTOModify points to area in memory which points to reference to x
### append 7 to x's list
### assigning [1,2,3] to listToModify sets up list in memory [1,2,3]
# and listToModify is assigned to point to that list.
x = [4,5,6]
modifyList(x)
print(x)
# pass by obj reference: can modify the caller list, but cannot REASSIGN





# Pass by obj reference Example 2:
def f(n):
    n = 3
a = 1
f(a)
print(a) # still 1

listA = [0]
listB = listA # they are pointing to same area in memory now (lists characteristic)
listB.append(a) # note: modifications change both lists as they point to same areas in memory.
# note: in reference passing, they ARE the same areas in memory so reassignments are also permanent.
print(a)
print(listA)
print(listB)

listB = [0,1,2] # note: reassigning it makes it point to somewhere else, so listA does not get modified.
print(listA)
print(listB)



# note source: http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/