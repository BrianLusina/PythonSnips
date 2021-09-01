from typing import Dict, List


def name_list(names: List[Dict]):
    if len(names) > 1:
        return f"{', '.join(name['name'] for name in names[:-1])} & {names[-1]['name']}"
    elif names:
        return names[0]['name']
    else:
        return ''
