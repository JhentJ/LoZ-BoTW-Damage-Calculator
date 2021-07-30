import json
import math

file = "BowData.json"
abbreviations = [
"Rgb", "Slb", "Geb", "Fbd"
]
# Armor Bonuses
ArmorSetBonuses = {
    "atkup": 1.5,
    "ap": 1.8,
    "ancient_proficiency": 1.8,
    "gem_headgear": 1.2,
    "midnas_helmet": 1.2,
    "bone_atkup": 1.8,
    "none": 1.0

}

# Food Bonus
FoodBonuses = {
    "lvl1": 1.2,
    "lvl2": 1.3,
    "lvl3": 1.5,
    "none": 1.0
}

# Arrow Types
Arrows = {
    "normal": 0,
    "lightning": 20,
    "fire": 10,
    "ice": 10,
    "bomb": 50,
    "ancient_arrow": 1.5,
    "none": 0
    # Normal enemies can only receive up to two headshots from a multishot bow
    # Overworld bosses can receive headshots from all arrows though.

    # Elemental arrows add fixed damage. Fire and ice add ten, shock adds 20, and bomb arrows add 50. Bomb Arrows have two hitboxes on the explosion.
    # The explosion does 40 with 10 fire damage. Explosions off bomb arrows do a flat 50 damage if the arrow doesn't connect.
    # Ancient Arrows on overworld bosses, minus Lynels and Guardians, have a 1.5 damage multiplier. Shot at the body reduces their HP by ⅓.
    # Headshots off elemental arrows double the damage of the bow, then add the fixed damage.

    # Multi shot bows and elemental arrows only have one arrow do the flat damage.
    # So firing a Shock Arrow off a Savage Lynel Bow will only do an extra 20 damage.

}

