from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_reverse_for_integer():
    assert reverse(23) == 32
