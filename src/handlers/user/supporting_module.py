from aiogram import types

async def delete_message_and_answer(query: types.CallbackQuery, text: str, state=None, markup=None):
    await query.message.delete()
    await query.message.answer(text, parse_mode='Markdown', reply_markup=markup)

    if state is not None: 
        await state.set()