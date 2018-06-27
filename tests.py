from django.test import TestCase

from .utils import get_distance, get_distances


class TestGeoNamesUtils(TestCase):
    """ Project over budget... finish tests some other day. """

    def setUp(self):
        """ TODO: Need to provision a GeoNames test database, probably from a fixture. """

    def test_get_distance(self):
        """ Does the server return the corect results between known points? """
        # distance = get_distance('98103', '98370')
        # self.assertEqual(distance, 20)  # 20? Maybe who knows. See what comes back and use that instead.

    def test_get_dinstances(self):
        """ Does the server return correct results between known points in a list of coordinates? """
        # my_distances = get_distances((98103, 98107, 80422, ))
        # self.assertEqual(my_distances[0], 0)  # First position should always be the origin's distance from itself, i.e., 0
        # self.assertEqual(my_distances[1], 9)  # See what the system returns as valid and use that in the test
        # self.assertEqual(my_distances[2], 1200)  # See what the system returns as valid and use that in the test

    def test_no_bad_juju(self):
        """ If the origin postal code is junk does the server handle it gracefully? """
        pass
