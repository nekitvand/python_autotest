
from model.group import Group
from model.group import Group_add

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="aaaaa", header="aaaav", footer="aaaab"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_address_book(app):
    app.group.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
