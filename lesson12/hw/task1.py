class Valid:
    def __set_name__(self, owner, name):
        self.name = name

    @staticmethod
    def valid(word):
        if not word.istitle() and not word.isalpha():
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')

    def __set__(self, inst, word):
        self.valid(word)
        setattr(inst, self.name, word)
