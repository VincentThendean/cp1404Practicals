class Band:

    def __init__(self,name=""):
        self.name = name
        self.players = []
        self.players_instruments = {}

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({str(self.players).strip('[').strip(']')})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(self)

    def add(self, player):
        """Add a player to band's ensemble."""
        self.players_instruments[player.name] = player.instruments
        self.players.append(f"{player.name}, {player.instruments}")

    def play(self):
        for player in self.players_instruments:
            # print(player)
            if not self.players_instruments[player]:
                print(f"{player} needs an instrument!")
            else:
                print(f"{player} is playing: {str(self.players_instruments[player]).strip('[').strip(']')}")
        return ""

#
# if __name__ == '__main__':
#     from musician import Musician
#
#     band = Band()
