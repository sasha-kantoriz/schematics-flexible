# -*- coding: utf-8 -*-

from schematics.types import StringType
from schematics.types.compound import DictType, BaseType
from schematics.models import Model
from schematics.exceptions import ValidationError as schematicsValidationError


class Flexible(Model):
    """ Save code, version and props of schema """

    __slots__ = []

    _loaded = False
    _schema_source = None

    version = StringType()
    code = StringType(max_length=10)
    properties = DictType(BaseType, default=dict)

    def __init__(self, raw_data=None, deserialize_mapping=None,
                 strict=True, store_handler=None):
        super(Flexible, self).__init__(
            raw_data, deserialize_mapping, strict)
        if store_handler:
            self._schema_source = store_handler

    def validate(self, *args, **kwargs):
        """ Try find json schema and validate it with properties """
        if not self._loaded:
            self._load_schemas()
        try:
            schema_tuple = self._schema_source.get_schema(self.code,
                                                          self.version)
        except self._schema_source.import_exception as error:
            raise schematicsValidationError(error.message)
        if schema_tuple:
            try:
                schema_tuple.schema.validate(self.properties)
            except self._schema_source.validation_exception as error:
                raise schematicsValidationError(error.message)
            else:
                self.code = schema_tuple.code
                self.version = schema_tuple.version
        super(Flexible, self).validate(*args, **kwargs)

    def _load_schemas(self):
        """ Load schemas from _schema_source """
        self._schema_source.load()
        self._loaded = True

