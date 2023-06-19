import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from initializer import dp, bot

from keyboards.admin.inline_keyboard import admin_keyboard_work_mode

from states.general_states import SpectateGitHubState, SpectateTwitchState, SpectateVKState, SpectateDiscordState, SpectateTelegramState

from logic.github_state_logic import *
from logic.twitch_state_logic import * 
from logic.vk_state_logic import * 
from logic.discord_state_logic import *
from logic.telegram_state_logic import *

# SPECTATE GITHUB
@dp.callback_query_handler(state=SpectateGitHubState)
async def github_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)

        await state.finish()

# SPECTATE TWITCH
@dp.callback_query_handler(state=SpectateTwitchState)
async def twitch_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)

        await state.finish()

# SPECTATE VK
@dp.callback_query_handler(state=SpectateVKState)
async def vk_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)

        await state.finish()

# SPECTATE DISCORD
@dp.callback_query_handler(state=SpectateDiscordState)
async def discord_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)

        await state.finish()

# SPECTATE TELEGRAM
@dp.callback_query_handler(state=SpectateTelegramState)
async def telegram_state_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'add_user_to_list': 
        await callback_query.answer('add')

    elif callback_query.data == 'go_to_previous_step': 
        await callback_query.message.delete()
        await callback_query.message.answer('*Service selection panel*', parse_mode='Markdown', reply_markup=admin_keyboard_work_mode)

        await state.finish()