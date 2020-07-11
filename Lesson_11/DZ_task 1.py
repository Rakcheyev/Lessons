
def outer_func(a):     # глобальная область видимости
    ''' Продемонструвати:1. Що таке замикання на прикладі вкладеної функції '''

    def inner_func(b): # локальная область
        return a * b
        
    return inner_func
    
new_func = outer_func(2) # при передаче значения во внешнюю - вложенная запоминает его
print(new_func.__name__) # показал что возвращает новая при ссылке на внешнюю

print(new_func(10)) # перемножили значение из аргумента, на то что хранится во внутренней (сборищик ее не трогает)
