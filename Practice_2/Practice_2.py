import matplotlib.pyplot as plt
import numpy as np

# JSON-данные
tablets_compact = [
    {
        "model": "iPad Pro 12.9",
        "screen_size_in": 12.9,
        "ram_gb": 16,
        "storage_gb": 256,
        "battery_mah": 10758,
        "weight_g": 682,
        "stylus_support": True,
    },
    {
        "model": "Samsung Galaxy Tab S9 Ultra",
        "screen_size_in": 14.6,
        "ram_gb": 12,
        "storage_gb": 256,
        "battery_mah": 11200,
        "weight_g": 732,
        "stylus_support": True,
    },
    {
        "model": "Microsoft Surface Pro 9",
        "screen_size_in": 13.0,
        "ram_gb": 16,
        "storage_gb": 512,
        "battery_mah": 5070,
        "weight_g": 891,
        "stylus_support": True,
    },
    {
        "model": "Xiaomi Pad 6",
        "screen_size_in": 11.0,
        "ram_gb": 8,
        "storage_gb": 256,
        "battery_mah": 8840,
        "weight_g": 490,
        "stylus_support": False,
    },
]

# названия характеристик
name_char = [
    "Экран",
    "ОЗУ",
    "Память",
    "Батарея",
    "Вес",
    "Стилус",
]


# 🔹 формирование массива моделей
def get_models(data):
    return [item["model"] for item in data]


# 🔹 преобразование JSON → матрица характеристик
def get_char_matrix(data):
    result = []
    for item in data:
        row = [
            item["screen_size_in"],
            item["ram_gb"],
            item["storage_gb"],
            item["battery_mah"],
            item["weight_g"],
            1 if item["stylus_support"] else 0,
        ]
        result.append(row)
    return result


# 🔹 нормализация (как в примере)
def get_normal(char):
    normal = []
    base = char[0]
    for item in char:
        normal.append([a / b for a, b in zip(item, base)])
    return normal


# 🔹 расчет качества
def get_quality(normal):
    return [round(sum(item) / len(item), 2) for item in normal]


# 🔹 столбчатая диаграмма
def create_bar(name, values):
    plt.bar(name, values)
    plt.xlabel("Модель")
    plt.ylabel("Kту")
    plt.xticks(rotation=15)
    plt.show()


# 🔹 радиальная диаграмма
def create_radial(models, name, values):
    for item in values:
        item += item[:1]

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values)):
        ax.plot(angles, values[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=10)
    ax.set_ylim(0, 2)

    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение планшетов")
    plt.show()


# 🔹 запуск
models = get_models(tablets_compact)
char = get_char_matrix(tablets_compact)

normal = get_normal(char)
quality = get_quality(normal)

create_bar(models, quality)
create_radial(models, name_char, normal)