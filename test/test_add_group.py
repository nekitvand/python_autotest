
from model.group import Group
from model.group import Group_add

def test_add_group(app):
    app.group.create(Group(name="aaaaa", header="aaaav", footer="aaaab"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

def test_add_address_book(app):
    app.group.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
