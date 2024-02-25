import random

def get_user_guess(player_name: str, lower_bound: int, upper_bound: int) -> int:
    while True:
        try:
            guess = int(input(f"{player_name}, devinez le nombre mystère (entre {lower_bound} et {upper_bound}) : "))
            return guess
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def generate_secret_number(difficulty: str) -> int:
    if difficulty == "easy":
        return random.randint(1, 50)
    elif difficulty == "medium":
        return random.randint(1, 100)
    elif difficulty == "hard":
        return random.randint(1, 150)

def determine_number_game_winner(player_name: str, user_guess: int, secret_number: int) -> str:
    if user_guess == secret_number:
        return f"Félicitations, {player_name} a deviné le nombre mystère!"
    elif user_guess < secret_number:
        return "Trop bas! Essayez à nouveau."
    else:
        return "Trop haut! Essayez à nouveau."

def play_number_game():
    try:
        num_players = int(input("Combien de joueurs ? (1 ou 2) "))
        if num_players not in [1, 2]:
            print("Nombre de joueurs invalide!")
            return

        player1_name = input("Entrez votre pseudo : ")

        if num_players == 2:
            player2_name = input("Entrez le pseudo du joueur 2 : ")
        else:
            player2_name = "Ordinateur"

        difficulty = input("Choisissez la difficulté (easy, medium, hard) : ").lower()
        if difficulty not in ["easy", "medium", "hard"]:
            print("Difficulté invalide!")
            return

        if difficulty == "easy":
            lower_bound, upper_bound = 1, 50
        elif difficulty == "medium":
            lower_bound, upper_bound = 1, 100
        else:
            lower_bound, upper_bound = 1, 150

        secret_number = generate_secret_number(difficulty)
        print(f"Le nombre mystère a été généré (difficulté : {difficulty}, intervalle : [{lower_bound}, {upper_bound}]).")

        player1_attempts = 0
        player2_attempts = 0
        max_attempts = {"easy": 10, "medium": 7, "hard": 5}

        while True:
            player1_guess = get_user_guess(player1_name, lower_bound, upper_bound)

            if num_players == 2:
                player2_guess = get_user_guess(player2_name, lower_bound, upper_bound)
                player2_attempts += 1
                print(f"{player2_name} a deviné {player2_attempts} fois.")

                result = determine_number_game_winner(player2_name, player2_guess, secret_number)
                print(result)

                if player2_guess == secret_number:
                    print(f"Félicitations, {player2_name} a deviné le nombre mystère!")
                    break

            player1_attempts += 1
            print(f"{player1_name} a deviné {player1_attempts} fois.")

            result = determine_number_game_winner(player1_name, player1_guess, secret_number)
            print(result)

            if player1_guess == secret_number:
                break

            if player1_attempts == max_attempts[difficulty]:
                print(f"Nombre maximal d'essais atteint. Le nombre mystère était {secret_number}.")
                break

        print(f"Nombre total d'essais de {player1_name} : {player1_attempts}")
        if num_players == 2:
            print(f"Nombre total d'essais de {player2_name} : {player2_attempts}")

    except ValueError:
        print("Veuillez entrer un nombre valide.")

def main():
    play_number_game()

if __name__ == "__main__":
    main()
