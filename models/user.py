from datetime import datetime

class User:
    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def sexo(self):
        return self.__sexo

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @data_nascimento.setter
    def data_nascimento(self, nova_data):

        if nova_data == "":
            self.__data_nascimento = nova_data
            return

        try:
            datetime.strptime(nova_data, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Data invalida deve ser no formato 'YYYY-MM-DD' ou ''")

        self.__data_nascimento = nova_data

    @sexo.setter
    def sexo(self, novo_sexo):
        
        if(novo_sexo != "m" and novo_sexo != "f" and novo_sexo != ""):
            raise ValueError("Sexo deve ser 'm' ou 'f' ou ''")

        self.__sexo = novo_sexo