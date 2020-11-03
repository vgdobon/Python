# global
text = 'this is a global variable'
def justprint():
    print(1, text)  # se puede "leer" la global sin problema
justprint()


def my_func():
    def enclosing():
        # local
        text = 'this is a local variable'
        print(3, text)
    
    global text  # podremos leer y modificar la global
    print(2, text)
    enclosing()
    print(10,text)
    text = "modified"
    print(5, text)
 
my_func()
print(6, text)