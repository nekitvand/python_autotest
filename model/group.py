class Group:

    def __init__(self,name=None,header=None,footer=None,id=None ):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

class Group_add:

    def __init__(self,firstname,middlename,lastname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname