import re
import json
import os
from pathlib import Path
import shutil
from utils import *


def copy_textures(args):
    list = args.file
    parse = args.parse
    overwrite = args.overwrite

    settings = json.load(open('settings.json', "r", encoding="utf8"))

    showInfo(f"Путь откуда будут копироваться файлы: {settings['input']}")
    showInfo(f"Путь куда будут копироваться файлы: {settings['output']}")
    showInfo(f"Файл, откуда берем список текстур: {list}")

    try:
        if parse:
            temp = open(Path(list).resolve(), "r", encoding="utf8").read()
            data = re.compile(r"(?<=\!\ Can\'t\ find\ texture\ \').*?(?=\')").findall(temp)
            files = [[x + t for t in settings["file_types"]] for x in data]
            showInfo(f"Лог был проанализирован. Количество текстур: {len(files)}\n")
        else:
            files = [[x + t for t in settings["file_types"]] for x in open(Path(list).resolve(), "r").read().split("\n")]
            showInfo(f"Программа взяла заготовленный список. Количество текстур: {len(files)}\n")
    except AttributeError as Error:
        showCriticalError(f"Ошибка при попытки чтения файла: {Path(list).resolve()}")
        showCriticalError(Error)
        return
    except:
        showCriticalError(f"Ошибка при попытки чтения файла: {Path(list).resolve()}")
        return

    result = 0
    skip = 0

    if not os.path.isdir(settings["input"]):
        showCriticalError(f"Не удалось найти папку: {settings['input']}")
        return

    for array in files:
        count = 1

        for file in array:
            inputPath = Path(settings["input"], file)
            outputPath = Path(settings["output"], file)

            if not inputPath.is_file():
                showWarning(f"Не удалось найти {inputPath}")
                if count != 1:
                    continue
                else:
                    break
            if not os.path.isdir(outputPath.parent.resolve()):
                try:
                    os.makedirs(outputPath.parent.resolve(), exist_ok=True)
                    showSuccess(f"Удачное создание папки: {outputPath.parent.resolve()}")
                except:
                    showError(f"Ошибка создания папок для копирования! Возможно, необходимо запустить программу от имени администратора!")
                    return

            try:
                if overwrite or (not overwrite and not os.path.isfile(outputPath)):
                    shutil.copy2(inputPath, outputPath)
                    showSuccess(f"Удачное копирование файла: {outputPath}")
                    result += 1
                else:
                    showWarning(f"Файл найден, однако уже существует в папке: {outputPath}")


                count += 1
            except:
                showError(f"Ошибка копирования файла: {inputPath}")
    
    print()
    showSuccess(f"Работа завершена!")
    showInfo(f"Скопировано {result} из {len(files)} файлов.")
    showInfo(f"Пропущено {skip} из {len(files)} файлов.")

    if not overwrite:
        showInfo(f"Чтобы перезаписывать файлы в папке, а не пропускать их, запусти программу с ключом -overwrite.")
