from .antiflood import ThrottlingMiddleware
from current_bot import dp

if __name__ == "middlewares":
    dp.message.middleware(ThrottlingMiddleware())
