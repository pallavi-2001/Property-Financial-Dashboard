# 🏘️ Property Financial Dashboard

A lightweight, secure Django-based dashboard for small property managers to analyze `.csv` financial records (rent, EMI, tax, expenses) — without Excel or logins.

**Property Financial Dashboard** is a web-based application built using Django that allows users to upload CSV files containing property-related financial data such as income and expenses. The system calculates net income and expenses and visualizes them in clean, interactive charts.

---

## 🚀 Features

- 📤 **Public CSV Upload** — No login required
- 🔐 **Admin-only View** — Uploaded data is only visible to Django admin 
- 📊 **Auto Calculations (JS)** — Net Expense & Net Income per property
- 📈 **Clean Charts** — Bar chart (Property vs Net Income & Net Expense) using Chart.js
- 💡 **Simple UI** — Built with TailwindCSS

---

## ⚙️ Tech Stack

| Technology     | Usage                                                                 |
|----------------|-----------------------------------------------------------------------|
| **Django (v3.2)** | Main backend framework for routing, models, and logic               |
| **SQLite**      | Default lightweight database for storing uploaded file metadata      |
| **Pandas**      | Processes and analyzes uploaded CSV files                             |
| **Python**      | Core backend language                                                 |
| **HTML5**       | Template structure rendered through Django                            |
| **TailwindCSS** | Responsive, utility-first CSS framework for clean UI                 |
| **JavaScript**  | Handles client-side table rendering, calculations, and interactivity |
| **Chart.js**    | Visualizes net income/expense as bar charts                           |
| **Django Admin**| Restricts view access to uploaded data for adminonly          |

---

## 🔄 Data Flow

1. Public user uploads a `.csv` file using the upload form
2. Django processes the file using **Pandas**
3. Data is passed to the frontend
4. JavaScript:
   - Displays tabular data
   - Calculates `Net Income` and `Net Expense`
   - Renders a bar chart using Chart.js

---

## 🛡️ Security

- 📝 **Upload**: Open to public users (no login)
- 🔐 **Data View**: Restricted to Django admin users

---

## 👥 Roles & Access

| Role   | Permissions                        |
|--------|------------------------------------|
| Public | Upload `.csv` files (no login)     |
| Admin  | View uploaded data and results via Django Admin |

---

## 📥 Expected CSV Format

```csv
property_name,property_price,property_rent,emi,tax,other_exp
Orchid,500000,5000,500,150,32
Sunset Villa,1200000,9000,800,200,32


