#(error message for if targeted game has not been played)
#(error message for invalid username)
#(error message for invalid game selection)
#(add option for all and main, including rank, cosmetics, and more in game_type (supported by api as "all" and "main"))

import webbrowser
import requests

#gets the information for the correct api url
username = input("What is the Hive username you wish to receive information about? ")
game_type = input("Which game would you like your stats for?  Available values: wars, dr, hide, sg, murder, sky, ctf, drop, ground, build, party, bridge, grav: ")

#gets the response from the api url
stats = requests.get(f"https://api.playhive.com/v0/game/all/{game_type}/{username}")
print (stats.json())

#if the game type is wars, parses the response and prints it in the terminal
if game_type == ("wars"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    final_kills = stats.json()["final_kills"]
    print(f"final kills: {final_kills}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")
    treasure_destroyed = stats.json()["treasure_destroyed"]
    print(f"treasures destroyed: {treasure_destroyed}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")

#if the game type is dr, parses the response and prints it in the terminal
if game_type == ("dr"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    checkpoints = stats.json()["checkpoints"]
    print(f"checkpoints: {checkpoints}")
    activated = stats.json()["activated"]
    print(f"traps activated: {activated}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")

#if the game type is hide, parses the response and prints it in the terminal
if game_type == ("hide"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    hider_kills = stats.json()["hider_kills"]
    print(f"hider kills: {hider_kills}")

#if the game type is sg, parses the response and prints it in the terminal
if game_type == ("sg"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    crates = stats.json()["crates"]
    print(f"crates opened: {crates}")
    deathmatches = stats.json()["deathmatches"]
    print(f"deathmatches reached: {deathmatches}")
    cows = stats.json()["cows"]
    print(f"cache cows: {cows}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")

#if the game type is murder, parses the response and prints it in the terminal
if game_type == ("murder"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    coins = stats.json()["coins"]
    print(f"coins collected: {coins}")
    murders = stats.json()["murders"]
    print(f"murders: {murders}")
    murderer_eliminations = stats.json()["murderer_eliminations"]
    print(f"murderer eliminations: {murderer_eliminations}")

#if the game type is sky, parses the response and prints it in the terminal
if game_type == ("sky"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")
    mystery_chests_destroyed = stats.json()["mystery_chests_destroyed"]
    print(f"mystery chests destroyed: {mystery_chests_destroyed}")   
    ores_mined = stats.json()["ores_mined"]
    print(f"ores mined: {ores_mined}")
    spells_used = stats.json()["spells_used"]
    print(f"spells used: {spells_used}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")

#if the game type is ctf, parses the response and prints it in the terminal
if game_type == ("ctf"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    assists = stats.json()["assists"]
    print(f"assists: {assists}")  
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    flags_captured = stats.json()["flags_captured"]
    print(f"flags captured: {flags_captured}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")
    flags_returned = stats.json()["flags_returned"]
    print(f"flags returned: {flags_returned}")

#if the game type is drop, parses the response and prints it in the terminal
if game_type == ("drop"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    blocks_destroyed = stats.json()["blocks_destroyed"]
    print(f"blocks destroyed: {blocks_destroyed}")
    powerups_collected = stats.json()["powerups_collected"]
    print(f"powerups collected: {powerups_collected}")
    vaults_used = stats.json()["vaults_used"]
    print(f"vaults used: {vaults_used}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")

#if the game type is ground, parses the response and prints it in the terminal
if game_type == ("ground"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    blocks_destroyed = stats.json()["blocks_destroyed"]
    print(f"blocks destroyed: {blocks_destroyed}")
    blocks_placed = stats.json()["blocks_placed"]
    print(f"blocks placed: {blocks_placed}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    projectiles_fired = stats.json()["projectiles_fired"]
    print(f"projectiles fired: {projectiles_fired}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")

#if the game type is build, parses the response and prints it in the terminal
if game_type == ("build"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    rating_good_received = stats.json()["rating_good_received"]
    print(f"rating good received: {rating_good_received}")
    rating_meh_received = stats.json()["rating_meh_received"]
    print(f"rating meh received: {rating_meh_received}")
    rating_okay_received = stats.json()["rating_okay_received"]
    print(f"rating okay received: {rating_okay_received}")   
    rating_great_received = stats.json()["rating_great_received"]
    print(f"rating great received: {rating_great_received}")  

#if the game type is party, parses the response and prints it in the terminal
if game_type == ("party"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    powerups_collected = stats.json()["powerups_collected"]
    print(f"powerups collected: {powerups_collected}")
    rounds_survived = stats.json()["rounds_survived"]
    print(f"rounds survived: {rounds_survived}")

#if the game type is bridge, parses the response and prints it in the terminal
if game_type == ("bridge"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    kills = stats.json()["kills"]
    print(f"kills: {kills}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    goals = stats.json()["goals"]
    print(f"goals: {goals}")

#if the game type is grav, parses the response and prints it in the terminal
if game_type == ("grav"):
    xp = stats.json()["xp"]
    print(f"xp: {xp}")
    played = stats.json()["played"]
    print(f"played: {played}")
    victories = stats.json()["victories"]
    print(f"victories: {victories}")
    first_played = stats.json()["first_played"]
    print(f"first played: {first_played}")
    deaths = stats.json()["deaths"]
    print(f"deaths: {deaths}")
    maps_completed = stats.json()["maps_completed"]
    print(f"maps completed: {maps_completed}")
    maps_completed_without_dying = stats.json()["maps_completed_without_dying"]
    print(f"maps completed without dying: {maps_completed_without_dying}")