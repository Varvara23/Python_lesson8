import time
import psutil
import os


def show_time(f):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print('Время выполнения операции: {} секунд'.format(end_time - start_time))
    return wrapper


def show_memory(f):

    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        print('Исп. память до вып. функции: ' + str(proc.memory_info().rss / 1000000))
        f(*args, **kwargs)
        proc = psutil.Process(os.getpid())
        print('Исп. память после вып. функции: ' + str(proc.memory_info().rss / 1000000))
    return wrapper


@show_time
@show_memory
def create_list():
    list_ = []
    for i in range(1, 1000000):
        list_.append(i)
    return list_


@show_time
@show_memory
def generate_ob():
    for num in range(1, 1000000):
        yield (num)
    return num

print('Создание списка')
create_list()
print('Генератор')
generate_ob()

