# Функция для сортировки порядка вывода на страницу
def ordering(request, obj):
    ordering_keys = list(obj.keys())

    # Проверка GET данных из чекбоксов в форме сортировки
    for i in range(len(ordering_keys)):
        if request.GET.get('ordering__' + ordering_keys[i]) == 'on':
            ordering_keys[i] = '-' + ordering_keys[i]

    return ordering_keys
