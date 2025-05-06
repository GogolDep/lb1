from brain_games.engine import run_game
from games.game_gcd import generate_question as gcd_game
from games.game_progression import generate_question as prog_game

def main():
    print("Choose a game:")
    print("1 - Least Common Multiple")
    print("2 - Geometric Progression")
    choice = input("Enter number: ")

    if choice == "1":
        run_game(gcd_game, "Find the smallest common multiple of given numbers.")
    elif choice == "2":
        run_game(prog_game, "What number is missing in the progression?")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
