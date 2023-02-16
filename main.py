import os
from texture_copier import copy_textures
from utils import *
import argparse


if __name__ == "__main__":
    os.system('color')

    # Указываем аргументы для работы
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Команды')
    parser.add_argument("-no_errors", required=False, dest = "no_errors", action='store_true', help="Отключить показ ошибок")
    parser.add_argument("-silent", required=False, dest = "silent", action='store_true', help="Отключить показ сообщений во время процесса")

    textures = subparsers.add_parser('textures', help='Копирование текстур')
    textures.add_argument("-file", required=True, dest = "file", type=str, help="Путь к текстовому файлу")
    textures.add_argument("-overwrite", required=False, dest = "overwrite", action='store_true', help="Перезаписывать текстуру, если она уже находиться в папке")
    textures.add_argument("-parse", required=False, dest = "parse", action='store_true', help="Анализировать файл, чтобы программа сама нашла недостающие текстуры")
    textures.set_defaults(func = copy_textures)

    args = parser.parse_args()

    # Вывод сообщения о том, что мы отключили вывод определённого типа сообщений
    if args.no_errors:
        setNoErrors(args.no_errors)
        showInfo(f"Найден ключ -no_errors, ошибки не будут показываться.")
    if args.silent:
        setSilent(args.silent)
        showInfo(f"Найден ключ -silent, отключаем вывод сообщений.")
        
    args.func(args)