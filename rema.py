
def main():#ذا تعريف الدالة الرئيسية main()
    
    print("🎓 Welcome to the Math Quiz Game!")# رسالة ترحيبية
    
    user_name = input("Please enter your name: ").strip()
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

    print(f"\nHi {user_name}, let's start!\n")#\n لإضافة سطر جديد لزيادة وضوح العرض

    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for idx, choice in enumerate(q["choices"], 1):
            print(f"  {idx}. {choice}")

        try:
            user_input = int(input("Enter your answer (1-4): "))
            if user_input < 1 or user_input > 4:
                raise ValueError("Invalid choice number.")

            selected = q["choices"][user_input - 1]

            if selected == q["answer"]:
                score += q["points"]
                print(f"✅ Correct! You earned {q['points']} point(s). Total score: {score}\n")
            else:
                score = 0
                print(f"❌ Wrong answer! The correct answer was: {q['answer']}")
                print("You lost all your points. Game Over!\n")
                break

        except ValueError:
            print("⚠️ Invalid input! Please enter a number from 1 to 4.")
            print("You lost all your points due to invalid input. Game Over!\n")
            score = 0
            break

    print(" Final Results:")
    print(f"👤 Player: {user_name}")
    print(f"🏁 Score: {score}")

# Run the game
if __name__ == "__main__":
    main()
