class Hero:

    def __init__(self, id, localized_name):
        self.id = id
        self.localized_name = localized_name

    def __str__(self):
        return '{} {}'.format(self.id, self.localized_name)
