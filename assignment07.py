# ------------------------------------------------- #
# Title: pickling to store data in Binary format
# Description: A simple example of storing and retrieve
# data in a binary file
# ChangeLog: (Who, When, What)
# NazneenM, 3.5.2020,Created Script
# ------------------------------------------------- #
import pickle # This imports code from another codee!
# Data -------------------------------------------- #
strFileName = 'AppData.dat' # The name of binary file
lstCustomer = [] # A list for costumer inforamtion
objFile= None # An object that represents a file

# Processing -------------------------------------- #

def save_data_to_file(file_name, list_of_data):
    """

    :param file_name: (string) with name of file
    :param list_of_data:(string) with data to save
    :return:nothing
    """
    # now we store the data with the pickle.dump method
    objFile = open(file_name, "wb") # open binary file to overwrite
    pickle.dump(list_of_data, objFile)
    objFile.close() # close the file

def read_data_from_file(file_name, list_of_data):
    """

    :param file_name: (string) with name of file
    :param list_of_data:(string) with data to save
    :return: List_of_data
    """
    # read the data back with the pickle.load method
    objFile = open(file_name, "rb") # open binary file to read from
    list_of_data = pickle.load(objFile)  #load() only loads one row of data
    return (list_of_data) #return list_0f_ data
    objFile.close() # close file for security


 # Presentation ------------------------------------ #
print() # this to look nice
while(True): # while loop repeat the loop until choose exit
 print('''\n --------- MAIN MENU--------- 
 Choose an option
 1 = Enter costumer Data
 2 = Store list to binary file
 3 = Display data from binary file 
 4 = Exit
 ''')
 choice = input('Enter an Option: ') # catching choice from user
 if choice == '1': # checks if choice =1 then execute the following steps
     # if not go to next elif
    print("(Type in a Customer Id and Name you want to add to the file)")
    # Get ID and NAME From user, then store it in a list object
    intId = int(input("Enter an Id: "))
    strName = str(input("Enter a Name: "))
    lstData = [intId, strName] # put enter data to list
    lstCustomer += lstData # append more data to list
    print(" Here is what you enter ") # for more declaration
    print(lstCustomer) # print the list for user

 elif choice == '2': # if choice =2 execute the following
    # store the list object into a binary file
    save_data_to_file(strFileName, list_of_data=lstCustomer)
    print('list saved to binary file') # displayed for user that data saved

 elif choice == "3":
    print ("Data retrieved from File")
    # Read the data from the file into a new list object
    # and display it
    print(read_data_from_file(strFileName, lstCustomer)) # print the returning data from read

 elif choice == '4': # if the choice =4 then exit the program
     print("Good bye!") # nice word for user
     break # exit the while loop
 else:
    print('Please Enter Choice 1,2,3,4 or 5!') # if the choice not included
    # hint for user to choose the correct choice


