file2 = "BowData.json"
file = "WeaponValues.json"
import json
import math

with open(file) as OpenFileVariable:
    LoadedWeaponFile = json.load(OpenFileVariable)
with open(file2) as OpenFileVariable2:
    LoadedBowFile = json.load(OpenFileVariable2)

WeaponList = LoadedWeaponFile['Weapons']
BowList = LoadedBowFile['Bows']


#Armor set bonus' and Food buffs

ArmorSetBonuses = {
    "atkup": 1.5,
    "ap": 1.8,
    "ancient_proficiency": 1.8,
    "gem_headgear": 1.2, #BUFFS ALL GUARDIAN AND ANCIENT WEAPONS AND WORKS ON EVERY ENEMY
    "midna_headgear": 1.2,  #BUFFS ALL GUARDIAN AND ANCIENT WEAPONS AND WORKS ON EVERY ENEMY
    "bone_atkup": 1.8,
    "none": 1.0
}

FoodBuff = {
    "lvl1": 1.2,
    "lvl2": 1.3,
    "lvl3": 1.5,
    "none": 1.0
}

#Modifiers

Talus4xBonus = 4.0
Talus2xBonus = 2.0
BoomerangThrownBonus = 1.5
RobbieBonus = 1.5
GuardianBonus = 1.3
HeadshotMultiplier = 2.0
SneakStrike = 8.0
ThrownOronHorseback = 2.0
FrozenEnemy = 3
MasterSwordBeam = 10
FullPoweredMasterSwordBeam = 20
FireAndIceElemental = 10
LightningElemental = 20
LightningDome = 40

chosenWeapon = (input("Enter Weapon:")).strip().replace(" ", "_").title()

if chosenWeapon == "Metal_Box":                                                     #EASTER EGG
    print("Damage dealt from a fully charged stasis'd metal box:", 100,
          "\nDamage dealt from a fully charged stasis'd metal box at a frozen enemy:", 300,
          "\nhttps://imgur.com/KUqZOYf")
    quit()

chosenMod = (input("Enter Modifier:")).strip().replace("yellowmod", "yellowbonusatkup").replace("yellow mod", "yellowbonusatkup").replace("whitemod", "whitebonusatkup").replace("white mod", "whitebonusatkup").lower()
chosenArmor = (input("Enter Armor Set Bonus:")).strip().replace(" ", "_").lower()
chosenFood = (input("Enter Food Buff:")).strip().replace(" ", "_").lower()

weaponVal = WeaponList[chosenWeapon]['baseatk']
armorVal = ArmorSetBonuses[chosenArmor]
foodVal = FoodBuff[chosenFood]

#Attribute checks
YellowAtkModCheck = WeaponList[chosenWeapon]['yellowbonusatkup']
WhiteAtkModCheck = WeaponList[chosenWeapon]['whitebonusatkup']
GuardianWeaponTypeCheck = WeaponList[chosenWeapon]['isguardianweapontype']
BoneWeaponTypeCheck = WeaponList[chosenWeapon]['isboneweapontype']
BowWeaponTypeCheck = WeaponList[chosenWeapon]['isbowweapontype']
RobbieWeaponTypeCheck = WeaponList[chosenWeapon]['isrobbieweapontype']
BoomerangWeaponTypeCheck = WeaponList[chosenWeapon]['isboomerangtype']

ElementalWeaponCheck = ["Frostblade", "Frostspear", "Great_Frostblade", "Blizzard_Rod", "Ice_Rod",
                        "Flameblade", "Flamespear", "Great_Flameblade", "Meteor_Rod", "Fire_Rod",
                        "Thunderblade", "Thunderspear", "Great_Thunderblade", "Thunderstorm_Rod", "Lightning_Rod"]
LightningWeapons = ["Frostblade", "Frostspear", "Great_Frostblade", "Blizzard_Rod", "Ice_Rod",
                        "Flameblade", "Flamespear", "Great_Flameblade", "Meteor_Rod", "Fire_Rod"]
FireAndIceWeapons = ["Thunderblade", "Thunderspear", "Great_Thunderblade", "Thunderstorm_Rod", "Lightning_Rod"]
#Checking user inputs

if chosenMod == "yellowbonusatkup":
    chosenMod = YellowAtkModCheck
elif chosenMod == "whitebonusatkup":
    chosenMod = WhiteAtkModCheck
else:
    chosenMod = 0

