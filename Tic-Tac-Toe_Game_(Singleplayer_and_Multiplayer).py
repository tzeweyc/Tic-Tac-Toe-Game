#tzeweyc
#Tic-Tac-Toe Game (Singleplayer and Multiplayer)

import time
import random

EMPTY = "."
X = "x"
O = "o"

PlayerScore = 0
ProgramScore = 0
Plays = 0
Score1 = 0
Score2 = 0
GameWon = False

def CreateGrid ():
    Grid = []
    for R in range(3):
        Grid.append([])
        for C in range(3):
            Grid[R].append(EMPTY)
    return Grid

def GetPlayerNames ():
    Player1 = input ("Player 1, please enter your name: ")
    Player2 = input ("Player 2, please enter your name: ")
    print ()
    return Player1, Player2

def GetPlayerName ():
    PlayerName = input ("Player, please enter your name: ")
    print ()
    return PlayerName

def GetPlayerSymbol ():
    PlayerSymbol = input ("Player, would you like to use an 'x' or an 'o'? ")
    while PlayerSymbol != "x" and PlayerSymbol != "o":
        print ("You keyed in value outside the range given. ")
        PlayerSymbol = input ("Player, would you like to use an 'x' or an 'o'? ")
    if PlayerSymbol == "x":
        PlayerSymbol = X
    elif PlayerSymbol == "o":
        PlayerSymbol = O
    return PlayerSymbol

def GetProgramSymbol (PlayerSymbol):
    if PlayerSymbol == X:
        ProgramSymbol = O
        print ("The computer will use the symbol 'o'.")
    elif PlayerSymbol == O:
        ProgramSymbol = X
        print ("The computer will use the symbol 'x'.")
    return ProgramSymbol

def Player1Symbol ():
    Symbol1 = input ("Player 1, would you like to use an 'x' or an 'o'? ")
    while Symbol1 != "x" and Symbol1 != "o":
        print ("You keyed in value outside the range given. ")
        Symbol1 = input ("Player 1, would you like to use an 'x' or an 'o'? ")
    if Symbol1 == "x":
        Symbol1 = X
    elif Symbol1 == "o":
        Symbol1 = O
    return Symbol1

def Player2Symbol (Symbol1):
    if Symbol1 == X:
        Symbol2 = O
        print ("Player 2, your symbol is o.")
    elif Symbol1 == O:
        Symbol2 = X
        print ("Player 2, your symbol is x.")
    return Symbol2

def GetColumnRow():
    print()
    Column = input("Please enter a column (between 0 and 2): ")
    Row = input("Please enter a row (between 0 and 2): ")
    print()
    return Column, Row

def CheckGetColumnInput(Column):
    try:
        Column = int(Column)
        if Column <= 2 and Column >= 0:
            return True
        else:
            return False
    except:
        return False

def CheckGetRowInput(Row):
    try:
        Row = int(Row)
        if Row <= 2 and Row >= 0:
            return True
        else:
            return False
    except:
        return False

def DisplayGrid (Grid):
    print()
    print("--")
    print("The grid looks like this:")  
    print ("{:2}".format(""), end="")
    for C in range(3):
        print(" {:2} ".format(str(C)), end="")
    print()
    for R in range(3):
        print ("{:3}".format(str(R)), end="")
        for C in range(3):
            if Grid[R][C] == X:
                print("{}".format(X), end="")
            elif Grid[R][C] == O:
                print("{}".format(O), end="")
            else:
                print("{}".format(EMPTY), end="")
            if C != 2:
                print(" {:2}".format("|"), end="")
        print()

