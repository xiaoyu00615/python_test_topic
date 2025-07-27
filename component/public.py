def hello():
    print('Hello-模块-public')


def message(mes,num = 3):
    if num > 2:
        return

    print(f'你好{mes}')

    new_message("新人你好")

def new_message(name):
    print(f"{name}:新消息来啦！！")