if chosenArmor == "atkup":
    foodVal = 1.0
elif chosenArmor in ("ap", "ancient_proficiency"):
    if not GuardianWeaponTypeCheck:
        armorVal = 1

elif chosenArmor == "bone_atkup":
    if not BoneWeaponTypeCheck:
        armorVal = 1

elif chosenArmor in ("gem_headgear", "midna_headgear"):
    if not GuardianWeaponTypeCheck:
        armorVal = 1

#Equation and result

result = math.floor((weaponVal + chosenMod) * armorVal * foodVal)

resultSNEAKSTRIKE = result * SneakStrike
resultGUARDIAN = result * GuardianBonus
resultTALUS2x = result * Talus2xBonus
resultTALUS4x = result * Talus4xBonus
resultROBBIE = result * RobbieBonus
resultBOOMERANG = result * BoomerangThrownBonus
resultTHROWorHORSEBACK = result * ThrownOronHorseback
resultFROZEN = result * FrozenEnemy

if chosenWeapon in FireAndIceWeapons:
    print("Damage total:", math.floor(result) + FireAndIceElemental)
    print("Damage dealt with a sneakstrike:", math.floor(resultSNEAKSTRIKE))
    print("Damage dealt if you threw the weapon or hit an enemy while on Horseback/MasterCycleZ:", math.floor(resultTHROWorHORSEBACK) + FireAndIceElemental)
    print("Damage dealt if the enemy is frozen:", math.floor(resultFROZEN))

elif chosenWeapon in LightningWeapons:
    print("Damage total:", math.floor(result) + LightningElemental)
    print("Damage dealt with a sneakstrike:", math.floor(resultSNEAKSTRIKE))
    print("Damage dealt if you threw the weapon or hit an enemy while on Horseback/MasterCycleZ:", math.floor(resultTHROWorHORSEBACK) + LightningElemental)
    print("Damage dealt if a normal enemy is hit while in the rain or frozen:", resultFROZEN + LightningElemental + LightningDome)

else:
    print("Damage total:", math.floor(result))
    print("Damage dealt with a sneakstrike:", math.floor(resultSNEAKSTRIKE))
    print("Damage dealt if you threw the weapon or hit an enemy while on Horseback/MasterCycleZ:", math.floor(resultTHROWorHORSEBACK))
    print("Damage dealt if the enemy is frozen:", math.floor(resultFROZEN))

#MASTERSWORD CHECK. CANNOT BE THROWN. Shoots a beam instead
if chosenWeapon == "Master_Sword":
    print("Damage dealt from the Master Swords beam:", MasterSwordBeam)
    print("Damage dealt from the Master Swords beam with Master Sword Beam Up Bonus:", math.floor(MasterSwordBeam * 1.5))
elif chosenWeapon == "Master_Sword_Full_Power":
    print("Damage dealt from the Full Power Master Sword beam:", FullPoweredMasterSwordBeam)
    print("Damage dealt from the Full Powered Master Swords beam with Master Sword Beam Up Bonus:", math.floor(FullPoweredMasterSwordBeam * 1.5))

#Checking for mining weapontype
elif chosenWeapon == "Iron_Sledgehammer":
    print("Damage dealt to a Talus:", math.floor(resultTALUS4x))
    print("Damage dealt to a Talus if the weapon were thrown:", math.floor(resultTALUS4x * ThrownOronHorseback))

elif chosenWeapon in ("Cobble_Crusher", "Stone_Smasher", "Boulder_Breaker"):
    print("Damage dealt against a Talus:", math.floor(resultTALUS2x))
    print("Damage dealt to a Talus if the weapon were thrown:", math.floor(resultTALUS4x * ThrownOronHorseback))

#Checking for guardian weapon type, apply 30% bonus
elif GuardianWeaponTypeCheck and not RobbieWeaponTypeCheck:
    print("Damage dealt against a Guardian:", math.floor(resultGUARDIAN))

#Checking for robbie weapon type, apply 50% bonus
elif RobbieWeaponTypeCheck:
    print("Damage dealt against a Guardian:", math.floor(resultROBBIE))
    print("Damage dealt from throwing the weapon or hitting a Guardian while on Horseback/MasterCycleZ:", math.floor(resultTHROWorHORSEBACK * RobbieBonus))

#Checking for boomerang weapon type
elif BoomerangWeaponTypeCheck:
    print("Damage dealt from throwing the boomerang:", math.floor(resultBOOMERANG))



