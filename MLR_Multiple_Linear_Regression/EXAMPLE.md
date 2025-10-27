# 📘 **Multiple Linear Regression (MLR)**

## 🔹 **The Theory (What is it?)**

Think of **Simple Linear Regression** as predicting one thing using just one other thing.
👉 *Example:* Predicting your **Final Exam Score** using only your **Hours Studied**.

**Multiple Linear Regression (MLR)** is just an upgrade. You predict one thing (the dependent variable) using **two or more** other things (the independent variables).
👉 *Example:* Predicting your **Final Exam Score** using **Hours Studied + Attendance % + Midterm Score**.

---

## 🎯 **The "Problem" (The Goal)**

The goal is to find the **best possible formula** that combines the inputs to make the most accurate prediction.

### The formula looks like this:

[ Y = b_0 + b_1 \cdot X_1 + b_2 \cdot X_2 + \dots + b_n \cdot X_n ]

Where:

* **Y** → The thing you want to predict (e.g., *House Price*).
* **X₁, X₂, ... Xₙ** → The inputs or features (e.g., *Square Feet, Number of Bedrooms*).
* **b₁, b₂, ... bₙ** → The coefficients or weights (how much each input affects the final result).
* **b₀** → The intercept or base value (starting value of Y when all inputs are 0).

🧠 The model’s job is to look at past data (like 100 houses that already sold) and find the **best** values of *b₀, b₁, b₂...* that make the predictions as close as possible to the real prices.

---

## 🏠 **Example Problem**

### 🎯 **Goal:**

Predict a house's price.

### 📥 **Inputs (Features):**

* **X₁** → Square Footage (sq. ft.)
* **X₂** → Number of Bedrooms

### 📤 **Output (Target):**

* **Y** → Price (in $)

| Price (Y) | Sq. Footage (X₁) | Bedrooms (X₂) |
| --------- | ---------------- | ------------- |
| $300,000  | 1500             | 3             |
| $250,000  | 1300             | 2             |
| $450,000  | 2000             | 4             |

---

### 🧩 **1. The "Problem" to Solve:**

Find the best values for:

[ \text{Price} = b_0 + (b_1 \cdot X_1) + (b_2 \cdot X_2) ]

---

### 💻 **2. The "Solution" (What the Model Finds):**

After running the data through the model, it might find:

* **b₀ = 50,000**
* **b₁ = 150**
* **b₂ = 20,000**

---

### 📊 **3. Interpretation (What This Means):**

* The **base price** of a house (if it had 0 sq. ft. and 0 bedrooms) is **$50,000**.
* For every **1 extra square foot**, the price increases by **$150**.
* For every **1 extra bedroom**, the price increases by **$20,000**.

---

### 🔮 **4. How to Use It (Prediction):**

Predict the price of a new house with **1800 sq. ft.** and **3 bedrooms**:

[
\text{Price} = 50,000 + (150 \times 1800) + (20,000 \times 3)
]

[
\text{Price} = 50,000 + 270,000 + 60,000 = 380,000
]

✅ **Predicted Price = $380,000**

---

### 💡 **Summary:**

Multiple Linear Regression helps us understand **how multiple factors** affect an outcome — whether it’s exam scores, house prices, or sales predictions.

✨ *It’s simple math + data = smart predictions!*
