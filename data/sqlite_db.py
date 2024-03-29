from bot_spec.sql_controller import TableController, Models


class UsersTable(TableController):
    telegram_id = Models().INTEGER_NUMBER(primary_key=True, max_length=10, not_null=True)
    full_name = Models().STRING_SHORT_TEXT(max_length=32, not_null=True)
    first_message = Models().STRING_LONG_TEXT(not_null=True)
