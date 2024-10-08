import random

# Функция для генерации случайных цветов
def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Функция для генерации уникальных случайных цветов
def generate_unique_colors(n):
    colors = set()
    while len(colors) < n:
        color = generate_random_color()
        colors.add(color)
    return list(colors)

# Функция для преобразования времени в десятичный формат
def time_to_decimal(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60

# Функция для разрезания изображения на части для печати на A4
def split_image(image_path, a4_width=3508, a4_height=2480, overlap=75):
    from PIL import Image
    image = Image.open(image_path)
    img_width, img_height = image.size

    cols = (img_width // (a4_width - overlap)) + (1 if img_width % (a4_width - overlap) != 0 else 0)
    rows = (img_height // (a4_height - overlap)) + (1 if img_height % (a4_height - overlap) != 0 else 0)

    # Разрезает изображение на части
    for row in range(rows):
        for col in range(cols):
            left = max(col * (a4_width - overlap), 0)
            upper = max(row * (a4_height - overlap), 0)
            right = min(left + a4_width, img_width)
            lower = min(upper + a4_height, img_height)

            cropped_image = image.crop((left, upper, right, lower))

            # Проверяет ширину и высоту
            if cropped_image.width < cropped_image.height:
                new_image = Image.new("RGB", (a4_width, cropped_image.height), (255, 255, 255))
                new_image.paste(cropped_image, (0, 0))
                cropped_image = new_image

            # Сохраняет каждую часть изображения
            cropped_image.save(f'{image_path.rsplit(".", 1)[0]}_part_{row}_{col}.png')