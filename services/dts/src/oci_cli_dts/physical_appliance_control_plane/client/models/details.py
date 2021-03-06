# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Details(object):
    """
    Details model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Details object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param details:
            The value to assign to the details property of this Details.
        :type details: str

        """
        self.swagger_types = {
            'details': 'str'
        }

        self.attribute_map = {
            'details': 'details'
        }

        self._details = None

    @property
    def details(self):
        """
        Gets the details of this Details.

        :return: The details of this Details.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Details.

        :param details: The details of this Details.
        :type: str
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
