

def wholeSaleCost(coverPrice, discount,
                  firstCopyShippingCost, otherCopiesShippingCost,
                  numCopies):
    salePrice = coverPrice - coverPrice * discount

    firstCost = salePrice + firstCopyShippingCost
    numCopies -= 1

    otherCopiesCost = numCopies * (salePrice + otherCopiesShippingCost)

    return(firstCost + otherCopiesCost)


def main():
    covPrice = float(input("Enter book cover price: "))
    disc = float(input("Enter discount: "))
    firstShipCost = float(input("Enter shipping cost of first book: "))
    otherShipCost = float(input("Enter shipping cost of additional books: "))
    numCop = float(input("Enter number of copies: "))

    print("\nWholesale cost is = ", wholeSaleCost(covPrice, disc, firstShipCost, otherShipCost, numCop),sep="")


if __name__ == '__main__':
    main()