#Python.
#Implement class MoneyBox for working with a virtual money box. 
#Each money box has a limited capacity (int): max number of coins in the money box. 
#When you create a money box the number of coins = 0.

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        # True, if you can add v coins, False otherwise
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        # put v coins to moneybox
        if self.capacity >= v:
            self.v = v
        
 
