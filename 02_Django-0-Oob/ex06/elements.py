#!/usr/bin/python3

from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', attr=attr, content=content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', attr=attr, content=content)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', attr=attr, content=content, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', attr=attr, content=content, tag_type='simple')

def _test01_subject():
    print( Html( [Head(), Body()] ) )

def _test02_subject():
    '''
    h1= H1(Text('"Oh no, not again!"'))
    img = Img(attr={"src" : "http://i.imgur.com/pfp3T.jpg"})
    body = Body([h1, img])
    title = Title(Text('"Hello ground!"'))
    head = Head(title)
    html = Html([head, body])
    '''
    html = Html([
        Head([Title(Text('"Hello ground!"'))]),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={"src" : "http://i.imgur.com/pfp3T.jpg"})
        ])
    ])
    print(html)

def _test03_img_attr():
    img = Img(attr={"src": "image.png", "alt": "my image"})
    print(img)

def _test04_p_text_escape():
    p = P(Text('<hello "world">'))
    print(p)

def _test05_p_with_span():
    p = P([
        Text("Normal text and"),
        Span(attr={"style" : "color: red; font-weight: bold;"} , content=Text("bold red text"))
     ])
    print(p)

def _test06_Div_with_H2_Ul_and_OL_list():
    div = Div([
        H2(Text("Title H2")),
        Ul([ Li(Text("UL item 1")), Li(Text("UL item 2")), Li(Text("UL item 3"))]),
        Ol([ Li(Text("OL item 1")), Li(Text("OL item 2"))])
    ])
    print(div)

def _test07_table():
    table = Table([
        Th([Td(Text("COLUMN 1")), Td(Text("COLUMN 2"))]),
        Tr([Td(Text("A1")), Td(Text("B1"))]),
        Tr([Td(Text("A2")), Td(Text("B2"))])
    ])
    print(table)

def _test08_div_br_hr():
    div = Div([ Text("line 1"), Br(), Text("line 2"), Hr(), Text("line 3") ])
    print(div)

def _test09_p_validation_error():
    try:
        p = P(123) 
    except Elem.ValidationError as e:
        print("ValidationError correctly raised by P()")

def _test10_div_invalid_content():
    try:
        Div(content=42)
    except Elem.ValidationError:
        print("Correct: ValidationError raised by Div()")

def _test11_html():
    page = Html([
        Head([
            Meta(attr={"charset" : "utf-8"}),
            Title(Text("Test page"))
        ]),
        Body([
            H1(Text("Header")),
            Div([
                P(Text("paragraph 1")),
                Hr(),
                P(Text("paragraph 2")),
                Ul([ 
                    Li(Text("UL item 1")),
                    Li(Text("UL item 2")),
                    Li(Text("UL item 3"))
                ]),
                Br(),
                Ol([
                    Li(Text("OL item 1")),
                    Li(Text("OL item 2"))
                ])
            ]),
            Hr(),
            H2(Text("Title H2")),
            Table([
                Th([Td(Text("COLUMN 1")), Td(Text("COLUMN 2"))]),
                Tr([Td(Text("A1")), Td(Text("B1"))]),
                Tr([Td(Text("A2")), Td(Text("B2"))])
            ]),
            Hr(),
            Img(attr={"src": "cat.png"})
        ])
    ])
    print(page)

def _menu():
    print("\n---Menu of tests:")
    print("1. test01 from subject")
    print("2. test02 from subject")
    print("3. img with several attributes")
    print("4. p with text escape")
    print("5. p with span")
    print("6. H2 with Ol and Ul lists")
    print("7. table with Th, Tr and Th")
    print("8. div with br and hr")
    print("9. p validation error")
    print("10. div with invalid content")
    print("11. Html test")
    print("0. Exit from program")

def _main():
    while True:
        _menu()
        option = input("\nSelect option [1-11 or 0]: ")
        if option == "0":
            break
        if option == "1":
            _test01_subject()
        elif option == "2":
            _test02_subject()
        elif option == "3":
            _test03_img_attr()
        elif option == "4":
            _test04_p_text_escape()
        elif option == "5":
            _test05_p_with_span()
        elif option == "6":
            _test06_Div_with_H2_Ul_and_OL_list()
        elif option == "7":
            _test07_table()
        elif option == "8":
            _test08_div_br_hr()
        elif option == "9":
            _test09_p_validation_error()
        elif option == "10":
            _test10_div_invalid_content()
        elif option == "11":
            _test11_html()
        else:
            print("No valid option!!!")

if __name__ == '__main__':
    try:
        _main()
    except Exception as e:
        print(f"Error: {e}")
