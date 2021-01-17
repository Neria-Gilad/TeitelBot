from enum import Enum, auto


class Action(Enum):
    NONE = auto()
    EMAIL_ACTION = auto()
    HAVING_ACTION = auto()
    REPEAT_SARCASTICALLY_ACTION = auto()
    DEFAULT_ACTION = auto()
    GENERIC_QUESTION_ACTION = auto()
    ARE_YOU_SURE_ACTION = auto()
    CHECK_NUMBER_ACTION = auto()
