import os
import glob


class DataImportOutput:
    
    """
    This class uses a data path in the same repo as the code.
    It will look for .csv and .xlsx files to import data.
    It will export data in either format.
    """
    
    def __init__(self) -> None:
        self.input_path = input_path
        self.output_path = output_path
        
        # used in get and export data to track file types for conditional use cases
        self.excel = False  
        self.comma_sep = False
    
    
    # create 2 cases: single file; multi file in folder
    # user input option to modify files 
    # conditions for csv and excel
    def get_data(self):
        self.input_path = 'data\input'
        # create
        # try - except
            # if no path
                # create path and ask user to upload files
                    # prompt to receive files
            # if filtered excel file return error
            # if no file found error
            # if wrong format error
        # check access to dir
        
        # check path anf file types
        file_list = []

        for root, dirs, files in os.walk(r"C:\\Users\\Trent_Brunson\\GitHub\\AOP-CC-splits\\data\\input"):
            for file in files:
                if file.endswith('.xlsx'):
                    file_list.append(file)
        print(file_list)
        
        # if .xlsx excel = True
        # .csv comma_sep = True
        
    
    def export_data(self):
        # try - except; create folder if none
        # user inout for excel or csv
            # if none, match import format
                # if multi, use csv
        self.output_path = 'data\output'
        