# 🛒 Django + Stripe API (Docker)

Этот проект – API для онлайн-магазина на Django с интеграцией **Stripe Payment Intent**.  
Позволяет создавать товары и оплачивать их через Stripe.  

## 🚀 Функционал
- API для получения информации о товаре (`/item/{id}/`).
- API для генерации Stripe Checkout Session (`/buy/{id}/`).
- Оплата товаров через **Stripe Payment Intent**.
- Запуск через **Docker + PostgreSQL**.

---

## 🔧 Установка и запуск (Docker)

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш-аккаунт/payment-system.git
   cd payment-system

Создайте .env с ключами Stripe:
touch .env
Заполните его:

STRIPE_PUBLIC_KEY_USD=pk_test_XXXXXXXXXXXXXXXXXXXXXXXX
STRIPE_SECRET_KEY_USD=sk_test_XXXXXXXXXXXXXXXXXXXXXXXX
STRIPE_PUBLIC_KEY_EUR=pk_test_YYYYYYYYYYYYYYYYYYYYYYYY
STRIPE_SECRET_KEY_EUR=sk_test_YYYYYYYYYYYYYYYYYYYYYYYY

## Запустите проект в Docker:
docker-compose up --build

## Примените миграции:
docker-compose exec web python manage.py migrate

## Создайте суперпользователя (если нужно):
docker-compose exec web python manage.py createsuperuser

## Откройте в браузере:
Товар: http://127.0.0.1:8000/item/1/
Админ-панель: http://127.0.0.1:8000/admin/

## 🛠 API эндпоинты

📌 1. Получить товар

GET /item/{id}/

📌 Пример ответа:

{
  "id": 1,
  "name": "Test Item",
  "description": "Описание товара",
  "price": 1000
}

📌 2. Создать Stripe Session

GET /buy/{id}/

📌 Пример ответа:

{
  "session_id": "cs_test_1234567890abcdef"
}

✅ Перенаправляет пользователя на оплату в Stripe.

## 🏗 Технологии

Django 3.2+
Django REST Framework
Stripe API
PostgreSQL
Docker & Docker Compose

