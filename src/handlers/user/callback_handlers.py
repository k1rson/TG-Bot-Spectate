from aiogram import types
from aiogram.dispatcher import FSMContext

from initializer import dp

from keyboards.user.inline_keyboard import keyboard_spectate_github, keyboard_spectate_twitch, keyboard_spectate_vk, keyboard_spectate_discord, keyboard_spectate_telegram, user_keyboard_verification_process

from states.general_states import SpectateGitHubState, SpectateTwitchState, SpectateVKState, SpectateDiscordState, SpectateTelegramState, VerificationAccountState

@dp.callback_query_handler(lambda c: True)
async def selectel_panel_handler(callback_query: types.CallbackQuery, state: FSMContext): 
    if callback_query.data == 'start_verification': 
        await callback_query.message.delete()
        await callback_query.message.answer('You *agree* to the processing of data?', parse_mode='Markdown', reply_markup=user_keyboard_verification_process)
        
        await VerificationAccountState.StartVerification.set()

    elif callback_query.data == 'cancel_verification':
        await callback_query.message.delete()
        await callback_query.message.answer('So bad. GoodBye and GoodLuck 😟 /start')
    
    elif callback_query.data == 'set_state_github': 
        await callback_query.message.delete()
        await callback_query.message.answer('The operation mode was selected. *Current mode: GitHub*', parse_mode='Markdown', reply_markup=keyboard_spectate_github)

        await SpectateGitHubState.StartSpectate.set()

    elif callback_query.data == 'set_state_twitch': 
        await callback_query.message.delete()
        await callback_query.message.answer('The operation mode was selected. *Current mode: Twitch*', parse_mode='Markdown', reply_markup=keyboard_spectate_twitch)

        await SpectateTwitchState.StartSpectate.set()

    elif callback_query.data == 'set_state_vk': 
        await callback_query.message.delete()
        await callback_query.message.answer('The operation mode was selected. *Current mode: VK*', parse_mode='Markdown', reply_markup=keyboard_spectate_vk)

        await SpectateVKState.StartSpectate.set()

    elif callback_query.data == 'set_state_discord': 
        await callback_query.message.delete()
        await callback_query.message.answer('The operation mode was selected. *Current mode: Discord*', parse_mode='Markdown', reply_markup=keyboard_spectate_discord)

        await SpectateDiscordState.StartSpectate.set()

    elif callback_query.data == 'set_state_telegram': 
        await callback_query.message.delete()
        await callback_query.message.answer('The operation mode was selected. *Current mode: Telegram*', parse_mode='Markdown', reply_markup=keyboard_spectate_telegram)

        await SpectateTelegramState.StartSpectate.set()