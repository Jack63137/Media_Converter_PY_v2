import ffmpeg

def convert_video(input_file):
    """
    Конвертация видео между форматами.
    """
    print("Выберите формат для конвертации: mp4, mkv, avi, mov, webm")
    target_format = input("Введите формат: ").strip().lower()

    supported_formats = ['mp4', 'mkv', 'avi', 'mov', 'webm']
    if target_format not in supported_formats:
        print(f"Формат {target_format} не поддерживается. Попробуйте снова.")
        return

    output_file = input_file.rsplit('.', 1)[0] + f"_converted.{target_format}"

    try:
        print(f"Конвертация видео в {target_format}...")
        ffmpeg.input(input_file).output(output_file).run()
        print(f"Видео успешно конвертировано: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при конвертации: {e}")


def extract_audio_from_video(input_file):
    """
    Извлечение аудио из видео.
    """
    output_file = input_file.rsplit('.', 1)[0] + "_audio.mp3"

    try:
        print("Извлечение аудио из видео...")
        ffmpeg.input(input_file).output(output_file, format='mp3').run()
        print(f"Аудио успешно извлечено: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при извлечении аудио: {e}")


def change_video_resolution(input_file):
    """
    Изменение разрешения видео.
    """
    width = input("Введите ширину видео (например, 1280): ").strip()
    height = input("Введите высоту видео (например, 720): ").strip()

    if not width.isdigit() or not height.isdigit():
        print("Ширина и высота должны быть числовыми значениями.")
        return

    output_file = input_file.rsplit('.', 1)[0] + f"_{width}x{height}.mp4"

    try:
        print(f"Изменение разрешения видео на {width}x{height}...")
        ffmpeg.input(input_file).output(output_file, vf=f"scale={width}:{height}").run()
        print(f"Разрешение успешно изменено: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при изменении разрешения: {e}")

def change_video_fps(input_file):
    """
    Изменение частоты кадров (FPS) видео.
    """
    fps = input("Введите желаемую частоту кадров (например, 30 или 60): ").strip()

    if not fps.isdigit():
        print("Частота кадров должна быть числом.")
        return

    output_file = input_file.rsplit('.', 1)[0] + f"_{fps}fps.mp4"

    try:
        print(f"Изменение частоты кадров видео на {fps} FPS...")
        ffmpeg.input(input_file).output(output_file, r=fps).run()
        print(f"Частота кадров успешно изменена: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при изменении частоты кадров: {e}")


def trim_video(input_file):
    """
    Обрезка видео по времени.
    """
    start_time = input("Введите время начала (в секундах): ").strip()
    end_time = input("Введите время окончания (в секундах): ").strip()

    # Проверка корректности введенных данных
    if not start_time.isdigit() or not end_time.isdigit():
        print("Время начала и окончания должно быть числом.")
        return

    start_time = int(start_time)
    end_time = int(end_time)

    if start_time >= end_time:
        print("Ошибка: Время окончания должно быть больше времени начала.")
        return

    output_file = input_file.rsplit('.', 1)[0] + f"_trimmed_{start_time}-{end_time}.mp4"

    try:
        print(f"Обрезка видео с {start_time} до {end_time} секунд...")
        ffmpeg.input(input_file, ss=start_time, to=end_time).output(output_file).run()
        print(f"Видео успешно обрезано: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при обрезке видео: {e}")


def add_watermark(input_file):
    """
    Добавление водяного знака к видео.
    """
    watermark_file = input("Введите путь к изображению для водяного знака: ").strip()
    position = input("Введите позицию водяного знака (top-left, top-right, bottom-left, bottom-right): ").strip().lower()

    # Проверяем существование файлов
    if not os.path.isfile(input_file):
        print(f"Файл {input_file} не найден.")
        return
    if not os.path.isfile(watermark_file):
        print(f"Файл водяного знака {watermark_file} не найден.")
        return

    # Позиции водяного знака
    overlay_positions = {
        "top-left": "10:10",
        "top-right": "main_w-overlay_w-10:10",
        "bottom-left": "10:main_h-overlay_h-10",
        "bottom-right": "main_w-overlay_w-10:main_h-overlay_h-10"
    }

    if position not in overlay_positions:
        print("Ошибка: Неверная позиция. Допустимые значения: top-left, top-right, bottom-left, bottom-right.")
        return

    output_file = input_file.rsplit('.', 1)[0] + "_watermarked.mp4"

    try:
        print(f"Добавление водяного знака в позицию {position}...")
        ffmpeg.input(input_file).output(
            output_file,
            vf=f"movie={watermark_file} [wm]; [in][wm] overlay={overlay_positions[position]} [out]"
        ).run()
        print(f"Водяной знак успешно добавлен: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при добавлении водяного знака: {e}")



def create_gif(input_file):
    """
    Создание GIF из видео.
    """
    start_time = input("Введите время начала (в секундах): ").strip()
    duration = input("Введите длительность GIF (в секундах): ").strip()

    if not start_time.isdigit() or not duration.isdigit():
        print("Время начала и длительность должны быть числами.")
        return

    output_file = input_file.rsplit('.', 1)[0] + ".gif"

    try:
        print(f"Создание GIF с {start_time} на {duration} секунд...")
        ffmpeg.input(input_file, ss=start_time, t=duration).output(output_file, vf="fps=15,scale=320:-1").run()
        print(f"GIF успешно создан: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при создании GIF: {e}")
