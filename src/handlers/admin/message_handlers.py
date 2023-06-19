from aiogram import types

from initializer import dp

from keyboards.admin.inline_keyboard import admin_keyboard_work_mode 

@dp.message_handler(commands=['admin', 'adm'])
async def cmd_admin(message: types.Message): 
    await message.delete()
    await message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)