from geo_calculator.rolling_stone.player import Player

def test_player():
    player = Player("Mick Jagger")
    assert isinstance(player, Player)
