from __future__ import annotations

from datetime import datetime
from typing import List, Tuple

from common.domain import Entity, URL
from crawler_context.domain.model.category_aggregate import Category


def create_vendor(name: str, base_url: str, date_last_crawled: datetime, categories: List[Category], categories_link: str) -> Vendor:
    base_url_object = URL(url=base_url)
    return Vendor(
        name=name,
        base_url=base_url_object,
        date_last_crawled=date_last_crawled,
        categories=categories,
        categories_link=categories_link,
    )


class Vendor(Entity):

    def __init__(self, name: str, base_url: URL, date_last_crawled: datetime,
                 categories: List[Category], categories_link: str):
        super().__init__()

        self._name = name
        self._base_url = base_url

        self.date_last_crawled = date_last_crawled
        self.categories_link = categories_link

        self._categories: List[Category] = []

        for category in categories:
            self.add_category(category)

    @property
    def name(self) -> str:
        self._check_not_discarded()
        return self._name

    @property
    def base_url(self) -> URL:
        self._check_not_discarded()
        return self._base_url

    @property
    def date_last_crawled(self) -> datetime:
        self._check_not_discarded()
        return self._date_last_crawled

    @date_last_crawled.setter
    def date_last_crawled(self, value: datetime):
        self._check_not_discarded()
        if not isinstance(value, datetime):
            raise ValueError('date_last_crawled must be a datetime')
        self._date_last_crawled = value
        self._increment_version()

    @property
    def categories_link(self) -> str:
        self._check_not_discarded()
        return self._categories_link

    @categories_link.setter
    def categories_link(self, link: str):
        self._check_not_discarded()
        if not isinstance(link, str):
            raise ValueError('categories_link must be a string')
        self._categories_link = link
        self._increment_version()

    @property
    def categories(self) -> Tuple[Category]:
        self._check_not_discarded()
        return tuple(self._categories)

    def add_category(self, category: Category):
        self._check_not_discarded()
        if not isinstance(category, Category):
            raise ValueError('category must be a Category instance')
        self._categories.append(category)
        self._increment_version()

    def remove_category(self, category: Category):
        self._check_not_discarded()
        if not isinstance(category, Category):
            raise ValueError('category must be a Category instance')
        self._categories.remove(category)
        self._increment_version()

    def delete(self):
        for category in self._categories:
            category.delete()
        super().delete()

    def __str__(self) -> str:
        return f"Vendor '{self._name}'"

    def __repr__(self) -> str:
        return "{c}({s}, name={name!r}, count_categories={count_categories!r}, base_url={base_url!r})".format(
            c=self.__class__.__name__,
            s=super().__repr__(),
            name=self._name,
            count_categories=len(self._categories),
            base_url=self._base_url,
        )
