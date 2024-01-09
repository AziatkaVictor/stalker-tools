import re
import os
from pathlib import Path
from logger import getCustomLogger
import shutil

_log = getCustomLogger(__name__)

class TexturesProvider():
    @classmethod
    def get(self, path: str, formats: list[str], parse: bool = False) -> list[str] | None:
        try:
            with open(Path(path).resolve(), "r", encoding="utf8") as file:
                data = file.read()

            if parse:
                files = re.compile(r"(?<=\!\ Can\'t\ find\ texture\ \').*?(?=\')").findall(data)
                _log.debug(f"Log was parsed")
            else:
                files = data.split("\n")
                _log.debug(f"Programm got list of textures")
            
            result = []
            for file in files:
                result.extend([file + format for format in formats])

            _log.info(f"Amount of textures: {len(files)}")
            _log.info(f"Amount of files: {len(result)}")

            return result
        
        except Exception as error:
            _log.fatal(f"Error while reading: {Path(path).resolve()}\n{error}")
            return

    @classmethod
    def copy(self, data: list[str], input: str, output: str, overwrite: bool = False):
        _log.info(f"Input: {input}")
        _log.info(f"Output: {output}")

        done = 0
        skipped = 0

        if not TexturesProvider._isDirExist(input):
            TexturesProvider._createDirs(input)

        for file in data:
            inputPath = Path(input, file)
            outputPath = Path(output, file)

            if not inputPath.is_file():
                _log.warning(f"Can't find: {inputPath}")
                continue

            outputDirPath = outputPath.parent.resolve()
            
            if not TexturesProvider._isDirExist(outputDirPath):
                TexturesProvider._createDirs(outputDirPath)

            try:
                fileExist = os.path.isfile(outputPath)
                if fileExist and not overwrite:
                    _log.warning(f"File was founded, but it's already exist: {outputPath}")
                    skipped += 1
                    continue

                shutil.copy2(inputPath, outputPath)
                done += 1
                _log.info(f"Done with {file}")
            except:
                _log.fatal(f"Error while copying file: {inputPath}")
        
        _log.info(f"Work is done!")
        _log.info(f"Copied {done}/{len(data)} files")
        _log.info(f"Skipped {skipped}/{len(data)} files")
        
    @classmethod
    def _isDirExist(self, path: str) -> bool:
        if os.path.isdir(path):
            return True
        
        _log.warning(f"Can't find directory by path: {path}")
        return False
    
    @classmethod
    def _createDirs(self, path: str) -> bool:
        try:
            if not path:
                raise ValueError("Path can't be None")
            _path = Path(path)
            _path.mkdir(parents=True)
            _log.debug(f"Directories for {path} is created")
            return True
        except Exception as Error:
            _log.error(f"Can't create directories for {path}\n{Error}")
            return False