loopdata = True
while loopdata:

    with open(file) as BowDataOpened:
        BowDataLoaded = json.load(BowDataOpened)

    BowList = BowDataLoaded['Bows']
    MultiShotBows = ["Duplex_Bow", "Lynel_Bow", "Mighty_Lynel_Bow", "Savage_Lynel_Bow", "Great_Eagle_Bow", "Forest_Dwellers_Bow"]
    BowListValidation = [
        'Bow_of_Light',
        'Wooden_Bow',
        'Travelers_Bow',
        'Soldiers_Bow',
        'Knights_Bow',
        'Royal_Bow',
        'Silver_Bow',
        'Swallow_Bow',
        'Falcon_Bow',
        'Golden_Bow',
        'Phrenic_Bow',
        'Royal_Guards_Bow',
        'Twilight_Bow',
        'Boko_Bow',
        'Spiked_Boko_Bow',
        'Lizal_Bow',
        'Strengthened_Lizal_Bow',
        'Steel_Lizal_Bow',
        'Forest_Dwellers_Bow',
        'Great_Eagle_Bow',
        'Lynel_Bow',
        'Mighty_Lynel_Bow',
        'Savage_Lynel_Bow',
        'Duplex_Bow',
        'Ancient_Bow',
    ]

    data = True
    while data:
        BowChoice = input('Enter Bow:').strip().replace(" ", "_").title()
        if BowChoice in BowListValidation or BowChoice in abbreviations:
            data = False
        else:
            print('Invalid Entry. Please try again.')

    while not data:
        if BowChoice == 'Slb':
            BowChoice = 'Savage_Lynel_Bow'
            data = True
        elif BowChoice == 'Rgb':
            BowChoice = 'Royal_Guards_Bow'
            data = True
        elif BowChoice == 'Geb':
            BowChoice = "Great_Eagle_Bow"
            data = True
        elif BowChoice == 'Fbd':
            BowChoice = 'Forest_Dwellers_Bow'
            data = True

    data = True
    while data:
        ModifierChoice = input('Enter Modifier:').strip().replace("yellowmod", "yellowbonusatkup").replace("yellow mod", "yellowbonusatkup").replace("whitemod", "whitebonusatkup").replace("white mod", "whitebonusatkup").lower()
        if ModifierChoice == "whitebonusatkup" or ModifierChoice == "yellowbonusatkup" or ModifierChoice == "none" or ModifierChoice == "fiveshot":
            data = False
        else:
            print('Invalid Entry. Please try again.')


    TwoShot = BowList[BowChoice]['twoshot']
    ThreeShot = BowList[BowChoice]['threeshot']
    FiveShot = BowList[BowChoice]['fiveshot']

    data = True
    while data:
        ArmorChoice = input('Enter Armor Bonus:').strip().lower().replace(" ", "_")
        if ArmorChoice in ArmorSetBonuses:
            data = False
        else:
            print("Invalid Entry. Please try again.")

    data = True
    while data:
        FoodChoice = input('Enter Food Bonus:').strip().lower().replace(" ", "_")
        if FoodChoice in FoodBonuses:
            data = False
        else:
            print("Invalid Entry. Please try again")

    data = True
    while data:
        ArrowChoice = input('Enter Arrow Type:').strip().lower().replace(" ", "_")
        if ArrowChoice in Arrows:
            data = False
        else:
            print("Invalid Entry. Please try again. ")


    BowValue = BowList[BowChoice]['baseatk']
    #Checking user input value and grabbing base atk value

    #Checking head shot value

    #Checking weapon type and damage mods
    WhiteModATK = BowList[BowChoice]['whitebonusatkup']
    YellowModATK = BowList[BowChoice]['yellowbonusatkup']
    BoneType = BowList[BowChoice]['isboneweapontype']
    GuardianType = BowList[BowChoice]['isguardianweapontype']
    RobbieType = BowList[BowChoice]['isrobbieweapontype']


    HeadShot = 2
    AncientBowBonus = 1.5

    FoodValue = FoodBonuses[FoodChoice]
    ArmorValue = ArmorSetBonuses[ArmorChoice]
    ArrowValue = Arrows[ArrowChoice]


    #checking for modifier choice
    if ModifierChoice == "whitebonusatkup":
        ModifierChoice = WhiteModATK
    elif ModifierChoice == "yellowbonusatkup":
        ModifierChoice = YellowModATK
    elif ModifierChoice == "fiveshot":
        ModifierChoice = 5
    else:
        ModifierChoice = 0

    #checking for food and armor choice
    if ArmorChoice == "atkup":
        FoodValue = 1

    #checking for bow type
    if ArmorChoice == "bone_atkup":
        if not BoneType:
            ArmorValue = 1
    elif ArmorChoice in ("ap", "ancient_proficiency", "gem_headgear", "midna_helmet"):
        if not GuardianType:
            ArmorValue = 1


    BaseResult = math.floor((BowValue + ModifierChoice) * FoodValue * ArmorValue)
    BaseResultTwoShot = math.floor(BaseResult * 2)
    BaseResultThreeShot = math.floor(BaseResult * 3)
    HeadShotResult = HeadShot * BaseResult
    #Ancient Bow Variables

    AncientBowResult = math.floor(math.floor(BowValue * FoodValue * ArmorValue) * AncientBowBonus)
    GuardianHeadshot = math.floor(AncientBowResult * HeadShot)

    if not FiveShot and not ThreeShot and not TwoShot:
        print("[Damage Dealt:]1", BaseResult + ArrowValue)
        print("[Headshot]:", HeadShotResult + ArrowValue)
    elif TwoShot:
        print("[Damage Dealt]2:", BaseResultTwoShot + ArrowValue)
        print("[Headshot]:", BaseResultTwoShot * TwoShot + ArrowValue)
    elif ModifierChoice == 5:
        ModifierChoice = math.floor((BowValue) * FoodValue * ArmorValue) + ArrowValue
        print("[Damage Dealt:]5", ModifierChoice * 5 + ArrowValue)
        print("[Headshot]:", ModifierChoice * 5 * HeadShot + ArrowValue)
    else:
        print("[Damage Dealt:]3", BaseResultThreeShot + ArrowValue)
        print("[Headshot]:", BaseResultThreeShot * HeadShot + ArrowValue)

    if ArrowChoice in ("fire", "ice", "lightning"):
        ArrowValue = 0
        print("Damage dealt to a Boss:", math.floor(BaseResult + ArrowValue))
        print("Damage dealt with a headshot to a Boss:", math.floor(HeadShotResult + ArrowValue))
    elif ArrowChoice == "bomb":
        ArrowValue = 40
        print("Damage dealt to a Boss:", math.floor(BaseResult + ArrowValue))
        print("Damage dealt with a headshot to a Boss:", math.floor(HeadShotResult + ArrowValue))
    # TODO: Implement a range of values. 5 - 15 dmg

    #Ancient Bow Check. Ancient Bow is special
    if BowChoice == "Ancient_Bow" and ArrowChoice == "normal":
        print("Damage Dealt to a Guardian enemy:", AncientBowResult + ArrowValue)
        print("Damage Dealt to a Guardian with a headshot:", math.floor(GuardianHeadshot + ArrowValue))
    elif ArrowChoice in ("lightning", "fire", "ice"):
        ArrowValue = 0
        print("Damage Dealt to a Guardian enemy:", math.floor(AncientBowResult + ArrowValue))
        print("Damage Dealt to a Guardian with a headshot:", math.floor(GuardianHeadshot + ArrowValue))
    elif ArrowChoice == "bomb":
        ArrowValue = (40 * .1)
        print("Damage Dealt to a Guardian enemy:", math.floor(AncientBowResult + ArrowValue))
        print("Damage Dealt to a Guardian with a headshot:", math.floor(GuardianHeadshot + ArrowValue))

    data = True

    while data:
        loopdecision = input("Do you want to input another weapon? ").strip().lower()
        if loopdecision == 'yes':
            data = False
        elif loopdecision == 'no':
            loopdata = False
            data = False
        else:
            print('Invalid input. Please try again.' )
            continue

