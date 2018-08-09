from model.group import Group
import random
from random import randrange

def test_delete_some_group(app,db,check_ui):
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id)
    #app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)