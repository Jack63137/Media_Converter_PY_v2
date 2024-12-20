import ffmpeg

def convert_audio_with_advanced_options(input_file):
    """
    Конвертирует аудиофайл с расширенными пользовательскими настройками.
    """
    print("Выберите формат для конвертации: mp3, wav, flac, ogg, aac, opus, wma, alac, aiff")
    target_format = input("Введите формат: ").strip().lower()

    supported_formats = ['mp3', 'wav', 'flac', 'ogg', 'aac', 'opus', 'wma', 'alac', 'aiff']
    if target_format not in supported_formats:
        print(f"Формат {target_format} не поддерживается. Попробуйте снова.")
        return

    # Битрейт
    bitrate = input("Введите желаемый битрейт (например, 128k или 320k, пропустите для значения по умолчанию): ").strip()

    # Изменение громкости
    volume = input("Введите изменение громкости (например, +5 для увеличения на 5 дБ, -3 для уменьшения): ").strip()

    # Число каналов
    channels = input("Введите число каналов (1 для моно, 2 для стерео, пропустите для значения по умолчанию): ").strip()

    # Частота дискретизации
    sample_rate = input("Введите частоту дискретизации (например, 44100, 48000, пропустите для значения по умолчанию): ").strip()

    # Обрезка
    start_time = input("Введите время начала обрезки (в секундах, пропустите для начала файла): ").strip()
    end_time = input("Введите время окончания обрезки (в секундах, пропустите для конца файла): ").strip()

    # Формируем имя выходного файла
    output_file = input_file.rsplit('.', 1)[0] + f"_advanced.{target_format}"

    try:
        print(f"Конвертация в {target_format} с расширенными настройками...")
        audio = ffmpeg.input(input_file)

        # Обрезка
        if start_time or end_time:
            audio = audio.filter_('atrim', start=start_time or None, end=end_time or None).filter_('asetpts', 'PTS-STARTPTS')

        # Применяем настройки
        output_args = {}
        if bitrate:
            output_args['audio_bitrate'] = bitrate
        if channels:
            output_args['ac'] = channels
        if sample_rate:
            output_args['ar'] = sample_rate
        if volume:
            audio = audio.filter('volume', volume)

        # Вывод
        audio.output(output_file, **output_args).run()
        print(f"Файл успешно конвертирован: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка при конвертации: {e}")
