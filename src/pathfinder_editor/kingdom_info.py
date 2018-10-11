from entity_info import EntityInfo
from file_utils import save_json


class KingdomInfo(EntityInfo):
    # pylint: disable=too-many-public-methods
    def has_kingdom_data(self):
        return "Kingdom" in self._json(self._player_json_name)

    def build_points(self):
        data = self._json(self._player_json_name)
        if "Kingdom" in data:
            return str(data["Kingdom"]["BP"])
        return "No Kingdom"

    def update_build_points(self, value):
        data = self._json(self._player_json_name)
        if self.has_kingdom_data() and data["Kingdom"]["BP"] != int(value):
            data["Kingdom"]["BP"] = int(value)
            save_json(self._temp_path, self._player_json_name, data)


def _kingdom(data):
    return data["Kingdom"]
