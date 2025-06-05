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
flowchart TD
    A([👤 User]) -->|Login Attempt| B([🌐 UI Login Page])
    B -->|🧪 Selenium Test| C([🧠 Selenium Validator])
    A -->|🔁 Login API Request| D([📨 Postman API Collection])
    D -->|💻 Newman CLI| E([🧠 API Validator])
    C --> F([✅ Unified Test Result 📊])
    E --> F
    F --> G([📌 JIRA Issue Logging 🐞])

    %% Style
    style A fill:#F9F871,stroke:#333,stroke-width:1px
    style B fill:#B1D4E0,stroke:#333,stroke-width:1px
    style D fill:#FEC8D8,stroke:#333,stroke-width:1px
    style C fill:#C3FDB8,stroke:#333,stroke-width:1px
    style E fill:#C3FDB8,stroke:#333,stroke-width:1px
    style F fill:#FFF1B6,stroke:#333,stroke-width:1px
    style G fill:#FFD6A5,stroke:#333,stroke-width:1px

