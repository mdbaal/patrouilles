class Scout:

    def __init__(self, name, age, insigne, title="lid"):
        self._name = name
        self._age = age
        # insignes level 0 = pionieren, 1 = hakken & stoken, etc..
        self._insigne = insigne

        self._scout_relations = {

        }

        self._title = title

    @property
    def name(self):
        return self._name

    def change_name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    def change_age(self, age):
        self._age = age

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def get_insigne(self):
        return self._insigne

    def set_insigne(self, level):
        self._insigne = level

    def set_relation(self, scout, level):
        self._scout_relations[scout] = level
        if not scout.has_relation(self):
            scout.set_relation(self, level)

    def has_relation(self, scout):
        return scout in self._scout_relations

    def get_relation(self, scout):
        if scout in self._scout_relations:
            return self._scout_relations[scout]
        else:
            return -1

    def remove_relation(self, scout):
        if scout in self._scout_relations.values():
            self._scout_relations.pop(scout)
