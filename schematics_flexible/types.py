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
        return json.loads(value)

