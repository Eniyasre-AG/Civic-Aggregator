# 🛠️ Civic Issue Aggregator

A smart civic tech platform that allows users to report local issues (like potholes, garbage, water leakage) using geolocation and images. Admins can view all reports on a map dashboard, powered by clustering, categorization, and email alerts to authorities.

---

## ✨ Features

- 📍 **Geo-tagged Issue Reporting**
- 🖼️ **Upload Images** with Description
- 🧠 **Auto-Tagging** using simple NLP
- 📬 **Email Notification** to Civic Authorities
- 🔒 **Admin Login** for Dashboard
- 🗺️ **Map View Dashboard** with Leaflet.js
- 🧪 **Clustering by Type/Area**
- 📱 **Responsive UI** (mobile-friendly)

---

## 🚀 Demo

> Coming soon – you can test it locally with the steps below!

---

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: HTML, CSS, JS, Leaflet.js
- **NLP & Clustering**: `sklearn`, `TfidfVectorizer`, `KMeans`
- **Email**: SMTP (Gmail app password)
- **Deployment-ready**: LocalStorage + dynamic paths

---

## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/civic-issue-aggregator.git
   cd civic-issue-aggregator/app
