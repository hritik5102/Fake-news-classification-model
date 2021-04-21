import os
_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data_path(path):
    return os.path.join(_ROOT, 'checkpoint', path)


print(get_data_path('tokenizer.pickle'))

# print(__file__)
# x = os.path.dirname(__file__)
# print(x)
# print(os.path.dirname(x))
# print(os.path.abspath(x))
# print()
