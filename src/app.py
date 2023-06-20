from handlers.user.callback_handlers import * 
from handlers.user.message_handlers import *
from handlers.user.states_handlers import *

from handlers.admin.callback_handlers import * 
from handlers.admin.message_handlers import * 
from handlers.admin.states_handlers import * 

from aiogram import executor

from initializer import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)