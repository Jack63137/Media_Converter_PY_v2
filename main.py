from audio.convert import convert_audio_with_advanced_options

def main():
    print("Добро пожаловать в медиаконвертер!")
    input_file = input("Введите путь к аудиофайлу: ").strip()

    # Запуск функции с расширенными настройками
    convert_audio_with_advanced_options(input_file)

if __name__ == "__main__":
    main()
