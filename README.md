# 🏥 Medical Image Classification Using CNN

## 📌 Project Overview

This project implements a **Medical Image Classification System** using **Deep Learning (CNN)**.  
The model classifies medical images into:

- ✅ Normal
- ⚠ Diseased

The system assists in identifying abnormalities in medical images such as **Chest X-rays**, helping in early diagnosis.

---

## 🎯 Problem Statement

Medical image analysis is crucial for disease detection.  
This project uses a **Convolutional Neural Network (CNN)** to automatically classify images as **Normal** or **Diseased**.

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- NumPy

---

## 📂 Dataset Structure

The dataset must be organized as follows:

dataset/
├── train/
│ ├── normal/
│ └── diseased/
│
└── test/
├── normal/
└── diseased/


✔ Only image files (JPG / PNG)

---

## 📊 Dataset Source (Recommended)

Chest X-Ray Pneumonia Dataset:

https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

---

## 🔁 Class Mapping

| Original Dataset | Project Folder |
|------------------|----------------|
| NORMAL           | normal         |
| PNEUMONIA        | diseased       |

⚠ Folder names are **case-sensitive**

---

## 🚀 How To Run The Project

### ✅ 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
## 2️⃣ Train Model

```
python main.py
```

Select:

1 → Train Model
✔ Model will be saved in:
models/medical_cnn_model.h5

## ✅ 3️⃣ Predict Image

```
python main.py
```
Select:

2 → Predict Image

Enter image path.

✅ Output

The system predicts:

✅ Normal

⚠ Diseased
