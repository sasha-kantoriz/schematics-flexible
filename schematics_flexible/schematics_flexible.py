# -*- coding: utf-8 -*-

from schematics.types import StringType
from schematics.models import Model
from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError as jsonschemaValidationError
from schematics.exceptions import ValidationError as schematicsValidationError


class Flexible(Model):
    """ Save code, version and props of schema """

    _loaded = False
    _schema_dist = None

    version = StringType()
    code = StringType(max_length=10)
    properties = StringType()

    def __init__(self, *args, schema_source, **kwargs):
        """ Save schema source """
        super(Flexible, self).__init__(*args, **kwargs)
        self._schema_source = schema_source

    def validate(self, partial=False, strict=False):
        """ Get schema and validate """
        if not self._loaded:
            self._load_schemas()
        schema = self._schema_dist.find(self.code, self.version)
        if schema:
            try:
                Draft4Validator(schema).validate(self.properties)
            except jsonschemaValidationError as error:
                raise schematicsValidationError(error.message)
        super(Flexible, self).validate()

    def _load_schemas(self):
        """ Load all schemas from source to dist """
        self._schema_dist = self._schema_source.load()
        self._loaded = True
