# Newportal-Website

## 🛠️ Tech Stack

![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript)
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-DB-lightgrey?logo=sqlite)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)





## 📰 Kantipur News Portal Website

A full-stack responsive news portal developed using **Django (Python)** for the backend and **HTML, CSS, Bootstrap, JavaScript** for the frontend. This project was developed as part of the final semester industrial training at Shark IT Services Pvt. Ltd.

## 🚀 Features

- 📝 News and Blog Posting
- 👥 User Registration & Login
- 🔎 Search Functionality
- 🗂️ Category-wise Filtering
- 💬 Comment System
- 📱 Mobile Responsive Design
- 🔐 Admin Panel for Content Management

## 🚀 Live Features Overview

### 🔐 1. User Signup/Registration
- New users can register with a username, email, and password
- Django's authentication system ensures secure login/logout
![Register](Screenshots/register.png)






### 🔐 1. User Login
- Logged-in users can comment on articles and blogs

![Register](Screenshots/login.png)












## 📷 Screenshots

### Homepage
![Homepage](Screenshots/homepage.png)

### Admin Panel
![Admin Panel](Screenshots/admin1.png)


![Admin Panel](Screenshots/admin.png)

## 🔧 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python, Django
- **Database**: SQLite
- **Tools**: VS Code, Git, GitHub


# Feature

### 📰 News Categories
- News filtered by categories: Politics, Sports, Technology, Entertainment, etc.
- Users can click on categories to view relevant news
- Admin can add/edit categories

### 📝 Blog Section
- Long-form content created by admin or contributors
- Supports title, image, author, publish date, and content
- Paginated layout for better readability

### 💬 Comment System
- Logged-in users can comment on blogs or news articles
- Comments are linked to the user and article
- Admin can moderate comments

### 📚 Admin Panel
- Powered by Django’s default admin interface
- Admin can manage:
  - News articles
  - Blog posts
  - Categories
  - Comments
  - Registered users
- Admin authentication required

### 🔍 Search Functionality
- Keyword-based search
- Searches titles and content of news & blogs
- Displays matched results in real-time

### 📱 Responsive Design
- Fully mobile-friendly and cross-browser compatible
- Navigation adjusts using Bootstrap grid and media queries
- Optimized for phone, tablet, and desktop

### 📤 Contact / Feedback Form
- Users can submit feedback or messages
- Includes fields: Name, Email, Subject, Message
- Data saved to database or emailed (if configured)


## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/kantipur-newsportal.git
cd kantipur-newsportal
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
