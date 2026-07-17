#Chemical Inventory Management System: #store,add and categorize the chemicals in a CSV file.
#Import modules for CSV handling ,file operations and terminating the program
import csv
import os
import sys
print("CHEMICAL USED IN LABORATORY:")
#Chemicals are grouped and displayed by category.
#some may appear in multiple groups.
chemical_inventory = {
"desiccants":[
    "silica gel",
    "calcium chloride",
    "molecular sieves",
    "phosphorus pentoxide"],
"acids":[
        "hydrochloric acid",
        "sulfuric acid",
        "nitric acid",
        "phosphoric acid",
        "hydrobromic acid",
        "acetic acid",
        "perchloric acid",
        "hydrofluoric acid"],
"bases":[
        "sodium hydroxide",
        "potassium hydroxide",
        "calcium hydroxide",
        "ammonium hydroxide"],
"catalysts":[
        "grubbs catalyst",
        "raney nickel",
        "phenolphthalein",
        "platinum dioxide",
        "palladium on carbon"],
"solvents":[
        "ethanol",
        "methanol",
        "ethylene glycol",
        "acetone",
        "diethyl ether",
        "hexane",
        "chloroform",
        "benzene",
        "glycerol",
        "carbon disulfide"],
"flammables":[
        "ethanol",
        "methanol",
        "acetone",
        "diethyl ether",
        "hexane",
        "carbon disulfide",
        "propane",
        "butane",
        "potassium metal",
        "sodium metal",
        "magnesium ribbon",
        "acetonitrile"],
"oxidizers":[
        "hydrogen peroxide",
        "potassium permanganate",
        "chromium trioxide",
        "perchloric acid",
        "organic peroxides",
        "phosphorus pentoxide",
        "sodium hypochlorite"],
"radioactive":[
        "phosphorus-32",
        "carbon-14",
        "iodine-125",
        "sulfur-35"],
"toxic":[
        "mercury chloride",
        "lead metal",
        "mercury",
        "cadmium",
        "benzene",
        "chloroform",
        "carbon monoxide",
        "phenol",
        "formaldehyde",
        "acrylamide",
        "sodium cyanide",
        "hydrofluoric acid"],
"corrosive":[
        "hydrochloric acid",
        "sulfuric acid",
        "nitric acid",
        "hydrofluoric acid",
        "perchloric acid",
        "potassium hydroxide",
        "ammonium hydroxide",
        "thionyl chloride",
        "phosphorus pentoxide"],
"engineering_reagents":[
        "aluminum chloride",
        "iron chloride",
        "silica gel",
        "silicon dioxide",
        "calcium carbonate",
        "sodium bicarbonate"],
"water_reactive":[
    "sodium metal",
    "potassium metal",
    "thionyl chloride",
    "sodium hydroxide"]
    }
#Update the inventory by adding or removing or modifying chemicals 

chemical_inventory["toxic"].append("lead iodide")
chemical_inventory["solvents"].extend(["water","dmso","dmf","ethyl acetate","toluene","isopropyl alcohol"])
chemical_inventory["water_reactive"].remove("sodium hydroxide")
target_list = chemical_inventory["flammables"]
if "acetonitrile" in target_list:
    index = target_list.index("acetonitrile")
    target_list[index] = "methylated spirits"
chemical_inventory["volatile_solvents"]=["toluene", "ethylene glycol", "glycerol"]
chemical_inventory["engineering_reagents"].extend(["zeolite catalysts", "sodium chloride", "ferric chloride", "nitrogen gas"
])
#To remove specific chemical from a specific category
chemical_inventory["desiccants"].pop(0)
#To print the chemicals by category
for category, chemicals in chemical_inventory.items():
    print(f"\n{'='*10} {category.upper()} {'='*10}")
    for chemical in chemicals:
        print(chemical.upper())
print()
#Count all unique chemicals across the inventory excluding duplicate appearances
all_chemicals = [
    chemical.lower().strip()
    for chemicals in chemical_inventory.values()
    for chemical in chemicals
]
unique_chemicals=set(all_chemicals)
print(f"total_unique_chemicals:{len(unique_chemicals)}")
# Creating the lookup dictionary to search chemicals quickly
chemical_locations = {}
for category, chemicals in chemical_inventory.items():
    for chemical in chemicals:
        chemical_lower = chemical.lower().strip()
        if chemical_lower not in chemical_locations:
            chemical_locations[chemical_lower] = []
        if category not in chemical_locations[chemical_lower]:
            chemical_locations[chemical_lower].append(category)
