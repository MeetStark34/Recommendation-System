# 🎬 MovieMatcher : A Python-Based Movie Recommendation CLI App

Welcome to **MovieMatcher**, your personal movie recommendation assistant — right from the terminal. Built with Python, CSV data, Caesar cipher authentication, and a clean CLI flow, it's a fun and functional project inspired by Netflix-style discovery.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Register, Login, Reset Password
  - Caesar Cipher password encryption

- 🍿 **Recommendation Modes**
  - Recommend movies by **Genre**
  - Search by **Keyword** (title, director, year, genre)
  - Find **Similar Movies** by genre match

- 📁 **CSV-Based Dataset**
  - 2,500+ randomly generated movie entries with title, genre, year, and director

- 📜 **Terminal UI**
  - Styled menus and navigation
  - Paginated search results (5 per page)

---

## 📂 Folder Structure

```
movie_matcher/
├── auth/
│   ├── login.py
│   ├── register.py
│   └── reset_password.py
├── recommend/
│   ├── genre_based.py
│   ├── keyword_search.py
│   └── similar_movies.py
├── utils/
│   └── cipher.py
├── data/
│   ├── users.json
│   └── movies.csv
├── main.py
└── README.md
```

---

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://MeetStark34/movie-matcher.git
   cd movie-matcher
   ```

2. **Make sure you have Python 3 installed.**

3. **Run the app:**
   ```bash
   python main.py
   ```

---

## 📝 Movie Data

- Format: `title, genre, year, director`
- Stored in: `data/movies.csv`
- Sample:
  ```
  Inception, Sci-Fi, 2010, Christopher Nolan
  Parasite, Drama, 2019, Bong Joon-ho
  ```

---

## ✅ Example Flow

```
🎬 Welcome to @MeetStark34 MovieMatcher —
Your Personal Movie Recommender

---
Home

1️⃣  User Login 
2️⃣  User Register 
3️⃣  Reset Password
4️⃣  Exit
```

---

## ✨ Author

- **@MeetStark34** — Project concept & design  
- Built using plain Python (no frameworks, no web)

---

## 📄 License

This project is open-source and free to use for educational purposes.
