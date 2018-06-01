import pytest

from fixture.application import Application
from model.group import Group
from model.group import Group_add


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create(Group(name="aaaaa", header="aaaav", footer="aaaab"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_add_address_book(app):
    app.session.login(username="admin", password="secret")
    app.group.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
    app.session.logout()