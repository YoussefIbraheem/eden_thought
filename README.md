# 🌱 EdenThought

EdenThought is a simple Django project built as part of a Django course by [Arno Pretorius](https://github.com/arnopretorius).  
It’s a lightweight web app where users can register, log in, and share their thoughts in a clean reading interface.

---

## 🚀 Features

- User registration and authentication (login/logout).
- Thought posting and reading page styled with Bootstrap.
- Crispy Forms integration for clean, responsive forms.
- Template inheritance with `base.html` for easy layout management.

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)

---

## 📂 Project Structure

```

EdenThought/
│
├── templates/        # HTML templates (base, home, login, register, etc.)
├── static/           # Static files (CSS, JS, images)
├── app/              # Main Django app (models, views, urls)
├── manage.py         # Django project manager
└── README.md         # Project documentation

```

---

## ⚡ Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/edenthougth.git
cd edenthought
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the server

```bash
python manage.py runserver
```

Visit 👉 `http://127.0.0.1:8000/`

---

## 🙏 Acknowledgments

This project was built while following **Arno Pretorius' Django course**.
Special thanks to him for making Django approachable and fun to learn.

---

## 📜 License

This project is for **learning purposes only**. You are free to fork, modify, and extend it.
