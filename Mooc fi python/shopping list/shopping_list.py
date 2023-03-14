class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]


def total_units(my_list: ShoppingList):
    suma=0
    for i in range(1,my_list.number_of_items()+1):
        suma=suma+my_list.amount(i)
    return suma

# -------------------------
# Write your solution here:
# -------------------------
if __name__=="__main__":
    shopping_list=ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("ananas", 3)
    shopping_list.add("avocado", 4)

    print(total_units(shopping_list))

