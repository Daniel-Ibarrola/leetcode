import pprint

registry: dict[str, int] = {}


class EnforceUppercase(type):
    def __new__(cls, name, bases, attrs):
        # 'attrs' is a dictionary of the class's attributes and methods
        uppercase_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith("__"):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value

        # Create the class using the modified attributes
        return super().__new__(cls, name, bases, uppercase_attrs)


class AddToRegister(type):
    def __new__(cls, name, bases, attrs):
        registry[name] = registry.get(name, 0) + 1
        return super().__new__(cls, name, bases, attrs)


# Use the metaclass
class MyConfig(metaclass=EnforceUppercase):
    setting = "value"
    another_setting = 123


class AnotherClass(metaclass=AddToRegister):
    config = "config"


if __name__ == "__main__":
    # The attributes are now uppercase, even though we defined them in lowercase.
    print(hasattr(MyConfig, "setting"))  # Output: False
    print(hasattr(MyConfig, "SETTING"))  # Output: True
    print(MyConfig.ANOTHER_SETTING)  # Output: 123

    my_instance = AnotherClass()

    pprint.pprint(registry)
