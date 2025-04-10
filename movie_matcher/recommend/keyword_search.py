import csv
import os
import math

DATA_FILE = "data/movies.csv"
RESULTS_PER_PAGE = 5

def search_movies():
    if not os.path.exists(DATA_FILE):
        print("❗ Movie dataset not found.\n")
        return

    print("Home 》Main User Page 》 Keyword Search\n")
    keyword = input("🔍 Enter a keyword (title, genre, year, director): ").strip().lower()

    results = []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (keyword in row["title"].lower() or
                keyword in row["genre"].lower() or
                keyword in row["year"].lower() or
                keyword in row["director"].lower()):
                results.append(row)

    if not results:
        print("\n❌ No results found for that keyword.\n")
        return

    total_pages = math.ceil(len(results) / RESULTS_PER_PAGE)
    current_page = 1

    while True:
        start = (current_page - 1) * RESULTS_PER_PAGE
        end = start + RESULTS_PER_PAGE
        page_results = results[start:end]

        print(f"\n📃 Page {current_page} of {total_pages} — Showing {start + 1} to {min(end, len(results))} of {len(results)} results:\n")
        for idx, row in enumerate(page_results, start=1 + start):
            print(f"{idx}. {row['title']} ({row['year']}) — {row['director']}")

        print("\n[N]ext page | [P]revious | [Q]uit")
        nav = input("Your choice: ").strip().lower()

        if nav == "n" and current_page < total_pages:
            current_page += 1
        elif nav == "p" and current_page > 1:
            current_page -= 1
        elif nav == "q":
            print()
            break
        else:
            print("❗ Invalid choice or no more pages.\n")
