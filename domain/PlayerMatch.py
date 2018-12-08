from domain.Hero import Hero


class PlayerMatch:

    def __init__(self, vitoria, heroi: Hero, kill, death, assist):
        self.vitoria = vitoria
        self.heroi = heroi
        self.kill = kill
        self.death = death
        self.assist = assist

    def venceu(self):
        return True if self.vitoria == "Vitoria" else False

    def resultado(self):
        return '{}  -  {} - KDA {}/{}/{}'.format(self.vitoria, self.heroi.localized_name, self.kill,
                                                          self.death, self.assist)
