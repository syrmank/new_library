try:
    import colorama

    version = getattr(colorama, '__version__', 'unknown')
    print(version)

    if version == "0.4.4":
        colorama.init()
        print(colorama.Fore.GREEN + "Установлена корректная версия 'colorama'")
    elif version == "0.4.6":
        colorama.init()
        print(colorama.Fore.RED + "Установлена некорректная версия 'colorama'")

except ImportError:
    print(" Библиотека 'colorama' не установлена!")
    print(" Установите: pip install colorama==0.4.4")