i = int(input("введите номер задачи от 1 до 10: "))
if 1 <= i <= 10:
    exec(f'import {i}.py') 
else:
    print("Пожалуйста, введите число от 1 до 10.")

exit_program = str(input("введите q для выхода из программы: "))
if exit_program == 'q':
    exit()