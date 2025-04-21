
# 🏡 House & Land Price Estimator

A simple and interactive desktop app built with Python and Tkinter to **estimate the price of land or house properties** based on location, condition, and additional house details like rooms, bathrooms, pool, etc.

--- 

## 🚀 Features

- 🔘 **Choose Property Type**: House or Land
- 🏘️ **Supports Location Type**: Urban, Suburban, Rural
- 🏚️ **Condition of House**: New, Old, Average
- 🧱 **Estimate based on Area (sq ft)**
- 🛏️ **House Details (optional)**:
  - Number of rooms & bathrooms
  - Parking availability
  - Garden availability
  - Pool availability
- 🔁 **Smooth Navigation** using **Enter key** (moves to next field)
- ✅ Dropdowns and toggles for clean & valid inputs
- 📦 Self-contained — no external files required

---

## 💻 How to Run

1. **Make sure you have Python 3 installed.**

2. Save the code in a file called `pricer.py`.

3. Run the file using:
```bash
python pricer.py
```


---

## 🧠 How It Works

- Pricing is calculated based on a **base rate per square foot** depending on the **location**.
- For **houses**, price adjusts based on:
  - **Condition** of the property (newer = higher)
  - **Additional features** like parking, pool, garden, etc.
- Intelligent backend logic estimates a realistic price using a multiplier system.

---

## 🔧 Technologies Used

- Python 🐍
- Tkinter (built-in GUI library)
- ttk Combobox for clean dropdowns

---

## 📌 To Do / Ideas

- [ ] Export report or price history
- [ ] Make web version with Flask or Django
- [ ] Add currency selection
- [ ] Save favorite properties

---

## 🧑‍💻 Author

Made with 💡 and ☕ by someone curious about real estate and Python automation.  
*Let’s build smarter tools together!*
