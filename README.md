A machine learning project for image classification using multiple models including Logistic Regression, Random Forest, and Support Vector Machine (SVM).
The project also provides interactive interfaces using Streamlit and Tkinter.

📂 Project Structure
├── logistic.joblib     # Trained Logistic Regression model
├── rf.joblib           # Trained Random Forest model
├── svm.rar             # Trained SVM model (compressed)
├── mlpjt.ipynb         # Jupyter Notebook (training & experiments)
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

Each model is saved using .joblib for fast loading and inference.

⚙️ Installation
git clone https://github.com/your-username/image-classification-project.git
cd image-classification-project
pip install -r requirements.txt
▶️ How to Run
1. Run Streamlit App
streamlit run steram.py

Then open the browser at:

http://localhost:8501
2. Run Tkinter App
python tekinter
3. Open Notebook
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
Load an image
Preprocess (resize / normalize)
Pass it to the selected model
Output the predicted class
💡 Future Improvements
Add Deep Learning model (CNN)
Improve UI/UX
Add model accuracy comparison dashboard
Deploy online (Streamlit Cloud / AWS)
