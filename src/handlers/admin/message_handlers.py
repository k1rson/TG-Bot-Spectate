from aiogram import types

from initializer import dp

@dp.message_handler(commands=['admin', 'adm'])
async def cmd_start(message: types.Message): 
    await message.answer('ff')