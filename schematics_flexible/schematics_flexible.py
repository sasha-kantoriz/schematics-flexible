# -*- coding: utf-8 -*-
import json

from schematics.types import StringType
from schematics.models import Model
from jsonschema.exceptions import ValidationError as jsonschemaValidationError
from schematics.exceptions import ValidationError as schematicsValidationError


class _Flexible(Model):
    """ Save code, version and props of schema """

    _loaded = False
    _schema_source = None

    version = StringType()
    code = StringType(max_length=10)
    properties = StringType()

    def validate(self, partial=False, strict=False):
        """ Try find schema and validate them """
        if not self._loaded:
            self._load_schemas()
        schema = self._schema_source.get_schema(self.code, self.version)
        if schema:
            try:
                schema[2].validate(json.loads(self.properties))
            except jsonschemaValidationError as error:
                raise schematicsValidationError(error.message)
        super(_Flexible, self).validate()

    def _load_schemas(self):
        """ Load all schemas from source to dist """
        self._schema_source.load()
        self._loaded = True


class Flexible(object):

    def __init__(self, store_handler, schema_path):
        _Flexible._schema_source = store_handler(schema_path)

    @staticmethod
    def get_module():
        return _Flexible
