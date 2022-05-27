class Student:
    school="AkiraChix"
    def __init__(Self,name,age,country,school,first_name,last_name):
            Self.name=name
            Self.age=age
            Self.country=country
            Self.first_name=first_name
            Self.last_name=last_name
           

    def greet(Self):
        return f"Hello {Self.name}, welcome to {Self.school}. How is {Self.country}"

    def full_name(Self):
        return f" Hello your full name is {Self.first_name} {Self.last_name}"

           
    def year_of_birth(Self):
         year=2022- Self.age
         return {year}

    def initials(Self):
        initial=Self.first_name[0] + Self.last_name[0]
        return initial
