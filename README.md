# 🫀 Heart Disease Prediction App

This is a **Heart Disease Prediction** web app built with:
- 🐍 Python & Scikit-learn
- 🎨 Streamlit for UI
- 📊 Pandas, Matplotlib, and Seaborn

---

## ✨ Features
- 🧠 Input clinical parameters like Age, Blood Pressure, Cholesterol, etc.
- ⚡ Instant heart-disease risk predictions.
- 🎨 Interactive and colorful UI with a responsive layout.
- 🧮 Uses a pre-trained RandomForest model (`heart_model.pkl`).

---

## 📂 Project Structure
```
Heart-Disease-Prediction/
├─ ml.py                # Streamlit app
├─ train_model.py       # Model training script
├─ heart_model.pkl       # Saved trained model
├─ heart-disease.csv     # Dataset file
├─ requirements.txt     # Dependencies
├─ LICENSE              # MIT License
├─ README.md            # Documentation file
```

---

## 🚀 Usage
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run ml.py
   ```

---

## 🧠 Retraining the model
Run the training script:
```bash
python train_model.py
```

---

💖 **Happy predicting!**
