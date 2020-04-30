# # Write your code here
class CoffeeMaker(object):
    def __init__(self, water, milk, coffee, cups, cash):
        self.water = [water]
        self.milk = [milk]
        self.coffee = [coffee]
        self.cups = [cups]
        self.cash = [cash]

    def take_order(self):
        order = input('Write action (buy, fill, take, remaining, exit):')
        while order.lower() not in ('buy', 'fill', 'take', 'remaining', 'exit'):
            print('Enter the correct order')
            order = input('Write action (buy, fill, take, remaining, exit):')
        else:
            while True:
                if order.lower() == 'buy':
                    return CoffeeMaker.purchase(self)
                elif order.lower() == 'fill':
                    return CoffeeMaker.fill(self)
                elif order.lower() == 'take':
                    return CoffeeMaker.take(self)
                elif order.lower() == 'remaining':
                    return CoffeeMaker.display(self)
                elif order == 'exit':
                    break

    def purchase(self):
        buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,'
                    ' back - to main menu: ')
        while buy not in ('1', '2', '3'):
            print('Enter the correct order')
            buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,'
                        ' back - to main menu: ')
        else:
            if buy == '1':
                if self.water[0] >= 250 and self.coffee[0] >= 16 and self.cups[0] >= 1:
                    self.water[0] = self.water[0] - 250
                    self.coffee[0] = self.coffee[0] - 15
                    self.cups[0] = self.cups[0] - 1
                    self.cash[0] = self.cash[0] + 4
                    print('I have enough resources, making your coffee!')
                else:
                    print('Sorry, not enough resources')
            elif buy == '2':
                if self.water[0] >= 250 and self.coffee[0] >= 16 and self.cups[0] >= 1:
                    self.water[0] = self.water[0] - 350
                    self.coffee[0] = self.coffee[0] - 20
                    self.milk[0] = self.milk[0] - 75
                    self.cups[0] = self.cups[0] - 1
                    self.cash[0] = self.cash[0] + 7
                    print('I have enough resources, making your coffee!')
                else:
                    print('Sorry, not enough resources')
            elif buy == '3':
                if self.water[0] >= 250 and self.coffee[0] >= 16 and self.cups[0] >= 1:
                    self.water[0] = self.water[0] - 200
                    self.coffee[0] = self.coffee[0] - 12
                    self.milk[0] = self.milk[0] - 100
                    self.cups[0] = self.cups[0] - 1
                    self.cash[0] = self.cash[0] + 6
                    print('I have enough resources, making your coffee!')
                else:
                    print('Sorry, not enough water')
            elif buy == 'back':
                return CoffeeMaker.take_order(self)
            return CoffeeMaker.take_order(self)

    def fill(self):
        try:
            add_water = int(input('Write how many ml of water do you need to add: '))
            add_milk = int(input('Write how many ml of milk do you need to add: '))
            add_coffee = int(input('Write how many grams of coffee do you need to add: '))
            add_cups = int(input('Write how many disposable cups of coffee do you need to add: '))
        except ValueError:
            print('Enter Number')
            return CoffeeMaker.fill(self)
        self.water[0] = self.water[0] + add_water
        self.milk[0] = self.milk[0] + add_milk
        self.coffee[0] = self.coffee[0] + add_coffee
        self.cups[0] = self.cups[0] + add_cups
        return CoffeeMaker.take_order(self)

    def take(self):
        print('I gave you $', self.cash[0])
        self.cash[0] = self.cash[0] - self.cash[0]
        return CoffeeMaker.take_order(self)

    def display(self):
        print('The coffee machine has: ',
              '\n', self.water[0], 'of water ',
              '\n', self.milk[0], 'of milk',
              '\n', self.coffee[0], 'of coffee beans',
              '\n', self.cups[0], 'of disposable cups',
              '\n', self.cash[0], 'of money')
        return CoffeeMaker.take_order(self)


p = CoffeeMaker(400, 540, 120, 9, 550)
p.take_order()
