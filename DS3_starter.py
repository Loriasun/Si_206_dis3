# import the random module
import random
#Unique Name: Loriasun
# create the class Dice
class Dice:
    # create the constructor (__init__) method
    # it takes as input the number sides and if none is specified use 6
    # it sets the dice object's number of sides (instance variable)
    # it sets the list that tracks the rolls to the empty list (instance variable)
    def __init__(self,num=6):
        
        self.num = num
        self.list = []

    # create the __str__ method
    # it returns "Last roll: value" where value is the last value in the list that tracks the rolls
    def __str__(self):
        return f"Last roll: {self.list[-1]}"

    # create the roll method
    # it randomly picks a value from 1 to the number of sides this dice object has
    # it adds that value to the end of the list that tracks all the rolls
    # it returns the value
    def roll(self):    
        n = random.randrange(1,self.num+1)
        self.list.append(n)
        return n

    # create the num_rolls method
    # uses user input to quantify the amount of rolls
    # it asks the users, "How many times do you want to roll?"
    # prints out each roll
    def num_rolls(self):
        print("How many times do you want to roll?")
        x = input()
        for i in range(int(x)):
           n = self.roll()
           print (n)



    # BONUS
    # create the print_count_for_num method
    # it will count how many times the passed number has been rolled and print 
    # number was rolled x times - where number is the number and x is the count
    def print_count_for_num(self,number):
        res = 0
        for i in range(len(self.list)):
            if(self.list[i] == number):
                res += 1
        #return res
        print(f"{number} was rolled {res} times")


# main function
def main():
    
    # Create an instance
    three_sided = Dice(3)
    print("Three sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(three_sided.roll())

    # Print last roll
    print(three_sided)

    # Create an instance
    six_sided = Dice()
    print("\nSix sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(six_sided.roll())

    # Print last roll
    print(six_sided)

    # prompts for user input
    dice = Dice()
    dice.num_rolls()
    

    # BONUS quiz
    # Print accumulation
    six_sided.print_count_for_num(3)

if __name__ == "__main__":
    main()