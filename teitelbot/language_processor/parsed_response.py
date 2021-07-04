from dataclasses import dataclass


@dataclass
class ParsedResponse:
    text: str
    confidence: float