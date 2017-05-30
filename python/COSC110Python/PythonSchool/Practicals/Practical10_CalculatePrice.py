
# price, order are dicts
def calculatePrice(price, order):
    '''Calculates price * order for each item in the order dict.

    price: A dictionary mapping the name of each item sold by the store to the price of the item (in dollars)
    order: A dictionary mapping the name of each item a customer wishes to buy to the quantity of that item they wish to purchase
    '''
    totalCost =  0
    for itemName in order:
        try:
            price[itemName]
        except KeyError:
            raise KeyError("The item {0} was not found in price".format(itemName))
        else:
            totalCost += price[itemName] * order[itemName]

    if totalCost > 100:
        totalCost -= 0.10 * totalCost
    elif totalCost > 50:
        totalCost -= 0.05 * totalCost

    return totalCost


if __name__ == "__main__":
    p1 = {"grain":14.75, "eggs":50, "silk":10.15, "flour":40.53}
    o1 = {"grain":3, "eggs":1, "silk":2, "flour":10}

    p2 = {"lace":20.4, "needle":1.15, "toy":0.05, "candy":1.20, "curtain":9.00}
    o2 = {"lace":1, "needle":2, "toy":2, "candy":1, "curtain":5}

    p3 = {"hat":0.15, "milk":5.16, "chocolate":1.45, "medicine":14.11}
    o3 = {"hat":1, "milk":2, "chocolate":1, "medicine":2}

    p4 = {"hat":0.15, "milk":5.16, "chocolate":1.45, "medicine":14.11}
    o4 = {"hat":1, "chocolate":1, "medicine":2}

    p5 = {"hat":0.15, "milk":5.16, "medicine":14.11}
    o5 = {"hat":1, "chocolate":1, "medicine":2}

    print(calculatePrice(p1, o1))
    print(calculatePrice(p2, o2))
    print(calculatePrice(p3, o3))

    try:
        calculatePrice(p4, o4)
    except KeyError as ke:
        print("p4,o4: ", str(ke))

    try:
        calculatePrice(p5, o5)
    except KeyError as ke:
        print("p5,o5: ", str(ke))