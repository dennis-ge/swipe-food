import re
from urllib.parse import urlparse

from common.domain.model_base import Immutable


class URL(Immutable):
    VALID_PROTOCOLS = ['http', 'https']

    def __init__(self, url: str):
        self.validate(url)
        self._value = url

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def validate(cls, url: str):
        if not isinstance(url, str):
            raise ValueError('url must be a string')

        parsed_url = urlparse(url)
        if parsed_url.scheme not in cls.VALID_PROTOCOLS or parsed_url.netloc == '':
            raise ValueError(f'Invalid {cls.__class__.__name__} {url}')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value == other._value

    def __str__(self) -> str:
        return self._value


class Language(Immutable):

    def __init__(self, name: str, code: str):
        if not isinstance(name, str):
            raise ValueError('language name must be a string')

        if not isinstance(code, str):
            raise ValueError('language code must be a string')

        if len(code) != 2:
            raise ValueError('Language Acronym must have a length of 2')

        self._name = name
        self._code = code

    @property
    def name(self) -> str:
        return self._name

    @property
    def code(self) -> str:
        """The language code according to ISO 639-1"""
        return self._code

    def __str__(self) -> str:
        return f"Language '{self._name}' with code '{self._code}'"


class AggregateRating(Immutable):

    def __init__(self, rating_count: int, rating_value: float):
        if not isinstance(rating_count, int):
            raise ValueError('rating count must be an int')

        if not isinstance(rating_value, float):
            raise ValueError('rating value must be a float')

        if rating_value < 0:
            raise ValueError('rating count cannot be less than 0')

        if not 0 <= rating_value <= 5:
            raise ValueError('rating value has to be between 0 and 5')

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
        return self._rating_count == other.rating_count and self._rating_value == other.rating_count

    def __str__(self) -> str:
        return f'Rating Count: {self._rating_count}, Rating Value: {self._rating_value}'


class RecipeURL(URL):

    def __init__(self, url: str, vendor_pattern: str):
        super().__init__(url)
        self.validate_vendor_pattern(url, vendor_pattern)

    @classmethod
    def validate_vendor_pattern(cls, url: str, vendor_pattern: str):
        cls.validate(url)
        regex = re.compile(vendor_pattern)
        if not regex.search(url):
            raise ValueError(f"Invalid {cls.__class__.__name__} '{url}' for Vendor pattern {vendor_pattern}")