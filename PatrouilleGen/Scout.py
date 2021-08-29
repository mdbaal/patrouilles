class Scout:

    def __init__(self, naam, leeftijd, insigneLevel, title="lid"):
        self._naam = naam
        self._leeftijd = leeftijd
        # insignes level 0 = pionieren 1 = hakken & stoken etc..
        self._insigneLevel = insigneLevel

        self._scoutRelations = {

        }

        self._title = title

    @property
    def Naam(self):
        return self._naam

    def ChangeNaam(self, naam):
        self._naam = naam

    @property
    def Leeftijd(self):
        return self._leeftijd

    def ChangeLeeftijd(self, leeftijd):
        self._leeftijd = leeftijd

    @property
    def Title(self):
        return self._title

    @Title.setter
    def Title(self, title):
        self._title = title

    def GetInsigneLevel(self):
        return self._insigneLevel

    def SetInsigne(self, level):
        self._insigneLevel = level

    def SetRelation(self, scout, level):
        self._scoutRelations[scout] = level
        if not scout.HasRelation(self):
            scout.SetRelation(self, level)

    def HasRelation(self, scout):
        return scout in self._scoutRelations

    def GetRelation(self, scout):
        if scout in self._scoutRelations:
            return self._scoutRelations[scout]
        else:
            return -1

    def RemoveRelation(self, scout):
        if scout in self._scoutRelations.values():
            self._scoutRelations.pop(scout)
