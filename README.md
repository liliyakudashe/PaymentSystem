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
