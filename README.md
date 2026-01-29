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
```text
task_manager/
├── main.py          # App assembly & router inclusion
├── routers/         # Endpoint definitions (Users & Tasks)
├── schemas/         # Pydantic models & field validation
└── README.md        # Project documentation