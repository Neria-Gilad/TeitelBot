from typing import Union, Optional
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
    intents: list[Union[Intent, dict]]
    entities: dict[str, list[Union[Entity, dict]]]
    traits: dict

    def __post_init__(self):
        if not self.intents:
            # no point responding if there is no intent to the query
            return

        self.intents = [Intent(**intent) for intent in self.intents]
        self.entities = {entity_list_name: [
                Entity(**entity) for entity in entity_list
            ]
            for entity_list_name, entity_list in self.entities.items()
        }

