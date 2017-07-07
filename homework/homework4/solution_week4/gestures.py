import random

class Rock(object):

    def __lt__(self, other):
        return isinstance(other, Paper)
    def __gt__(self,other):
        return isinstance(other, Scissors)
    def __eq__(self,other):
        return isinstance(other, Rock)
    def __str__(self):
        return "Rock"

class Paper(object):
    def __lt__(self, other):
        return isinstance(other, Scissors)
    def __gt__(self,other):
        return isinstance(other, Rock)
    def __eq__(self,other):
        return isinstance(other, Paper)
    def __str__(self):
        return "Paper"

class Scissors(object):
    def __lt__(self, other):
        return isinstance(other, Rock)
    def __gt__(self,other):
        return isinstance(other, Paper)
    def __eq__(self,other):
        return isinstance(other, Scissors)
    def __str__(self):
        return "Scissors"

class Player(object):
    def play(self):
        return random.choice([Rock(), Paper(), Scissors()])

class HumanPlayer(Player):
    def play(self):
        choice = input("Your gesture ([r]ock, [p]aper, [s]cissors): ").lower()
        if choice.startswith('r'): 
            return Rock()
        elif choice.startswith('p'):
            return Paper()
        elif choice.startswith('s'):
            return Scissors()


def main():
    human = HumanPlayer()
    computer = Player()

    scores = {'human': 0, 'computer':0}
    
    while True: 
        human_gesture = human.play()
        computer_gesture = computer.play()
        print("You chose {0}, I chose {1}.".format(human_gesture, computer_gesture))
        
        if human_gesture > computer_gesture:
            print("You win.")
            scores['human'] += 1
        elif human_gesture < computer_gesture:
            print("I win.")
            scores['computer'] += 1
        else: 
            print("Draw.")
        # Otherwise nothing changes
        print("You: {0[human]}, I: {0[computer]}".format(scores))

if __name__ == "__main__":    
    main()
