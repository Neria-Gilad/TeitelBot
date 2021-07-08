from collections import defaultdict

from wit import Wit

import config
from language_processor.constants.action import Action
from language_processor.nlp_types import WeightedAction
from language_processor.witai.types import WitParsedMessage

_client = Wit(access_token=config.WitAi.Client.API_KEY)

_intent_actions = defaultdict(lambda: Action.DEFAULT_ACTION)
_intent_actions["email_request"] = Action.EMAIL_ACTION
_intent_actions["having_query"] = Action.HAVING_ACTION
_intent_actions["pointless_question"] = Action.GENERIC_QUESTION_ACTION
# _intent_actions["general_statement"] = Action.DEFAULT_ACTION
# _intent_actions["information_query"] = Action.DEFAULT_ACTION


def ask_wit(message: str) -> WitParsedMessage:
    return WitParsedMessage(**_client.message(message))


def possible_actions(parsed_message: WitParsedMessage) -> list[WeightedAction]:
    return [
        WeightedAction(_intent_actions[intent.name], intent.confidence)
        for intent in parsed_message.intents
    ]
