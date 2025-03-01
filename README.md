# 🛒 Django + Stripe API (Docker)

Этот проект – это API для интернет-магазина на Django с интеграцией **Stripe Payment Intent**.  
Позволяет получать товары и оплачивать их через **Stripe Checkout**.  

---

## 🚀 Функционал
- ✅ API для получения информации о товаре **`/item/{id}/`**.
- ✅ API для генерации **Stripe Checkout Session** **`/buy/{id}/`**.
- ✅ Оплата товаров через **Stripe Payment Intent**.
- ✅ Запуск через **Docker + PostgreSQL**.

---

## 🔧 Установка и запуск (Docker)

### 1. Клонируйте репозиторий**
```bash
git clone https://github.com/ваш-аккаунт/payment-system.git
cd payment-system
```

### 2. Создайте .env с ключами Stripe
```bash
touch .env
```

Добавьте в файл .env:
```bash
STRIPE_PUBLIC_KEY_USD=pk_test_XXXXXXXXXXXXXXXXXXXXXXXX
STRIPE_SECRET_KEY_USD=sk_test_XXXXXXXXXXXXXXXXXXXXXXXX
STRIPE_PUBLIC_KEY_EUR=pk_test_YYYYYYYYYYYYYYYYYYYYYYYY
STRIPE_SECRET_KEY_EUR=sk_test_YYYYYYYYYYYYYYYYYYYYYYYY
```

⚠️ Важно! Убедитесь, что .env добавлен в .gitignore, чтобы не загружать его в публичный репозиторий.

### 3. Запустите проект в Docker
```bash
docker-compose up --build
```

### 4. Примените миграцию
```bash
docker-compose exec web python manage.py migrate
```

### 5. Создайте суперпользователя (для Django Admin)
```bash
docker-compose exec web python manage.py createsuperuser
```

### 6. Откройте в браузере

Товар: http://127.0.0.1:8000/item/1/
Админ-панель: http://127.0.0.1:8000/admin/


## 🛠 API эндпоинты

### 📌 1. Получить товар
```bash
GET /item/{id}/
```

📌 Пример ответа:
```bash
{
  "id": 1,
  "name": "Gaming Laptop",
  "description": "Мощный игровой ноутбук",
  "price": 120000
}
```

### 📌 2. Создать Stripe Session
```bash
GET /buy/{id}/
```

📌 Пример ответа:

{
  "session_id": "cs_test_1234567890abcdef"
}
✅ Перенаправляет пользователя на оплату в Stripe.


## 🔥 Технологии

### Django 3.2+
### Django REST Framework
### Stripe API
### PostgreSQL
### Docker & Docker Compose



