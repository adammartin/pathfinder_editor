from editor.character import stat_info, alignment_info, skills_info
from editor.character.search_algorithms import id_matches
from editor.character.search_algorithms import search_recursively
from editor.character.search_algorithms import next_id


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
    {'blueprint': 'a207eff7953731b44acf1a3fa4354c2d', 'name': 'Bear'},
    {'blueprint': 'f1c0b181a534f4940ae17f243a5968ec', 'name': 'Kanerah'},
    {'blueprint': 'c807d18a89f96c74f8bb48b31b616323', 'name': 'Kalikke'}
]


class EntityInfo():
    # pylint: disable=too-few-public-methods
    def __init__(self, party_data, key):
        self._party_data = party_data
        self._key = key
        self._character = self._find_character()
        stats = self._find_stats()
        self.stats = stat_info.StatInfo(stats)
        self.skills = skills_info.SkillsInfo(stats)
        self.alignment = alignment_info.AlignmentInfo(self._alignment_block())

    def name(self):
        if self._character['CustomName']:
            return self._character['CustomName']
        c_id = self._character['Blueprint']
        val = next((info for info in BLUEPRINTS if info['blueprint'] == c_id))
        return val['name']

    def experience(self):
        return str(self._character['Progression']['Experience'])

    def update_experience(self, value):
        if int(self.experience()) != int(value):
            self._character['Progression']['Experience'] = int(value)

    def portrait(self):
        portrait = self._character['UISettings']['m_CustomPortrait']
        try:
            return portrait['m_CustomPortraitId']
        except TypeError:
            return None

    def update_portrait(self, new_portrait):
        portrait = self._character['UISettings']['m_CustomPortrait']
        try:
            portrait['m_CustomPortraitId'] = new_portrait
        except TypeError:
            self._character['UISettings']['m_CustomPortrait'] = {
                '$id': str(next_id(self._party_data)),
                'm_CustomPortraitId': new_portrait
            }

    def _alignment_block(self):
        return self._character['Alignment']

    def _find_character(self):
        pass

    def _find_stats(self):
        stats = self._character['Stats']
        if '$id' in stats:
            return stats
        ref = stats['$ref']
        return search_recursively(self._party_data, ref, id_matches)
