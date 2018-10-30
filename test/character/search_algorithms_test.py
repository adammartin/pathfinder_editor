import pytest
from editor.character.search_algorithms import id_matches, search_recursively


def test_id_matches_exact():
    data = {'$id': '2'}
    assert id_matches(data, data['$id'])


def test_id_matches_no_id():
    data = {'blarg': '2'}
    assert not id_matches(data, data['blarg'])


def test_id_does_not_match():
    data = {'$id': '2'}
    ref = str(int(data['$id'])+1)
    assert not id_matches(data, ref)


def test_none_is_not_match_and_does_not_error():
    assert not id_matches(None, '2')


def test_empty_is_not_match_and_does_not_error():
    assert not id_matches({}, '2')


def test_non_iterable_data_type_is_not_match_and_does_not_error():
    assert not id_matches(2.14376, '2')


def test_list_is_not_match_and_does_not_error():
    data = [{'$id': '2'}, {'$id': '3'}]
    assert not id_matches(data, '2')


expected_key = 1234
expected_node = {'match': expected_key}


def example_algorithm(data, key):
    try:
        return 'match' in data and data['match'] == key
    except TypeError:
        return False


def test_top_node_match():
    result = search_recursively(expected_node, expected_key, example_algorithm)
    assert result == expected_node


def test_no_match():
    data = {'blah': ['blarg', {'foo': 'bar'}]}
    result = search_recursively(data, expected_key, example_algorithm)
    assert result == None


def test_in_array_match():
    data = ['blarg', {'foo': 'bar'}, expected_node]
    result = search_recursively(data, expected_key, example_algorithm)
    assert result == expected_node


def test_in_dict_match():
    data = {'blah': expected_node}
    result = search_recursively(data, expected_key, example_algorithm)
    assert result == expected_node


def test_deeply_nested_match():
    data = {'blah': ['blarg', None, {'foo': ['jar', {'blob': expected_node}]}]}
    result = search_recursively(data, expected_key, example_algorithm)
    assert result == expected_node
