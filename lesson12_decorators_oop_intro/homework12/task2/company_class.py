import datetime


class SonyCo:
    def __init__(self, name, country, founded_year, sphere):
        self.name = name
        self.country = country
        self.founded_year = founded_year
        self.sphere = sphere

    def show_info(self):
        print(f"Назва: {self.name}, Країна: {self.country}, Заснована: {self.founded_year}")

    def show_sphere(self):
        print(f"Сфера роботи компанії: {self.sphere}")

    def active_years(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.founded_year
        print(f"Існує на ринку: {age} років")

    @classmethod
    def child_company(cls, founded_year):
        return cls("Vaio", "Japan", founded_year, "Laptops")


vaio = SonyCo.child_company(1996)

vaio.show_info()
vaio.show_sphere()
vaio.active_years()

sony = SonyCo("Sony", "Japan", 1946, "Electronics")

sony.show_info()
sony.show_sphere()
sony.active_years()
