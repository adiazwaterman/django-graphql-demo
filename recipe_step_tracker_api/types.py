import strawberry_django
from strawberry import auto, ID

from .models import RecipeStep as RecipeStepModel

@strawberry_django.type(RecipeStepModel)
class RecipeStep:
    id: ID
    step: auto
    completed: auto

@strawberry_django.input(RecipeStepModel)
class RecipeStepInput:
    step: auto
    completed: auto

@strawberry_django.partial(RecipeStepModel)
class UpdateRecipeStep:
    id: auto
    step: auto
    completed: auto
 