import argparse

parser = argparse.ArgumentParser(description="Мой первый скрипт")
parser.add_argument("name", help="Ваше имя")
args = parser.parse_args()
print(f"Привет, {args.name}!")