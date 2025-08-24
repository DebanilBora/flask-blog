📝 Flask Blog with User Authentication & Comments

A full-featured Flask-powered blogging platform that allows users to register, log in, create blog posts, and comment on posts. The app integrates authentication, rich text editing, gravatars, and email-powered contact forms.
---
## 🚀 Live Demo  
🔗 [View Blog on Render](https://flask-blog-25rs.onrender.com/)
-----
🚀 Features

🔑 User Authentication (Register, Login, Logout)

✍️ Create, Edit, Delete Blog Posts (only by author or admin)

💬 Comment System (users must log in to comment)

🖼 Gravatar Integration for user profile images

📩 Contact Form with Email Support (via Gmail SMTP)

🛡️ Password Hashing for secure login

🗄 SQLite / PostgreSQL database support

🎨 Bootstrap & CKEditor for styling and rich text editing
---------
🛠 Tech Stack

Backend: Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Login

Frontend: Bootstrap, Jinja2 Templates, CKEditor

Database: SQLite (default) / PostgreSQL (via DB_URI)

Authentication: Werkzeug Security (Password Hashing)

Email Service: smtplib (Gmail SMTP)

Deployment Ready: Render / Heroku / Any WSGI platform

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://DebanilBora/flask-blog.git
cd flask-blog

2️⃣ Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file in the project root:

FLASK_KEY=your_secret_key
DB_URI=sqlite:///instance/posts.db
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password


⚠️ For Gmail, use an App Password (not your real password).

5️⃣ Run the app
flask run

🌐 Routes Overview
Route	Method	Description
/	GET	Homepage with all posts
/register	GET/POST	Register new user
/login	GET/POST	Login user
/logout	GET	Logout user
/post/<id>	GET/POST	View single post + comments
/new-post	GET/POST	Create new blog post
/edit-post/<id>	GET/POST	Edit post (author/admin only)
/delete/<id>	GET	Delete post (author/admin only)
/contact	GET/POST	Contact form (sends email)
/about	GET	About page
/create-tables	GET	Initialize database tables
📸 Screenshots

(Add screenshots of homepage, login, editor, etc. here for your portfolio)

🏷 Tags

#Flask #WebDevelopment #FullStack #Python #BlogApp #Authentication #PortfolioProject



