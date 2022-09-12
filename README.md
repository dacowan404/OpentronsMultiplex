# OpentronsMultiplex
Used to create Opentrons OT-2 scripts for combining multiple 96 well plates into one 96 well plate

These scripts work together to create a python script that can be run on the Opentron OT-2 that can used variety of project types. It was initially designed for a multiplex project which combined 8 different wells with differing volume into a singe well. But it also can make transfers from a plate to another plate. Overall, I feel that it is a versatile program.

### There are 3 different python files and a sample csv provided. 
- unfinishedScript.py is the base python script. It has everything to run  except for the pandas dataframe (table) which tells where to transfer to and from and also how much volume to transfer.
- EditFilePath.py is the script that generates the final script. Edit inputFile to an appropriate csv file using column descriptions below. The csv is read into the program as pandas dataframe which is converting into a string. The time and import packages lines are added to the string. Then unfinishedScript.py as a string. These 2 strings are then written to the output file, Multiplex.py.
- Multiplex.py is the output file and is usable on the OT-2 robot. It converts the csv data which is a string back into a pandas dataframe. Then uses that data to make the transfers. It currently only uses the P20 pippette, but could be easily adapted to use other pippettes.

### CSV Setup: 
- col 1: Volumes
- col 2: Start Plate Number (1-3)
- col 3: Start Plate Position (row first, then column ie. A1, D6. NOT 6D)
- col 4: Finish Plate Position (row first, then column)
Any Volume less than or equal to 0 will be skipped

### opentron layout: Position
- Finish Plate:   2
- Start Plate 1:  4
- Start Plate 2:  5
- Start Plate 3:  6
- 20uL Tips:      7, 8, and 9
