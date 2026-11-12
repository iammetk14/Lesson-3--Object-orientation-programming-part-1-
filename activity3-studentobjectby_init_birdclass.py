class bird:
    species="parrot"

    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=bird("Blu",4)
rio=bird("Rio",3)

print("Blu is a {}".format(blu.species))
print("Rio is a {}".format(rio.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(rio.name,rio.age))