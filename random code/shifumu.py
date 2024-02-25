import random

CHOICES = ["pierre", "papier", "ciseaux"]

def get_user_choice(player_name: str) -> str:
    while True:
        try:
            choice = input(f"{player_name}, choisissez pierre, papier ou ciseaux : ").lower()
            if choice in CHOICES:
                return choice
            else:
                print("Choix invalide! Veuillez choisir entre pierre, papier ou ciseaux.")
        except KeyboardInterrupt:
            print("\nAu revoir!")
            exit()

def get_computer_choice() -> str:
    return random.choice(CHOICES)

def determine_winner(player_name: str, user_choice: str, computer_choice: str) -> str:
    if user_choice == computer_choice:
        return "Égalité!"
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "papier" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "papier"):
        return f"{player_name} a gagné!"
    else:
        return "L'ordinateur a gagné!"

def play_game():
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

        num_games = int(input("Combien de parties voulez-vous jouer ? "))

        player1_wins = 0
        player2_wins = 0
        game_count = 0

        while game_count < num_games:
            player1_choice = get_user_choice(player1_name)

            if player1_choice == "stop":
                print("Au revoir!")
                break

            player2_choice = get_user_choice(player2_name) if num_players == 2 else get_computer_choice()

            print(f"{player1_name} a choisi :", player1_choice)
            print(f"{player2_name} a choisi :", player2_choice)

            winner = determine_winner(player1_name, player1_choice, player2_choice)
            print(winner)

            if winner == f"{player1_name} a gagné!":
                player1_wins += 1
            elif winner == "L'ordinateur a gagné!" or winner == f"{player2_name} a gagné!":
                player2_wins += 1

            game_count += 1

        print(f"Nombre de victoires de {player1_name} :", player1_wins)
        print(f"Nombre de victoires de {player2_name} :", player2_wins)

    except ValueError:
        print("Veuillez entrer un nombre valide.")

def main():
    play_game()

if __name__ == "__main__":
    main()

