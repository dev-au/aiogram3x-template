from current_bot import _, types, filters, dp


@dp.message(filters.Command("help"))
async def help_command(message: types.Message):
    await message.answer("you get help")