def PlayGame_Multiplayer (Grid, GameWon, Score1, Score2, Plays):
    Moves = 0
    MaxMoves = 9
    Starting = Plays % 2
    if Starting == 1:
        Moves = 1
        MaxMoves = 10
    while GameWon is False and Moves < MaxMoves:
        Turn = Moves % 2
        DisplayGrid (Grid)
        print ()
        if Turn == 0:
            print ("It is ", Player1, "'s turn.")
            Column, Row = GetColumnRow()
        elif Turn == 1:
            print ("It is ", Player2, "'s turn.")
            Column, Row = GetColumnRow()
        while CheckGetColumnInput(Column) == False:
            print("You entered a value outside the range. Please try again.")
            Column = input("Please enter a column (between 0 and 2): ")
            print ()
        while CheckGetRowInput(Row) == False:
            print("You entered a value outside the range. Please try again.")
            Row = input("Please enter a row (between 0 and 2): ")
            print ()
        Column = int (Column)
        Row = int (Row)
        if Turn == 0:
            Grid = Player1Turn (Grid, Column, Row, Symbol1)
            GameWon = CheckWin_diagonallines (Grid, GameWon)
            GameWon = CheckWin_straightlines (Grid, GameWon)
            if GameWon == True:
                Score1 = Score1 + 1
                print ()
                print ("Congratulations, ", Player1, ", you won!")
            else: 
                Moves = Moves + 1
        elif Turn == 1:
            Grid = Player2Turn (Grid, Column, Row, Symbol2)
            GameWon = CheckWin_diagonallines (Grid, GameWon)
            GameWon = CheckWin_straightlines (Grid, GameWon)
            if GameWon == True:
                Score2 = Score2 + 1
                print ()
                print ("Congratulations, ", Player2, ", you won!")
            else:
                Moves = Moves + 1
    print ()
    DisplayGrid (Grid)
    if GameWon == True:
        print ()
        print ("End of current game, thank you.")
        print ()
    else:
        print ()
        print ("You both tied, no winners for this round.")
        print ("End of current game, thank you.")
        print ()
    Plays = Plays + 1
    return Score1, Score2, Plays

def PlayGame_Singleplayer (Grid, PlayerName, GameWon, ProgramScore, PlayerScore, Plays):
    Moves = 0
    MaxMoves = 9
    Starting = Plays % 2
    if Starting == 1:
        Moves = 1
        MaxMoves = 10
    while GameWon == False and Moves < MaxMoves:
        Turn = Moves % 2
        if Turn == 0:
            DisplayGrid (Grid)
            print ()
            print ("It is ", PlayerName, "'s turn.")
            Grid, Row, Column = MakeMovePlayer (Grid, PlayerSymbol)
            GameWon = CheckWin_diagonallines (Grid, GameWon)
            GameWon = CheckWin_straightlines (Grid, GameWon)
            if GameWon == True:
                PlayerScore = PlayerScore + 1
                Plays = Plays + 1
                print ("Congratulations", PlayerName, ", you won!")
                print ()
                DisplayGrid (Grid)
                print ()
                print ("End of current game, thank you.")
                print ()
            else:
                Moves = Moves + 1
        elif Turn == 1:
            DisplayGrid (Grid)
            print ()
            print ("It is the computer's turn.")
            Grid = MakeMoveProgram (Grid, PlayerSymbol, ProgramSymbol)
            GameWon = CheckWin_diagonallines (Grid, GameWon)
            GameWon = CheckWin_straightlines (Grid, GameWon)
            if GameWon == True:
                ProgramScore = ProgramScore + 1
                Plays = Plays + 1
                print ("The computer won this round.")
                print ()
                DisplayGrid (Grid)
                print ()
                print ("End of current game, thank you.")
                print ()
            else:
                Moves = Moves + 1
    if GameWon == False:
        print ()
        print ("You tied, no winners for this round.")
        print ("End of current game, thank you.")
        DisplayGrid (Grid)
        print ()
        Plays = Plays + 1
    return PlayerScore, ProgramScore, Plays

def Player1Turn (Grid, Column, Row, Symbol1):
    if CheckCharacter(Grid[Row][Column]) == "Unfilled":
        print("Alright, thank you.")
        Grid[Row][Column] = Symbol1
    elif CheckCharacter(Grid[Row][Column]) == "Filled":
        print("Someone has already selected the tile (" + str(Column) + "," + str(Row) + ") before.")
        while CheckCharacter(Grid[Row][Column]) == "Filled":
            Column, Row = GetColumnRow()
            while CheckGetColumnInput(Column) is False:
                print("You entered a value outside the range. Please try again.")
                Column = input("Please enter a column (between 0 and 2): ")
                print ()
            while CheckGetRowInput(Row) is False:
                print("You entered a value outside the range. Please try again.")
                Row = input("Please enter a row (between 0 and 2): ")
                print ()
            Column = int (Column)
            Row = int (Row)
            CharacterType = CheckCharacter(Grid[Row][Column])
    Grid[Row][Column] = Symbol1
    return Grid

