# Classe de base pour tout élément du menu
class MenuItem:
    """Modélise un élément générique du menu."""
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# Sous-classe spécifique pour les cafés, héritant de MenuItem
class CoffeeItem(MenuItem):
    """Modélise une boisson de type café."""
    def __init__(self, name, water, milk, coffee, cost):
        super().__init__(name, cost)  # Appel au constructeur de la classe parent
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

# Classe Menu utilisant les objets CoffeeItem
class Menu:
    """Modélise le menu avec les boissons."""
    def __init__(self):
        self.menu = [
            CoffeeItem(name="latte", water=200, milk=150, coffee=24, cost=3),
            CoffeeItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            CoffeeItem(name="cappuccino", water=250, milk=50, coffee=24, cost=2.5),
        ]

    def get_items(self):
        """Retourne les noms de toutes les boissons disponibles."""
        return "/".join([item.name for item in self.menu])

    def find_drink(self, order_name):
        """Recherche une boisson par nom et la retourne si elle existe."""
        for item in self.menu:
            if item.name == order_name:
                return item  # Retourne l'objet CoffeeItem si trouvé
        print("Sorry, that item is not available.")  # Affiché si aucune boisson n'est trouvée
        return None  # Retourne None si la boisson n'existe pas
