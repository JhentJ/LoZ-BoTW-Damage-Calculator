file2 = "BowData.json"
file = "WeaponValues.json"
import json
import math

with open(file) as OpenFileVariable:
    LoadedWeaponFile = json.load(OpenFileVariable)
with open(file2) as OpenFileVariable2:
    LoadedBowFile = json.load(OpenFileVariable2)
loopdata = True
while loopdata:

    WeaponList = LoadedWeaponFile['Weapons']
    BowList = LoadedBowFile['Bows']

    # Armor set bonus' and Food buffs

    ArmorSetBonuses = {
        "atkup": 1.5,
        "ap": 1.8,
        "ancient_proficiency": 1.8,
        "gem_headgear": 1.2,  # BUFFS ALL GUARDIAN AND ANCIENT WEAPONS AND WORKS ON EVERY ENEMY
        "midna_headgear": 1.2,  # BUFFS ALL GUARDIAN AND ANCIENT WEAPONS AND WORKS ON EVERY ENEMY
        "bone_atkup": 1.8,
        "none": 1.0
    }

    FoodBuff = {
        "lvl1": 1.2,
        "lvl2": 1.3,
        "lvl3": 1.5,
        "none": 1.0
    }

    # Modifiers
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

    weaponnames = [
        'Master_Sword',
        'Master_Sword_Full_Power',
        'Tree_Branch',
        'Torch',
        'Soup_Ladle',
        'Spring_Loaded_Hammer',
        'Travelers_Sword',
        'Soldiers_Broadsword',
        'Knights_Broadsword',
        'Royal_Broadsword',
        'Forest_Dwellers_Sword',
        'Zora_Sword',
        'Feathered_Edge',
        'Gerudo_Scimitar',
        'Moonlight_Scimitar',
        'Scimitar_of_the_Seven',
        'Eightfold_Blade',
        'Rusty_Broadsword',
        'Royal_Guards_Sword',
        'Flameblade',
        'Frostblade',
        'Thunderblade',
        'Goddess_Sword',
        'Sword',
        'Boko_Club',
        'Spiked_Boko_Club',
        'Lynel_Sword',
        'Mighty_Lynel_Sword',
        'Savage_Lynel_Sword',
        'Fire_Rod',
        'Meteor_Rod',
        'Ice_Rod',
        'Blizzard_Rod',
        'Lightning_Rod',
        'Thunderstorm_Rod',
        'Vicious_Sickle',
        'Demon_Carver',
        'Bokoblin_Arm',
        'Lizalfos_Arm',
        'Korok_Leaf',
        'Farming_Hoe',
        'Boat_Oar',
        'Woodcutters_Axe',
        'Double_Axe',
        'Travelers_Claymore',
        'Soldiers_Claymore',
        'Knights_Claymore',
        'Royal_Claymore',
        'Silver_Longsword',
        'Golden_Claymore',
        'Eightfold_Longblade',
        'Edge_of_Duality',
        'Rusty_Claymore',
        'Royal_Guards_Claymore',
        'Great_Flameblade',
        'Great_Frostblade',
        'Great_Thunderblade',
        'Sword_of_the_Six_Sages',
        'Biggorons_Sword',
        'Fierce_Deity_Sword',
        'Boko_Bat',
        'Spiked_Boko_Bat',
        'Moblin_Club',
        'Spiked_Moblin_Club',
        'Lynel_Crusher',
        'Mighty_Lynel_Crusher',
        'Savage_Lynel_Crusher',
        'Windcleaver',
        'Moblin_Arm',
        'Wooden_Mop',
        'Farmers_Pitchfork',
        'Fishing_Harpoon',
        'Throwing_Spear',
        'Travelers_Spear',
        'Soldiers_Spear',
        'Knights_Halberd',
        'Royal_Halberd',
        'Forest_Dwellers_Spear',
        'Zora_Spear',
        'Silverscale_Spear',
        'Ceremonial_Trident',
        'Lightscale_Trident',
        'Drillshaft',
        'Feathered_Spear',
        'Gerudo_Spear',
        'Serpentine_Spear',
        'Rusty_Halberd',
        'Royal_Guards_Spear',
        'Flamespear',
        'Frostspear',
        'Thunderspear',
        'Boko_Spear',
        'Spiked_Boko_Spear',
        'Moblin_Spear',
        'Spiked_Moblin_Spear',
        'Lizal_Spear',
        'Enhanced_Lizal_Spear',
        'Forked_Lizal_Spear',
        'Lynel_Spear',
        'Mighty_Lynel_Spear',
        'Savage_Lynel_Spear',
        'Dragonbone_Boko_Spear',
        'Dragonbone_Moblin_Spear',
        'Dragonbone_Boko_Bat',
        'Dragonbone_Moblin_Club',
        'Guardian_Sword',
        'Guardian_Sword2',
        'Guardian_Sword3',
        'Guardian_Spear',
        'Guardian_Spear2',
        'Guardian_Spear3',
        'Ancient_Battle_Axe',
        'Ancient_Battle_Axe2',
        'Ancient_Battle_Axe3',
        'Giant_Boomerang',
        'Lizal_Boomerang',
        'Lizal_Forked_Boomerang',
        'Lizal_Tri_Boomerang',
        'Boomerang',
        'Sea_Breeze_Boomerang',
        'Cobble_Crusher',
        'Stone_Smasher',
        'Boulder_Breaker',
        'Iron_Sledgehammer',
        'Ancient_Spear',
        'Ancient_Bladesaw',
        'Ancient_Short_Sword',
    ]

    data = True
    while data:
        chosenWeapon = (input("Enter Weapon:")).strip().replace(" ", "_").title()
        if chosenWeapon not in weaponnames:
            print('Invalid Entry. Please try again.')

        else:
            data = False

    data = True
    while data:
        chosenMod = (input("Enter Modifier:")).strip().replace("yellowmod", "yellowbonusatkup").replace("yellow mod",
                                                                                                        "yellowbonusatkup").replace(
            "whitemod", "whitebonusatkup").replace("white mod", "whitebonusatkup").lower()
        if chosenMod == "whitebonusatkup" or chosenMod == "yellowbonusatkup" or chosenMod == "none":
            data = False
        else:
            print('Invalid Entry. Please try again.')
            continue

    data = True
    while data:
        chosenArmor = (input("Enter Armor Set Bonus:")).strip().replace(" ", "_").lower()
        if chosenArmor not in ArmorSetBonuses:
            print('Invalid Entry. Please try again.')
            continue
        else:
            data = False

    data = True
    while data:
        chosenFood = (input("Enter Food Buff:")).strip().replace(" ", "_").lower()
        if chosenFood not in FoodBuff:
            print('Invalid Entry. Please try again')
            continue
        else:
            data = False

    weaponVal = WeaponList[chosenWeapon]['baseatk']
    armorVal = ArmorSetBonuses[chosenArmor]
    foodVal = FoodBuff[chosenFood]

    # Attribute checks

    YellowAtkModCheck = WeaponList[chosenWeapon]['yellowbonusatkup']
    WhiteAtkModCheck = WeaponList[chosenWeapon]['whitebonusatkup']
    WeaponTypeCheck = WeaponList[chosenWeapon]['weapontype']
    WeaponStyleCheck = WeaponList[chosenWeapon]['weaponstyle']

    ElementalWeaponCheck = ["Frostblade", "Frostspear", "Great_Frostblade", "Blizzard_Rod", "Ice_Rod",
                            "Flameblade", "Flamespear", "Great_Flameblade", "Meteor_Rod", "Fire_Rod",
                            "Thunderblade", "Thunderspear", "Great_Thunderblade", "Thunderstorm_Rod", "Lightning_Rod"]
    FireAndIceWeapons = ["Frostblade", "Frostspear", "Great_Frostblade", "Blizzard_Rod", "Ice_Rod",
                         "Flameblade", "Flamespear", "Great_Flameblade", "Meteor_Rod", "Fire_Rod"]
    LightningWeapons = ["Thunderblade", "Thunderspear", "Great_Thunderblade",
                        "Thunderstorm_Rod", "Lightning_Rod"]
    # Checking user inputs

    if chosenMod == "yellowbonusatkup":
        chosenMod = YellowAtkModCheck
    elif chosenMod == "whitebonusatkup":
        chosenMod = WhiteAtkModCheck
    else:
        chosenMod = 0
