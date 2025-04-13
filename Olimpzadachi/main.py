a = [1, 2, 3, "4"]
b = 5


def func(a: list) -> int | None:
    for i in a:
        if not isinstance(i, int):
            raise ValueError("Ошибка")
    if a and len(a) > 1:
        max1 = max(a)
        a.remove(max1)
        return max(a)
    return None


print(func(a))
