import csv
import os

DATA_FILE = "data/movies.csv"

def recommend_by_genre():
    if not os.path.exists(DATA_FILE):
        print("❗ Movie dataset not found.\n")
        return

    print("Home 》Main User Page 》 Genre\n")

    genres = set()
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            genres.add(row["genre"])

    genre_list = sorted(genres)
    print("🎭 Available Genres:")
    for genre in genre_list:
        print(f"> {genre}")
    
    selected = input("\nPick a genre: ").strip().title()

    print(f"\nHome 》Main User Page 》 Genre 》 {selected}\n")

    recommendations = []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["genre"].lower() == selected.lower():
                recommendations.append(f"{row['title']} ({row['year']})")

    if recommendations:
        print(f"🧠 Based on your interest in \"{selected}\", we recommend:\n")
        for movie in recommendations[:5]:
            print(f"• {movie}")
        print("\n🍿 Enjoy your movie time!\n")
    else:
        print("❗ No movies found in that genre.\n")
