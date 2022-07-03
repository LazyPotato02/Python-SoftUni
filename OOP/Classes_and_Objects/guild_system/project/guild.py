from .player import Player


class Guild:

    def __init__(self, name) -> None:
        self.name = name
        self.players = list()

    def assign_player(self,player:Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name:str):
        try:
            player = None
            for p in self.players:
                if p.name == player_name:
                    player = p
                    break

            self.players.remove(player)
            player.guild = player.default_guild
            return f'Player {player_name} has been removed from the guild.'

        except ValueError:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self) -> str:
        retval = f'Guild: {self.name}'
        if self.players:
            retval += '\n' + '\n'.join([player.player_info() for player in self.players])
        return retval