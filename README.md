📂 Project Structure
├── logistic.joblib     # Trained Logistic Regression model
├── rf.joblib           # Trained Random Forest model
├── svm.rar             # Trained SVM model (compressed)
├── mlpjt.ipynb         # Training & experiments notebook
├── steram.py           # Streamlit web app
├── tekinter            # Tkinter GUI version
🚀 Features
🖼️ Image classification using multiple ML models
🔄 Compare performance between models
🌐 Web interface using Streamlit
🖥️ Desktop GUI using Tkinter
📊 Training and experimentation in Jupyter Notebook
🧪 Models Used
Logistic Regression
Random Forest
Support Vector Machine (SVM)

All models are saved using .joblib for fast loading and inference.

⚙️ Installation
git clone https://github.com/your-username/image-classification-project.git
cd image-classification-project
pip install -r requirements.txt
▶️ How to Run
🌐 Run Streamlit App
streamlit run steram.py

Open in browser:
👉 http://localhost:8501

🖥️ Run Tkinter App
python tekinter
📓 Open Notebook
jupyter notebook mlpjt.ipynb
📦 Requirements
numpy
pandas
scikit-learn
joblib
streamlit
Pillow
opencv-python
📸 How It Works
Upload or load an image
Preprocess (resize / normalize)
Pass it to the selected model
Get predicted class
💡 Future Improvements
🤖 Add Deep Learning model (CNN)
🎨 Improve UI/UX
📊 Add accuracy comparison dashboard
☁️ Deploy online (Streamlit Cloud / AWS)
👨‍💻 Author

Elmostafa Mohamed
Cybersecurity & Software Engineering Student

⚠️ Notes
Extract the SVM model before using it
Keep all .joblib files in the same directory
