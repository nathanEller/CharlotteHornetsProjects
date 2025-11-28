"""
main fuction
"""
import rostersAndPlayers

def main():
        #df = rostersAndPlayers.getRoster(2019)
        #print(df)

        #playerID = rostersAndPlayers.playerNameToID("Brandon Miller")
        #print(playerID)

        df = rostersAndPlayers.getPlayerStats("LaMelo Ball", "counting")
        print(df)

if __name__ == "__main__":
        main()