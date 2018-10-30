def search_recursively(data, key, match_logic):
    if match_logic(data, key):
        return data
    if isinstance(data, list):
        for node in data:
            result = search_recursively(node, key, match_logic)
            if match_logic(result, key):
                return result
    elif isinstance(data, dict):
        for node in data.values():
            result = search_recursively(node, key, match_logic)
            if match_logic(result, key):
                return result
    return None


def id_matches(data, ref):
    try:
        return '$id' in data and data['$id'] == ref
    except TypeError:
        return False
