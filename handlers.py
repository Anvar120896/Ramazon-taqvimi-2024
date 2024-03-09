import datetime

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboard as kb
from app.request import f1

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Salom {message.from_user.full_name} \nRamazon taqvimi botiga xush kelibsiz",
                         reply_markup=kb.menu)


bugun = datetime.date.today().strftime("%m/%d/%Y").split('/')
x = '/'.join([str(i) for i in [int(bugun[0]), int(bugun[1]), int(bugun[2])]])

@router.message(F.text == "Bugungi ramazon taqvim")
async def bugungi(message: Message):
    if x in f1()[0]:
        await message.answer(f"Saharlik: {f1()[0][x]} \nIftorlik: {f1()[1][x]}")
    else:
        await message.answer(f"xatolik")


@router.message(F.text == "oylik ramazon taqvim")
async def oylik(message: Message):
    if x in f1()[0]:
        await message.answer_photo("https://images.app.goo.gl/NJpYq8wbC4Nkfcxx8")
    else:
        await message.answer("xatolik")

