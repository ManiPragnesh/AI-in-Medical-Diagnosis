# **AI in Medical Diagnosis**

This project is a web-based application that leverages machine learning models to assist in diagnosing various medical conditions like diabetes, heart disease, and respiratory illnesses. Designed with accessibility and efficiency in mind, the platform empowers users with early disease detection through advanced AI tools integrated into a user-friendly interface.

## **Features**
- AI-powered predictions for multiple diseases based on user-provided data.
- Dynamic forms that adapt to the selected disease, ensuring relevant health parameters are input.
- Reliable and scalable backend API developed using Flask.
- Frontend built with HTML, CSS, and JavaScript for seamless interaction.
- Easy deployment using Docker and Kubernetes for scalability and portability.

## **Project Structure**
```
AI-in-Medical-Diagnosis/
├── backend/
│   ├── api.py                # Flask API for predictions
│   ├── models/               # Pre-trained machine learning models
│   ├── features/             # JSON files specifying disease-related features
├── frontend/
│   ├── index.html            # Main user interface
│   ├── script.js             # Client-side logic for dynamic forms and interactions
│   ├── styles.css            # Styling for the web application
├── requirements.txt          # Python dependencies
├── run_app.py                # Script to start both the frontend and backend
├── README.md                 # Project documentation
└── other scripts/            # Additional utilities (e.g., training scripts)
```

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/ManiPragnesh/AI-in-Medical-Diagnosis.git
cd AI-in-Medical-Diagnosis
```

### **2. Set Up the Virtual Environment**
```bash
python -m venv venv
.\venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Linux/Mac
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
python run_app.py
```
Once the script is running, open the application in your browser at:
```
http://127.0.0.1:5500
```

## **Usage**
1. Select a disease from the dropdown menu.
2. Provide the required health parameters in dynamically generated input fields.
3. Click "Diagnose" to receive predictions powered by trained machine learning models.
4. View the results displayed on the web interface.

## **Technologies Used**
- **Backend**:
  - Flask: Lightweight and robust framework for API development.
  - scikit-learn: Machine learning library for model training and predictions.
  - joblib: Used for saving and loading pre-trained models.
  - pandas: Data manipulation and preprocessing.
- **Frontend**:
  - HTML, CSS, JavaScript: For building interactive and responsive user interfaces.
- **Deployment**:
  - Docker: Containerization for portability.
  - Kubernetes: Scaling and orchestration of the application (optional).

## **Future Work**
- Integrate support for additional diseases to expand the scope.
- Enable real-time data analysis from wearable devices for enhanced diagnostics.
- Develop a mobile-friendly version to improve accessibility.
- Incorporate multi-language support to reach diverse user bases.
- Implement advanced security features to protect user data.

## **GitHub Repository**
[AI in Medical Diagnosis](https://github.com/ManiPragnesh/AI-in-Medical-Diagnosis)
