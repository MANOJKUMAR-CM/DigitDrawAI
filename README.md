# DigitDrawAI
# 🖌️ AI Handwritten Digit Recognition

## 🎯 Project Overview
This AI application allows users to **draw a digit** using their mouse pointer on a UI canvas. The drawn digit is then recognized using an underlying **machine learning classifier**. The system is designed as a **REST API** using FastAPI, and the UI component interacts with the API for digit prediction.

## 🏗️ Architecture
1. **Frontend UI** – A simple interface where users can draw a digit.
2. **FastAPI Backend** – A REST API that receives the drawing, processes it, and returns the predicted digit.
3. **Machine Learning Model** – A trained neural network model that classifies handwritten digits.
4. **Dockerized API** – The backend service is containerized using Docker for easy deployment.

## 🚀 How It Works
1. **User draws a digit** on the canvas.
2. **The UI sends the drawing** to the FastAPI backend.
3. **The backend processes the image** and uses a trained model to predict the digit.
4. **The predicted digit is returned** and displayed on the UI.

---

## 🛠️ Setting Up & Running the Application

### **Method 1: Using Docker** 🐳
1. **Build the Docker image:**
   ```sh
   docker build -t digit_recognizer:v1 .
   ```
2. **Run the Docker container:**
   - Configure Docker to map a host port to the exposed container port.
   - Example: Map port `7000` on the host to the container.
   ```sh
   docker run -p 7000:8080 digit_recognizer:v1
   ```
3. **Start the UI:**
   ```sh
   python app.py http://localhost:7000/predict
   ```

### **Method 2: Running Manually** 🖥️
1. **Start the FastAPI server:**
   ```sh
   python server.py
   ```
2. **Start the UI:**
   ```sh
   python app.py http://localhost:8080/predict
   ```

---

## 📝 Project Files
📂 **Dockerfile**
```dockerfile
FROM python:3.10
ADD dense_neural_class.py .
ADD utils.py .
ADD model.pkl .
ADD requirementsDigit.txt .
ADD server.py .
EXPOSE 8080
RUN pip install --upgrade pip
RUN pip install -r requirementsDigit.txt
CMD [ "python", "./server.py" ]
```

📂 **requirementsDigit.txt**
```
uvicorn
fastapi
pydantic
pickle-mixin
matplotlib
```

---

## 🎯 Key Features  

✅ **Intuitive UI** – Users can easily draw digits using a mouse.  

✅ **Real-time Predictions** – Quick response from the backend.  

✅ **FastAPI-based API** – Lightweight, efficient, and scalable.  

✅ **Docker Support** – Easy deployment with containerization.  

✅ **Customizable Model** – Swap out the ML model for improvements.  

---

## 🚀 Future Enhancements  

🔹 **Improve UI design** for a smoother experience.  

🔹 **Enhance the model** for better accuracy.  

🔹 **Extend support** for recognizing letters and symbols.  

🔹 **Deploy on cloud** for broader accessibility.  

---


## 📌 Conclusion
This AI-powered digit recognition app demonstrates how **machine learning models** can be deployed as **REST APIs** and integrated with **interactive user interfaces**. With Docker support, it becomes even more portable and scalable. 🚀

## 📧 Contact

If you have questions, suggestions, or just want to connect, feel free to reach out!

- **Name**: Manoj Kumar.CM  
- **Email**: [manoj.kumar@dsai.iitm.ac.in]  
- **GitHub Profile**: [Manoj Kumar C M](https://github.com/MANOJKUMAR-CM)


Happy Coding! 💡✨

