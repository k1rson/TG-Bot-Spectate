import random, asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from initializer import dp, bot
from database.models import User, session

from keyboards.user.inline_keyboard import user_keyboard_work_mode

from states.general_states import SpectateGitHubState, SpectateTwitchState, SpectateVKState, SpectateDiscordState, SpectateTelegramState, VerificationAccountState

from handlers.user.logic.github_state_logic import *
from handlers.user.logic.twitch_state_logic import *
from handlers.user.logic.vk_state_logic import *
from handlers.user.logic.discord_state_logic import *
from handlers.user.logic.telegram_state_logic import *

messages = []
# VERIFICATION 
@dp.callback_query_handler(state=VerificationAccountState.StartVerification)
async def start_verification_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'continue_verification': 
        await callback_query.message.delete()

        rnd_value = random.sample(range(10), 4)
        password = int(''.join(map(str, rnd_value)))

        user = User(
            username = callback_query.from_user.username, 
            user_id = callback_query.from_user.id, 
            is_verification = True, 
            password = password
        )

        session.add(user)
        session.commit()

        msg = await bot.send_message(callback_query.message.chat.id, f'Great! You have passed verification, you need a password to work: *{password}*.\n'\
            'The message will be deleted after 10 seconds. GoogLuck 😃', parse_mode='Markdown')
        
        await asyncio.sleep(3)
        await msg.delete()

        msg = await callback_query.message.answer('Enter your *password*: ', parse_mode='Markdown')
        await VerificationAccountState.WaitPassword.set()

    elif callback_query.data == 'cancel_verification': 
        await callback_query.message.delete()
        await callback_query.message.answer('So bad. GoodBye and GoodLuck 😟 /start')
        await state.finish()

@dp.message_handler(state=VerificationAccountState.WaitPassword)
async def wait_password_handler(message: types.Message, state: FSMContext): 
    messages.append(message)

    try: 
        password = int(message.text)
    except: 
        msg = await message.answer('Please enter the correct password! 4 digits')
        messages.append(msg)
        return

    user = session.query(User).filter_by(user_id=message.from_user.id).first()

    if user.password != password: 
        msg = await message.answer('Invalid password. Try again')
        messages.append(msg)
        return 
    
    msg = await message.answer('Great! Googluck!')
    messages.append(msg)
    await asyncio.sleep(1)

    for msg in messages: 
        await msg.delete()

    await state.finish()
    await message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)
    
    messages.clear()

# SPECTATE GITHUB
@dp.callback_query_handler(state=SpectateGitHubState.StartSpectate)
async def github_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)

        await state.finish()

# SPECTATE TWITCH
@dp.callback_query_handler(state=SpectateTwitchState.StartSpectate)
async def twitch_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)

        await state.finish()

# SPECTATE VK
@dp.callback_query_handler(state=SpectateVKState.StartSpectate)
async def vk_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)

        await state.finish()

# SPECTATE DISCORD
@dp.callback_query_handler(state=SpectateDiscordState.StartSpectate)
async def discord_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)

        await state.finish()

# SPECTATE TELEGRAM
@dp.callback_query_handler(state=SpectateTelegramState.StartSpectate)
async def telegram_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=user_keyboard_work_mode)

        await state.finish()