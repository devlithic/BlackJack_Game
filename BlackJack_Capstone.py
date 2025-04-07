import random

def deal_card():
    """Retourne une carte aléatoire du jeu."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calcule la somme des cartes en tenant compte des règles du Blackjack."""
    # Si la main contient un As (11) et le score dépasse 21, on considère l'As comme 1
    if sum(cards) > 21 and 11 in cards:
        index = cards.index(11)
        cards[index] = 1
    return sum(cards)


def display_status(user_cards, computer_cards, show_all=False):
    """Affiche l'état du jeu."""
    print(f"\nVos cartes: {user_cards}, score actuel: {calculate_score(user_cards)}")
    if show_all:
        print(f"Cartes du croupier: {computer_cards}, score: {calculate_score(computer_cards)}")
    else:
        print(f"Première carte du croupier: {computer_cards[0]}")


def compare_scores(user_score, computer_score):
    """Compare les scores et détermine le gagnant."""
    if user_score > 21:
        return "Vous avez dépassé 21. Vous perdez! 😭"
    elif computer_score > 21:
        return "Le croupier a dépassé 21. Vous gagnez! 😁"
    elif user_score > computer_score:
        return "Votre score est supérieur. Vous gagnez! 😁"
    elif user_score < computer_score:
        return "Le croupier a un meilleur score. Vous perdez! 😭"
    else:
        return "Égalité! 🙃"


def play_blackjack():
    """Fonction principale pour jouer au Blackjack."""
    print("\n🃏 Bienvenue au jeu de Blackjack! 🃏\n")

    # Initialisation des mains
    user_cards = []
    computer_cards = []
    game_over = False

    # Distribution des 2 premières cartes
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Vérification des Blackjack (21 avec 2 cartes)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    display_status(user_cards, computer_cards)

    if user_score == 21:
        print("Blackjack! Vous gagnez avec un 21 naturel! 🎉")
        return
    elif computer_score == 21:
        print("Le croupier a un Blackjack. Vous perdez! 😢")
        display_status(user_cards, computer_cards, show_all=True)
        return

    # Tour du joueur
    while not game_over:
        choice = input("\nTapez 'h' pour tirer une carte, 's' pour rester: ").lower()

        if choice == 'h':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            display_status(user_cards, computer_cards)

            if user_score > 21:
                print("Vous avez dépassé 21! 💥")
                game_over = True

        elif choice == 's':
            game_over = True

        else:
            print("Entrée invalide. Veuillez taper 'h' ou 's'.")

    # Tour du croupier (seulement si le joueur n'a pas dépassé 21)
    if user_score <= 21:
        print("\nTour du croupier:")

        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            print(f"Le croupier tire une carte. Cartes: {computer_cards}, score: {computer_score}")

        # Afficher le résultat final
        computer_score = calculate_score(computer_cards)
        display_status(user_cards, computer_cards, show_all=True)
        print("\n" + compare_scores(user_score, computer_score))


# Lancer le jeu
play_blackjack()

# Pour jouer à nouveau
while input("\nVoulez-vous jouer une autre partie? (o/n): ").lower() == 'o':
    print("\n" * 20)
    play_blackjack()

print("\nMerci d'avoir joué! À bientôt!")