print("\n"+ "="*40)
#display the recommended storage methods for chemicals 
stable_reagents_and_solvents=[
"magnesium ribbon","hydrochloric acid","sulfuric acid","phosphoric acid","nitric acid","acetic acid","hydrobromic acid","sodium hydroxide","potassium hydroxide","calcium hydroxide","ammonium hydroxide","sodium bicarbonate","iron chloride","aluminum chloride","calcium carbonate","nitrogen gas","potassium permanganate","chromium trioxide","phenolphthalein","sodium hypochlorite","sodium chloride","ferric chloride","silicon dioxide","molecular sieves","ethylene glycol","glycerol","water","dmf","dmso","calcium chloride","acetic acid"]
#Display chemicals on seperate line for better understanding 
print("Stable Reagents and Solvents")
for chemical in stable_reagents_and_solvents:
    print("-", chemical)    
print("reagents and solvents:general cabinet")
print("\n"+"="*10)
pyrophoric_and_moisture_sensitive=["raney nickel", "grubbs catalyst","sodium metal","potassium metal","thionyl chloride","zeolite catalysts","phosphorus pentoxide","palladium on carbon"]
print("Pyrophoric & moisture Sensitive")
for chemical in pyrophoric_and_moisture_sensitive: 
    print("-", chemical),
print("Pyrophoric & moisture-Sensitive:Sealed (Inert Atmosphere / Oil)")
print("\n"+"="*10)
toxins_and_carcinogens =["mercury", "sodium cyanide", "benzene", "chloroform","lead metal","cadmium","carbon monoxide","phenol","hydrofluoric acid","lead iodide","mercury chloride","formaldehyde","acrylamide"]
print("Toxins & Carcinogens")
for chemical in toxins_and_carcinogens:
    print("-", chemical),
print("Toxins & Carcinogens:Locked in Poison Cabinet")
print("\n"+"="*10)
radioactive_materials = ["phosphorus-32", "carbon-14", "iodine-125","sulfur-35"]
print("radioactive materials")
for chemical in radioactive_materials:
    print("-", chemical)  
print("Radioactive materials:sealed in radiation shielding")
print("\n"+"="*10)
moisture_reactive_and_oxidizers = [ "perchloric acid", "organic peroxides","palladium on carbon","platinum dioxide","hydrogen peroxide","phosphorus pentoxide","chromium trioxide","potassium permanganate"]
print(" moisture_reactive_and_oxidizers")
for chemical in moisture_reactive_and_oxidizers:
    print("-", chemical)  
print("Oxidizers&moisture reactive:isolated")
print("\n"+"="*10)
volatile_solvents_and_flammables=["ethanol", "methanol","diethyl ether", "acetone", "hexane", "carbon disulfide", "propane","butane","toluene","methylated spirits","isopropyl alcohol","ethyl acetate"]
print("Volatile Solvents & Flammables")
for chemical in volatile_solvents_and_flammables:
    print("-", chemical)  
print("Volatile Solvents & Flammables:flammable stroage cabinate")
# Build it as a dictionary that maps each chemical to all of its categories.
def build_lookup_index():
     lookup={}
     for category,chemicals in chemical_inventory.items():
        for chemical in chemicals:
               chemical_lower=chemical.strip().lower() 
               if chemical_lower not in lookup:
                    lookup[chemical_lower]=[]
               if category not in lookup[chemical_lower]:
                    lookup[chemical_lower].append(category)
     return lookup       
