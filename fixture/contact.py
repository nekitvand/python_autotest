

from model.contact import Contact


class ContactHelper:

    def __init__(self):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_element_by_name["entry"]:
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_elements_by_tag_name("input").get_attribute('value')
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname,lastname=lastname,id=id
                                                  homephone=all_phones[0],mobilephome=all_phones[1],
                                                workphone=all_phones[2],secondatyphone = all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_name("entry")
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact__info_from_edit_page(self,index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname,id = id,homephone = homephone ,
                       workphone=workphone,secondaryphone= secondaryphone)