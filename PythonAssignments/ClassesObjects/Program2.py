def outer():
    def inner():
        return "Hello, I'm in the inner function!"

    return inner

ans = outer()
print(ans)

