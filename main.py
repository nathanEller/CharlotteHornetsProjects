"""
main fuction
"""
import rostersAndPlayers

def main():
        df = rostersAndPlayers.getRoster(2026)
        print(df)

        #playerID = rostersAndPlayers.playerNameToID("Brandon Miller")
        #print(playerID)

        #df = rostersAndPlayers.getPlayerStats("Bryce McGowens", "adv")
        #print(df)

if __name__ == "__main__":
        main()