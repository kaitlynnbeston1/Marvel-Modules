

#-----------------------------------------------------------------------------
# Title: Make and use a Module
# Coders: Kaitlynn, Calvin
# Version: 001
#-----------------------------------------------------------------------------
''' Example Code - Storing Your Functions and Data in Modules.

    Syntax for accessing module.
        import [module]
    
    When a function from a module is called, you use the following syntax.
        module_name.function_name()
        
    When a variable from a module is called, you use the following syntax.
        module_name.variable_name
    
'''
#-----------------------------------------------------------------------------
# Imports and Global Variables -----------------------------------------------
import mod1 as m


# Functions ------------------------------------------------------------------
def choose_char():
    
    print("What character would you like to be?")
    for key in m.Marvel_Superheros:
      print(f"  - {key}")
    choice = input("Choice: ").title()
    m.Hero = choice


# Main -----------------------------------------------------------------------
print("Welcome to my example.\n")
choose_char()
print(f"\nYou choose to be {m.Hero}!")
print("Finished!\n\n")
print("Your weapons are:")
weapons = m.Marvel_Superheros[m.Hero]["Weapons"]
for weapon in weapons:
   print(weapon)