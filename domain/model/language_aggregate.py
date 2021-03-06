from __future__ import annotations

from uuid import UUID

from domain.exceptions import InvalidValueException
from domain.model.base import Entity


def create_language(language_id: UUID, name: str, code: str) -> Language:
    if not isinstance(name, str):
        raise InvalidValueException(Language, 'language name must be a string')

    if not isinstance(code, str):
        raise InvalidValueException(Language, 'language code must be a string')

    if len(code) != 2:
        raise InvalidValueException(Language, 'Language Acronym must have a length of 2')
    return Language(language_id=language_id, name=name, code=code)


class Language(Entity):

    def __init__(self, language_id: UUID, name: str, code: str):
        super().__init__(language_id)

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

    def __repr__(self) -> str:
        return "{c}({s}, name={name!r}, code={code!r})".format(
            c=self.__class__.__name__,
            s=super().__repr__(),
            name=self._name,
            code=self._code
        )
