class PlayerCharacter:
    def __init__(self, name):
        self.name = name;

    def run(self):
        print('run')
        return 'Done'

player1 = PlayerCharacter('Prashant')
player2 = PlayerCharacter('Mayur')

print(player1.run())
print(player2.name)