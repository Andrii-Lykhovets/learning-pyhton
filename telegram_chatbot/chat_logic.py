import logging
import json
import aiohttp
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Конфигурация (замените на ваши токены)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
YANDEX_API_KEY = "YOUR_YANDEX_API_KEY"  # API ключ от Яндекс Cloud
YANDEX_FOLDER_ID = "YOUR_FOLDER_ID"  # ID папки в Яндекс Cloud

# База данных продуктов (замените на вашу реальную БД)
PRODUCTS_DB = {
    "skin_care": [
        {
            "name": "Сыворотка с ниацинамидом и цинком",
            "description": "Нормализует работу сальных желез, уменьшает жирность кожи",
            "price": "1500 руб",
            "links": {
                "site": "https://yoursite.com/niacinamide",
                "ozon": "https://ozon.ru/product/niacinamide",
                "wb": "https://wildberries.ru/catalog/niacinamide"
            },
            "keywords": ["жирная кожа", "поры", "себум", "прыщи", "акне"]
        },
        {
            "name": "Гиалуроновая кислота",
            "description": "Увлажняет кожу, борется со стрессом и усталостью",
            "price": "1200 руб",
            "links": {
                "site": "https://yoursite.com/hyaluronic",
                "ozon": "https://ozon.ru/product/hyaluronic",
                "wb": "https://wildberries.ru/catalog/hyaluronic"
            },
            "keywords": ["сухость", "увлажнение", "морщины", "стресс"]
        }
    ],
    "energy": [
        {
            "name": "Витамин C",
            "description": "Поддерживает иммунитет и энергию, улучшает состояние кожи",
            "price": "800 руб",
            "links": {
                "site": "https://yoursite.com/vitamin-c",
                "ozon": "https://ozon.ru/product/vitamin-c",
                "wb": "https://wildberries.ru/catalog/vitamin-c"
            },
            "keywords": ["усталость", "иммунитет", "энергия", "простуда"]
        },
        {
            "name": "5-НТР (5-гидрокситриптофан)",
            "description": "Улучшает самочувствие и повышает уровень энергии",
            "price": "2000 руб",
            "links": {
                "site": "https://yoursite.com/5htp",
                "ozon": "https://ozon.ru/product/5htp",
                "wb": "https://wildberries.ru/catalog/5htp"
            },
            "keywords": ["депрессия", "настроение", "сон", "энергия", "усталость"]
        }
    ],
    "digestion": [
        {
            "name": "Пробиотик + Пребиотик",
            "description": "Нормализует метаболизм и улучшает пищеварение",
            "price": "1700 руб",
            "links": {
                "site": "https://yoursite.com/probiotics",
                "ozon": "https://ozon.ru/product/probiotics",
                "wb": "https://wildberries.ru/catalog/probiotics"
            },
            "keywords": ["пищеварение", "живот", "метаболизм", "вздутие", "кишечник"]
        }
    ]
}


