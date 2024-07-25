import csv
import matplotlib.pyplot as plt
import numpy as np
from alive_progress import alive_bar
from random import randrange

SIMULATED_GAMES = 100000


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
                nextRoundPlayers = remainingPlayers.copy()
                for player in remainingPlayers:
                    playerDecision = player.executeStrategy(rollNumber, roundScore)
                    # Player chooses to bank
                    if not playerDecision:
                        player.gameScore += roundScore
                        nextRoundPlayers.remove(player)
                remainingPlayers = nextRoundPlayers

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
    # # Always banks after 3rd roll
    # playerList.append(player(3, None))

    # # Always banks after 4th roll
    # playerList.append(player(4, None))

    # # Always banks after 5th roll
    # playerList.append(player(5, None))

    # # Always banks after 6th roll
    # playerList.append(player(6, None))

    # # Always banks after 7th roll
    # playerList.append(player(7, None))

    # # Always banks after 8th roll
    # playerList.append(player(8, None))

    # # Always banks after 9th roll
    # playerList.append(player(9, None))

    # # Always banks after 10th roll
    # playerList.append(player(10, None))

    # Banks as soon as score is >= 10
    playerList.append(player(None, 10))

    # Banks as soon as score is >= 20
    playerList.append(player(None, 20))

    # Banks as soon as score is >= 30
    playerList.append(player(None, 30))

    # Banks as soon as score is >= 40
    playerList.append(player(None, 40))

    # Banks as soon as score is >= 50
    playerList.append(player(None, 50))

    # Banks as soon as score is >= 60
    playerList.append(player(None, 60))

    # Banks as soon as score is >= 70
    playerList.append(player(None, 70))

    # Banks as soon as score is >= 80
    playerList.append(player(None, 80))

    # Banks as soon as score is >= 90
    playerList.append(player(None, 90))

    # Banks as soon as score is >= 100
    playerList.append(player(None, 100))

    # Banks as soon as score is >= 110
    playerList.append(player(None, 110))

    # Banks as soon as score is >= 120
    playerList.append(player(None, 120))

    # Banks as soon as score is >= 130
    playerList.append(player(None, 130))

    # Banks as soon as score is >= 140
    playerList.append(player(None, 140))

    # Banks as soon as score is >= 150
    playerList.append(player(None, 150))

    # Banks as soon as score is >= 160
    playerList.append(player(None, 160))

    # Banks as soon as score is >= 170
    playerList.append(player(None, 170))

    # Banks as soon as score is >= 180
    playerList.append(player(None, 180))

    # Banks as soon as score is >= 190
    playerList.append(player(None, 190))

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

    # Banks as soon as score is >= 500
    playerList.append(player(None, 500))

    # Banks as soon as score is >= 600
    playerList.append(player(None, 600))

    # Banks as soon as score is >= 700
    playerList.append(player(None, 700))

    # Banks as soon as score is >= 800
    playerList.append(player(None, 800))

    # Banks as soon as score is >= 900
    playerList.append(player(None, 900))

    # Banks as soon as score is >= 1000
    playerList.append(player(None, 1000))

    # # Banks as soon as score is >= 1100
    # playerList.append(player(None, 1100))

    # # Banks as soon as score is >= 1200
    # playerList.append(player(None, 1200))

    # # Banks as soon as score is >= 1300
    # playerList.append(player(None, 1300))

    # # Banks as soon as score is >= 1400
    # playerList.append(player(None, 1400))

    # # Banks as soon as score is >= 1500
    # playerList.append(player(None, 1500))

    # # Banks as soon as score is >= 1600
    # playerList.append(player(None, 1600))

    # # Banks as soon as score is >= 1700
    # playerList.append(player(None, 1700))

    # # Banks as soon as score is >= 1800
    # playerList.append(player(None, 1800))

    # # Banks as soon as score is >= 1900
    # playerList.append(player(None, 1900))

    # # Banks as soon as score is >= 2000
    # playerList.append(player(None, 2000))

    # # Banks as soon as score is >= 2100
    # playerList.append(player(None, 2100))

    # # Banks as soon as score is >= 2200
    # playerList.append(player(None, 2200))

    # # Banks as soon as score is >= 2300
    # playerList.append(player(None, 2300))

    # # Banks as soon as score is >= 2400
    # playerList.append(player(None, 2400))

    # # Banks as soon as score is >= 2500
    # playerList.append(player(None, 2500))

    # # Banks as soon as score is >= 2600
    # playerList.append(player(None, 2600))

    # # Banks as soon as score is >= 2700
    # playerList.append(player(None, 2700))

    # # Banks as soon as score is >= 2800
    # playerList.append(player(None, 2800))

    # # Banks as soon as score is >= 2900
    # playerList.append(player(None, 2900))

    # # Banks as soon as score is >= 3000
    # playerList.append(player(None, 3000))

    # # Banks as soon as score is >= 4000
    # playerList.append(player(None, 4000))

    # # Banks as soon as score is >= 5000
    # playerList.append(player(None, 5000))

    # # Banks as soon as score is >= 8000
    # playerList.append(player(None, 8000))

    # # Banks as soon as score is >= 10000
    # playerList.append(player(None, 10000))

    # # Banks as soon as score is >= 12000
    # playerList.append(player(None, 12000))

    # # Banks as soon as score is >= 14000
    # playerList.append(player(None, 14000))

    # # Banks as soon as score is >= 16000
    # playerList.append(player(None, 16000))

    # # Banks as soon as score is >= 18000
    # playerList.append(player(None, 18000))

    # # Banks as soon as score is >= 20000
    # playerList.append(player(None, 20000))

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


def plotWins(playerList, winRate):
    # x-axis = score strategy, y-axis = number of wins
    playerStrategies = []
    for player in playerList:
        playerStrategies.append(player.scoreCountStrat)
    
    playerWins = []
    for player in winRate:
        playerWins.append(winRate[player])
    
    xpoints = np.array(playerStrategies)
    ypoints = np.array(playerWins)

    plt.plot(xpoints, ypoints, "o")
    plt.show()


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

    # print("Writing results to CSV.")
    # writeToCSV(playerList, [wins])

    plotWins(playerList, wins)


if __name__ == "__main__":
    main()