def Player2Turn (Grid, Column, Row, Symbol2):
    if CheckCharacter(Grid[Row][Column]) == "Unfilled":
        print("Alright, thank you.")
        Grid[Row][Column] = Symbol2
    elif CheckCharacter(Grid[Row][Column]) == "Filled":
        while CheckCharacter(Grid[Row][Column]) == "Filled":
            print("Someone has already selected the tile (" + str(Column) + "," + str(Row) + ") before.")
            Column, Row = GetColumnRow()
            while CheckGetColumnInput(Column) is False:
                print("You entered a value outside the range. Please try again.")
                Column = input("Please enter a column (between 0 and 2): ")
                print ()
            while CheckGetRowInput(Row) is False:
                print("You entered a value outside the range. Please try again.")
                Row = input("Please enter a row (between 0 and 2): ")
                print ()
            Column = int (Column)
            Row = int (Row)
            CharacterType = CheckCharacter(Grid[Row][Column])
    Grid[Row][Column] = Symbol2
    return Grid

def MakeMovePlayer (Grid, PlayerSymbol):
    Column, Row = GetColumnRow()
    while CheckGetColumnInput(Column) is False:
        print("You entered a value outside the range. Please try again.")
        Column = input("Please enter a row (between 0 and 2): ")
        print ()
    while CheckGetRowInput(Row) is False:
        print("You entered a value outside the range. Please try again.")
        Row = input("Please enter a row (between 0 and 2): ")
        print ()
    Column = int (Column)
    Row = int (Row)
    if CheckCharacter(Grid[Row][Column]) == "Unfilled":
        print("Alright, thank you.")
        Grid[Row][Column] = PlayerSymbol
    elif CheckCharacter(Grid[Row][Column]) == "Filled":
        print("Someone has already selected the tile (" + str(Column) + "," + str(Row) + ") before.")
        while CheckCharacter(Grid[Row][Column]) == "Filled":
            Column, Row = GetColumnRow()
            while CheckGetColumnInput(Column) is False:
                print("You entered a value outside the range. Please try again.")
                Column = input("Please enter a row (between 0 and 2): ")
                print ()
            while CheckGetRowInput(Row) is False:
                print("You entered a value outside the range. Please try again.")
                Row = input("Please enter a row (between 0 and 2): ")
                print ()
            Column = int (Column)
            Row = int (Row)
            CharacterType = CheckCharacter(Grid[Row][Column])
    Grid[Row][Column] = PlayerSymbol
    return Grid, Row, Column

