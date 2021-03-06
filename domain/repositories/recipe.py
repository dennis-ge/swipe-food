from abc import abstractmethod, ABC
from typing import List

from domain.model.recipe_aggregate import Recipe
from domain.model.user_aggregate import User
from domain.repositories.base import AbstractBaseRepository


class AbstractRecipeRepository(AbstractBaseRepository, ABC):

    @abstractmethod
    def get_by_name(self, recipe_name: str) -> Recipe:
        raise NotImplementedError

    @abstractmethod
    def get_matched_users(self, recipe: Recipe) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def get_unseen_recipes_for_user(self, user: User, limit: int = None) -> List[Recipe]:
        raise NotImplementedError
