from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import json, io, os

def extract_file(path, temp_dir_path):
    if path.is_file():
        with ZipFile(str(path.resolve()), 'r') as save_zip:
            save_zip.extractall(path=str(temp_dir_path.resolve()))

def load_json(dir_path, file_name):
    contents = io.open(full_path(dir_path, file_name), 'r', encoding='utf-8-sig').read()
    return json.loads(contents)

def save_json(dir_path, file_name, contents):
    with io.open(full_path(dir_path, file_name), 'w', encoding='utf-8-sig') as json_file:
        json.dump(contents, json_file)

def full_path(dir_path, file_name):
    return str((dir_path / file_name).resolve())

def persist_as_zip(save_root, save_file, directory_path):
    zip_path = full_path(save_root, save_file)
    _zipdir(directory_path, zip_path)

def _zipdir(dirPath, zipFilePath):
    if not os.path.isdir(dirPath):
        raise OSError("dirPath argument must point to a directory. "
            "'%s' does not." % dirPath)
    parentDir, dirToZip = os.path.split(dirPath)

    def trimPath(path):
        archivePath = path.replace(parentDir, "", 1)
        archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
        return os.path.normcase(archivePath)

    outFile = ZipFile(zipFilePath, "w", compression=ZIP_DEFLATED)
    for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
        for fileName in fileNames:
            filePath = os.path.join(archiveDirPath, fileName)
            outFile.write(filePath, trimPath(filePath))
        if not fileNames and not dirNames:
            zipInfo = ZipInfo(trimPath(archiveDirPath) + "/")
            outFile.writestr(zipInfo, "")
    outFile.close()
