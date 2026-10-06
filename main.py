import random as rand

class Guess_Game:
    
    def get_answer(self):
        answer = rand.randint(0,999)
        if answer % 2 == 0:
            answer += 1
        return answer
    
    def get_input(self):
        valid_guess = False
        while(valid_guess == False):
            guess = input("Guess an *odd* number 1-1000: \n").strip()
            
            try:
                guess = int(guess)
                if(guess % 2 != 0):
                    valid_guess = True
                    return guess
                else:
                    print("Number MUST be odd.")
            except:
                print("Please enter a valid *odd* number 1-1000")
                continue
                
    
    def play(self):
        guessed = False
        answer = self.get_answer()

        while guessed == False:

            guess = self.get_input()

            if (guess == answer):
                print(f"\nCongrats! You guessed the number! (", answer, ")")
                print("Thanks for playing!")
                guessed = True

            elif (guess < answer):
                print("The number is greater than", guess, "\n")

            else:
                print("The number is less than", guess,"\n")
        
def main():
    game = Guess_Game()
    game.play()

if __name__ == '__main__':
    main()