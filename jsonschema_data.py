import jsonschema


def make_validator(schema, default_document, resolver=None):
    if resolver is None:
        resolver = jsonschema.RefResolver.from_schema(schema)
    resolver.store[""] = default_document

    def data_callable(validator_instance, property_value, instance, schema):
        _schema = {}
        for pv in property_value:
            _schema[pv] = validator_instance.resolver.resolve_from_url(property_value[pv])

        for error in validator_instance.descend(instance, _schema):
            yield error

    _mapping = {
        "data": data_callable
    }

    return jsonschema.validators.extend(jsonschema.Draft7Validator, _mapping)(schema, resolver=resolver)


def validate(schema, instance, default_document=None, resolver=None):
    if default_document is None:
        default_document = instance

    validator = make_validator(schema, default_document, resolver=resolver)
    validator.validate(instance)
