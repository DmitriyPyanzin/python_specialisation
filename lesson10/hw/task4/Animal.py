class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclasses should implement this method')

    def __str__(self):
        return f'{self.__class__.__name__} named {self.name}'
    