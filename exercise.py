from random import randint

def choose_difficulty():
    """
    Prompt the player to select a difficulty level and return game settings.

    Returns:
        tuple: A configuration tuple containing (max_number, max_attempts)
    """
    print("=" * 40)
    print("      🎯 WELCOME TO NUMBER MASTER 🎯      ")
    print("=" * 40)
    print("Select your difficulty level:")
    print("1. Easy   (Range: 1-50,  🎈 Unlimited Lives)")
    print("2. Medium (Range: 1-100, ❤️ 7 Lives)")
    print("3. Hard   (Range: 1-200, 🔥 5 Lives)")
    print("=" * 40)

    while True:
        choice = input("Enter choice (1, 2, or 3): ").strip()
        if choice == '1':
            return 50, float('inf')
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 200, 5
        print("❌ Invalid selection. Please enter 1, 2, or 3.")

def play_game():
    """
    Run the main game loop for the enhanced number guessing game.
    """
    max_number, lives = choose_difficulty()
    secret_number = randint(1, max_number)
    attempts = 0

    print(f"\n🔢 I have chosen a secret number between 1 and {max_number}.")
    if lives != float('inf'):
        print(f"❤️ You have {lives} lives to guess it. Good luck!\n")
    else:
        print("🎈 You have infinite lives for this practice round.\n")

    while True:
        # Validate that the input is actually a valid integer
        try:
            guess = int(input("👉 Guess the number: "))
        except ValueError:
            print("❌ That's not a valid number! Please enter an integer.")
            continue

        attempts += 1

        # Check the guess
        if guess == secret_number:
            print("\n" + "🎉" * 20)
            print("🏆 CONGRATULATIONS! YOU WON! 🏆")
            print(f"The winning number was indeed {secret_number}.")
            print(f"It took you {attempts} attempts to crack the code!")
            print("🎉" * 20 + "\n")
            break
        
        # Give directional feedback
        if guess > secret_number:
            print("📉 Too high! Your guess is GREATER than my number.")
        else:
            print("📈 Too low! Your guess is LESS than my number.")

        # Manage remaining lives if not on easy mode
        if lives != float('inf'):
            remaining_lives = lives - attempts
            if remaining_lives <= 0:
                print("\n" + "💀" * 20)
                print("💥 GAME OVER! 💥")
                print(f"You ran out of lives. The secret number was {secret_number}.")
                print("💀" * 20 + "\n")
                break
            else:
                print(f"❤️ Lives remaining: {remaining_lives}\n")
        print("-" * 30)

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("🔄 Play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\n👋 Thanks for playing Number Master! Goodbye!")
            break
