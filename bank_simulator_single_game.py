from random import randrange


class player:
    def __init__(self, rollCountStrat, scoreCountStrat):
        self.rollCountStrat = rollCountStrat
        self.scoreCountStrat = scoreCountStrat
        self.gameScore = 0

    def __str__(self):
        return f"{self.gameScore} (rollStrat: {self.rollCountStrat}, scoreStrat: {self.scoreCountStrat}"

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
                    print(f"A 7 was rolled! Round over. Top round score: {roundScore}")
                    return roundScore
                if diceRoll[0] == "DOUBLE":
                    roundScore = roundScore * 2
                else:
                    roundScore = roundScore + diceRoll[1]
            print(
                f"Roll number: {rollNumber} \nDice Rolled: {diceRoll[0]} {diceRoll[1]}. \nCurrent round score: {roundScore}. \n"
            )

            if rollNumber >= 3:
                for player in remainingPlayers:
                    playerDecision = player.executeStrategy(rollNumber, roundScore)
                    # Player chooses to bank
                    if not playerDecision:
                        print(
                            f"A player is banking! rollCountStrat: {player.rollCountStrat}, scoreCountStrat: {player.scoreCountStrat}"
                        )
                        player.gameScore += roundScore
                        remainingPlayers.remove(player)

            input(f"Finished roll: {rollNumber}. Press Enter to continue...\n\n")
            rollNumber += 1
        print(f"All players have banked! Round over. Top round score: {roundScore}")

        return roundScore

    def playGame(self):
        for round in range(self.numberOfRounds):
            print(f"Starting round {round}! Current scores:")
            playerNumb = 1
            for player in self.players:
                print(f"Player {playerNumb}: {str(player)})")
                playerNumb += 1
            input(f"Press Enter to continue...\n\n")
            self.__playRound()

        print(f"GAME OVER! Final Scores:\n")
        playerNumb = 1
        for player in self.players:
            print(f"Player {playerNumb}: {str(player)})")
            playerNumb += 1


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


def main():
    playerList = initializePlayers()
    diceGame = game(playerList, 15)
    diceGame.playGame()

    # TODO: reset all player's scores before starting another game


if __name__ == "__main__":
    main()
