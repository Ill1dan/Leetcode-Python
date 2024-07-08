def numWaterBottles(numBottles, numExchange):

    total = numBottles + (numBottles - 1) // (numExchange - 1)
    return total

print(numWaterBottles(15, 4))