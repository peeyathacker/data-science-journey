class Seller:

    product_quantity = {}
    product_price = {}
    profit = 0

    #def __int__(self):
        #self.product_quantity = {}
        #self.product_price = {}
        #self.profit = 0

    def update(self):
        item_name = input('enter item name: ')
        item_quantity = int(input('enter item quantity: '))
        item_price = int(input('enter selling price: '))
        self.product_quantity[item_name] = item_quantity
        self.product_price[item_name] = item_price

    def show(self):
        print('--showing items--')
        for i, j in self.product_quantity.items():
            print(i, j)

    def buy(self, item_name, quantity):
        if quantity > self.product_quantity.get(item_name):
            print("sorry, we don't have that much in stock")
        else:
            self.product_quantity[item_name] = self.product_quantity.get(item_name) - quantity
            self.profit += self.product_price.get(item_name) * quantity


class Buyer:

    cart = {}
    quantity = {}
    total_amount = 0

    #def __int__(self):
        #self.cart = {}
        #self.quantity = {}
        #self.total_amount = 0

    def search(self, seller, item_name):
        if seller.product_quantity.get(item_name):
            print('quantity: ' + str(seller.product_quantity.get(item_name)))
            print('price per item: ' + str(seller.product_price.get(item_name)))
            choice = input('do u want to add this in cart? y/n?')
            if choice == 'y':
                quantity = int(input('enter quantity: '))
                if quantity > seller.product_quantity.get(item_name):
                    print('quantity does not exist')
                    self.search(seller, item_name)
                else:
                    self.cart[item_name] = seller.product_price.get(item_name) * quantity
                    self.quantity[item_name] = quantity
                    self.total_amount += seller.product_price.get(item_name) * quantity
            else:
                pass
        else:
            print('sorry, item does not exist')

    def show(self):
        print('--showing items--')
        for i, j in self.cart.items():
            print(i, j)

    def buy(self, seller):
        print('--items in your cart--')
        self.show()
        for item, quantity in self.quantity.items():
            seller.buy(item, quantity)


seller = Seller()
buyer = Buyer()
out_option = True
while out_option:
    choice = input('are you seller or buyer? s/b?: ')
    if choice == 's':
        print('*welcome to the seller section*')
        option = True
        while option:
            print('1. update items')
            print('2. show items')
            print('3. exit')
            choice = input('enter choice: ')
            if choice == '1':
                seller.update()
            elif choice == '2':
                seller.show()
            elif choice == '3':
                option = False
            else:
                print('enter valid choice')
    elif choice == 'b':
        print('*welcome to the buyer section*')
        option = True
        while option:
            print('1. search items')
            print('2. buy items')
            print('3. exit')
            choice = input('enter choice: ')
            if choice == '1':
                key = input('enter item name to search: ')
                buyer.search(seller,key)
            elif choice == '2':
                buyer.buy(seller)
            elif choice == '3':
                option = False
            else:
                print('enter valid choice')
    else:
        out_option = False
        print('exiting the system, thank you!')