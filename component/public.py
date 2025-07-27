def hello():
    print('Hello-模块-public')


def message(mes: str, num: int = 1) -> None:
    if num <= 2:
        print(f'你好{mes}')


