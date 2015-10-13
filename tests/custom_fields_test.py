from zendesk.custom_fields import CustomFields


def test_example():
    name = 'Jonh Tdd'
    number = 100
    kwargs = {'custom_name': name, 'custom_number': number}
    custom_fields = CustomFields(**kwargs)
    assert custom_fields.custom_name == name
    assert custom_fields.custom_number == number
    assert not custom_fields.other_value
