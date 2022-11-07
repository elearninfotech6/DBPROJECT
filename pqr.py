def abc():
    yield 'ja'
    yield  'py'
    yield 'test'
x=abc()
for i in x:
    print(i)
