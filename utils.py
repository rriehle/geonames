import math

from .models import GeoNames


def great_circle_distance(lat1, lon1, lat2, lon2):
    """ Return the Great Circle Distance between two coordinates """

    # TODO: Use cython to make run this calculation in C to speed it up if necessary.

    radius = 3956  # miles
    x = math.pi / 180.0
    a = (90.0 - lat1) * (x)
    b = (90.0 - lat2) * (x)
    theta = (lon2 - lon1) * (x)
    c = math.acos((math.cos(a) * math.cos(b)) + (math.sin(a) * math.sin(b) * math.cos(theta)))
    return radius * c


def get_distance(origin_postal_code, destination_postal_code):
    """ Take an origin and destination postal code and return the distance between them """
    gcd = 0.0  # Return a float consistently

    if origin_postal_code == destination_postal_code:
        return gcd

    origin = GeoNames.objects.filter(postal_code=origin_postal_code).first()
    destination = GeoNames.objects.filter(postal_code=destination_postal_code).first()

    # If we have both origin and destination coordinates return the gcd calculation
    if origin and destination:

        # TODO: memoize results to redis if this gets slow
        gcd = great_circle_distance(
            origin.latitude,
            origin.longitude,
            destination.latitude,
            destination.longitude
        )

        if origin.country_code == "CA":
            gcd /= 0.62137  # Convert from miles to kilometers

    return gcd


def get_distances(postal_codes):
    """ Take a list or tuple of postal codes and return a list of distances """

    origin = postal_codes[0]

    return [get_distance(origin, destination) for destination in postal_codes]


def get_distances_as_dict(postal_codes):
    """ Take a list or tuple of postal codes and return a dict of distances """

    origin = postal_codes[0]

    return {destination: get_distance(origin, destination) for destination in postal_codes}
