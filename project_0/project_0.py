import numpy as np


def game_core(number):
    """Функция принимает загаданное компьютером число, угадывает его
    и возвращает кол-во попыток угадывания.

    Args:
        number (int): загаданное компьютером число

    Returns:
        int: кол-во попыток угадать число
    """
    bottom = 0
    up = 101
    count = 1

    
    predict = (up-bottom) // 2 
    while number != predict:
        count += 1
        if number > predict:
            bottom = max(bottom, predict) 
            predict += (up-predict) // 2
        else: 
            up = min(up, predict)
            predict -= (predict-bottom) // 2
            
    return count


def score_game(game_core):
    """Функция запускает игру 1000 раз и смотрит среднее кол-во попыток угадывания

    Args:
        game_core: функция угадывания числа

    Returns:
        int: среднее количество попыток, за которое угадывается число
    """
    count_ls = []
    
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(game_core(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Проверяем запуск игры 1000 раз
if __name__ == '__main__':
    score_game(game_core)