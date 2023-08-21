from aiogram.dispatcher.filters.state import State, StatesGroup

class WorkModeState(StatesGroup):
    StartSpectateMode = State()
    StartTrainingMode = State()

class InputState(StatesGroup): 
    StartInputMode = State()
    ConfirmAction = State()

class VerificationAccountState(StatesGroup):
    StartVerification = State()
    WaitPassword = State()

class SpectateStateMixin(StatesGroup):
    StartSpectate = State()

class SpectateGitHubState(SpectateStateMixin):
    pass

class SpectateTwitchState(SpectateStateMixin):
    pass

class SpectateVKState(SpectateStateMixin):
    pass

class SpectateDiscordState(SpectateStateMixin):
    pass

class SpectateTelegramState(SpectateStateMixin):
    pass
