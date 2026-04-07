#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        text = super().__str__()
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        text = text.replace('"', '&quot;')
        return text.replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, msg = "Elem validation Error!!!"):
            super().__init__(msg)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if content == '' and not isinstance(content, Text):
            raise Elem.ValidationError("Error : No valid content type!")
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        self.content = []

        if content:
            self.add_content(content)

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """

        attrs = self.__make_attr()

        if self.tag_type == 'double':
            content = self.__make_content()
            if content:
                return f"<{self.tag}{attrs}>{content}</{self.tag}>"
            return f"<{self.tag}{attrs}></{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag}{attrs} />"
        return ''

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += "".join(f"  {line}\n" for line in str(elem).splitlines())
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
    try:
        h1_elem = Elem(tag="h1", content=Text('"Oh no, not again!"'))
        img_elem = Elem(tag="img", attr={"src" : "http://i.imgur.com/pfp3T.jpg"} , tag_type = "simple")
        body_elem = Elem(tag="body", content=[h1_elem, img_elem])
        title_elem = Elem(tag="title", content=Text('"Hello ground!"'))
        head_elem = Elem(tag="head", content = [title_elem])
        html_element = Elem(tag="html", content=[head_elem, body_elem])
        print(html_element)
    except Exception as e:
        print(f"Error: {e}")
