# test set
print(set("my name is Eric and Eric is my name".split()))

# test events set
eventParty = set(["Jake", "John", "Eric"])
eventMountainHike = set(["John", "Jill"])
print(eventParty, "and", eventMountainHike)


# find who attended both events
print(eventParty.intersection(eventMountainHike))

# find who attended one of events
print(eventParty.symmetric_difference(eventMountainHike))

# who attended only event in front (eventParty)
print(eventParty.difference(eventMountainHike))

# who attended only event in front before dot (eventMountainHike)
print(eventMountainHike.difference(eventParty))

#to get list of all participants
print(eventParty.union(eventMountainHike))

# exercise: print participants from eventParty that did not attend eventMountainHike
print(eventParty.difference(eventMountainHike))