DATABASE_FILE = "chemical_inventory.csv"
#CSV file to store inventory data 
def save_data():
    try:
        with open(DATABASE_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Chemical"])
            for category, chemicals in chemical_inventory.items():
                for chemical in chemicals:
                    writer.writerow([category, chemical])
        print(f"\n inventory save to '{DATABASE_FILE}'")
    except Exception as e:
        print(f"\nUnable to save inventory: {e}")
#load inventory data from the csv file 
def load_data():
    global chemical_inventory
    if os.path.exists(DATABASE_FILE):
        try:
            new_inventory = {key: [] for key in chemical_inventory.keys()}
            with open(DATABASE_FILE, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) == 2:
                        category, chemical = row[0], row[1]
                        if category not in new_inventory:
                            new_inventory[category] = []
                        new_inventory[category].append(chemical)
            chemical_inventory = new_inventory
            print(f"\nInventory data loaded from '{DATABASE_FILE}.'")
        except Exception as e:
            print(f"\n[WARNING] could not read CSV file: {e}")
    else:
        print("\nNo inventory found.Using default inventory")
 #to display specific data about searched chemical  
def search_chemical():
     user_query=input("Enter a name of chemical to search in chemical_inventory:").strip().lower()
     categories = chemical_locations.get(user_query)
     if not categories:
          print(f"{user_query.title()} is not in inventory")
          return
     print(f"CHEMICAL FOUND:{user_query.title()}")
     print(categories)
     print(f"categories:{','.join (categories)}")
     if user_query in stable_reagents_and_solvents:
          print(f"Status:Available for daily use")
     elif user_query in pyrophoric_and_moisture_sensitive:
           print(f"Status:Sealed under Inert Atmosphere / Oil")
     elif user_query in toxins_and_carcinogens:
          print(f"Status:Locked in Poison Cabinet")
     elif user_query in radioactive_materials:
          print(f"Status:Sealed in Radiation Shielding")
     elif user_query in moisture_reactive_and_oxidizers:
          print(f"Status:Isolated")
     elif user_query in volatile_solvents_and_flammables:
          print(f"Status: Sealed tightly")  
     else:
          print("Storage Status: not classified")
#Add new chemical into the inventory and save in CSV file.   
def add_chemical():
     print("\n add_new_chemical")
     new_chemical=input("Enter a new chemical to register:").strip().lower()
     if not new_chemical:
        print("invalid entry:name can not be registered")
        return
     categories_list=list(chemical_inventory.keys())
     print("\nAvailable Categories:")
     for index,cat in enumerate(categories_list,1):
         print(f"{index}.{cat}")
     try:
          choice=int(input("\nSelect category number to append chemical to:"))
          if 1 <=choice<=len(categories_list):
               selected_category=categories_list[choice-1]
               if new_chemical not in chemical_inventory[selected_category]:
                    chemical_inventory[selected_category].append(new_chemical)
                    print(f"NEW CHEMICAL IS SUCCESSFULLY ADDED:Add'{new_chemical} 'to'{selected_category}'.")
                    save_data()
               else:
                    print("\n warning:chemical is already in the category")
          else:
              print("\nInvalid category selection")
     except ValueError:
          print("please enter a valid category number")
     current_cat_count = len(chemical_inventory[selected_category])
     print("Updated category count:", current_cat_count)
     total_count = sum(len(lst) for lst in chemical_inventory.values())
     print("Total chemical count:", total_count)
     unique_chemicals = set()
     for chemicals in chemical_inventory.values():
          for chemical in chemicals:
               unique_chemicals.add(chemical.lower().strip())
     print("Total unique chemicals:", len(unique_chemicals))
def display_inventory_stats():
    print("\n" + "=" * 10)
    print("Chemical count per category")

    for category, chemicals in chemical_inventory.items():
        print(f"-> {category}: {len(chemicals)} items")

    unique_chemicals = set()

    for chemicals in chemical_inventory.values():
        for chemical in chemicals:
            unique_chemicals.add(chemical.lower().strip())

    print(f"Total unique chemical tracking: {len(unique_chemicals)}")
#Display main menu and process user command like adding,display count or search
def main_menu():
     while True:
          print("\n"+"="*40)
          print("User interactive part for laboratory")
          print("\n"+"="*40)
          print("1.Search For Chemical")
          print("2.Display inventory statistics")
          print("3.Add New Chemical ")
          print("4.Exit the System ")
          choice=input("\n select system execution parameter(1-4):").strip()
          if choice=="1":
               search_chemical()
          elif choice=="2":
               display_inventory_stats()
          elif choice=="3":
               add_chemical()
          elif choice=="4":
               print("shutting down lab database network.......")
               sys.exit()
          else:
            print("Invalid option.please choose a number from (1-4)")
#enter point for the program
if __name__=="__main__":
     if os.path.exists(DATABASE_FILE):
          load_data()
     else:
          save_data()
     chemical_locations = build_lookup_index()  
     main_menu()