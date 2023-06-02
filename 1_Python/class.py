class Human:
    def __init__(self, name, occupation):
        self.name == name
        self.occupation == occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "Playes Ten")
        elif self.occupation == "actor":
            print(self.name, "Shoots a Film")

    def speaks(self):
        print(self.name, "Says How Are You")

# tom = Human("Tom Cruise", "actor")
# tom.do_work()
# tom.speaks()

maria = Human("Maria Sharapova", "actor")
maria.do_work()
maria.speaks()