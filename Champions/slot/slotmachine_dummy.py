#!/usr/bin/python3


import random
import collections

# from .secret import flag
flag = "45"
PRINTABLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~s"
flag_length = len(flag)
SLOT_LENGTH = 10
NO_COINS = "No more coins! Goodbye."
NOT_ENOUGH_COINS = "You don't have enough coins!"
INVALID_COIN_NUMBER = "Coin number can't be negative"
INITIAL_COINS = 10

class Slotmachine(object):
    def __init__(self):
        # for i in flag:
        #     arr = [i]
        #     print(arr)
        self.slots = [[i]+[random.choice(PRINTABLE) for i in range(SLOT_LENGTH)] for i in flag]
        print(self.slots)
        self.attempt_num = 0
        self.total_coins = INITIAL_COINS
        self.last_result = ""
        self.last_gamble = 0

    def get_prize(self):
        result = self.last_result
        prize = sum([x for x in collections.Counter(result).values() if x > 2])
        print("prize", prize)
        prize *= self.last_gamble
        self.total_coins += prize
        return prize

    def check_invalid_input(self, coins):
        if self.total_coins <= 0:
            self.last_result = ""
            return NO_COINS
        if self.total_coins < coins:
            self.last_result = ""
            return NOT_ENOUGH_COINS
        if coins < 0:
            self.last_result = ""
            return INVALID_COIN_NUMBER
        return None

    def spin(self, coins):
        invalid_message = self.check_invalid_input(coins)
        if invalid_message:
            return invalid_message.center(flag_length, ' ')

        self.last_gamble = coins
        self.total_coins -= coins

        random.seed(coins + self.attempt_num)
        self.attempt_num += 1
        print("test", self.slots)

        for i in self.slots:
            random.shuffle(i)

        result = ""
        for i in self.slots:
            
            result += random.choice(i)
        self.last_result = result
        print("result", result)
        return result 

# This is used to run the slotmachine locally, the server doesn't use this.
def main():
    slotmachine = Slotmachine()
    print("You have {} coins".format(slotmachine.total_coins))
    get_next_num = True
    while get_next_num:
        try:
            prize = 0 
            coins =  int(input("Enter number of coins:\n"))
            result =  slotmachine.spin(coins)
            if result == NO_COINS:
                get_next_num = False
            elif result != NOT_ENOUGH_COINS:
                prize = slotmachine.get_prize()
            print(result)
            print("You won {} coins!".format(prize))
            print("{} coins left.".format(slotmachine.total_coins))

        except ValueError:
            get_next_num = False
        except NameError:
            get_next_num = False


if __name__ == '__main__':
    for i in range(28):
        print(2, end = '')
    # main()