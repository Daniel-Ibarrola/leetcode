"""The property listings module contains functions to process and format properties."""

from __future__ import annotations

import enum
import dataclasses
from abc import ABC, abstractmethod

MAX_PRICE_FILTER = 1000000
MIN_SCORE_FILTER = 50
PRICE_SCORE_DIVISOR = 10000


class ScoringStrategy(ABC):
    """Abstract base class for a scoring strategy."""

    @abstractmethod
    def calculate(self, prop: Property) -> float:
        pass


class SingleFamilyScoringStrategy(ScoringStrategy):
    """Scoring strategy for SINGLE_FAMILY properties."""

    def calculate(self, prop: Property) -> float:
        return prop.sqft * 0.5 + prop.bedrooms * 20


class CondoScoringStrategy(ScoringStrategy):
    """Scoring strategy for CONDO properties."""

    def calculate(self, prop: Property) -> float:
        return prop.sqft * 0.3 + (5 - prop.bedrooms) * 10


class OtherScoringStrategy(ScoringStrategy):
    """Default scoring strategy."""

    def calculate(self, prop: Property) -> float:
        return prop.sqft * 0.2


class PropertyType(enum.Enum):
    """Enumeration of property types."""

    CONDO = "CONDO"
    SINGLE_FAMILY = "SINGLE_FAMILY"
    TOWNHOUSE = "TOWNHOUSE"
    OTHER = "OTHER"

    @property
    def scoring_strategy(self) -> ScoringStrategy:
        """Gets the scoring strategy for the property type."""
        if self == PropertyType.SINGLE_FAMILY:
            return SingleFamilyScoringStrategy()
        if self == PropertyType.CONDO:
            return CondoScoringStrategy()
        return OtherScoringStrategy()


@dataclasses.dataclass
class Property:
    """A property listing with associated metadata."""

    id: str
    price: float
    bedrooms: int
    sqft: int
    type: PropertyType

    @property
    def score(self) -> float:
        """Calculates the property score using a strategy."""
        base_score = self.type.scoring_strategy.calculate(self)
        return base_score - (self.price / PRICE_SCORE_DIVISOR)

    def is_eligible(self) -> bool:
        """Checks if the property is eligible for display."""
        return self.price < MAX_PRICE_FILTER and self.score > MIN_SCORE_FILTER

    def format(self) -> str:
        """Formats the property listing for display."""
        return f"Property {self.id} [{self.type.value}] - Score: {self.score:.2f} - Price: ${self.price:,}"


def process_properties(properties: list[Property]) -> list[str]:
    """Filters and formats property listings based on price and score."""
    formatted_properties: list[str] = []

    for prop in properties:
        if prop.is_eligible():
            formatted_properties.append(prop.format())

    return formatted_properties