class YandexGPT:
    def __init__(self, api_key: str, folder_id: str):
        self.api_key = api_key
        self.folder_id = folder_id
        self.base_url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    async def generate_response(self, user_message: str, products_context: str) -> str:
        """Генерирует ответ используя Yandex GPT"""

        system_prompt = f"""Ты - консультант по БАДам и здоровью. Твоя задача:
1. Проанализировать проблемы клиента
2. Дать краткий совет по здоровью
3. Рекомендовать подходящие продукты из доступного каталога

Доступные продукты:
{products_context}

Отвечай дружелюбно, профессионально. Структурируй ответ:
- Понимание проблемы
- Краткий совет
- Конкретные рекомендации продуктов
- Предложение дополнительной помощи

Используй эмодзи для лучшего восприятия."""

        payload = {
            "modelUri": f"gpt://{self.folder_id}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.3,
                "maxTokens": 2000
            },
            "messages": [
                {
                    "role": "system",
                    "text": system_prompt
                },
                {
                    "role": "user",
                    "text": user_message
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.api_key}"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                        self.base_url,
                        headers=headers,
                        json=payload,
                        timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result['result']['alternatives'][0]['message']['text']
                    else:
                        logger.error(f"Yandex API error: {response.status}")
                        return "Извините, произошла ошибка при обработке запроса. Попробуйте позже."
        except Exception as e:
            logger.error(f"Error calling Yandex API: {e}")
            return "Извините, сервис временно недоступен. Попробуйте позже."


def find_relevant_products(user_message: str) -> list:
    """Находит релевантные продукты на основе ключевых слов"""
    user_message_lower = user_message.lower()
    relevant_products = []

    for category, products in PRODUCTS_DB.items():
        for product in products:
            for keyword in product["keywords"]:
                if keyword.lower() in user_message_lower:
                    if product not in relevant_products:
                        relevant_products.append(product)
                    break

    return relevant_products


def format_products_context(products: list) -> str:
    """Форматирует продукты для контекста ИИ"""
    if not products:
        return "Продукты не найдены для данного запроса."

    context = ""
    for i, product in enumerate(products, 1):
        context += f"{i}. {product['name']} - {product['description']} ({product['price']})\n"

    return context


def format_product_recommendation(product: dict) -> str:
    """Форматирует рекомендацию продукта для пользователя"""
    links_text = " | ".join([
        f"[{name.upper()}]({url})"
        for name, url in product["links"].items()
    ])

    return f"**{product['name']}**\n{product['description']}\n💰 {product['price']}\n🔗 {links_text}\n"


# Инициализация ИИ
yandex_gpt = YandexGPT(YANDEX_API_KEY, YANDEX_FOLDER_ID)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    welcome_message = """
🌿 **Добро пожаловать в консультант по БАДам!**

Я помогу вам подобрать подходящие добавки и средства для здоровья.

📝 **Как это работает:**
1. Опишите ваши проблемы со здоровьем
2. Я проанализирую ваш запрос
3. Предложу подходящие продукты из нашего каталога

💬 **Просто напишите мне, что вас беспокоит!**

Например: "У меня проблемы с кожей и постоянная усталость"
    """

    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown'
    )


# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Обработчик текстовых сообщений"""
#     user_message = update.message.text
#     user_id = update.effective_user.id
#
#     # Отправляем сообщение о том, что запрос обрабатывается
#     processing_msg = await update.message.reply_text("🔄 Анализирую ваш запрос...")
#
#     try:
#         # Находим релевантные продукты
#         relevant_products = find_relevant_products(user_message)
#
#         # Формируем контекст для ИИ
#         products_context = format_products_context(relevant_products)
#
#         # Получаем ответ от ИИ
#         ai_response = await yandex_gpt.generate_response(user_message, products_context)
#
#         # Удаляем сообщение о обработке
#         await processing_msg.delete()
#
#         # Отправляем ответ ИИ
#         await update.message.reply_text(
#             ai_response,
#             parse_mode='Markdown'
#         )
#
#         # Если найдены продукты, отправляем их отдельным сообщением
#         if relevant_products:
#             products_message = "🛍️ **Рекомендованные продукты:**\n\n"
#             for product in relevant_products[:5]:  # Максимум 5 продуктов
#                 products_message += format_product_recommendation(product) + "\n"
#
#             await update.message.reply_text(
#                 products_message,
#                 parse_mode='Markdown',
#                 disable_web_page_preview=True
#             )
#
#         # Предлагаем дополнительную помощь
#         keyboard = [
#             [InlineKeyboardButton("❓ Задать другой вопрос", callback_data="new_question")],
#             [InlineKeyboardButton("📞 Связаться с консультантом", callback_data="contact")]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#
#         await update.message.reply_text(
#             "Чем еще могу помочь?",
#             reply_markup=reply_markup
#         )
#
#     except Exception as e:
#         logger.error(f"Error handling message: {e}")
#         await processing_msg.edit_text(
#             "😔 Извините, произошла ошибка. Попробуйте еще раз или обратитесь к нашему консультанту."
#         )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Простой обработчик для теста"""
    user_message = update.message.text

    simple_response = f"🤖 Бот работает! Вы написали: '{user_message}'"

    await update.message.reply_text(simple_response)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()

    if query.data == "new_question":
        await query.edit_message_text("💬 Задайте новый вопрос о вашем здоровье!")
    elif query.data == "contact":
        contact_info = """
📞 **Связаться с консультантом:**

🌐 Сайт: https://yourcompany.com
📧 Email: info@yourcompany.com  
📱 Телефон: +7 (XXX) XXX-XX-XX
💬 Telegram: @your_support_bot

⏰ Работаем: Пн-Пт 9:00-18:00 (МСК)
        """
        await query.edit_message_text(
            contact_info,
            parse_mode='Markdown'
        )


def main() -> None:
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Запускаем бота
    print("🤖 Бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
