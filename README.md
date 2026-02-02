🛍️ Shopaholic – Full-Stack E-Commerce Website

Shopaholic is a full-stack e-commerce web application built using Django and Bootstrap, designed to replicate real-world shopping platforms.
It provides a smooth shopping experience for users and a custom frontend admin dashboard for managing products, orders, and users.

🔥 Features
👤 User Features

User registration, login & logout

Product browsing & category-based search

Product detail pages (similar to real shopping websites)

Add to cart & remove from cart

Checkout flow

Order history (My Orders)

Secure authentication & session handling

Responsive and modern UI with gradients & hover effects

🛠 Admin Features (Custom Frontend)

Separate Admin Login Page

Custom Admin Dashboard (not Django default admin)

View:

Total users

Total products

Total orders

Total revenue

Update product stock directly from dashboard

Manage products from frontend

Role-based access (admin vs user)

Django Admin panel is also enabled for advanced control.

🧰 Tech Stack
Layer	Technology
Backend	Django (Python)
Frontend	HTML, CSS, Bootstrap 5
Database	SQLite
Authentication	Django Auth
Styling	Custom CSS, Gradients, Animations
📂 Project Structure
shopaholic/
│

├── shop/           # Products, cart, checkout, orders

├── userapp/        # User authentication (login, register)

├── adminapp/       # Custom admin dashboard

├── templates/      # HTML templates

├── static/         # CSS & assets

├── media/          # Product images

├── db.sqlite3

├── manage.py

└── README.md


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/khushietiwari/Shopaholic-An-e-commerce-website-for-clothes-and-more
cd shopaholic

2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install django

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Admin)
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver


Open browser →
👉 http://127.0.0.1:8000/

🔐 Login URLs
Purpose	URL
User Login	/user/login/
Admin Login	/dashboard/login/
Admin Dashboard	/dashboard/
Django Admin	/admin/
📸 Screenshots

<img width="1366" height="657" alt="Screenshot (197)" src="https://github.com/user-attachments/assets/11a33268-923a-4558-b791-272caeccc8ca" />
Home Page


<img width="1366" height="669" alt="Screenshot (200)" src="https://github.com/user-attachments/assets/93dc4c21-80f6-4689-8d80-19e1f4135c75" />
Collection Page

<img width="1366" height="633" alt="Screenshot (201)" src="https://github.com/user-attachments/assets/ec4e6164-4928-4c07-81ef-2261bdb2b176" />
Product Detail

<img width="1366" height="669" alt="Screenshot (202)" src="https://github.com/user-attachments/assets/263ae01e-8f32-4feb-8b88-1c36dcdc745f" />
Cart & Checkout

<img width="1366" height="687" alt="Screenshot (195)" src="https://github.com/user-attachments/assets/58c824e6-cbcf-4887-820a-c7b06dcb83cf" />
Admin Dashboard


🎯 Learning Outcomes

This project helped in understanding:

Full-stack Django development

Authentication & authorization

Role-based access control

Cart & order management logic

Custom admin dashboards

UI/UX design for real-world apps

🚀 Future Enhancements

Payment gateway integration

Order status tracking

Email notifications

Admin analytics (charts)

Deployment (AWS / Render / Railway)

🧑‍💻 Author

Khushi Tiwari
Full-Stack Developer (Django)

⭐ If you like this project

Give it a ⭐ on GitHub!
