
'''
total_cost = 0
cost_of_nail = 1
for horse_foot in range(4):
    for nail in range(6):
        total_cost += cost_of_nail * 2

print("The total cost to shoe the horse would be ${0:.2f}".format(total_cost / 100))

'''




### HELP - don't get this yet!!!!

def shoeHorseCost(nailCost, numNailsPerShoe, numShoes):
    totalNailCost = 0 # initialize

    #for horseFoot in range(numShoes):
    for nail in range(numNailsPerShoe * numShoes):
        totalNailCost = totalNailCost + 2 ** nail

    return totalNailCost



totalCost = shoeHorseCost(1, 6, 4)
print("The total cost to shoe the horse would be ${0:.2f}".format(totalCost / 100))

print(shoeHorseCost(1, 6, 1)/100)
print(shoeHorseCost(1, 6, 2)/100)
print(shoeHorseCost(1, 6, 3)/100)
print(shoeHorseCost(1, 6, 4)/100)
print(shoeHorseCost(1, 8, 4)/100)