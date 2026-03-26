# django-rest-api-1

# 🚀 Django REST API shablon

Ushbu loyiha Django REST API asosida yaratilgan.

## 📥 Loyihani yuklab olish

```bash
git clone <project-url>
cd <project-folder>

## 🐍 Virtual muhit (venv) yaratish

python -m venv venv
# yoki
py -m venv venv
# yoki
python3 -m venv venv

## ⚙️ Virtual muhitni faollashtirish

### Windows:

venv\Scripts\activate

### Linux / macOS:

source venv/bin/activate

## 📦 Kerakli paketlarni o‘rnatish

pip install -r requirements.txt

## 📁 Loyihaning asosiy papkasiga kirish

cd src/

## 🔐 .env fayl yaratish

cp .env.example .env

> .env fayl ichiga kerakli sozlamalarni kiriting

## 🗄 Ma’lumotlar bazasini yaratish

python manage.py migrate

## 👤 Superuser yaratish

python manage.py createsuperuser

## ▶️ Serverni ishga tushirish

python manage.py runserver
