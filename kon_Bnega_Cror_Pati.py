# Program to play the game of Kon Bnega Cror Pati
def play_game():
    print("Welcome to Kon Bnega Cror Pati!")
    questions = ["What is the capital of France",
                 "What is 2 + 2",
                 "What is the largest planet in our solar system"]
    options = [["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
               ["A) 3", "B) 4", "C) 5", "D) 6"],
               ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"]]
    answers = ["A", "B", "C"]

    score = 0
    for i in range(len(questions)):
        print(i+1,". ", questions[i], end="?\n")
        for option in options[i]:
            print(" ", option, end="\n")
        user_answer = input("Your answer (A/B/C/D):").strip().upper()
        if user_answer == answers[i]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer! The correct answer was", answers[i])
            print("Game Over!")
            return score
    
    print("Congratulations! You've answered all questions correctly.")
    return score

if __name__ == "__main__":
    print("Starting the game Kon Bnega Cror Path")
    starting_prize = 5000
    score = play_game()
    print("you won",starting_prize * score, "rupees!")
    print("Thank you for playing Kon Bnega Cror Pati!")
