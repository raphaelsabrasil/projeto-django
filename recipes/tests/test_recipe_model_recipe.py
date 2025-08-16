from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug-for-no-defaults',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe Preparation Steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    
    
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False',
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False',
        )

    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = needed
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), needed,
            msg=f'Recipe string representation must be'
                f'"{needed}" but "{str(self.recipe)}" was received.'
        )


    # def test_the_test(self):
    #     recipe = self.recipe
    #     ...

    # def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
    #     # self.fail(len(self.recipe.title))
    #     self.recipe.title = 'A' * 70
        
    #     # teste passou, pois o titulo tem mais de 65 caracteres e levantou o ValidationError. Se tiver menos de 65, o ValidationError não levanta e o teste quebra.
    #     with self.assertRaises(ValidationError):  # com isso daqui o teste passa e a validação abaixo não quebra
    #         self.recipe.full_clean()    # aqui a validação ocorre, mas o python considera um erro e quebra o teste
    #     # self.recipe.save()      # salva na base de dados, mas não valida
    #     # self.fail(self.recipe.title)
        