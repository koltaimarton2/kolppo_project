from json import load

class itemGroups:
    keyItems = "keyItems"
    healItems = "healItems"

class Item:
    def __init__(self, name: str, amount: int = 1, itemGroup: itemGroups = itemGroups.keyItems) -> None:
        self.name = name
        self.dataName = name.lower().replace(" ", "_")
        self.amount = amount
        self.group = itemGroup
        self.stats = {"description": "", "value": 0}
        self.getData()
    def use(self, *args, **kwargs):
        pass
    def getData(self, *args):
        if args:
            for arg in args:
                self.stats[arg] = None
        with open('data/items.json', encoding='utf-8') as file:
            model = dict(load(file))
        for idx, stat in enumerate(self.stats):
            self.stats[stat] = model[self.group][self.dataName][idx]

class healItem(Item):
    def __init__(self, name:str, amount: int = 1, itemGroup: itemGroups = itemGroups.healItems) -> None:
        super().__init__(name, amount, itemGroup)
        self.getData("healAmount")
    def use(self, player):
        player.Heal(self.stats["healAmount"])
        print(f"Healed : {self.stats["healAmount"]}")

items = {
    "Fél személyi":Item("Fél személyi"), 
    "Bicska": Item("Bicska")
}