'''
http://www.careercup.com/question?id=15422849
Pots of gold game: Two players A & B. There are pots of gold arranged in a line, each containing some gold coins (the players can see how many coins are there in each gold pot - perfect information). They get alternating turns in which the player can pick a pot from one of the ends of the line. The winner is the player which has a higher number of coins at the end. The objective is to "maximize" the number of coins collected by A, assuming B also plays optimally. A starts the game. 

The idea is to find an optimal strategy that makes A win knowing that B is playing optimally as well. How would you do that? 

'''
from random import randint

class Pot_Of_Gold(object):
    def __init__(self, player1, player2, size):
        self.player1 = [player1, 0]
        self.player2 = [player2, 0]
        print "Hello " + player1 + " and  " + player2
        self.gold = [None] * size
        for i in range(0, size):
            self.gold[i] = randint(1, 100)
            print i
        print self.gold

    def play(self):
        print 'hello'
        player = self.player1
        while self.is_empty() != True:
            choice = input("Enter your choice " + player[0] +", (front is 1 , back is 2, quit is 4): ")
            print "you have :" + str(player[1])
            if choice == 4:
                print self.gold
                break
            if choice == 1:
                self.take_front_gold(player)
                print self.gold
                print player[1]
            elif choice == 2:
                self.take_back_gold(player)
                print self.gold
                print player[1]
            else:
                pass
            if player[0] == self.player1[0]:
                player = self.player2
            else:
                player = self.player1
        self.ending()

    def take_front_gold(self, player):
        for i in range(0, len(self.gold)):
            if self.gold[i] != None:
                player[1] += self.gold[i]
                self.gold[i] = None
                break

    def take_back_gold(self, player):
        for i in range(len(self.gold)-1, -1, -1):
            if self.gold[i] != None:
                player[1] += self.gold[i]
                self.gold[i] = None
                break

    def is_empty(self):
        for i in self.gold:
            if i != None:
                return False
        return True

    def ending(self):
        if self.player1[1] > self.player2[1]:
            print self.player1[0] + " wins!"
        elif self.player1[1] < self.player2[1]:
            print self.player2[0] + " wins!"
        else:
            print "its a tie!"

def main():
    game = Pot_Of_Gold('Robert', 'Loser', 10)
    game.play()

main()








