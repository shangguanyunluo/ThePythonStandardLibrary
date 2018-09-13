def dump(expression):
    result = eval(expression)
    print(expression, "=>", result, "--", type(expression))


dump("1")
dump("1.0")
dump("'string'")
dump("'*' * 10")
dump("len('world')")

print('-' * 20)

print eval("__import__('os').getcwd()")
# print eval("__import__('os').remove('file')")
print eval("__import__('os').remove('file')", {"__builtins__": {}})
