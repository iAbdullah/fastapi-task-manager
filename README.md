---
# 🚀 Task Management System API

A professional, modular RESTful API built with **FastAPI**. This system is designed to manage work tasks and users efficiently, featuring robust data validation and a clean architectural structure.

## 📌 Project Overview
The Task Management System provides a backend infrastructure for teams to organize and track their work. It implements modern Python practices, including:
* **Modular Routing**: Organized using `APIRouter` for scalability.
* **Data Integrity**: Strict validation using Pydantic `BaseModel` and `@field_validator`.
* **Type Hinting**: Extensive use of `Annotated`, `Literal`, and `Optional` for clear data structures.

---

## 🏗️ Directory Structure
Following a modular design to separate concerns:


task_manager/
├── main.py          # Application entry point & router assembly
├── routers/         # API route handlers (Users & Tasks)
├── schemas/         # Pydantic data models & validation logic
└── README.md
## 📸 API Documentation & Testing Screenshots


### 1️⃣ Interactive API Hub (Swagger UI)
**Description:** This screenshot captures the FastAPI auto-generated documentation, highlighting the clean, modular organization of User and Task routers implemented using `APIRouter`. It serves as the central hub for testing all API functionality.

<img width="1918" height="1016" alt="1-29-2026" src="https://github.com/user-attachments/assets/fb4ed87d-c186-4fdc-a7fb-fe0c1052906f" />

---

### 2️⃣ Validation Test (Success Case - 200 OK)
**Description:** This test demonstrates a successful `POST` request to the `/tasks` endpoint. The input passes the custom `@field_validator` logic, which requires task titles to start with a capital letter.
---------

<img width="1918" height="1016" alt="1-29-2026" src="https://github.com/user-attachments/assets/5bcd7f3c-bd99-4459-a714-58e967c0bd78" />

---

### 3️⃣ Error Handling (Validation Error - 422)
**Description:** Demonstrating the API's robust error handling. A `422 Unprocessable Entity` status is returned when validation rules are violated—such as using a lowercase title or an invalid role—ensuring data integrity before processing.

------------
> <img width="1918" height="1016" alt="Screenshot ---2026-01-29 220219" src="https://github.com/user-attachments/assets/648ff118-2f60-4919-b345-565fcfeeacd6" />
