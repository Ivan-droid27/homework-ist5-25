import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'тут должен быть токен'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_tasks = {}
user_quiz = {}

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить задачу')],
        [KeyboardButton(text='Мои задачи')],
        [KeyboardButton(text='Очистить задачи')],
        [KeyboardButton(text='Викторина 🎯')],
        [KeyboardButton(text='Кинуть кубик 🎲'), KeyboardButton(text='Подкинуть монетку 🪙')]
    ],
    resize_keyboard=True
)

# вопросы
quiz_questions = [
    {
        "question": "Какой тип данных в Python является изменяемым?",
        "options": ["tuple", "list", "str"],
        "answer": "list"
    },
    {
        "question": "Что выведет код?\nprint(type(10 / 2))",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>"],
        "answer": "<class 'float'>"
    },
    {
        "question": "Какой оператор проверяет принадлежность?",
        "options": ["in", "is", "has"],
        "answer": "in"
    },
    {
        "question": "HTTP-метод для обновления данных?",
        "options": ["GET", "POST", "PUT"],
        "answer": "PUT"
    },
    {
        "question": "Что выведет код?\nx=[1,2,3]\ny=x\ny.append(4)\nprint(x)",
        "options": ["[1,2,3]", "[1,2,3,4]", "Ошибка"],
        "answer": "[1,2,3,4]"
    },
    {
        "question": "Результат bool([])?",
        "options": ["True", "False", "Ошибка"],
        "answer": "False"
    },
    {
        "question": "Порт HTTPS по умолчанию?",
        "options": ["80", "443", "21"],
        "answer": "443"
    },
    {
        "question": "Что делает await?",
        "options": [
            "Запускает функцию",
            "Ждёт завершения async операции",
            "Останавливает программу"
        ],
        "answer": "Ждёт завершения async операции"
    },
    {
        "question": "Принцип ООП с одним интерфейсом?",
        "options": ["Инкапсуляция", "Наследование", "Полиморфизм"],
        "answer": "Полиморфизм"
    },
    {
        "question": "SQL — это?",
        "options": [
            "Язык разметки",
            "Язык запросов к БД",
            "ОС"
        ],
        "answer": "Язык запросов к БД"
    }
]

#старт
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет 👋\n\n"
        "Я бот с задачами и викториной 🎯\n"
        "Нажми кнопку «Викторина 🎯» или используй /start_quiz",
        reply_markup=keyboard
    )

@dp.message(lambda msg: msg.text == 'Добавить задачу')
async def add_task(message: types.Message):
    await message.answer("Напиши задачу 👇")

@dp.message(lambda msg: msg.text == 'Мои задачи')
async def show_tasks(message: types.Message):
    tasks = user_tasks.get(message.from_user.id, [])
    if not tasks:
        await message.answer("Задач нет")
        return

    text = "Ваши задачи:\n\n"
    for i, t in enumerate(tasks, 1):
        text += f"{i}. {t}\n"
    await message.answer(text)

@dp.message(lambda msg: msg.text == 'Очистить задачи')
async def clear_tasks(message: types.Message):
    user_tasks[message.from_user.id] = []
    await message.answer("Все задачи удалены")

@dp.message(lambda msg: msg.text == 'Кинуть кубик 🎲')
async def dice(message: types.Message):
    msg = await message.answer_dice()
    await asyncio.sleep(3)
    await message.answer(f"Выпало: {msg.dice.value}")

@dp.message(lambda msg: msg.text == 'Подкинуть монетку 🪙')
async def coin(message: types.Message):
    await message.answer(random.choice(["Орёл 🦅", "Решка 👑"]))

@dp.message()
async def save_task(message: types.Message):
    if message.text.startswith('/') or message.text in [
        'Добавить задачу', 'Мои задачи', 'Очистить задачи',
        'Кинуть кубик 🎲', 'Подкинуть монетку 🪙', 'Викторина 🎯'
    ]:
        return

    user_tasks.setdefault(message.from_user.id, []).append(message.text)
    await message.answer("Задача добавлена ✅")

# викторина

@dp.message(Command("start_quiz"))
@dp.message(lambda msg: msg.text == 'Викторина 🎯')
async def start_quiz(message: types.Message):
    user_quiz[message.from_user.id] = {"current": 0, "correct": 0}
    await send_question(message)

async def send_question(message: types.Message):
    quiz = user_quiz[message.from_user.id]
    i = quiz["current"]

    if i >= 10:
        correct = quiz["correct"]
        wrong = 10 - correct

        if correct >= 9:
            place = "🥇 Первое место"
        elif correct >= 7:
            place = "🥈 Второе место"
        elif correct == 6:
            place = "🥉 Третье место"
        else:
            place = "❌ Без призового места"

        await message.answer(
            f"🎉 Викторина завершена!\n\n"
            f"✅ Правильных: {correct}\n"
            f"❌ Неправильных: {wrong}\n\n"
            f"Результат: {place}",
            reply_markup=keyboard
        )
        return

    q = quiz_questions[i]
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=o)] for o in q["options"]],
        resize_keyboard=True
    )
    await message.answer(q["question"], reply_markup=kb)

@dp.message(lambda msg: msg.text in sum([q["options"] for q in quiz_questions], []))
async def quiz_answer(message: types.Message):
    quiz = user_quiz.get(message.from_user.id)
    if not quiz:
        return

    i = quiz["current"]
    if message.text == quiz_questions[i]["answer"]:
        quiz["correct"] += 1

    quiz["current"] += 1
    await send_question(message)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
