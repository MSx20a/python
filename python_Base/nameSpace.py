# python的LEGB rule
# 1.先檢查是否有符合的local namespace
# 2.次檢查是否有符合的global namespace
# 3.再檢查是否有符合的built-in namespace
# 4.都沒找到符合的，會跳出error

import sys
print(__builtins__)  # is object
print(dir(__builtins__))
# 以下是built-in namespace的所有東西，並用list的方式回傳
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
# 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis',
# 'EnvironmentError', 'Exception', 'False', 'FileExistsError',
# 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit',
# 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
# 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
# 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
# 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
# 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
# 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
# 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
# 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__',
# '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii',
# 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile',
# 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
# 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help',
# 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
# 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
# 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str',
# 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
print("-----------------------")

x = 10


def test():
    x = 5
    z = 20
    print(locals())  # 會以dict的方式回傳local namespace
    print((x, z))


test()
print(globals())  # 會以dict的方式回傳global namespace
