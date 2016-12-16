# -*- coding: utf-8 -*-
import json

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

    def to_native(self, value):
        return json.dumps(value)

    def to_primitive(self, value):
        if type(value) == dict:
            return json.loads(value)
        else:
            return value
