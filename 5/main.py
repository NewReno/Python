import file_operations
from faker import Faker
import random
import os

fake = Faker("ru_RU")

runic_skills = []

def transform_string(letter):
    for key, value in letter_mapping.items():
        letter = letter.replace(key, value)
    return letter

letter_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

skills = ["Стремительный прыжок",
"Электрический выстрел",
"Ледяной удар",
"Стремительный удар",
"Кислотный взгляд",
"Тайный побег",
"Ледяной выстрел",
"Огненный заряд"
]

def main():
    for i in range(10):
        runic_skills = [transform_string(skill) for skill in skills]
        runic_skills  = random.sample(runic_skills , k=3)

        chars = {
            "first_name" : fake.first_name_female(),
            "last_name" : fake.last_name_female(),
            "job" : fake.job(),
            "town" : fake.city(),
            "strength" : random.randint(3, 18),
            "agility" : random.randint(3, 18),
            "endurance" : random.randint(3, 18),
            "intelligence" : random.randint(3, 18),
            "luck" : random.randint(3, 18),
            "skill_1" : runic_skills [0],
            "skill_2" : runic_skills [1],
            "skill_3" : runic_skills [2]
        }

        output_dir = "5/output/svg/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        filename = f"{output_dir}character_{i+1}.svg"
        file_operations.render_template("5/src/charsheet.svg", filename, chars)
        print(f"Сохранено в файл: {filename}")

if __name__ == "__main__":
    main()