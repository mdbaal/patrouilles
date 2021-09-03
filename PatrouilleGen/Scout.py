from typing import Dict


class Scout:

    def __init__(self, name, age, insigne, relations, title="lid"):
        self._name = name
        self._age = age
        # insignes level 0 = pionieren, 1 = hakken & stoken, etc..
        self._insigne = insigne

        self._scout_relations: Dict[str, int] = relations

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