def MakeMoveProgram (Grid, PlayerSymbol, ProgramSymbol):
    for R in range (0, 3):
        if Grid [R][0] == Grid [R][1]:
            if Grid [R][1] == ProgramSymbol:
                if CheckCharacter(Grid [R][2]) == "Unfilled":
                    Grid [R][2] = ProgramSymbol
                    return Grid
        if Grid [R][1] == Grid [R][2]:
            if Grid [R][1] == ProgramSymbol:
                if CheckCharacter(Grid [R][0]) == "Unfilled":
                    Grid [R][0] = ProgramSymbol
                    return Grid
        if Grid [R][0] == Grid [R][2]:
            if Grid [R][2] == ProgramSymbol:
                if CheckCharacter(Grid [R][1]) == "Unfilled":
                    Grid [R][1] = ProgramSymbol
                    return Grid
    for C in range (0, 3):
        if Grid [0][C] == Grid [1][C]:
            if Grid [1][C] == ProgramSymbol:
                if CheckCharacter(Grid [2][C]) == "Unfilled":
                    Grid [2][C] = ProgramSymbol
                    return Grid
        if Grid [1][C] == Grid [2][C]:
            if Grid [1][C] == ProgramSymbol:
                if CheckCharacter(Grid [0][C]) == "Unfilled":
                    Grid [0][C] = ProgramSymbol
                    return Grid
        if Grid [0][C] == Grid [2][C]:
            if Grid [2][C] == ProgramSymbol:
                if CheckCharacter(Grid [1][C]) == "Unfilled":
                    Grid [1][C] = ProgramSymbol
                    return Grid
    if Grid [0][0] == Grid [1][1]:
        if Grid [1][1] == ProgramSymbol:
            if CheckCharacter(Grid [2][2]) == "Unfilled":
                Grid [2][2] = ProgramSymbol
                return Grid
    if Grid [1][1] == Grid [2][2]:
        if Grid [1][1] == ProgramSymbol:
            if CheckCharacter(Grid [0][0]) == "Unfilled":
                Grid [0][0] = ProgramSymbol
                return Grid
    if Grid [0][0] == Grid [2][2]:
        if Grid [0][0] == ProgramSymbol:
            if CheckCharacter(Grid [1][1]) == "Unfilled":
                Grid [1][1] = ProgramSymbol
                return Grid
    if Grid [0][2] == Grid [1][1]:
        if Grid [1][1] == ProgramSymbol:
            if CheckCharacter(Grid [2][0]) == "Unfilled":
                Grid [2][0] = ProgramSymbol
                return Grid
    if Grid [1][1] == Grid [2][0]:
        if Grid [1][1] == ProgramSymbol:
            if CheckCharacter(Grid [0][2]) == "Unfilled":
                Grid [0][2] = ProgramSymbol
                return Grid
    if Grid [0][2] == Grid [2][0]:
        if Grid [0][2] == ProgramSymbol:
            if CheckCharacter(Grid [1][1]) == "Unfilled":
                Grid [1][1] = ProgramSymbol
                return Grid
    for R in range (0, 3):
        if Grid [R][0] == Grid [R][1]:
            if Grid [R][1] == PlayerSymbol:
                if CheckCharacter(Grid [R][2]) == "Unfilled":
                    Grid [R][2] = ProgramSymbol
                    return Grid
        if Grid [R][1] == Grid [R][2]:
            if Grid [R][1] == PlayerSymbol:
                if CheckCharacter(Grid [R][0]) == "Unfilled":
                    Grid [R][0] = ProgramSymbol
                    return Grid
        if Grid [R][0] == Grid [R][2]:
            if Grid [R][2] == PlayerSymbol:
                if CheckCharacter(Grid [R][1]) == "Unfilled":
                    Grid [R][1] = ProgramSymbol
                    return Grid
    for C in range (0, 3):
        if Grid [0][C] == Grid [1][C]:
            if Grid [1][C] == PlayerSymbol:
                if CheckCharacter(Grid [2][C]) == "Unfilled":
                    Grid [2][C] = ProgramSymbol
                    return Grid
        if Grid [1][C] == Grid [2][C]:
            if Grid [1][C] == PlayerSymbol:
                if CheckCharacter(Grid [0][C]) == "Unfilled":
                    Grid [0][C] = ProgramSymbol
                    return Grid
        if Grid [0][C] == Grid [2][C]:
            if Grid [2][C] == PlayerSymbol:
                if CheckCharacter(Grid [1][C]) == "Unfilled":
                    Grid [1][C] = ProgramSymbol
                    return Grid
    if Grid [0][0] == Grid [1][1]:
        if Grid [1][1] == PlayerSymbol:
            if CheckCharacter(Grid [2][2]) == "Unfilled":
                Grid [2][2] = ProgramSymbol
                return Grid
    if Grid [1][1] == Grid [2][2]:
        if Grid [1][1] == PlayerSymbol:
            if CheckCharacter(Grid [0][0]) == "Unfilled":
                Grid [0][0] = ProgramSymbol
                return Grid
    if Grid [0][0] == Grid [2][2]:
        if Grid [0][0] == PlayerSymbol:
            if CheckCharacter(Grid [1][1]) == "Unfilled":
                Grid [1][1] = ProgramSymbol
                return Grid
    if Grid [0][2] == Grid [1][1]:
        if Grid [1][1] == PlayerSymbol:
            if CheckCharacter(Grid [2][0]) == "Unfilled":
                Grid [2][0] = ProgramSymbol
                return Grid
    if Grid [1][1] == Grid [2][0]:
        if Grid [1][1] == PlayerSymbol:
            if CheckCharacter(Grid [0][2]) == "Unfilled":
                Grid [0][2] = ProgramSymbol
                return Grid
    if Grid [0][2] == Grid [2][0]:
        if Grid [0][2] == PlayerSymbol:
            if CheckCharacter(Grid [1][1]) == "Unfilled":
                Grid [1][1] = ProgramSymbol
                return Grid
    ProgramRow = random.randint (0, 2)
    ProgramColumn = random.randint (0, 2)
    while CheckCharacter(Grid [ProgramRow][ProgramColumn]) == "Filled":
        ProgramRow = random.randint (0, 2)
        ProgramColumn = random.randint (0, 2)
    Grid [ProgramRow][ProgramColumn] = ProgramSymbol
    return Grid

