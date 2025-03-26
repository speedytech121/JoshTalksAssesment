# **Django Task Management API**

## **📌 Description**  
A simple Task Management API built with **Django** and **Django REST Framework (DRF)**. It allows users to:  
✅ Create Users  
✅ Create tasks  
✅ Assign tasks to users  
✅ Retrieve assigned tasks  

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/speedytech121/JoshTalksAssesment.git
cd task-manager
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
```
- **Activate the virtual environment:**  
  - **On macOS/Linux:**  
    ```bash
    source venv/bin/activate
    ```
  - **On Windows:**  
    ```bash
    venv\Scripts\activate
    ```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Superuser (Admin Access)**  
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### **6️⃣ Run the Development Server**  
```bash
python manage.py runserver
```
Your API will be accessible at: **`http://127.0.0.1:8000/`**

---

## **🛠 API Endpoints** (Test with Postman)  

### **🔹 1. Create a User**  
📌 **Endpoint:** `POST http://127.0.0.1:8000/tasks/create-user/`  
📌 **Request Body (JSON):**  
```json
{
    "name": "Rahul",
    "email": "rahul@example.com",
    "mobile": 9076548880
}
```

---

### **🔹 2. Create a Task**  
📌 **Endpoint:** `POST http://127.0.0.1:8000/tasks/create/`  
📌 **Request Body (JSON):**  
```json
{
    "name": "Login Form Creation",
    "description": "Create login form for the clients.",
    "task_type": "Feature",
    "status": "Pending"
}
```

---

### **🔹 3. Assign Task to a User**  
📌 **Endpoint:** `POST http://127.0.0.1:8000/tasks/2/assign/`  
📌 **Request Body (JSON):**  
```json
{
    "user_ids": [1]
}
```

---

### **🔹 4. Get Tasks Assigned to a User**  
📌 **Endpoint:** `GET http://127.0.0.1:8000/tasks/user/1/`  

---

## **🔑 Admin Panel Access**  
You can manage users and tasks through the **Django Admin Panel**:  
📌 **URL:** `http://127.0.0.1:8000/admin/`  

Log in using the superuser credentials you created earlier.


