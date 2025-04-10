from auth import login, register, reset_password
from recommend import genre_based, keyword_search, similar_movies

def main():
    print("\n🎬 Welcome to @MeetStark34 MovieMatcher —")
    print("Your Personal Movie Recommender\n")

    while True:
        print("---")
        print("Home\n")
        print("1️⃣  User Login")
        print("2️⃣  User Register")
        print("3️⃣  Reset Password")
        print("4️⃣  Exit\n")

        choice = input("Enter your choice: ").strip()
        print("---\n")

        if choice == "1":
            username = login.authenticate()
            if username:
                user_menu(username)
        elif choice == "2":
            register.create_account()
        elif choice == "3":
            reset_password.reset_user_password()
        elif choice == "4":
            print("👋 Goodbye! See you next time!\n")
            break
        else:
            print("❗ Invalid option. Please try again.\n")

def user_menu(username):
    while True:
        print("---")
        print(f"Home 》Main User Page ({username})\n")
        print("1️⃣  Recommend Movies by Genre")
        print("2️⃣  Search Movies by Keyword")
        print("3️⃣  Recommend Similar Movies")
        print("4️⃣  Logout\n")

        choice = input("Enter your choice: ").strip()
        print("---\n")

        if choice == "1":
            genre_based.recommend_by_genre()
        elif choice == "2":
            keyword_search.search_movies()
        elif choice == "3":
            similar_movies.recommend_similar()
        elif choice == "4":
            print("🔒 Logged out.\n")
            break
        else:
            print("❗ Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
