import uuid
from abc import ABC
from datetime import datetime

from domain.exceptions import DiscardEntityError


class Entity(ABC):
    """The base class of all entities.

    Attributes:
        id: A unique identifier
        version: An integer version
        discarded: True if this entity should no longer be used. otherwise False

    """

    def __init__(self):
        self._id = uuid.uuid4()
        self._version = 1
        self._discarded = False
        self._date_created = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def version(self):
        return self._version

    @property
    def discarded(self):
        return self._discarded

    @property
    def date_created(self):
        return self._date_created

    def delete(self):
        self._discarded = True

    def _check_not_discarded(self):
        if self._discarded:
            raise DiscardEntityError(f"Attempt to use {repr(self)}")

    def __repr__(self) -> str:
        return "discarded={d!r}, id={id!r}, version={v!r}".format(
            d=self._discarded,
            id=self._id.__str__(),
            v=self._version)

    def _increment_version(self):
        self._version += 1