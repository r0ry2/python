def is_valid_name(name):
    return name.isalpha()  # يتحقق إذا كان الاسم يحتوي فقط على حروف

def play_game():
    print("[INFO] Welcome to the Math Quiz Game!")

    # التحقق من الاسم
    while True:
        user_name = input("Please enter your name: ").strip()
        if is_valid_name(user_name):
            break
        else:
            print("[ERROR] Invalid name! Please enter letters only (no numbers or symbols).")

    score = 0

    questions = [
        {
            "question": "What is 9 + 6?",
            "choices": ["14", "15", "16", "17"],
            "answer": "15",
            "points": 1
        },
        {
            "question": "What is 7 × 4?",
            "choices": ["28", "24", "32", "30"],
            "answer": "28",
            "points": 2
        },
        {
            "question": "What is the square root of 49?",
            "choices": ["6", "7", "8", "9"],
            "answer": "7",
            "points": 3
        },
        {
            "question": "What is (3 + 5) × 2?",
            "choices": ["16", "13", "18", "20"],
            "answer": "16",
            "points": 4
        }
    ]

    print(f"\n[INFO] Hi {user_name}, let's start!\n")

    for i, q in enumerate(questions):
        print(f"[Q{i+1}] {q['question']}")
        for idx, choice in enumerate(q["choices"], 1):
            print(f"  {idx}. {choice}")

        try:
            user_input = int(input("Enter your answer (1-4): "))
            if user_input < 1 or user_input > 4:
                raise ValueError("Invalid choice number.")

            selected = q["choices"][user_input - 1]

            if selected == q["answer"]:
                score += q["points"]
                print(f"[OK] Correct! You earned {q['points']} point(s). Total score: {score}\n")
            else:
                score = 0
                print(f"[ERROR] Wrong answer! The correct answer was: {q['answer']}")
                print("[INFO] You lost all your points. Game Over!\n")
                break

        except ValueError:
            print("[ERROR] Invalid input! Please enter a number from 1 to 4.")
            print("[INFO] You lost all your points due to invalid input. Game Over!\n")
            score = 0
            break

    print("----- Final Results -----")
    print(f"[PLAYER] {user_name}")
    print(f"[SCORE]  {score}")
    print("-------------------------")

def main():
    while True:
        play_game()

        retry = input("Do you want to play again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("[INFO] Thanks for playing! Goodbye!")
            break

# Start the program
if __name__ == "__main__":
    main()
