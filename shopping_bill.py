
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


# Main Program
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
finalAmount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics GST Amount =", format(calculateElectronicsGST(a, b), ".2f"))
print("Fashion GST Amount =", format(calculateFashionGST(c, d), ".2f"))
print("Food GST Amount =", format(calculateFoodGST(e), ".2f"))
print("Total after GST =", format(total, ".2f"))
print("Discount =", format(discount, ".2f"))
print("Final payable amount =", format(finalAmount, ".2f"))
