from editor.character import stat_info, alignment_info, skills_info
from editor.character.search_algorithms import id_matches, search_recursively


BLUEPRINTS = [
    {'blueprint': '77c11edb92ce0fd408ad96b40fd27121', 'name': 'Linzi'},
    {'blueprint': '5455cd3cd375d7a459ca47ea9ff2de78', 'name': 'Tartuccio'},
    {'blueprint': '54be53f0b35bf3c4592a97ae335fe765', 'name': 'Valerie'},
    {'blueprint': 'b3f29faef0a82b941af04f08ceb47fa2', 'name': 'Amiri'},
    {'blueprint': 'aab03d0ab5262da498b32daa6a99b507', 'name': 'Harrim'},
    {'blueprint': '32d2801eddf236b499d42e4a7d34de23', 'name': 'Jaethal'},
    {'blueprint': 'b090918d7e9010a45b96465de7a104c3', 'name': 'Regongar'},
    {'blueprint': 'f9161aa0b3f519c47acbce01f53ee217', 'name': 'Octavia'},
    {'blueprint': 'f6c23e93512e1b54dba11560446a9e02', 'name': 'Tristian'},
    {'blueprint': 'd5bc1d94cd3e5be4bbc03f3366f67afc', 'name': 'Ekundayo'},
    {'blueprint': '3f5777b51d301524c9b912812955ee1e', 'name': 'Jubilost'},
    {'blueprint': 'f9417988783876044b76f918f8636455', 'name': 'Nok-Nok'},
    {'blueprint': 'ef4e6551044872b4cb99dff10f707971', 'name': 'Dog'},
    {'blueprint': 'a207eff7953731b44acf1a3fa4354c2d', 'name': 'Bear'}
]


class CompanionInfo():
    def __init__(self, party_data, key):
        self._party_data = party_data
        self._key = key
        self.stats = stat_info.StatInfo(self._companion_stats())
        self.alignment = alignment_info.AlignmentInfo(self._alignment_block())
        self.skills = skills_info.SkillsInfo(self._companion_stats())

    def name(self):
        if self._companion()['CustomName']:
            return self._companion()['CustomName']
        c_id = self._companion()['Blueprint']
        val = next((info for info in BLUEPRINTS if info['blueprint'] == c_id))
        return val['name']

    def experience(self):
        return str(self._companion()['Progression']['Experience'])

    def update_experience(self, value):
        if int(self.experience()) != int(value):
            self._companion()['Progression']['Experience'] = int(value)

    def _companion_stats(self):
        stats = self._companion()['Stats']
        if '$id' in stats:
            return stats
        ref = stats['$ref']
        return search_recursively(self._party_data, ref, id_matches)

    def _companion(self):
        return search_recursively(self._party_data, self._key, _key_matches)

    def _alignment_block(self):
        return self._companion()['Alignment']


def _key_matches(data, key):
    try:
        return 'Unit' in data and data['Unit'] == key
    except TypeError:
        return False
