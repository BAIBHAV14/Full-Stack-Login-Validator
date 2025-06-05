# 🔐 Full Stack Login Validator

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Tech](https://img.shields.io/badge/tech-stack-yellow)

A **QA Testing Automation Project** that validates login functionalities across both **Frontend (UI)** and **Backend (API)** using **Selenium** and **Postman/Newman**.

---

## 📌 Tech Stack

| Tool        | Purpose                  |
|-------------|--------------------------|
| 🐍 Python   | Backend scripting        |
| 🌐 Selenium | UI automation            |
| 🔁 Postman  | API testing              |
| 🧪 Newman   | CLI execution of APIs    |
| 🪲 JIRA     | Bug tracking             |
| 🧬 Git      | Version control          |

---

## 🧭 Project Architecture

```mermaid
graph TD;
    A[User] --> B[Login Page UI]
    B -->|Selenium UI Test| C[Test Case Executor]
    A --> D[Postman API Test]
    D -->|Newman CLI| C
    C --> E[Validation Layer]
    E --> F[Pass/Fail Report]
