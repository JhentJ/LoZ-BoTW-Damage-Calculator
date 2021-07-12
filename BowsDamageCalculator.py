import json
import math
# TODO: -ERROR HANDLING -LOOP PROGRAM
file = "BowData.json"

with open(file) as BowDataOpened:
    BowDataLoaded = json.load(BowDataOpened)

BowList = BowDataLoaded['Bows']

WeaponChoice = input('Enter Bow:').strip().replace(" ", "_").title()
ModifierChoice = input('Enter Modifier:').strip().replace("yellowmod", "yellowbonusatkup").replace("yellow mod", "yellowbonusatkup").replace("whitemod", "whitebonusatkup").replace("white mod", "whitebonusatkup").lower().replace("five", "fiveshot").replace("three", "threeshot")

TwoShot = BowList[WeaponChoice]['twoshot']
ThreeShot = BowList[WeaponChoice]['threeshot']
FiveShot = BowList[WeaponChoice]['fiveshot']

ArmorChoice = input('Enter Armor Bonus:').strip().lower().replace(" ", "_")
FoodChoice = input('Enter Food Bonus:').strip().lower().replace(" ", "_")
ArrowChoice = input('Enter Arrow Type:').strip().lower().replace(" ", "_")
# TODO: add abbreviations for weapons. RGB Royal Guards Bow, SLB Savage Lynel Bow, GEB Great Eagle Bow, FDB Forest Dwellers Bow
BowValue = BowList[WeaponChoice]['baseatk']
#Checking user input value and grabbing base atk value

#Checking head shot value

#Checking weapon type and damage mods
WhiteModATK = BowList[WeaponChoice]['whitebonusatkup']
YellowModATK = BowList[WeaponChoice]['yellowbonusatkup']
BoneType = BowList[WeaponChoice]['isboneweapontype']
GuardianType = BowList[WeaponChoice]['isguardianweapontype']
RobbieType = BowList[WeaponChoice]['isrobbieweapontype']

#Armor Bonuses
ArmorSetBonuses = {
    "atkup": 1.5,
    "ap": 1.8,
    "ancient_proficiency": 1.8,
    "gem_headgear": 1.2,
    "midnas_helmet": 1.2,
    "bone_atkup": 1.8,
    "none": 1.0

}

#Food Bonus
FoodBonuses = {
    "lvl1": 1.2,
    "lvl2": 1.3,
    "lvl3": 1.5,
    "none": 1.0
}

#Arrow Types
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
#TODO: account for multishot bows having multiple multishot modifiers
BaseResult = math.floor((BowValue + ModifierChoice) * FoodValue * ArmorValue)
BaseResultTwoShot = math.floor(BaseResult * 2)
BaseResultThreeShot = math.floor(BaseResult * 3)
BaseResultFiveShot = math.floor(BowValue * FoodValue * ArmorValue) * 5
HeadShotResult = HeadShot * BaseResult

#Ancient Bow Variables
AncientBowResult = math.floor(math.floor(BowValue * FoodValue * ArmorValue) * AncientBowBonus)
GuardianHeadshot = math.floor(AncientBowResult * HeadShot)

if not FiveShot: #this gets used for normal bows
    print("Damage dealt to a/// normal enemy:", math.floor(BaseResult + ArrowValue))
    print("Damage dealt with a headshot:", math.floor(HeadShotResult + ArrowValue))
elif ModifierChoice == "fiveshot": #FIXME: fiveshot if statement is not working. Goes to 3 shot else statement instead. Restructure the whole thing. Create a list of all the multi shot bows and put that into a list
    print("Damage dealt to a normal enemy:", math.floor(BaseResultFiveShot + ArrowValue))
    print("Damage dealt with a headshot:", math.floor(BaseResultFiveShot * HeadShot + ArrowValue))
else:
    print("Damage dealt to ///a normal enemy:", math.floor(BaseResultThreeShot + ArrowValue))
    print("Damage dealt with a headshot:", math.floor(BaseResultThreeShot * HeadShot + ArrowValue))


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
if WeaponChoice == "Ancient_Bow" and ArrowChoice == "normal":
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
