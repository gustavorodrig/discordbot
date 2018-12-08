class Feeders:

    def __init__(self) -> None:
        super().__init__()

    feeders = {"insano": "99255581",
               "jhon": "143290778",
               "fake": "95910923",
               "ronaldo": "128685170",
               "alemao": "91466015",
               "fernanda": "118472812",
               "japa": "94779221",
               "luizao": "27963205",
               "deffa": "104211779"}

    def steamIdByName(self, name):
        return self.feeders.get(name)

    def getFeedersList(self):
        return self.feeders

    def getFeedersPrint(self):
        mensage = ''
        for key, value in self.feeders.items():
            mensage += "{} \n".format(key)
        return mensage
