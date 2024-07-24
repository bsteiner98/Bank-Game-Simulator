import csv
from alive_progress import alive_bar
from random import randrange

SIMULATED_GAMES = 1000000


class player:
    def __init__(self, rollCountStrat, scoreCountStrat):
        self.rollCountStrat = rollCountStrat
        self.scoreCountStrat = scoreCountStrat
        self.gameScore = 0

    def __str__(self):
        return f"rollStrat: {self.rollCountStrat}, scoreStrat: {self.scoreCountStrat}"

    def executeStrategy(self, currentRollCount, currentScoreCount):
        # Returns 1 if proceeding with rolls, 0 if banking

        if self.rollCountStrat and currentRollCount == self.rollCountStrat:
            return 0
        if self.scoreCountStrat and currentScoreCount >= self.scoreCountStrat:
            return 0

        return 1


class game:
    def __init__(self, players, numberOfRounds):
        self.players = players
        self.numberOfRounds = numberOfRounds

    def __rollDice(self):
        firstDie = randrange(1, 6)
        secondDie = randrange(1, 6)
        if firstDie == secondDie:
            diceRoll = ("DOUBLE", firstDie + secondDie)
        else:
            diceRoll = ("NORMAL", firstDie + secondDie)
        return diceRoll

    def __playRound(self):
        remainingPlayers = self.players.copy()
        roundScore = 0
        rollNumber = 1

        # Continue rolling dice until all players have banked or a 7 is rolled
        while remainingPlayers:
            diceRoll = self.__rollDice()
            if rollNumber <= 3:
                if diceRoll[1] == 7:
                    roundScore += 70
                else:
                    roundScore += diceRoll[1]
            else:
                if diceRoll[1] == 7:
                    return roundScore
                if diceRoll[0] == "DOUBLE":
                    roundScore = roundScore * 2
                else:
                    roundScore = roundScore + diceRoll[1]

            if rollNumber >= 3:
                for player in remainingPlayers:
                    playerDecision = player.executeStrategy(rollNumber, roundScore)
                    # Player chooses to bank
                    if not playerDecision:
                        player.gameScore += roundScore
                        remainingPlayers.remove(player)

            rollNumber += 1

        return roundScore

    def playGame(self):
        for round in range(self.numberOfRounds):
            self.__playRound()

        gameScores = {}

        # print(f"GAME OVER! Final Scores:\n")
        playerNumb = 1
        for player in self.players:
            gameScores[str(player)] = player.gameScore
            # print(f"Player {playerNumb}: {player.gameScore} ({str(player)})")
            playerNumb += 1

        return gameScores


def initializePlayers():
    playerList = []
    # Always banks after 3rd roll
    playerList.append(player(3, None))

    # Always banks after 4th roll
    playerList.append(player(4, None))

    # Always banks after 5th roll
    playerList.append(player(5, None))

    # Always banks after 6th roll
    playerList.append(player(6, None))

    # Always banks after 7th roll
    playerList.append(player(7, None))

    # Always banks after 8th roll
    playerList.append(player(8, None))

    # Always banks after 9th roll
    playerList.append(player(9, None))

    # Always banks after 10th roll
    playerList.append(player(10, None))

    # Banks as soon as score is >= 100
    playerList.append(player(None, 100))

    # Banks as soon as score is >= 150
    playerList.append(player(None, 150))

    # Banks as soon as score is >= 200
    playerList.append(player(None, 200))

    # Banks as soon as score is >= 250
    playerList.append(player(None, 250))

    # Banks as soon as score is >= 300
    playerList.append(player(None, 300))

    # Banks as soon as score is >= 350
    playerList.append(player(None, 350))

    # Banks as soon as score is >= 400
    playerList.append(player(None, 400))

    return playerList


def writeToCSV(playerList, masterGameScores):
    # Make a column for each player (name is the player's strategy)
    headers = []
    for player in playerList:
        headers.append(str(player))

    with open("Game Results.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for game in masterGameScores:
            gameRow = []
            for player in game:
                gameRow.append(game[player])

            writer.writerow(gameRow)


def countWins(masterGameScore):
    # Initialize a dictionary to keep track of wins for each player
    wins = {}

    # Iterate over each game to populate the wins dictionary with all players set to 0 wins
    for game in masterGameScore:
        for player in game:
            if player not in wins:
                wins[player] = 0

    # Iterate over each game to count the wins
    for game in masterGameScore:
        # Find the player with the highest score
        winner = max(game, key=game.get)
        # Increment the win count for the winning player
        wins[winner] += 1

    return wins


def main():
    playerList = initializePlayers()
    diceGame = game(playerList, 15)
    masterGameScores = []

    with alive_bar(SIMULATED_GAMES) as bar:
        for gameNumber in range(SIMULATED_GAMES):
            # Record the results of the game
            masterGameScores.append(diceGame.playGame())

            # Reset all players' scores before next game
            for player in playerList:
                player.gameScore = 0
            bar()

    print("Determining win rate stats")
    wins = countWins(masterGameScores)
    print(wins)

    masterGameScores.append(wins)

    print("Writing results to CSV.")
    writeToCSV(playerList, [wins])


if __name__ == "__main__":
    main()
