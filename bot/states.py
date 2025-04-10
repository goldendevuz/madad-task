from aiogram.fsm.state import State, StatesGroup


class FeedbackState(StatesGroup):
    body = State()

class AdminState(StatesGroup):
    ask_ad_content = State()

class RegistrationStates(StatesGroup):
    name = State()
    phone = State()
    course = State()