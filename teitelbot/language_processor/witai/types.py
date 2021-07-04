from dataclasses import dataclass, field


@dataclass
class Intent:
    id: str
    name: str
    confidence: float


@dataclass
class Entity:
    id: str
    name: str
    role: str
    start: int
    end: int
    body: str
    confidence: float
    entities: list
    value: str
    type: str
    suggested: bool = field(default=False)


@dataclass
class WitParsedMessage:
    text: str
    intents: list[Intent]
    entities: dict[list[Entity]]
    traits: dict
    main_intent: Intent = field(init=False)
    confidence: float = field(default=-1)

    def __post_init__(self):
        if not self.intents:
            # no point responding if there is no intent to the query
            return

        self.intents = [Intent(**intent) for intent in self.intents]
        self.main_intent = self.intents[0]
        self.confidence = self.main_intent.confidence

        self.entities = {entity_list_name: [
                Entity(**entity) for entity in entity_list
            ]
            for entity_list_name, entity_list in self.entities.items()
        }

    # def __init__(self, wit_response: wit_response_struct):
    #     self.confidence = -1
    #     self._parse(wit_response)
    #
    # def _parse(self, wit_response: wit_response_struct):
    #     self.message_text = wit_response["text"]
    #     intents: list = wit_response["intents"]
    #     if not intents:
    #         # no point responding if there is no intent to the query
    #         return
    #     chosen_intent: dict = intents[0]
    #     self.action = _intent_actions[chosen_intent["name"]]
    #     self.confidence = chosen_intent["confidence"]
    #     self.wit_entities: dict = wit_response["entities"]
