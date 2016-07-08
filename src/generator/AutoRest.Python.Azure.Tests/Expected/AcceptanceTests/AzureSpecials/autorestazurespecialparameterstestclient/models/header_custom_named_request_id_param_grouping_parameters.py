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


class HeaderCustomNamedRequestIdParamGroupingParameters(Model):
    """Additional parameters for the header_customNamedRequestIdParamGrouping
    operation.

    :param foo_client_request_id: The fooRequestId
    :type foo_client_request_id: str
    """ 

    _validation = {
        'foo_client_request_id': {'required': True},
    }

    def __init__(self, foo_client_request_id):
        self.foo_client_request_id = foo_client_request_id