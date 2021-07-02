from collections import defaultdict

from wit import Wit

import config
from language_processor.constants.action import Action
from language_processor.parsed_message import ParsedMessage

_client = Wit(access_token=config.WitAi.Client.API_KEY)

_intent_actions = defaultdict(lambda: Action.DEFAULT_ACTION)
_intent_actions["email_request"] = Action.EMAIL_ACTION
_intent_actions["having_query"] = Action.HAVING_ACTION
_intent_actions["pointless_question"] = Action.GENERIC_QUESTION_ACTION
_intent_actions["general_statement"] = Action.DEFAULT_ACTION
_intent_actions["information_query"] = Action.DEFAULT_ACTION


class WitParsedMessage(ParsedMessage):
    def __init__(self, wit_response: dict):
        super().__init__(wit_response["text"], -1)
        self._parse(wit_response)

    def _parse(self, wit_response: dict):
        self.message_text = wit_response["text"]
        intents: list = wit_response["intents"]
        if 0 == len(intents):
            # no point responding if there is no intent to the query
            return
        chosen_intent: dict = intents[0]
        self.action = _intent_actions[chosen_intent["name"]]
        self.confidence = chosen_intent["confidence"]
        self.wit_entities: dict = wit_response["entities"]


def ask_wit(message: str) -> WitParsedMessage:
    return WitParsedMessage(_client.message(message))
