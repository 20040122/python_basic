def login(username, password):
    if username == 'admin' and password == '123456':
        return '登陆成功'
    else:
        return '登陆失败'