import re

class Player:
    def __init__(self, name, id):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

class Question:
    def __init__(self, id, text, choices, answer, mark):
        self.id = id
        self.text = text
        self.choices = choices
        self.answer = answer
        self.mark = mark

    def is_correct(self, choice_index):
        return self.choices[choice_index] == self.answer

class Game:
    def __init__(self):
        self.questions = [
            Question(1, "What is 9 + 6?", ["14", "15", "16", "17"], "15", 1),
            Question(2, "What is 7 × 4?", ["28", "24", "32", "30"], "28", 2),
            Question(3, "What is the square root of 49?", ["6", "7", "8", "9"], "7", 3),
            Question(4, "What is (3 + 5) × 2?", ["16", "13", "18", "20"], "16", 4)
        ]
        self.player = None

    def get_player_name(self):
        while True:
            name = input("[INPUT] Please enter your name: ").strip()
            if not re.match("^[A-Za-z ]+$", name):
                print("[ERROR] Name must contain only letters. Try again.")
            else:
                return name

    def play(self):
        print("[INFO] Welcome to the Math Quiz Game!")

        name = self.get_player_name()
        self.player = Player(name, 1)

        for q in self.questions:
            print(f"[QUESTION {q.id}] {q.text}")
            for idx, choice in enumerate(q.choices, 1):
                print(f"   {idx}. {choice}")

            try:
                user_input = int(input("[INPUT] Enter your answer (1-4): "))
                if user_input < 1 or user_input > 4:
                    raise ValueError

                if q.is_correct(user_input - 1):
                    self.player.add_score(q.mark)
                    print(f"[OK] Correct! +{q.mark} points. Total score: {self.player.score}\n")
                else:
                    print(f"[WRONG] Incorrect. Correct answer was: {q.answer}")
                    self.player.reset_score()
                    print("[GAME OVER] You lost all your points.\n")
                    break

            except ValueError:
                print("[ERROR] Invalid input. Please enter a number between 1 and 4.")
                self.player.reset_score()
                print("[GAME OVER] Invalid input caused game over.\n")
                break

        print("[RESULTS] Game Over")
        print(f"[PLAYER] Name: {self.player.name}")
        print(f"[SCORE] Final Score: {self.player.score}")

    def ask_play_again(self):
        while True:
            again = input("[INPUT] Do you want to play again? (y/n): ").lower()
            if again == "y":
                self.play()
            elif again == "n":
                print("[EXIT] Thank you for playing!")
                break
            else:
                print("[ERROR] Please enter 'y' or 'n'.")

# Start the game
if __name__ == "__main__":
    game = Game()
    game.play()
    game.ask_play_again()
