from aiogram import types

from initializer import dp

from keyboards.user.inline_keyboard import (
    keyboard_spectate_github,
    keyboard_spectate_twitch,
    keyboard_spectate_vk,
    keyboard_spectate_discord,
    keyboard_spectate_telegram,
    user_keyboard_verification_process,
)

from states.general_states import (
    SpectateGitHubState,
    SpectateTwitchState,
    SpectateVKState,
    SpectateDiscordState,
    SpectateTelegramState,
    VerificationAccountState,
)

async def delete_message_and_answer(query: types.CallbackQuery, text: str, state=None, markup=None):
    await query.message.delete()
    await query.message.answer(text, parse_mode='Markdown', reply_markup=markup)

    if state is not None: 
        await state.set()

@dp.callback_query_handler(lambda c: True)
async def selectel_panel_handler(query: types.CallbackQuery): 
    data = query.data

    if data == 'start_verification': 
        await delete_message_and_answer(query, 'You *agree* to the processing of data?', VerificationAccountState.StartVerification, user_keyboard_verification_process)
    
    elif data == 'cancel_verification':
        await delete_message_and_answer(query, 'So bad. GoodBye and GoodLuck 😟 /start')

    elif data == 'set_state_github':
        await delete_message_and_answer(query, 'The operation mode was selected. *Current mode: GitHub*', SpectateGitHubState.StartSpectate, keyboard_spectate_github)

    elif data == 'set_state_twitch':
        await delete_message_and_answer(query, 'The operation mode was selected. *Current mode: Twitch*', SpectateTwitchState.StartSpectate, keyboard_spectate_twitch)

    elif data == 'set_state_vk':
        await delete_message_and_answer(query, 'The operation mode was selected. *Current mode: VK*', SpectateVKState.StartSpectate, keyboard_spectate_vk)

    elif data == 'set_state_discord':
        await delete_message_and_answer(query, 'The operation mode was selected. *Current mode: Discord*', SpectateDiscordState.StartSpectate, keyboard_spectate_discord)

    elif data == 'set_state_telegram':
        await delete_message_and_answer(query, 'The operation mode was selected. *Current mode: Telegram*', SpectateTelegramState.StartSpectate, keyboard_spectate_telegram)