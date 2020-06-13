import random as rnd

class GuessGame():
    def __init__(self):
        self.min_guess = 0
        self.max_guess = 20
        
        self.correct_guess = rnd.randint(self.min_guess, self.max_guess)
        self.guessesTaken = 0
        self.guessingRange = range(1, 7)

        self.user_guess = 0

    def play(self):
        print(f'I am thinking of a number between {self.min_guess} and {self.max_guess}, Can you guess it right?')
        for g in self.guessingRange:
            self.user_guess = int(input())
            self.guessesTaken += 1
            if self.user_guess > self.correct_guess:
                print("You're higher than the number I am thinking of.")
            elif self.user_guess < self.correct_guess:
                print("You're lower than the number I am thinking of.")
            else:
                break

        if self.user_guess == self.correct_guess:
            print(f'Congratulations, you guessed it right, it is {self.correct_guess} indeed!')
        else:
            print(f'Sorry dude, the number I was thinking of is {self.correct_guess}!')


def main():
    GuessGame().play()
    
if __name__ == '__main__':
    main()
    
