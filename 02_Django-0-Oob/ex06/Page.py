#!/usr/bin/python3

from elem import Elem, Text
from elements import *

class Page:
    def __init__(self, content=None):
        if not isinstance(content, Elem):
            raise Elem.ValidationError("Page must be initialized with an Elem")
        self.root = content
        
    def __str__(self):
        doc = str(self.root)
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + doc
        return doc

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))

    def is_valid(self):
        return self._check_node(self.root)
    # =========================
    # VALIDATION LOGIC
    # =========================

    def _check_node(self, node):
        valid_types = (
            Html, Head, Body, Title, Meta, Img, Table,
            Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div,
            Span, Hr, Br, Text
        )
        if not isinstance(node, valid_types):
            return False

        if isinstance(node, Text):
            return True

        children = node.content
        # -------- Html --------
        if isinstance(node, Html):
            if len(children) != 2:
                return False
            return isinstance(children[0], Head) and isinstance(children[1], Body) \
                   and all(self._check_node(c) for c in children)

        # -------- Head --------
        if isinstance(node, Head):
            '''
            titles = [c for c in children if isinstance(c, Title)]
            return len(titles) == 1 and all(self._check_node(c) for c in children)
            '''
            if len(children) != 1 or not isinstance(children[0], Title):
                return False
            return self._check_node(children[0])

        # -------- Body / Div --------
        if isinstance(node, (Body, Div)):
            allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            return all(isinstance(c, allowed) and self._check_node(c) for c in children)

        # -------- Title, H1, H2, Li, Th, Td --------
        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            return len(children) == 1 and isinstance(children[0], Text)

        # -------- P --------
        if isinstance(node, P):
            return all(isinstance(c, Text) for c in children)

        # -------- Span --------
        if isinstance(node, Span):
            return all(isinstance(c, (Text, P)) for c in children)

        # -------- Ul / Ol --------
        if isinstance(node, (Ul, Ol)):
            return len(children) >= 1 and all(isinstance(c, Li) for c in children) and all(self._check_node(c) for c in children)
        # -------- Tr --------
        if isinstance(node, Tr):
            if len(children) == 0:
                return False
            if all(isinstance(c, Th) for c in children) and all(self._check_node(c) for c in children):
                return True
            if all(isinstance(c, Td) for c in children) and all(self._check_node(c) for c in children):
                return True
            return False

        # -------- Table --------
        if isinstance(node, Table):
            if len(children) == 0:
                return False
            return (all(isinstance(c, Tr) for c in children) and all(self._check_node(c) for c in children))

        # -------- default --------
        return all(self._check_node(c) for c in children)

def _check_print_write(page, file, test_name):
    print(page)
    if page.is_valid():
        page.write_to_file(file)
        print(f"\n{test_name} -> Is valid.  File \"{file}\" has been writen")
    else:
        print(f"\n{test_name} -> No valid page")

def _test_no_valid_page_with_elem(file):
    page= Page(Elem())
    _check_print_write(page, file, "_test_no_valid_page_with_elem")

def _test_Ok_page_head_body(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body([
                H1(Text("Head H1")),
                Text("Text 1"),
                H2(Text("Head H2")),
                Text("Text 2")
            ])
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_head_body")

def _test_Ko_page_body_head(file):
    page = Page(
        Html([
            Body([
                H1(Text("Head H1")),
                Text("Text 1"),
                H2(Text("Head H2")),
                Text("Text 2")
            ]),
            Head(Title(Text("Page Tittle")))
        ])
    )

    _check_print_write(page, file, "_test_Ko_page_body_head")

def _test_Ko_page_body_with_p(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body([
                H1(Text("Head H1")),
                P(Text("This is a test"))
            ])
        ])
    )

    _check_print_write(page, file, "_test_Ko_page_body_with_p")

def _test_Ok_page_body_with_span_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body([
                Span(Text("Text in Span")),
            ])
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_body_with_scan_text")

def _test_Ok_page_body_with_span_text_and_p_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body([
                Span(Text("Text 1 in Span")),
                Span(P(Text("Text 1 in P"))),
                Span([
                    Text("Text 2 in Span"),
                    P(Text("Text 2 in P"))
                ]),
            ])
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_body_with_scan_text_and_p_text")

def _test_Ko_page_body_with_div_inside_span(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body( Span(Div(Text("Text 1 in Div")))),
        ])
    )

    _check_print_write(page, file, "test_Ko_page_body_with_div_inside_span");

