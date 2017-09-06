class addressbook:
    person_list =[]
    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)

    def serch(self,keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.firstname + " " + person.lastname)

class Person:
    import datetime

    firstname = ''
    lastname = ''
