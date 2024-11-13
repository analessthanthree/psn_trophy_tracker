from psnawp_api import PSNAWP
from psnawp_api.models.trophies import PlatformType

from time import sleep
from pprint import pp

#######################################################################
# When putting your code in here, make sure to keep the double quotes
npsso = "YourCodeGoesHere"
#######################################################################

#######################################################################
# Do not edit beyond this point unless
# you know what you're doing :)
#######################################################################

output_file = "./trophies.txt"

user_platform = PlatformType.UNKNOWN
while user_platform.name == "UNKNOWN":
    print("Type the platform of the game you wish to track, then hit Enter")
    for platform in PlatformType:
        if platform.name == "UNKNOWN":
            continue
        print(f"  {platform.name}")
    user_input = input("Platform: ").upper()
    try:
        user_platform = PlatformType[user_input]
    except:
        continue

print("------------------------------------------------")

psnawp = PSNAWP(npsso)
client = psnawp.me()

title_stats = list(client.title_stats())

# Keep only the games of user's selected PlatformType
title_stats = [ title for title in title_stats if title.category.name == user_platform.name ]

# TODO basic error handling in case somebody types something that's not a number
print("Type the number of the game you wish to track, then hit Enter")
for i,title in enumerate(title_stats):
    print(f"  {i}. {title.name}")

game_index = int(input("Game: "))
game = title_stats[game_index]

# The np_communication_id for the game is necessary to query trophies
np_comm_id = psnawp.game_title(game.title_id, client.account_id).np_communication_id

print("------------------------------------------------")

while True:
    # Get the trophies for the selected game
    trophies = list(client.trophies(np_comm_id, user_platform, trophy_group_id='all', include_progress=True))
    collected = [ trophy for trophy in trophies if trophy.earned ]

    # Write to file
    with open(output_file, 'w') as f:
        f.write(f"{len(collected)}/{len(trophies)}")

    sleep(60)
