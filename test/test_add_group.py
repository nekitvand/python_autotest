
from model.group import Group
from model.group import Group_add

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="aaaaa", header="aaaav", footer="aaaab")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_address_book(app):
    app.group.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
