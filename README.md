# 📦 KoreInventory

A modern, real-time, full-stack inventory management web application built specifically for small and local businesses to replace outdated spreadsheets and paper ledgers with a clean, efficient, and robust platform.

---

## 🚀 Overview

Most small and local businesses still rely on physical notebooks or messy Excel spreadsheets to manage inventory. This manual tracking is error-prone, time-consuming, and makes it nearly impossible to spot trends like fast-moving items versus dead stock. 

**KoreInventory** strips away complex enterprise jargon to provide a simple, no-nonsense platform where local business owners can easily track stock levels and inventory movement through clear visuals and real-time dashboards.

---

## ✨ Key Features

- **Dynamic Visual Dashboard:** Instant view of current stock levels and recent inventory movements using interactive charts—no page reloads required.
- **Frictionless Product Management:** Add new products or adjust stock quantities with just a few clicks.
- **Concurrency & Transaction Safety:** Robust API layer that safely manages simultaneous updates (e.g., two employees updating stock at the exact same time) without risking negative stock balances.
- **Strict Data Validation:** Powered by Pydantic to automatically catch typos (like entering a letter in a price field) and prevent data corruption.

---

## 🛠️ Tech Stack & Why It Was Selected

KoreInventory is engineered using a modern, resilient tech stack:

| Technology | Role | Why It Was Chosen |
| :--- | :--- | :--- |
| **ReactJS** | Frontend | Local business owners need a snappy, responsive interface. React’s virtual DOM enables instant searching through hundreds of items and filtering of charts without reloading the page. |
| **FastAPI** | Backend | Incredibly fast performance, with native Pydantic integration for strict incoming data validation to prevent corrupt data entry. |
| **PostgreSQL** | Database | Inventory data is financial data. PostgreSQL’s ACID compliance ensures records are safe, atomic, and secure compared to local spreadsheets. |

---

## 🏗️ Architecture & Concurrency Control

- **Frontend:** Single Page Application (SPA) communicating with the backend via RESTful APIs.
- **Backend API:** FastAPI handles routing, business logic, and transactional integrity.
- **Database Layer:** PostgreSQL enforces relational constraints, foreign keys, and atomic transactions to prevent race conditions during simultaneous inventory adjustments.

---

## ⚙️ Getting Started (Local Development)

### Prerequisites
- Python 3.9+
- Node.js & npm
- PostgreSQL installed and running locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Raviraj-Kutwal/Inventory-System-Fastapi-React-.git](https://github.com/Raviraj-Kutwal/Inventory-System-Fastapi-React-.git)
cd Inventory-System-Fastapi-React-
