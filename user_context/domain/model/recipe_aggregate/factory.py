from datetime import timedelta, datetime
from typing import List
from uuid import UUID

from common.domain.model.ingredient_aggregate import Ingredient
from common.domain.model.language_aggregate import Language
from common.domain.model.value_objects import URL, RecipeURL, AggregateRating, Author
from common.exceptions import InvalidValueError
from user_context.domain.model.category_aggregate import Category
from user_context.domain.model.recipe_aggregate.recipe import Recipe
from user_context.domain.model.vendor_aggregate import Vendor


def create_recipe(recipe_id: UUID, name: str, description: str, author: str, vendor_id: str,
                  prep_time: timedelta, cook_time: timedelta, total_time: timedelta, date_published: datetime,
                  recipe_url: str, category: Category, vendor: Vendor, language: Language, rating_count: int,
                  rating_value: float, image_url: str, ingredients: List[Ingredient]) -> Recipe:
    if not isinstance(name, str):
        raise InvalidValueError(Recipe, 'name must be a string')

    if not isinstance(description, str):
        raise InvalidValueError(Recipe, 'description must be a string')

    if not isinstance(vendor_id, str):
        raise InvalidValueError(Recipe, 'vendor_id must be a string')

    if not isinstance(prep_time, timedelta):
        raise InvalidValueError(Recipe, 'prep_time must be a timedelta')

    if not isinstance(cook_time, timedelta):
        raise InvalidValueError(Recipe, 'cook_time must be a timedelta')

    if not isinstance(total_time, timedelta):
        raise InvalidValueError(Recipe, 'total_time must be a timedelta')

    if not isinstance(date_published, datetime):
        raise InvalidValueError(Recipe, 'date_published must be a datetime')

    if not isinstance(category, Category):
        raise InvalidValueError(Recipe, 'category must be a Category instance')

    if not isinstance(vendor, Vendor):
        raise InvalidValueError(Recipe, 'vendor must be a Vendor instance')

    if not isinstance(language, Language):
        raise InvalidValueError(Recipe, 'language must be a Language instance')

    if not isinstance(image_url, str):
        raise InvalidValueError(Recipe, 'image_urls must be a list of strings')

    if not isinstance(ingredients, list):
        raise InvalidValueError(Recipe, 'ingredients must be a list of strings')

    author_object = Author(name=author)
    recipe_url_object = RecipeURL(url=recipe_url, vendor_pattern=vendor.recipe_pattern)
    image_url_object = URL(url=image_url)
    aggregate_rating_object = AggregateRating(rating_count=rating_count, rating_value=rating_value)

    return Recipe(
        recipe_id=recipe_id,
        name=name,
        description=description,
        author=author_object,
        vendor_id=vendor_id,
        prep_time=prep_time,
        cook_time=cook_time,
        total_time=total_time,
        date_published=date_published,
        url=recipe_url_object,
        category=category,
        vendor=vendor,
        language=language,
        aggregate_rating=aggregate_rating_object,
        image=image_url_object,
        ingredients=ingredients,
    )