def helper():
    from time import sleep
    while True:
        print('\033[0;30;42m', '~' * 30, f'\n{"SISTEMA DE AJUDA PyHELP": ^30}\n', '~' * 30)
        sleep(0.5)
        function_name = str(input('\033[mFunção ou biblioteca > '))
        if function_name.strip().upper() == 'FIM':
            print('\033[0;30;41m', '~' * 20, f'\n{"ATÉ LOGO!": ^20}\n', '~' * 20, )
            break
        else:
            print('\033[0;30;46m', '~' * 40, f'\n{f"Acessando o manual do comando {function_name}": ^40}\n', '~' * 40)
            sleep(0.5)
            print('\033[0;7;30m'), help(function_name), print('\033[m', end='')
            sleep(0.5)


helper()
