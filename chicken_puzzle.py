"""
Assignment 3:- 
We have a count 35 heads and 94 legs among the chickens and rabbits in a farm. How many
rabbits and how many chickens do we have? Write a program to get the answer,
"""


class Puzzle:
    def __init__(self, heads, legs):
        self.legs = legs
        self.heads = heads

    def calculate(self):
        legs = self.legs
        heads = self.heads

        """
        1 rabbit and 1 chicken, we will have two heads but 6 legs.
        So, the number of legs should always be greater than the number
        of heads and all legs are even numbers. So, there is no posibilities
        that the legs should be an odd number.
        """
        if legs % 2 != 0 or heads == 0 or heads > legs:
            print('No posibility to count rabbits and chickens.')
        else:

            """
            A rabbit is equal to 2 chickens. so based on it equation
            is 4 legs of rabbit = 2 legs of 2 chickens.
            4rabbits + 2chickens = total legs
            and 1 head of rabbit and 1 head of chicken, representated as
            rabbit + chicken = total heads
            """

            rabbits = int((legs + (-2*heads))/2)
            chickens = int(heads - rabbits)
            print('{} {}'.format(chickens, rabbits))


p = Puzzle(35, 94)
p.calculate()