def CheckCharacter(CharacterSymbol):
    CharacterType = "None"
    if CharacterSymbol == O or CharacterSymbol == X:
        CharacterType = "Filled"
    elif CharacterSymbol == EMPTY:
        CharacterType = "Unfilled"
    return CharacterType

def CheckWin_diagonallines (Grid, GameWon):
    if Grid [0][0] == Grid [1][1] == Grid [2][2]:
        if Grid [1][1] == X or Grid [1][1] == O:
                GameWon = True
    if Grid [0][2] == Grid [1][1] == Grid [2][0]:
        if Grid [1][1] == X or Grid [1][1] == O:
                GameWon = True
    return GameWon

def CheckWin_straightlines (Grid, GameWon):
    for R in range (0,3):
        if Grid [R][0] == Grid [R][1] == Grid [R][2]:
            if Grid [R][0] == X or Grid [R][0] == O:
                GameWon = True
    for C in range (0,3):
        if Grid [0][C] == Grid [1][C] == Grid [2][C]:
            if Grid [0][C] == X or Grid [0][C] == O:
                GameWon = True
    return GameWon

def CheckScore_Multiplayer(Score1, Score2, Player1, Player2, Plays, Symbol1, Grid, GameWon):
    print ()
    print ("End of game, thank you for playing.")
    print (Player1, " and ", Player2, ", you have played a total of", Plays, " time(s), and the winner is: ")
    for i in range(3):
        print(".", end =' ')
        time.sleep(1)
    print ()
    print ()
    if Score1 > Score2:
        print (Player1, "! You won a total of", Score1, "game(s).")
        print (Player2, ", you won a total of", Score2, "game(s).")
        print ("Thank you for playing! Have a nice day ahead, ", Player1, " and ", Player2, ".")
    elif Score2 > Score1:
        print (Player2, "! You won a total of", Score2, "game(s).")
        print (Player1, ", you won a total of", Score1, "game(s).")
        print ("Thank you for playing! Have a nice day ahead, ", Player1, " and ", Player2, ".")
    elif Score1 == Score2:
        print ("Well, you both tied in the game.")
        print ()
        PlayAgain = input("Would you like to play a tie-breaker round? (y/n) ")
        if PlayAgain == 'y':
            Symbol1 = Player1Symbol ()
            Symbol2 = Player2Symbol (Symbol1)
            Grid = CreateGrid ()
            Score1, Score2, Plays = PlayGame_Multiplayer (Grid, GameWon, Score1, Score2, Plays)
            CheckScore_Multiplayer(Score1, Score2, Player1, Player2, Plays, Symbol1, Grid, GameWon)
        elif PlayAgain == 'n':
            print ()
            print ("Alright, thank you for playing! Have a nice day ahead, ", Player1, " and ", Player2, ".")
            MenuOption = "9"
            
