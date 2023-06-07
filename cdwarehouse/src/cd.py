class CD:
    def __init__(self, stock):
        self.stock = stock

    def buy(self, quantity, credit_card):
        if self.stock < quantity:
            return
        if credit_card:
            self.stock = self.stock - quantity
