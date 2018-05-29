import pytest

from application import Application
from group import Group
from group import Group_add

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="aaaaa", header="aaaav", footer="aaaab"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

def test_add_address_book(app):
    app.login(username="admin", password="secret")
    app.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
    app.logout()