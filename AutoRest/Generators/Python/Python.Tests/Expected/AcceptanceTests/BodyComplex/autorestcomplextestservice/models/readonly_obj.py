# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReadonlyObj(Model):
    """ReadonlyObj

    :param id:
    :type id: str
    :param size:
    :type size: int
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
    }

    def __init__(self, id=None, size=None, **kwargs):
        self.id = id
        self.size = size
