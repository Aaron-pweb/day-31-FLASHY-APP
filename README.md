# ⚡ Flashy – Flash Card App (Day 31)

This is a **Flash Card learning app** built using **Tkinter** as part of **Day 31** of the [100 Days of Code: Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu on Udemy.

The app helps users learn **foreign language vocabulary** (e.g., French to English) using a simple and elegant GUI-based flash card system.

---

## 📸 Preview

*(Add screenshots here if you have any!)*

---

## 🧠 Features

- Displays a random French word on a flash card  
- Automatically flips the card to show the English translation after 3 seconds  
- User can mark words they know, which will be saved and removed from the learning list  
- Data is saved locally using `pandas` so progress is preserved  
- Simple, intuitive Tkinter GUI

---

## 🚀 How to Clone and Use

To use this app on your local machine, first clone the repository using `git clone https://github.com/your-username/flashy-app.git`, then navigate into the project folder with `cd flashy-app`. You can optionally create a virtual environment using `python -m venv venv` and activate it using `source venv/bin/activate` on macOS/Linux or `venv\Scripts\activate` on Windows. Next, install the dependencies by running `pip install pandas`. Once everything is set up, you can start the app by executing `python main.py`.

---

## 🛠️ Dependencies

- Python 3.x  
- `pandas`  
- `tkinter` (pre-installed with Python)

---

## 🧾 Files in This Project

- `main.py` – Main Python script with GUI logic  
- `data/french_words.csv` – Original vocabulary list  
- `images/` – Contains front and back flash card images and button icons  
- `words_to_learn.csv` – Auto-generated file that tracks learning progress

---

## 💡 What I Learned

- GUI development using Tkinter  
- Handling timed events with `after()`  
- Reading/writing CSV files with pandas  
- Randomization using `random.choice()`  
- Creating persistent, user-friendly apps

---

## 📅 Part of

> 💯 **100 Days of Code – The Complete Python Pro Bootcamp for 2023**  
> 📆 **Day 31** – Flashy Flash Card App

---

## 📘 License

This project is for educational and personal use.

---

## 🙌 Credits

Inspired by the **Flashy App** project from Angela Yu’s 100 Days of Code Python course on Udemy.