def _test_Ok_page_body_with_Table_Tr_Th(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body(
                Table([
                    Tr(Th(Text("Th text 1")))
                ])
            )
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_body_with_Table_Tr_Th()");

def _test_Ok_page_body_with_Table_2Tr_2Th(file):
    page = Page(
        Html([
            Head(Title(Text("Page Tittle"))),
            Body(
                Table([
                    Tr([
                        Th(Text("Th1 text 1")),
                        Th(Text("Th2 text 2"))
                    ])
                ])
            )
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_body_with_Table_2Tr_2Th()");

def _test_Ok_page_body_with_Table_Tr_Td(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Table([
                    Tr(Td(Text("Td text 1")))
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_body_with_Table_Tr_Td()")


def _test_Ok_page_body_with_Table_2Tr_2Td(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Table([
                    Tr([
                        Td(Text("Td1 text 1")),
                        Td(Text("Td2 text 2"))
                    ])
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_body_with_Table_2Tr_2Td()")

def _test_Ko_page_body_with_Table_Tr_Th_without_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Table([
                    Tr(Th())
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_body_with_Table_Tr_Th_without_text")

def _test_Ko_page_body_with_Table_Tr_Td_without_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Table([
                    Tr(Td())
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_body_with_Table_Tr_Td_without_text")

def _test_Ok_page_with_ul_one_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ul(Li(Text("Item 1")))
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_with_ul_one_li")


def _test_Ok_page_with_ol_one_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ol(Li(Text("Item 1")))
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_with_ol_one_li")

def _test_Ok_page_with_ul_two_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ul([
                    Li(Text("Item 1")),
                    Li(Text("Item 2"))
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_with_ul_two_li")


def _test_Ok_page_with_ol_two_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ol([
                    Li(Text("Item 1")),
                    Li(Text("Item 2"))
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ok_page_with_ol_two_li")

def _test_Ko_page_with_ul_li_without_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ul(Li())
            )
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_with_ul_li_without_text")


def _test_Ko_page_with_ol_li_without_text(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ol(Li())
            )
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_with_ol_li_without_text")

def _test_Ko_page_with_ul_mixed_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(
                Ul([
                    Li(Text("Item 1")),
                    Li()
                ])
            )
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_with_ul_mixed_li")

def _test_Ko_page_with_ul_without_li(file):
    page = Page(
        Html([
            Head(Title(Text("Page Title"))),
            Body(Ul())
        ])
    )
    _check_print_write(page, file, "_test_Ko_page_with_ul_mixed_li")

def _test_Ko_page_head_no_title(file):
    page = Page(
        Html([
            Head(),
            Body([
                H1(Text("Head H1")),
                Text("Text 1"),
                H2(Text("Head H2")),
                Text("Text 2")
            ])
        ])
    )

    _check_print_write(page, file, "_test_Ok_page_head_body")

def _test_page_div(file):
    page = Page(Div(P()))
    _check_print_write(page, file, "_test_page_div")

def _test_page_text(file):
    page = Page(Text("Test Text"))
    _check_print_write(page, file, "_test_page_text")

def _test_Error_no_page_element(file):
    page = Page()
    _check_print_write(page, file, "test_Ko_no_page_element")

def _menu():
    print("\n---Menu of tests:")
    print("1. _test_no_valid_page_with_elem()")
    print("2. _test_Ok_page_head_body()")
    print("3. _test_Ko_page_body_head()")
    print("4. _test_Ko_page_body_with_p()")
    print("5. _test_Ok_page_body_with_span_text()");
    print("6. _test_Ok_page_body_with_span_text_and_p_text()")
    print("7. _test_Ko_page_body_with_div_inside_span()")
    print("8. _test_Ok_page_body_with_Table_Tr_Th()")
    print("9. _test_Ok_page_body_with_Table_2Tr_2Th()")
    print("10. _test_Ok_page_body_with_Table_Tr_Td()")
    print("11. _test_Ok_page_body_with_Table_2Tr_2Td()")
    print("12. _test_Ko_page_body_with_Table_Tr_Th_without_text()")
    print("13. _test_Ko_page_body_with_Table_Tr_Td_without_text()")
    print("14. _test_Ok_page_with_ul_one_li()")
    print("15. _test_Ok_page_with_ol_one_li()")
    print("16. _test_Ok_page_with_ul_two_li()")
    print("17. _test_Ok_page_with_ol_two_li()")
    print("18. _test_Ko_page_with_ul_li_without_text()")
    print("19. _test_Ko_page_with_ol_li_without_text()")
    print("20. _test_Ko_page_with_ul_mixed_li()")
    print("21. _test_Ko_page_with_ul_without_li()")
    print("22. _test_Ko_page_head_no_title()")
    print("23. _test_Error_no_page_element()")
    print("0. Exit from program")


def _tests():

    file = "ex06.html"

    while True:
        _menu()
        option = input("\nSelect option [1-22 or 0]: ")
        if option == "0":
            break
        elif option == "1":
            _test_no_valid_page_with_elem(file)
        elif option == "2":
            _test_Ok_page_head_body(file)
        elif option == "3":
            _test_Ko_page_body_head(file)
        elif option == "4":
            _test_Ko_page_body_with_p(file)
        elif option == "5":
            _test_Ok_page_body_with_span_text(file)
        elif option == "6":
            _test_Ok_page_body_with_span_text_and_p_text(file)
        elif option == "7":
            _test_Ko_page_body_with_div_inside_span(file)
        elif option == "8":
            _test_Ok_page_body_with_Table_Tr_Th(file)
        elif option == "9":
            _test_Ok_page_body_with_Table_2Tr_2Th(file);
        elif option == "10":
            _test_Ok_page_body_with_Table_Tr_Td(file)
        elif option == "11":
            _test_Ok_page_body_with_Table_2Tr_2Td(file)
        elif option == "12":
            _test_Ko_page_body_with_Table_Tr_Th_without_text(file)
        elif option == "13":
            _test_Ko_page_body_with_Table_Tr_Td_without_text(file)
        elif option == "14":
            _test_Ok_page_with_ul_one_li(file)
        elif option == "15":
            _test_Ok_page_with_ol_one_li(file)
        elif option == "16":
            _test_Ok_page_with_ul_two_li(file)
        elif option == "17":
            _test_Ok_page_with_ol_two_li(file)
        elif option == "18":
            _test_Ko_page_with_ul_li_without_text(file)
        elif option == "19":
            _test_Ko_page_with_ol_li_without_text(file)
        elif option == "20":
            _test_Ko_page_with_ul_mixed_li(file)
        elif option == "21":
            _test_Ko_page_with_ul_without_li(file)
        elif option == "22":
            _test_Ko_page_head_no_title(file)
        elif option == "23":
            try:
                _test_Error_no_page_element(file)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No valid option!!!")

if __name__ == '__main__':
    try:
        _tests()
    except Exception as e:
        print(f"Error: {e}")
