```ipython

$ ./manage.py shell_plus

Python 3.6.5 (default, Apr  1 2018, 05:46:30)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from apps.geonames.utils import get_distance, get_distances, get_distances_as_dict

In [2]: get_distance("80808", "51342")  # Get the distance between two postal codes
Out[2]: 580.2183897303665

In [3]: get_distances(["80808", "51342", "98102", "35411"])  # Get distances from the origin postal code in the first position of the list
Out[3]: [0.0, 580.2183897303665, 1078.9653188110271, 0.0]

In [4]: get_distances(("80808", "51342", "98102", "35412"))  # Works with tuples too of course
Out[4]: [0.0, 580.2183897303665, 1078.9653188110271, 0.0]

In [5]: get_distances(("80808", "51342", "98102", "72351"))  # Let's find a zip code that exists for that last position
Out[5]: [0.0, 580.2183897303665, 1078.9653188110271, 814.2641580921866]

In [6]: get_distances_as_dict(("80808", "51342", "98102", "72351"))  # Return results as a dictionary
Out[6]:
{'80808': 0.0,
 '51342': 580.2183897303665,
 '98102': 1078.9653188110271,
 '72351': 814.2641580921866}

```
