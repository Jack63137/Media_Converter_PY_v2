from video.convert import (
    convert_video,
    extract_audio_from_video,
    change_video_resolution,
    change_video_fps,
    trim_video,
    add_watermark,
    create_gif,
)

def main():
    print("Добро пожаловать в медиаконвертер!")

    print("Выберите действие:")
    print("1. Конвертация аудио")
    print("2. Конвертация видео")
    print("3. Извлечение аудио из видео")
    print("4. Изменение разрешения видео")
    print("5. Изменение частоты кадров видео")
    print("6. Обрезка видео")
    print("7. Добавление водяного знака")
    print("8. Создание GIF")

    choice = input("Введите номер действия: ").strip()

    if choice == '1':
        input_file = input("Введите путь к аудиофайлу: ").strip()
        from audio.convert import convert_audio_batch_with_advanced_options
        convert_audio_batch_with_advanced_options([input_file])
    elif choice == '2':
        input_file = input("Введите путь к видеофайлу: ").strip()
        convert_video(input_file)
    elif choice == '3':
        input_file = input("Введите путь к видеофайлу: ").strip()
        extract_audio_from_video(input_file)
    elif choice == '4':
        input_file = input("Введите путь к видеофайлу: ").strip()
        change_video_resolution(input_file)
    elif choice == '5':
        input_file = input("Введите путь к видеофайлу: ").strip()
        change_video_fps(input_file)
    elif choice == '6':
        input_file = input("Введите путь к видеофайлу: ").strip()
        trim_video(input_file)
    elif choice == '7':
        input_file = input("Введите путь к видеофайлу: ").strip()
        add_watermark(input_file)
    elif choice == '8':
        input_file = input("Введите путь к видеофайлу: ").strip()
        create_gif(input_file)
    else:
        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
