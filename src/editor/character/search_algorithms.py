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


def next_id(data):
    return _max_id(data)+1


def _max_id(data):
    max_id = 0
    try:
        if '$id' in data:
            max_id = max(int(data['$id']), max_id)
        if isinstance(data, list):
            for item in data:
                max_id = max(_max_id(item), max_id)
        elif isinstance(data, dict):
            for node in data.values():
                max_id = max(_max_id(node), max_id)
    except TypeError:
        return max_id
    return max_id
