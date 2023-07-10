#!/usr/bin/python3
"""module documentation"""


def inherits_from(obj, a_class):
    """
    returns true if an obj is an istance of a class that inherited(directly)
    or indirectly from a specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class

