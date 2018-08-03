
from model.group import Group
import random
import string



def random_sring(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix + " ".join ([random.choice(symbol) for 1 in range(random.randrange(maxlen))])



testdata = [
    Group(name = random_sring ("name",10 ), header=random_sring ("header",20 ), footer=random_sring ("footer", 20)),
    Group(name="", header="", footer="")
]



@pytest.parametrize("group",testdata,ids=[repr(x) for x in testdata])
def test_add_group(app,group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)