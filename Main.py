
# Import necessary modules
from display_AEF import *
from deterministe_list import *
from CompletAEF import *
from Input2 import *
from ReconnaissanceWorldByAEF import *
from AEF_operand import *
from input_file import *
from Language2 import *
from prunedAEF import * 
from Equivalent import * 

def main_menu():
    print("\nFinite State Automaton Editor")
    print("1. Create AEF")
    print("2. Import AEF from file")
    print("3. Display AEF")
    print("4. Verify if a word is recognized by AEF")
    print("5. Check if AEF is complete")
    print("6. Make AEF complete")
    print("7. Check if AEF is deterministic")
    print("8. Make AEF deterministic")
    print("9. Create the complement of an AEF")
    print("10. Create the mirror of an AEF")
    print("11. Create the Regular Expression of an AEF")
    print("12. Create the Pruned AEF of an AEF")
    print("13. Multiply two AEFs")
    print("14. Concatenate two AEFs")
    print("15. Check if two AEFs are Equivalent")
    print("0. Exit")
    return input("Choose an option: ")

def main():
    aef = None
    while True:
        choice = main_menu()
        if choice == '0':
            break
        elif choice == '1':
            aef = CreateAEF()
        elif choice == '2':
            file_name = input("Enter the file name to import: ")
            aef = readAefFile(file_name)
            if aef == -1:
                print("Failed to read file.")
        elif choice == '3':
            if aef:
                displayAef(aef)
            else:
                print("No AEF loaded.")
        elif choice == '4':
            if aef:
                print("Recognizes word:", AEFRecogniseWord(aef))
            else:
                print("No AEF loaded.")
        elif choice == '5':
            if aef:
                print("AEF is complete:", isComplete(aef))
            else:
                print("No AEF loaded.")
        elif choice == '6':
            if aef:
                aef = makeComplete(aef)
                print("AEF made complete.")
            else:
                print("No AEF loaded.")
        elif choice == '7':
            if aef:
                print("AEF is deterministic:", isDeterminist(aef[2]))
            else:
                print("No AEF loaded.")
        elif choice == '8':
            if aef:
                aef = makeDeterministAef(aef)
                print("AEF made deterministic.")
            else:
                print("No AEF loaded.")
        elif choice == '9':
            if aef:
                print("debug",aef)
                aef = makeComplement(aef)
                print("Complement AEF created.",aef)
            else:
                print("No AEF loaded.")
        elif choice == '10':
            if aef:
                aef = makeMiror(aef)
                print("Mirror AEF created.")
                print(aef)
            else:
                print("No AEF loaded.")
        elif choice == '11':
            if aef:
                regularExpression(aef)
                print("Regular Expression created")
            else:
                print('No AEF loaded')
        elif choice == '12':
            if aef:
                aef = makePruned(aef)
                displayAef(aef)
                print("Pruned AEF created")
            else:
                print('No AEF loaded')
        elif choice == '13':
            if aef:
                second_aef_name = input("Enter the name of the second AEF to multiply: ")
                second_aef = readAefFile(second_aef_name)  # Assuming you have a function to read an AEF
                if second_aef != -1:
                    product_aef = mutliplyAef(aef, second_aef)
                    print("Product AEF created.")
                    displayAef(product_aef)
                else:
                    print("Failed to read second AEF file.")
            else:
                print("First AEF not loaded.")
                
                
        elif choice == '14':
            if aef:
                second_aef_name = input("Enter the name of the second AEF to concatenate: ")
                second_aef = readAefFile(second_aef_name)  # Assuming you have a function to read an AEF
                if second_aef != -1:
                    concateneted_Aef = concatenateAef(aef, second_aef)
                    print("Product AEF created.")
                    displayAef(concateneted_Aef)
                else:
                    print("Failed to read second AEF file.")
            else:
                print("First AEF not loaded.")
                
                
        elif choice == '15':
            if aef:
                if aef:
                    second_aef_name = input("Enter the name of the second AEF : ")
                    second_aef = readAefFile(second_aef_name)  # Assuming you have a function to read an AEF
                    if second_aef != -1:
                        if isEquivalent(aef, second_aef):
                            print("The AEFs are equivalent")
                        else:
                            print("The AEFs are not equivalent")
                else:
                    print("Failed to read second AEF file.")
            else:
                print("First AEF not loaded.")
                
        else:
            print("Invalid option. Please try again.")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
