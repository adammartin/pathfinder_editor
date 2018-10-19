from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from shutil import rmtree
from pathlib import Path
import json
import io
import os
import time


def save_game_file(file_name, temp_path):
    save_root = Path(file_name).parent
    save_file = str(int(round(time.time() * 1000))) + ".zks"
    persist_as_zip(save_root, save_file, temp_path)


def extract_file(path, temp_dir_path):
    if path.is_file():
        with ZipFile(str(path.resolve()), 'r') as save_zip:
            save_zip.extractall(path=str(temp_dir_path.resolve()))


def load_json(dir_path, file_name):
    path = full_path(dir_path, file_name)
    contents = io.open(path, 'r', encoding='utf-8-sig').read()
    return json.loads(contents)


def save_json(dir_path, file_name, contents):
    path = full_path(dir_path, file_name)
    with io.open(path, 'w', encoding='utf-8-sig') as json_file:
        json.dump(contents, json_file)


def full_path(dir_path, file_name):
    return str((dir_path / file_name).resolve())


def persist_as_zip(save_root, save_file, directory_path):
    zip_path = full_path(save_root, save_file)
    _zipdir(directory_path, zip_path)


def _zipdir(dir_path, zip_file_path):
    if not os.path.isdir(dir_path):
        message = "dir_path argument must point to a directory. '%s' does not."
        raise OSError(message % dir_path)
    parent_dir, dir_to_zip = os.path.split(dir_path)

    def trim_path(path):
        archive_path = path.replace(parent_dir, "", 1)
        archive_path = archive_path.replace(dir_to_zip + os.path.sep, "", 1)
        return os.path.normcase(archive_path)

    out_file = ZipFile(zip_file_path, "w", compression=ZIP_DEFLATED)
    for (archive_dir_path, dir_names, file_names) in os.walk(dir_path):
        for file_name in file_names:
            file_path = os.path.join(archive_dir_path, file_name)
            out_file.write(file_path, trim_path(file_path))
        if not file_names and not dir_names:
            file_info = ZipInfo(trim_path(archive_dir_path) + "/")
            out_file.writestr(file_info, "")
    out_file.close()


def clean_temp_storage(path):
    if path.exists():
        rmtree(path)
