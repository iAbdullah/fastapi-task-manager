# 🚀 Task Management System API

A professional-grade backend built with **FastAPI**. This project implements a modular architecture, modern Python type hinting, and robust data validation.

---

## 📌 Project Goals
The **Task Management System** provides a foundation for team collaboration by managing work items with strict validation rules:
* **User Roles**: Support for `admin`, `manager`, and `team_member`.
* **Task Validation**: Custom logic ensuring task titles are always capitalized.
* **Data Integrity**: Using `Literal` and `Annotated` for precise input control.

---

## 🏗️ Project Structure
Organized into logical modules for scalability:

task_manager/
├── main.py          # App assembly & router inclusion
├── routers/         # Endpoint definitions (Users & Tasks)
├── schemas/         # Pydantic models & field validation
└── README.md        # Project documentation
--------------------------------------------------------

---

## 📸 API Documentation & Testing Screenshots

### 1️⃣ Interactive API Hub (Swagger UI)
**Description:** This screenshot captures the FastAPI auto-generated documentation, highlighting the clean, modular organization of User and Task routers implemented using `APIRouter`. It serves as the central hub for testing all API functionality.

<img width="1918" height="1016" alt="1-29-2026" src="https://github.com/user-attachments/assets/fb4ed87d-c186-4fdc-a7fb-fe0c1052906f" />

---

### 2️⃣ Validation Test (Success Case - 200 OK)
**Description:** This test demonstrates a successful `POST` request to the `/tasks` endpoint. The input passes the custom `@field_validator` logic, which requires task titles to start with a capital letter.

----


<img width="1918" height="1023" alt="Screenshot --2026-01-29 220117" src="https://github.com/user-attachments/assets/9f56dbc7-0e00-46c7-b6ec-96b0b89f19be" />


---

### 3️⃣ Error Handling (Validation Error - 422)
**Description:** Demonstrating the API's robust error handling. A `422 Unprocessable Entity` status is returned when validation rules are violated—such as using a lowercase title or an invalid role—ensuring data integrity before processing.



---

<img width="1919" height="1024" alt="Screenshot 2026-01-29 220117" src="https://github.com/user-attachments/assets/53efbb66-58f9-48a5-b7c7-6ee22f87cfbb" />

---

