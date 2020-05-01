####a = 3
####b = "tin"
####c = 1, 2, 3
####
####
####print(a)
####print(b)
####print(c)
##
##
##class duck(object):
##
##    def walk(self):
##        print("waddle, waddle, waddle")
##
##    def swim(self):
##        print("come on it, the water's lovely")
##
##    def quack(self):
##        print("Quack quack")
##
##
##
##class Penguin(object):
##
##    def walk(self):
##         print("waddle, waddle, I waddle too")
##
##    def swim(self):
##        print("Come on in, but its abit chilly this far south")
##
##    def quack(self):
##        print("Are you 'avin' a larf? I'M A penguiun")
##
##
##def test_duck(duck):
##    duck.walk()
##    duck.swim()
##    duck.quack()
##
##
##if __name__ == '__main__':
##    donald = duck()
##    test_duck(donald)
##
##
##    percy = Penguin()
##    test_duck(percy)


class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_Tag}{0.contents}{0.end_tag}".format(self)

    def display(self):
        print(self)

class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd','')
        self.end_tag = '' # DOCTYPE doesnt have an end tag


class Head(Tag):
    def __init__(self):
        super().__init__('head', '')

class Body(Tag):
    def __init__(self):
        super().__init__('body', '') #body contents will be built
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display()
        
