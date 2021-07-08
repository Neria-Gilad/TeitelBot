from dataclasses import dataclass
from typing import Optional

from .constants.action import Action


@dataclass
class WeightedResponse:
    text: Optional[str]
    confidence: float


@dataclass
class WeightedAction:
    action: Action
    confidence: float
