# -*- coding: utf-8 -*-
import json
import sys

from schematics.types import BaseType
from schematics.exceptions import ValidationError


class JsonType(BaseType):
    """
    Take json object and save like strgin
    """

    def validate_jsontype(self, value):
        try:
            json.dumps(value)
        except TypeError as error:
            raise ValidationError(error.args[0])

    def to_native(self, value, context=None):
        if isinstance(value, str) or \
                sys.version_info[0] == 2 and isinstance(value, unicode):
            return value
        else:
            return json.dumps(value)

    def to_primitive(self, value, context=None):
        if isinstance(value, dict):
            return json.loads(value)
        else:
            return value
