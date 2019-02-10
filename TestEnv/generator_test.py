def first_func():
    for i in range(10):
        print(f'1 step {i+1}')


def second_func():
    for i in range(10):
        print(f'2 step {i+1}')


def third_func():
    for i in range(10):
        print(f'3 step {i+1}')


def generator():
    print('START')
    yield first_func()
    print('first_func finished')
    yield second_func()
    print('second_func finished')
    yield third_func()
    print('third_func finished')
    print('THE END')


gen = generator()

while True:
    try:
        gen.__next__()
    except StopIteration:
        break
