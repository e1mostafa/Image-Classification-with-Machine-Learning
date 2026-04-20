import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import joblib
from tensorflow.keras.preprocessing.image import img_to_array
import os

# Load models
def load_models():
    try:
        return {
            "SVM": joblib.load("svm.joblib"),
            "Decision Tree": joblib.load("tree.joblib"),
            "Logistic Regression": joblib.load("logistic.joblib"),
            "Random Forest": joblib.load("rf.joblib")
        }
    except Exception as e:
        messagebox.showerror("Error", f"Model loading failed: {e}")
        return {}

models = load_models()

# Image preprocessing
def preprocess_image(img, target_size=(64, 64)):
    img = img.convert("L")  # Grayscale
    img = img.resize(target_size)
    img_array = img_to_array(img) / 255.0
    return img_array.reshape(1, -1)

# GUI Setup
app = tk.Tk()
app.title("🖼️ Image Classification (Tkinter)")
app.geometry("420x560")

canvas = tk.Canvas(app, width=300, height=300)
canvas.pack(pady=10)

label_info = tk.Label(app, text="Classes: buildings = 0, forest = 1, glacier = 2", font=("Arial", 11))
label_info.pack()

result_box = tk.Text(app, height=10, width=50)
result_box.pack(pady=10)

# Classify function
def classify_image():
    result_box.delete(1.0, tk.END)
    if not models:
        messagebox.showerror("Error", "Models not loaded.")
        return

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    try:
        image = Image.open(file_path).convert("RGB")
        tk_img = ImageTk.PhotoImage(image.resize((300, 300)))
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
        canvas.image = tk_img  # Prevent garbage collection

        processed = preprocess_image(image)

        result_box.insert(tk.END, "🔍 Prediction Results:\n\n")
        for name, model in models.items():
            pred = model.predict(processed)[0]
            result_box.insert(tk.END, f"{name}: {pred}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Error processing image:\n{e}")

# Button
btn = tk.Button(app, text="📤 Upload Image", command=classify_image, font=("Arial", 12))
btn.pack(pady=10)

app.mainloop()
