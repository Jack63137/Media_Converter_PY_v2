import os
import ffmpeg
from concurrent.futures import ThreadPoolExecutor

def process_audio_file(input_file, target_format, bitrate, volume, channels, sample_rate, start_time, end_time):
    """
    Обрабатывает один аудиофайл с заданными настройками.
    """
    output_file = input_file.rsplit('.', 1)[0] + f"_processed.{target_format}"
    try:
        print(f"Обработка файла: {input_file} -> {output_file}")
        audio = ffmpeg.input(input_file)

        # Обрезка
        if start_time or end_time:
            audio = audio.filter_('atrim', start=start_time or None, end=end_time or None).filter_('asetpts', 'PTS-STARTPTS')

        # Настройки вывода
        output_args = {}
        if bitrate:
            output_args['audio_bitrate'] = bitrate
        if channels:
            output_args['ac'] = channels
        if sample_rate:
            output_args['ar'] = sample_rate
        if volume:
            audio = audio.filter('volume', volume)

        # Запуск конвертации
        audio.output(output_file, **output_args).run()
        print(f"Файл успешно обработан: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при обработке файла {input_file}: {e}")


def batch_process_audio(files, target_format, bitrate, volume, channels, sample_rate, start_time, end_time):
    """
    Обрабатывает список файлов в многопоточном режиме.
    """
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(
                process_audio_file, file, target_format, bitrate, volume, channels, sample_rate, start_time, end_time
            )
            for file in files
        ]
        for future in futures:
            future.result()


def convert_audio_batch_with_advanced_options(file_paths):
    """
    Пакетная обработка аудиофайлов с пользовательскими настройками.
    """
    print("Выберите формат для конвертации: mp3, wav, flac, ogg, aac, opus, wma, alac, aiff")
    target_format = input("Введите формат: ").strip().lower()

    supported_formats = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'opus', 'wma', 'alac', 'aiff']
    if target_format not in supported_formats:
        print(f"Формат {target_format} не поддерживается. Попробуйте снова.")
        return

    # Настройки
    bitrate = input("Введите желаемый битрейт (например, 128k или 320k, пропустите для значения по умолчанию): ").strip()
    volume = input("Введите изменение громкости (например, +5 для увеличения на 5 дБ, -3 для уменьшения): ").strip()
    channels = input("Введите число каналов (1 для моно, 2 для стерео, пропустите для значения по умолчанию): ").strip()
    sample_rate = input("Введите частоту дискретизации (например, 44100, 48000, пропустите для значения по умолчанию): ").strip()
    start_time = input("Введите время начала обрезки (в секундах, пропустите для начала файла): ").strip()
    end_time = input("Введите время окончания обрезки (в секундах, пропустите для конца файла): ").strip()

    # Пакетная обработка
    print(f"Запуск пакетной обработки файлов: {file_paths}")
    batch_process_audio(file_paths, target_format, bitrate, volume, channels, sample_rate, start_time, end_time)
