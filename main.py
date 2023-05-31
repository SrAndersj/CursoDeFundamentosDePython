

def print_full_name(name,last_name):
    full_name = name + ' '+ last_name

    print(full_name)

def print_full_name_format(name,last_name):

    template ="hola , mi nombre es {} y mis apellidos son {}".format(name,last_name)
    print(template)
    print("#-------")
    template = f'hola soy {name} usando f form'
    print(template)


if __name__ == '__main__':
    print_full_name('nicolas','Molina Monroy')
    print("---")
    print_full_name_format('Nicolas', 'Molina Monroy')

