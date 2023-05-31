

def print_typeVariable(name):

    print(f'el tipo de variable es:{type(name)}')

    print(f'el tipo de variable es:{type(name).__name__}')

def print_input(entrada):

    print(f'El valor ingresado es : {entrada} y el tipo de dato es {type(entrada).__name__}')



if __name__ == '__main__':
    print_typeVariable('PyCharm')
    print("--------")
    print_typeVariable(23)

    entrada = input("escribe un numer o letra")

    print_input(entrada)
