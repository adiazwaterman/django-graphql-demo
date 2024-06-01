import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from strawberry_django import mutations

from .types import RecipeStep, RecipeStepInput, UpdateRecipeStep

@strawberry.type
class Query:
    recipe_steps: list[RecipeStep] = strawberry_django.field()

@strawberry.type
class Mutation:
    add_recipe_step: RecipeStep = mutations.create(RecipeStepInput)
    update_recipe_step: RecipeStep = mutations.update(UpdateRecipeStep)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[DjangoOptimizerExtension]
    )