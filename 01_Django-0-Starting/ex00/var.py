def my_var() :
    myvar1 = 42
    myvar2 = "42"
    myvar3 = "quarante-deux"
    myvar4 = 42.0
    myvar5 = True
    myvar6 = [42]
    myvar7 = {42: 42}
    myvar8 = (42,)
    myvar9 = set();
    print( myvar1, " has a type " , type(myvar1)) 
    print( myvar2, " has a type " , type(myvar2)) 
    print( myvar3, " has a type " , type(myvar3)) 
    print( myvar4, " has a type " , type(myvar4)) 
    print( myvar5, " has a type " , type(myvar5)) 
    print( myvar6, " has a type " , type(myvar6)) 
    print( myvar7, " has a type " , type(myvar7)) 
    print( myvar8, " has a type " , type(myvar8)) 
    print( myvar9, " has a type " , type(myvar9)) 

if __name__ == '__main__':
    my_var()
