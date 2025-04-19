# برای دسترسی به متد باید حتما پرانتز باز و بسته گذاشته بشود ولی برای پراپرتی نباید پرانتز گذاشت

class Behrooz:

    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def fullname(self):
        return f"{self.name} {self.family}"

    def show_fullname(self):
        return f"{self.name} {self.family}"


obj1 = Behrooz("behrooz", "MohamadiNasab")

print(obj1.show_fullname())
print(obj1.fullname)
