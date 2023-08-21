import random, asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from initializer import dp, bot
from database.models import User, session

from keyboards.user.inline_keyboard import user_keyboard_work_mode

from states.general_states import (
    SpectateGitHubState, 
    SpectateTwitchState, 
    SpectateVKState, 
    SpectateDiscordState, 
    SpectateTelegramState, 
    VerificationAccountState, 
    InputState
)

from handlers.user.logic.github_state_logic import *
from handlers.user.logic.twitch_state_logic import *
from handlers.user.logic.vk_state_logic import *
from handlers.user.logic.discord_state_logic import *
from handlers.user.logic.telegram_state_logic import *

async def delete_message_and_answer(query: types.CallbackQuery, text, markrup, state: None): 
    await query.message.delete()
    await query.message.answer(text, parse_mode='Markdown', reply_markup=markrup)

    if state is not None: 
        await state.finish()

# INPUT 
@dp.message_handler(state=InputState.StartInputMode)
async def input_message_handler(message: types.Message, state: FSMContext): 
    pass

# VERIFICATION 
@dp.callback_query_handler(state=VerificationAccountState.StartVerification)
async def start_verification_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message
    
    if data == 'continue_verification': 
        await message.delete()

        rnd_value = random.sample(range(10), 4)
        password = int(''.join(map(str, rnd_value)))

        user = User(
            username = query.from_user.username, 
            user_id = query.from_user.id, 
            is_verification = True, 
            password = password
        )

        session.add(user)
        session.commit()

        msg = await bot.send_message(query.message.chat.id, f'Great! You have passed verification, you need a password to work: *{password}*.\n'\
            'The message will be deleted after 10 seconds. GoogLuck 😃', parse_mode='Markdown')
        
        await asyncio.sleep(3) # ten seconds 
        await msg.delete()

        msg = await query.message.answer('Enter your *password*: ', parse_mode='Markdown')
        await VerificationAccountState.WaitPassword.set()

    elif data == 'cancel_verification': 
        await delete_message_and_answer(query, 'So bad. GoodBye and GoodLuck 😟 /start')
        await state.finish()

messages = [] 
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
async def github_state_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message

    user_data = {
        'user_id': query.from_user.id, 
        'username': query.from_user.username
    }

    if data == 'add_user_to_list':
        await message.answer('Input username:')
        await state.set_state(InputState.StartInputMode)

    elif data == 'delete_user_from_list': 
        await message.answer() 
    
    elif data == 'get_detail_info': 
        pass

    elif data == 'get_checker_list': 
        checker_list = await get_checker_list(user_data)

        if not checker_list: 
            await message.answer('Sorry! Checker list is empty')
            await message.answer()
            return 

        await message.answer(checker_list)
        await message.answer()

    elif data == 'go_to_previous_step': 
        await delete_message_and_answer(query, '*Service selection panel*', user_keyboard_work_mode, state)

# SPECTATE TWITCH
@dp.callback_query_handler(state=SpectateTwitchState.StartSpectate)
async def twitch_state_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message

    if data == 'add_user_to_list': 
        await message.answer('Input username:')
        await InputState.StartInputMode.set()

    elif data == 'delete_user_from_list': 
        pass
    
    elif data == 'get_detail_info': 
        pass

    elif data == 'get_checker_list': 
        pass

    elif data == 'go_to_previous_step': 
        await delete_message_and_answer(query, '*Service selection panel*', user_keyboard_work_mode, SpectateGitHubState.StartSpectate)

# SPECTATE VK
@dp.callback_query_handler(state=SpectateVKState.StartSpectate)
async def vk_state_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message

    if data == 'add_user_to_list': 
        pass

    elif data == 'delete_user_from_list': 
        pass
    
    elif data == 'get_detail_info': 
        pass

    elif data == 'get_checker_list': 
        pass

    elif data == 'go_to_previous_step': 
        await delete_message_and_answer(query, '*Service selection panel*', user_keyboard_work_mode, SpectateGitHubState.StartSpectate)

# SPECTATE DISCORD
@dp.callback_query_handler(state=SpectateDiscordState.StartSpectate)
async def discord_state_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message

    if data == 'add_user_to_list': 
        pass

    elif data == 'delete_user_from_list': 
        pass
    
    elif data == 'get_detail_info': 
        pass

    elif data == 'get_checker_list': 
        pass

    elif data == 'go_to_previous_step': 
        await delete_message_and_answer(query, '*Service selection panel*', user_keyboard_work_mode, SpectateGitHubState.StartSpectate)

# SPECTATE TELEGRAM
@dp.callback_query_handler(state=SpectateTelegramState.StartSpectate)
async def telegram_state_handler(query: types.CallbackQuery, state: FSMContext): 
    data = query.data
    message = query.message

    if data == 'add_user_to_list': 
        pass

    elif data == 'delete_user_from_list': 
        pass
    
    elif data == 'get_detail_info': 
        pass

    elif data == 'get_checker_list': 
        pass

    elif data == 'go_to_previous_step': 
        await delete_message_and_answer(query, '*Service selection panel*', user_keyboard_work_mode, SpectateGitHubState.StartSpectate)