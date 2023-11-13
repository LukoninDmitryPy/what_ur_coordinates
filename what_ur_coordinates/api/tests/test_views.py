from django.test import TestCase

from cadastral.models import Coordinates


class ResponseTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.coord = Coordinates.objects.create(
            cadastral_numb=1,
            latitude=12.564878,
            longitude=15.564778
        )

    def check_context(self, response):
        self.response = response
        response_numb = response.context['page_obj'][0].cadastral_numb
        response_lat = response.context['page_obj'][0].latitude
        response_lon = response.context['page_obj'][0].longitude
        self.assertEqual(response_numb, self.coord.cadastral_numb)
        self.assertEqual(response_lat, self.coord.latitude)
        self.assertEqual(response_lon, self.coord.longitude)
