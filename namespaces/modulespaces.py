def test_function():
    b = "Я в объемлющей области видимости функции test_function"
    def inner_function():
        nonlocal b
        b = "Я в локальной области видимости функции test_function"

    inner_function()
    print(b)
    return b

test_function()

def test_function():
    b = "Я в объемлющей области видимости функции test_function"
    def inner_function():
        b = "Я в локальной области видимости функции test_function"

    inner_function()
    print(b)
    return b

test_function()


b = "Я в глобальной области видимости функции test_function"
def test_function():
    def inner_function():
        b = "Я в локальной области видимости функции test_function"

    inner_function()
    print(b)
    return b

test_function()