def hello():
    print('Hello-模块-public')


def message(mes: str, num: int = 1) -> None:
    if num <= 2:
        print(f'你好{mes}')
        new_message("新人你好")

def new_message(name):
    print(f"{name}:新消息来啦！！")

