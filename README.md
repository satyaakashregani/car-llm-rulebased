# 🚗 India Cars LLM (Rule-Based Car Assistant)

A rule-based car assistant built in Python that answers queries about Indian cars (2000–2026) without using any external APIs.

This project simulates LLM-like behavior using structured data, search logic, and rule-based intent detection.

---

## 💡 Features

* 🔍 Fuzzy search with alias resolution
  (e.g., "brezza", "vitara brezza", typos)

* 🧠 Intent detection
  (price, mileage, engine, features, full details)

* 📊 Car comparison
  (e.g., "compare creta vs seltos")

* 🏷️ Brand-level and general queries
  (best EVs, safest cars, discontinued models)

* 💻 Interactive CLI interface

---

## ⚙️ Tech Stack

* Python
* Object-Oriented Programming (OOP)
* `difflib` (fuzzy matching)
* Rule-based logic (if / elif / else)
* Dictionaries & lists for structured data

---

## 🧠 Python Concepts Used

* Variables & Data Types
* Operators
* Conditional Statements
* Loops (for, while)
* Functions
* Data Structures (list, dict)
* Classes & Objects

---

## ▶️ How to Run

```bash
python main.py
```

---

## 💻 Example Usage

```
You: creta price
Price: ₹11L – ₹20L

You: alto engine
1.0L: 998cc, 67 PS

You: compare creta vs seltos
  Hyundai Creta   VS   Kia Seltos
--------------------------------------------------------------------------------
Feature                      Creta                     Seltos
--------------------------------------------------------------------------------
Category                     Mid-size SUV              Mid-size SUV
Mileage                      17.4 km/l (1.5 petrol IV  18.4 km/l (NA IVT)
Price Range                  Rs 10.99 lakh - Rs 20.15  Rs 10.89 lakh - Rs 21.15
Safety                       5-star IIHS Top Safety P  3-star Global NCAP

  ENGINES:
  1.5L MPi Petrol (NA)                     1.5L MPi Petrol (NA)
  1.5L mHEV Petrol (Mild Hybrid)           1.5L T-GDi Petrol (Turbo)
  1.5L U2 CRDi Diesel                      1.5L CRDi Diesel
  1.5L T-GDi Petrol Turbo                  ---

  TRANSMISSION:
  6-speed MT, IVT, 6-speed AT, 7-speed D   6-speed MT, 6-speed IVT (NA), 7-speed

---

## 🤖 Development Approach

This project was built with the help of AI tools (Claude) for refining and structuring parts of the code.

My primary focus was on:

* Understanding the logic
* Designing the system structure
* Implementing and modifying features

---

## 💡 Motivation

Choosing a car often leads to endless research.

This project aims to provide a quick, simple first-stop solution for basic car queries using a lightweight offline system.

---

## 🚀 Future Improvements

* Add web interface (Streamlit / Flask)
* Integrate real LLM APIs
* Expand car database
* Add advanced filtering (budget, fuel type, etc.)
* Voice-based interaction

---

## 📌 Note

This is a rule-based system built for learning purposes and does not use machine learning models.

---

## 📬 Feedback

Open to suggestions, improvements, and ideas!
