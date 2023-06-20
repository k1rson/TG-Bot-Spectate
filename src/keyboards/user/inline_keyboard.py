from aiogram import types


user_keyboard_work_mode = types.InlineKeyboardMarkup(row_width=2)
user_keyboard_work_mode.add(
    types.InlineKeyboardButton('GitHub', callback_data='set_state_github'), 
    types.InlineKeyboardButton('Twitch', callback_data='set_state_twitch'), 
    types.InlineKeyboardButton('VK', callback_data='set_state_vk'), 
    types.InlineKeyboardButton('Discord', callback_data='set_state_discord'), 
    types.InlineKeyboardButton('Telegram', callback_data='set_state_telegram'),
)

# keyboard for verification state
user_keyboard_verification_state = types.InlineKeyboardMarkup(row_width=2)
user_keyboard_verification_state.add(
    types.InlineKeyboardButton('Start Verification', callback_data='start_verification'),
    types.InlineKeyboardButton('Cancel Verification', callback_data='cancel_verification'),
)

user_keyboard_verification_process = types.InlineKeyboardMarkup(row_width=2)
user_keyboard_verification_process.add(
    types.InlineKeyboardButton('Yes, I agree', callback_data='continue_verification'),
    types.InlineKeyboardButton('I don"t agree', callback_data='cancel_verification'),
)

# keyboard for spectate state - github
keyboard_spectate_github = types.InlineKeyboardMarkup(row_width=2)
keyboard_spectate_github.add(
    types.InlineKeyboardButton('Add user to the checker list', callback_data='add_user_to_list'),
    types.InlineKeyboardButton('Delete user from spectate', callback_data='delete_user_from_list'),
    types.InlineKeyboardButton('Get detail info about user', callback_data='get_detail_info'),
    types.InlineKeyboardButton('Come back', callback_data='go_to_previous_step'),
)

# keyboard for spectate state - twitch
keyboard_spectate_twitch = types.InlineKeyboardMarkup(row_width=2)
keyboard_spectate_twitch.add(
    types.InlineKeyboardButton('Add user to the checker list', callback_data='add_user_to_list'),
    types.InlineKeyboardButton('Delete user from spectate', callback_data='delete_user_from_list'),
    types.InlineKeyboardButton('Get detail info about user', callback_data='get_detail_info'),
    types.InlineKeyboardButton('Come back', callback_data='go_to_previous_step'),
)

# keyboard for spectate state - vk
keyboard_spectate_vk= types.InlineKeyboardMarkup(row_width=2)
keyboard_spectate_vk.add(
    types.InlineKeyboardButton('Add user to the checker list', callback_data='add_user_to_list'),
    types.InlineKeyboardButton('Delete user from spectate', callback_data='delete_user_from_list'),
    types.InlineKeyboardButton('Get detail info about user', callback_data='get_detail_info'),
    types.InlineKeyboardButton('Come back', callback_data='go_to_previous_step'),
)

# keyboard for spectate state - discord
keyboard_spectate_discord = types.InlineKeyboardMarkup(row_width=2)
keyboard_spectate_discord.add(
    types.InlineKeyboardButton('Add user to the checker list', callback_data='add_user_to_list'),
    types.InlineKeyboardButton('Delete user from spectate', callback_data='delete_user_from_list'),
    types.InlineKeyboardButton('Get detail info about user', callback_data='get_detail_info'),
    types.InlineKeyboardButton('Come back', callback_data='go_to_previous_step'),
)

# keyboard for spectate state - telegram
keyboard_spectate_telegram = types.InlineKeyboardMarkup(row_width=2)
keyboard_spectate_telegram.add(
    types.InlineKeyboardButton('Add user to the checker list', callback_data='add_user_to_list'),
    types.InlineKeyboardButton('Delete user from spectate', callback_data='delete_user_from_list'),
    types.InlineKeyboardButton('Get detail info about user', callback_data='get_detail_info'),
    types.InlineKeyboardButton('Come back', callback_data='go_to_previous_step'),
)