#TODO: ANCIENT WEAPONS ARENT BEING CALCULATED PROPERLY. armor val for AP gets changed to 0 for some reason
    if chosenArmor == "atkup":
        foodVal = 1.0
    elif chosenArmor in ("ap", "ancient_proficiency"):
        if WeaponTypeCheck not in ("ancient", "robbie"):
            armorVal = 1



    elif chosenArmor == "bone_atkup":
        if WeaponTypeCheck != "bone":
            armorVal = 1

    elif chosenArmor in ("gem_headgear", "midna_headgear"):
        if WeaponTypeCheck != "ancient" and WeaponTypeCheck != "robbie":
            armorVal = 1

    # Equation and result

    result = math.floor((weaponVal + chosenMod) * armorVal * foodVal)

    resultSNEAKSTRIKE = math.floor(result * SneakStrike)
    (resultGUARDIAN) = math.floor(result * GuardianBonus)
    resultTALUS2x = math.floor(result * Talus2xBonus)
    resultTALUS4x = math.floor(result * Talus4xBonus)
    resultROBBIE = math.floor(result * RobbieBonus)
    resultBOOMERANG = math.floor(result * BoomerangThrownBonus)
    resultTHROWorHORSEBACK = math.floor(result * ThrownOronHorseback)
    resultFROZEN = math.floor(result * FrozenEnemy)
    icespearspecificvalue = (result + FireAndIceElemental)

    if chosenWeapon in FireAndIceWeapons:
        print("[Damage Total]:", math.floor(result) + FireAndIceElemental)
        print("[SneakStrike]:", math.floor(resultSNEAKSTRIKE))
        print("[Thrown/Riding]:",
              math.floor(resultTHROWorHORSEBACK) + FireAndIceElemental)
        print("[FrozenEnemy]:", math.floor(resultFROZEN))
        if WeaponStyleCheck == "onehanded":
            print("[FlurryRush]:", (math.floor(result) * 7) + FireAndIceElemental)
        elif WeaponStyleCheck == "twohanded":
            print("[FlurryRush]:", (math.floor(result) * 4) + FireAndIceElemental)
        else:
            print("[FlurryRush]:", (math.floor(result) * 9) + FireAndIceElemental)
            if chosenWeapon == "Frostspear":
                print("[FullChargedAttack]:", (math.floor(result) * 7) + (icespearspecificvalue * 6))
                print("[FullChargedAttackFrozen]:", (math.floor(result) * 6) + (icespearspecificvalue * 7))

    elif chosenWeapon in LightningWeapons:
        print("[Damage Total]:", math.floor(result) + LightningElemental)
        print("[SneakStrike]:", math.floor(resultSNEAKSTRIKE))
        print("[Thrown] or [Riding]:", math.floor(resultTHROWorHORSEBACK) + LightningElemental)
        print("[Rain] or [EnemyIsFrozen]:", resultFROZEN + LightningElemental + LightningDome)
        if WeaponStyleCheck == "onehanded":
            print("[FlurryRush]:", math.floor(result) * 7 + LightningElemental)
            print("[FlurryRush][WetEnemy/Rain]:", math.floor(result) * 7 + LightningElemental + 160)
        elif WeaponStyleCheck == "twohanded":
            print("[FlurryRush]:", math.floor(result) * 4 + LightningElemental)
            print("[FlurryRush][WetEnemy/Rain]:", math.floor(result) * 4 + LightningElemental + 160)
        else:
            print("[FlurryRush]:", math.floor(result) * 9 + LightningElemental)
            print("[FlurryRush][WetEnemy/Rain]:", math.floor(result) * 9 + LightningElemental + 160)

    else:
        print("[Damage Total]:", math.floor(result))
        print("[SneakStrike]:", math.floor(resultSNEAKSTRIKE))
        print("[Thrown/Riding]:", math.floor(resultTHROWorHORSEBACK))
        print("[FrozenEnemy]:", math.floor(resultFROZEN))
        if WeaponStyleCheck == "onehanded":
            print("[FlurryRush]:", math.floor(result) * 7)
        elif WeaponStyleCheck == "twohanded":
            print("[FlurryRush]:", math.floor(result) * 4)
        else:
            print("[FlurryRush]:", math.floor(result) * 9)

    # MASTERSWORD CHECK. CANNOT BE THROWN. Shoots a beam instead
    if chosenWeapon == "Master_Sword":
        print("[Master Swords beam]:", MasterSwordBeam)
        print("[MasterSwordBeam + MasterSwordBeamUp Bonus]:", math.floor(MasterSwordBeam * 1.5))
    elif chosenWeapon == "Master_Sword_Full_Power":
        print("[FullPoweredMasterSwordBeam]:", FullPoweredMasterSwordBeam)
        print("[FullPoweredMasterSwordsBeam + MasterSwordBeamUpBonus]:", math.floor(FullPoweredMasterSwordBeam * 1.5))

    # Checking for mining weapontype
    elif chosenWeapon == "Iron_Sledgehammer":
        print("[Talus]:", math.floor(resultTALUS4x))
        print("[ThrownAtTalus]:", math.floor(resultTALUS4x * ThrownOronHorseback))

    elif chosenWeapon in ("Cobble_Crusher", "Stone_Smasher", "Boulder_Breaker"):
        print("[Talus]:", math.floor(resultTALUS2x))
        print("[ThrownAtTalus]:", math.floor(resultTALUS4x * ThrownOronHorseback))

    # Checking for guardian weapon type, apply 30% bonus
    elif WeaponTypeCheck == "ancient":
        print("[Guardian]:", math.floor(resultGUARDIAN))
        print("[Guardian] & [Thrown/Riding]:", math.floor(math.floor(resultGUARDIAN) * ThrownOronHorseback))
        if WeaponStyleCheck == "onehanded":
            print("[GuardianFlurryRush]:", math.floor(resultGUARDIAN) * 7)
        elif WeaponStyleCheck == "twohanded":
            print("[GuardianFlurryRush]:", math.floor(resultGUARDIAN) * 4)
        else:
            print("[GuardianFlurryRush]:", math.floor(resultGUARDIAN) * 9)

    # Checking for robbie weapon type, apply 50% bonus
    elif WeaponTypeCheck == "guardian & robbie":
        print("[Guardian]:", math.floor(resultROBBIE))
        print("[Guardian] & [Thrown/Riding]:", math.floor(math.floor(resultROBBIE) * ThrownOronHorseback))
        if WeaponStyleCheck == "onehanded":
            print("[GuardianFlurryRush]:", math.floor(resultROBBIE) * 7)
        elif WeaponStyleCheck == "twohanded":
            print("[GuardianFlurryRush]:", math.floor(resultROBBIE) * 4)
        else:
            print("[GuardianFlurryRush]:", math.floor(resultROBBIE) * 9)


    # Checking for boomerang weapon type
    elif WeaponTypeCheck == "boomerang":
        print("[BoomerangThrown]:", math.floor(resultBOOMERANG))

    data = True

    while data:
        loopdecision = input("Do you want to input another weapon? ").strip().lower()
        if loopdecision == 'yes':
            data = False
        elif loopdecision == 'no':
            data = False
            loopdata = False
        else:
            print('Invalid input. Try again. ')
            data = True


