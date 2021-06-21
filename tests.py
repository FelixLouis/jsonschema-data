import jsonschema_data

schema1 = {
  "$schema": "https://gregsdennis.github.io/json-everything/meta/data",
  "type": "object",
  "properties": {
    "foo": {
      "type": "integer",
      "data": {
        "minimum": "#/minValue"
      }
    },
    "minValue": {
      "type": "integer"
    }
  },
  "dependentRequired": {
    "foo": ["minValue"]
  }
}

passing_instance = {
  "minValue": 5,
  "foo": 10
}

failing_instance = {
  "minValue": 15,
  "foo": 10
}

jsonschema_data.validate(schema1, passing_instance)
jsonschema_data.validate(schema1, failing_instance)
