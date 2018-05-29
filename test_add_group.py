import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from group import Group

class test_add_group(unittest.TestCase):
    def setUp(self):
      self.wd = WebDriver()
      self.wd.implicitly_wait(3)


    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")


    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_group_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()


    def create_group(self, wd, group):
        self.open_group_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit to group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)


    def return_to_groups_page(self, wd):
        # return group page
        wd.find_element_by_link_text("group page").click()


    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()


    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="aaaaa", header="aaaav", footer="aaaab"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def tearDown(self):
       self.wd.quit()

if __name__ == '__main__':
    unittest.main