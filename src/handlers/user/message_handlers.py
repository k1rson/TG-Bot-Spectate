from aiogram import types

from initializer import dp
from database.models import session

from database.models import User
from keyboards.user.inline_keyboard import user_keyboard_verification_state

from states.general_states import VerificationAccountState

@dp.message_handler(commands=['start', 'str'])
async def cmd_start(message: types.Message): 
    await message.delete()
    user = session.query(User).filter_by(user_id=message.from_user.id).first()

    if not user:
        await message.answer(f'Hello, {message.from_user.username} 👋\nIm a bot that allows you to track the activity of accounts that you add.\n'\
             f'To get started, you must pass a *quick* verification 🔓\n', parse_mode='Markdown', reply_markup=user_keyboard_verification_state)
        return 

    if not user.is_verification: 
        await message.answer(f'Hello, {message.from_user.username} 👋\nIm a bot that allows you to track the activity of accounts that you add.\n'\
            f'To get started, you must pass a *quick* verification 🔓\n', parse_mode='Markdown', reply_markup=user_keyboard_verification_state)        
        return

    await message.answer(f'Hello, {message.from_user.username} 👋\nInter your password please:', parse_mode='Markdown')        
    await VerificationAccountState.WaitPassword.set()