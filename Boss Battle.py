"""
 Boss Battle Attempt
 Where I try to develop a boss fight within Python
 Things to add eventually:
   1. Defend Function (Using division)
   2. More Attacks (Special Attack that deals more damage)
       2A. A mana system 
   3. More fluid actions (Attack animations?)
"""
import random
commands = ["ATTACK", "BAG", "RUN"]
bagOptions = ["HEALTH POTION", "STRENGTH POTION"]
bossHealth = 250
yourHealth = 250
swordAttack = 50
potionHeal = 35
bossHeal = 45
strengthPotionBuff =  1.5
healthPotioncount = 5
strengthPotioncount = 5
bossAttack = random.randint(1,3)
bossAttackdamage = random.randint(15,35)
progFiredamage = 5
progFiredamagecondition = False

# Boss prompt

print("\n\t\tFronnyt, Champion Of The Skies, blocks your path!")

print("""   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(>: :<)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v) """)
print("""
    _ ,                                    
  ,- -                                  ,  
 _||_                                  ||  
' ||   ,._-_  /'\\ \\/\\ \\/\\ '\\/\\ =||= 
  ||    ||   || || || || || ||  || ;'  ||  
  |,    ||   || || || || || ||  ||/    ||  
_-/     \\,  \\,/  \\ \\ \\ \\  |/     \\, 
                               (           
                                -_-        
""")
#Command prompt

# ATTACK, BAG, and RUN options
while yourHealth > 0 and bossHealth > 0:
    Yourcommand = ""
    while Yourcommand not in commands:
        Yourcommand = input("What will you do?\n(ATTACK / BAG / RUN): ")
        if Yourcommand == "ATTACK":
            print("You attack the fierce dragon. \n The slash of your sword deals a hefty sum of damage to it!")
            print("<<<YOU HAVE DEALT", swordAttack, "DAMAGE TO THE DRAGON>>>")
            bossHealth = bossHealth - swordAttack
            print("The dragon is at", bossHealth, "Health.")
        elif Yourcommand == "BAG":
            bagcommands = ""
            while bagcommands not in bagOptions:
                print("You look inside your bag...")
                print("Inside you have several health and strength potions")
                bagcommands = input("Which item shall you choose?: (HEALTH POTION, STRENGTH POTION)")
                if bagcommands == "HEALTH POTION":
                    while healthPotioncount == 0:
                        print("You have ran out of health potions!")
                        bagcommands = input("Which item shall you choose?: (HEALTH POTION, STRENGTH POTION)")
                    while yourHealth == 200:
                        print("You already have maximum health! Using a health potion seems quite redundant at the moment...")
                        bagcommands = input("Which item will you choose? (HEALTH POTION, STRENGTH POTION): ")
                    else:
                        yourHealth =+ potionHeal
                        print("You have regained 25 health!")
                        healthPotioncount = healthPotioncount - 1
                        print("You have", healthPotioncount, " health potions remaining.")                                 
                if bagcommands == "STRENGTH POTION":
                    while strengthPotioncount == 0:
                        print("You have ran out of strength potions!")
                        bagcommands = input("Which item shall you choose?: (HEALTH POTION, STRENGTH POTION)")
                    else:
                        print("You drink the strength potion, you feel yourself becoming much more powerful!")
                        print("1.5x Attack bonus!")
                        swordAttack = swordAttack * strengthPotionBuff
                        strengthPotioncount = strengthPotioncount - 1
                        print("You have", strengthPotioncount , "strength potions remaining.") 
        elif Yourcommand == "RUN":
            print("You have run away from battle..."\
                  "Unfortunately... You fell right into the pit of lava that surrounds you!")
            input("""    __ ,                                 __                               
  ,-| ~                                ,-||-,                             
 ('||/__,   _                         ('|||  )  ;                         
(( |||  |  < \, \\/\\/\\  _-_        (( |||--)) \\/\  _-_  ,._-_          
(( |||==|  /-|| || || || || \\       (( |||--)) || | || \\  ||            
 ( / |  , (( || || || || ||/          ( / |  )  || | ||/    ||            
  -____/   \/\\ \\ \\ \\ \\,/          -____-   \\/  \\,/   \\,  <> <> <> 
                                                                          
                                                                          """)
            quit()
#Boss attack 1 (Slash Attack)
    if bossAttack == 1:
        print("The dragon slashes you with its large claws, dealing a large amount of damage!")
        print("<<<THE BOSS HAS DEALT",bossAttackdamage,"DAMAGE>>>")
        yourHealth = yourHealth - bossAttackdamage
        print("Your health is:", yourHealth)
# Boss Attack 2 (Fire Breath)
    elif bossAttack == 2:
        print("The dragon breathes fire at you, scorching you and damaging you greatly!")
        progFiredamagecondition = True
        print("You are now burnt!")
        yourHealth = yourHealth - (bossAttackdamage + progFiredamage)
        print("<<<THE BOSS HAS DEALT",bossAttackdamage,"DAMAGE>>>")
        print("Your health is:", yourHealth)
# Boss Attack 3 (Heal)
    elif bossAttack == 3:
        print("")
        
#Boss defeated
if bossHealth <= 0:
    print("Fronnyt has been slain!")
    print("""   ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(X: :X)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v) """)
    print("\nYou have gained 100 experience!"\
          "\nYou have gained 500 gold!")
    input(""" _                                         
- - _-            ,                     /\ 
  )-  )  '       ||                     \/ 
  )___) \\  _-_ =||=  /'\\ ,._-_ '\\/\\ }{ 
 ~)___) || ||    ||  || ||  ||    || ;' \/ 
  )  )  || ||    ||  || ||  ||    ||/      
 /-_/   \\ \\,/  \\, \\,/   \\,   |/    <> 
                                 (         
                                  -_-      """)
#Your defeated
if yourHealth <= 0:
    print("You have been slain by the dragon. Your dead body falls to the ground as you become the foul beasts' next prey...")
    input("""    __ ,                                 __                               
  ,-| ~                                ,-||-,                             
 ('||/__,   _                         ('|||  )  ;                         
(( |||  |  < \, \\/\\/\\  _-_        (( |||--)) \\/\  _-_  ,._-_          
(( |||==|  /-|| || || || || \\       (( |||--)) || | || \\  ||            
 ( / |  , (( || || || || ||/          ( / |  )  || | ||/    ||            
  -____/   \/\\ \\ \\ \\ \\,/          -____-   \\/  \\,/   \\,  <> <> <> 
                                                                          
                                                                          """)