def CheckScore_Singleplayer (PlayerScore, ProgramScore, PlayerName, Plays, PlayerSymbol, Grid, GameWon):
    print ()
    print ("End of game, thank you for playing.")
    print (PlayerName, ", you have played a total of", Plays, " time(s).")
    for i in range(3):
        print(".", end =' ')
        time.sleep(1)
    print ()
    print ()
    if PlayerScore > ProgramScore:
        print (PlayerName, ", you won a total of", PlayerScore, "game(s).")
        print ("You are the winner!")
        print ("The computer won a total of", ProgramScore, "game(s).")
        print ()
    elif ProgramScore > PlayerScore:
        print ("The computer won a total of", ProgramScore, "game(s).")
        print (PlayerName, ", you won a total of", PlayerScore, "game(s).")
        print ("Unfortunately, you did not win. Try again next time! ")
        print ()
    elif PlayerScore == ProgramScore:
        print ("Well, you are tied with the computer.")
        print ()
        PlayAgain = input("Would you like to play a tie-breaker round? (y/n) ")
        if PlayAgain == 'y':
            PlayerName = GetPlayerName ()
            PlayerSymbol = GetPlayerSymbol ()
            ProgramSymbol = GetProgramSymbol (PlayerSymbol)
            Grid = CreateGrid ()
            PlayerScore, ProgramScore, Plays = PlayGame_Singleplayer (Grid, PlayerName, GameWon,  ProgramScore, PlayerScore, Plays)
            CheckScore_Singleplayer(PlayerScore, ProgramScore, PlayerName, Plays, PlayerSymbol, Grid, GameWon)
        elif PlayAgain == 'n':
            print ()
            MenuOption = "9"
    print ("Thank you for playing! Have a nice day ahead, ", PlayerName, ".")


def DisplayMenu():
    print ("Hi there, welcome to a classic game of Tic-Tac-Toe!")
    print ("Start the game, and choose whether you would like to play again at the end of each game.")
    print ("Your accumulated score will be displayed when you wish not to play anymore, along with who won.")
    print ("You will take turns to start first.")
    print ("Have fun! :)")
    print ()
    print("MAIN MENU")
    print()
    print("1. Play multiplayer game")
    print("2. Player singleplayer game")
    print("9. Quit")
    print()
    
def GetMainMenuChoice():
    print ("What would you like to do? ")
    Choice = input("Please enter your choice ('1'/'2'/'9'): ")
    print()
    return Choice[0]

if __name__ == "__main__":
    MenuOption = "0"
    while MenuOption != "9" and Plays == 0:
        DisplayMenu ()
        MenuOption = GetMainMenuChoice()
        if MenuOption == "1":
            Player1, Player2 = GetPlayerNames ()
            Symbol1 = Player1Symbol ()
            Symbol2 = Player2Symbol (Symbol1)
            Grid = CreateGrid ()
            Score1, Score2, Plays = PlayGame_Multiplayer (Grid, GameWon, Score1, Score2, Plays)
        if MenuOption == "2":
            PlayerName = GetPlayerName ()
            PlayerSymbol = GetPlayerSymbol ()
            ProgramSymbol = GetProgramSymbol (PlayerSymbol)
            Grid = CreateGrid ()
            PlayerScore, ProgramScore, Plays = PlayGame_Singleplayer (Grid, PlayerName, GameWon,  ProgramScore, PlayerScore, Plays)
        if MenuOption == "9":
            print ("Goodbye!")
    while MenuOption != "9" and Plays >= 1:
        if MenuOption == "1":
            PlayAgain = input("Would you like to play again? (y/n) ")
            print ()
            if PlayAgain == 'y':
                Symbol1 = Player1Symbol ()
                Symbol2 = Player2Symbol (Symbol1)
                Grid = CreateGrid ()
                Score1, Score2, Plays = PlayGame_Multiplayer (Grid, GameWon, Score1, Score2, Plays)
            elif PlayAgain == 'n':
                CheckScore_Multiplayer (Score1, Score2, Player1, Player2, Plays, Symbol1, Grid, GameWon)
                MenuOption = "9"
        if MenuOption == "2":
            PlayAgain = input("Would you like to play again? (y/n) ")
            print ()
            if PlayAgain == 'y':
                PlayerSymbol = GetPlayerSymbol ()
                ProgramSymbol = GetProgramSymbol (PlayerSymbol)
                Grid = CreateGrid ()
                PlayerScore, ProgramScore, Plays = PlayGame_Singleplayer (Grid, PlayerName, GameWon,  ProgramScore, PlayerScore, Plays)
            elif PlayAgain == 'n':
                CheckScore_Singleplayer (PlayerScore, ProgramScore, PlayerName, Plays, PlayerSymbol, Grid, GameWon)
                MenuOption = "9"
