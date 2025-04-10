import csv
import os
import random

DATA_FILE = "data/movies.csv"

def recommend_similar():
    if not os.path.exists(DATA_FILE):
        print("❗ Movie dataset not found.\n")
        return

    print("Home 》Main User Page 》 Similar Movie Recommender\n")
    title = input("🎬 Enter the name of a movie you like: ").strip().lower()

    target_genre = None
    recommendations = []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))
        for row in reader:
            if title in row["title"].lower():
                target_genre = row["genre"]
                break

        if not target_genre:
            print("❌ Movie not found in database.\n")
            return

        for row in reader:
            if target_genre == row["genre"] and title not in row["title"].lower():
                recommendations.append(f"{row['title']} ({row['year']})")

    print(f"\n🔎 Based on your liking for that movie, here are similar movies in genre \"{target_genre}\":\n")
    for movie in random.sample(recommendations, min(5, len(recommendations))):
        print(f"• {movie}")
    print("\n🎬 Hope you find a new favorite!\n")
