from django.test import TestCase

from cadastral.models import Coordinates


class ModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.coord = Coordinates.objects.create(
            cadastral_numb=1,
            latitude=12.564878,
            longitude=15.564778
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        task = ModelTest.coord
        field_verboses = {
            'cadastral_numb': 'Кадастровый номер',
            'latitude': 'широта',
            'longitude': 'долгота',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        task = ModelTest.coord
        field_help_texts = {
            'latitude': 'Введите широту',
            'longitude': 'Введите долготу'
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).help_text, expected_value)
