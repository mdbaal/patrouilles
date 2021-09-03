from typing import Dict


class Scout:

    def __init__(self, data: Dict):
        self._name = data["Name"]
        self._age = data["Age"]
        # insignes level 0 = pionieren, 1 = hakken & stoken, etc..
        self._insigne = data["Insigne"]

        self._patrouille = data["Patrouille"]

        self._scout_relations: Dict[str, int] = data["Relations"]

        self._title = data["Title"]

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

    def set_relation(self, other, level):
        self._scout_relations[other] = level

    def set_relations(self, relations: Dict):
        self._scout_relations = dict(relations)

    def remove_relation(self, other):
        if other in self._scout_relations.values():
            self._scout_relations.pop(other)

    def has_relation(self, other) -> bool:
        return other in self._scout_relations

    def get_relation(self, other):
        if other in self._scout_relations:
            return self._scout_relations[other]
        else:
            return 0

    def get_relations(self):
        return self._scout_relations

    def __repr__(self):
        return self.name

    def to_dict(self):
        if isinstance(self, Scout):
            dict = {
                "Name": self._name,
                "Age": self._age,
                "Insigne": self._insigne,
                "Title": self._title,
                "Patrouille": self._patrouille,
                "Relations": self._scout_relations
            }

            return dict
        else:
            type_name = self.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))

    def set_patrouille(self, patrouille):
        self._patrouille = patrouille
