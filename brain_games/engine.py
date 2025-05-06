MAX_ROUNDS = 3

def run_game(game_logic, task_message):
    from brain_games.cli import welcome_user

    name = welcome_user()
    print(task_message)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
