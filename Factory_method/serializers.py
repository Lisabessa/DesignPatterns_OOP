import json
import xml.etree.ElementTree as et


class ObjectSerializer:  # client - the part of the code that depends on the interface
    def serialize(self, serializable, format):
        factory = SerializerFactory()
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


class SerializerFactory:  # creator - the part of the code that decides which specific implementation to use
    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            return DefaultSerializer()


class JsonSerializer:  # product - defined interface
    def __init__(self):
        self._report = None

    def start_object(self, object_name, object_id):
        self._report = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._report[name] = value

    def to_str(self):
        return json.dumps(self._report)


class XmlSerializer:  # product - defined interface
    def __init__(self):
        self._report = None

    def start_object(self, object_name, object_id):
        self._report = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        property = et.SubElement(self._report, name)
        property.text = value

    def to_str(self):
        return et.tostring(self._report, encoding='unicode')


class DefaultSerializer:  # product - defined interface
    def __init__(self):
        self._report = None

    def start_object(self, object_name, object_id):
        self._report = "| id: " + object_id + " | "

    def add_property(self, name, value):
        self._report += name + ": " + value + " | "

    def to_str(self):
        return self._report