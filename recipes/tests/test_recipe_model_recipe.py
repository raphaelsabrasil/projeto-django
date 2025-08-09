from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    # def test_the_test(self):
    #     recipe = self.recipe
    #     ...

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        # self.fail(len(self.recipe.title))
        self.recipe.title = 'A' * 70
        
        # teste passou, pois o titulo tem mais de 65 caracteres e levantou o ValidationError. Se tiver menos de 65, o ValidationError não levanta e o teste quebra.
        with self.assertRaises(ValidationError):  # com isso daqui o teste passa e a validação abaixo não quebra
            self.recipe.full_clean()    # aqui a validação ocorre, mas o python considera um erro e quebra o teste
        # self.recipe.save()      # salva na base de dados, mas não valida
        # self.fail(self.recipe.title)
        