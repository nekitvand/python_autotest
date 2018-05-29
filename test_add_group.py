import unittest
from application import Application
from group import Group
from group import Group_add


class test_add_group(unittest.TestCase):
    def setUp(self):
     self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="aaaaa", header="aaaav", footer="aaaab"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def test_add_address_book(self):
        self.app.login(username="admin", password="secret")
        self.app.create_add_new(Group_add(firstname='Nikita', middlename='Sergeeyvich', lastname='Vandyshev'))
        self.app.logout()


    def tearDown(self):
       self.app.destroy()

if __name__ == '__main__':
    unittest.main