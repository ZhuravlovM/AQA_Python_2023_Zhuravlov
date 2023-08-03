def function_name(func):
    def title(*args, **kwargs):
        print(f"Використовую функцію: {func.__name__}")
        return func(*args, **kwargs)
    return title


@function_name
def summ(a, b):
    return a + b


@function_name
def subtrack(a, b):
    return a - b


print(summ(3, 4))

print(subtrack(99, 50))
