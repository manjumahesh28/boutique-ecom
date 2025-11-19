# Boutique E-Commerce

A modern, user-friendly **boutique e-commerce platform** built with **Django**. This project allows users to browse products, add them to a cart, and make purchases while providing an admin interface to manage products, orders, and users.

---

## Features

* Browse and search boutique products with categories and filters.
* User authentication (register, login, logout).
* Shopping cart and checkout functionality.
* Admin dashboard for managing products, orders, and users.
* Responsive design suitable for desktop and mobile.
* Secure handling of user data and orders.

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** HTML, CSS, JavaScript ( React integration)
* **Database:** SQLite (default) / PostgreSQL 
* **Other Tools:** Git, GitHub for version control

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (for admin access)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Open in browser**
   Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

* Browse products on the home page.
* Add products to your cart and proceed to checkout.
* Admin users can manage products, orders, and users via the `/admin` dashboard.

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is open source and available under the **MIT License**.
