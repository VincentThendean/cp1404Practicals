class Band:

    def __init__(self,name=""):
        self.name = name
        self.players = []
        self.players_instruments = {}

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.players})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, player):
        """Add a player to band's ensemble."""
        self.players_instruments[player.name] = player.instruments
        self.players.append(player)

    def play(self):
        for i in range(3):
            return self.players[i].play()


if __name__ == '__main__':
    from musician import Musician

    band = Band()

