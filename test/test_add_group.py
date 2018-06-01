
from model.group import Group
from model.group import Group_add

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="aaaaa", header="aaaav", footer="aaaab"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_address_book(app):
    app.session.login(username="admin", password="secret")
    app.group.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
    app.session.logout()