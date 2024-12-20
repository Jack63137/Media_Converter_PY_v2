import ffmpeg

def convert_audio(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file).run()
        print(f"Файл успешно конвертирован: {output_file}")
    except ffmpeg.Error as e:
        print(f"Ошибка: {e}")

# Укажи путь к тестовому файлу
convert_audio('input.mp3', 'output.wav')
