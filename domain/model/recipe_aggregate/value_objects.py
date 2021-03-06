import re

from domain.exceptions import InvalidValueException
from domain.model.base import Immutable
from domain.model.common_value_objects import URL


class RecipeURL(URL):

    def __init__(self, url: str, vendor_pattern: str):
        super().__init__(url)
        self.validate_vendor_pattern(url, vendor_pattern)

    @classmethod
    def validate_vendor_pattern(cls, url: str, vendor_pattern: str):
        cls.validate(url)
        regex = re.compile(vendor_pattern)
        if not regex.search(url):
            raise InvalidValueException(cls, f"invalid url '{url}' for Vendor pattern {vendor_pattern}")


class AggregateRating(Immutable):

    def __init__(self, rating_count: int, rating_value: float):
        if not isinstance(rating_count, int):
            raise InvalidValueException(
                self, 'rating count must be an int')

        if not isinstance(rating_value, float):
            raise InvalidValueException(self, 'rating value must be a float')

        if rating_value < 0:
            raise InvalidValueException(self, 'rating count cannot be less than 0')

        if not 0 <= rating_value <= 5:
            raise InvalidValueException(self, 'rating value has to be between 0 and 5')

        self._rating_count = rating_count
        self._rating_value = rating_value

    @property
    def rating_count(self) -> int:
        return self._rating_count

    @property
    def rating_value(self) -> float:
        return self._rating_value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._rating_count == other.rating_count and self._rating_value == other.rating_value

    def __str__(self) -> str:
        return f'Rating Count: {self._rating_count}, Rating Value: {self._rating_value}'


class Author(Immutable):
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise InvalidValueException(self, 'name must be a string')

        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._name == other._name

    def __str__(self):
        return f"Recipe Author '{self._name}'"
