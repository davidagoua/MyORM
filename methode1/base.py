

class Basetable:

    nom_table = ""
    _list_champ = list()

    def get_all(self):
        sql = f"SELECT * FROM {self.nom_table}"
        return sql

    def insert(self, data=list()):
        sql = f"INSERT INTO ({','.join(self._list_champ)}) VALUE ({','.join(data)})"
        return sql

    def getWhere(self, champ, value):
        sql = f"SELECT * FROM {self.nom_table} WHERE {champ}=({value})"

    @staticmethod
    def parse_champ_list():
        sql = ""
        for champ in Basetable._list_champ:
            pass



class UserTable(Basetable):
    nom_table = 'users'
    list_champ = ['id', 'nom', 'prenom', 'email', 'adresse']