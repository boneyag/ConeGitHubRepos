'''
This is the utility function. It takes data from LibraryData.json and returns the results. The result is a list of dictionaries where is dictionary is the data for a single library.
'''

import json

def read_json_file(file_path): 
    
    main_array = []
    with open(file_path, 'r') as myfile:
        main_array = json.loads(myfile.read())    
    return main_array


class Debug:
    """ Just a debugger class for formatted logs. """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def info(msg):
        print(f"{Debug.OKBLUE}Info     --> {Debug.ENDC}{msg}")
    
    @staticmethod
    def error(msg):
        print(f"{Debug.FAIL}Error    --> {Debug.ENDC}{msg}")
    
    @staticmethod
    def warn(msg):
        print(f"{Debug.WARNING}Warning  --> {Debug.ENDC}{msg}")

    @staticmethod
    def separator():
        print(Debug.BOLD + "-" * 20 + Debug.ENDC + "\n")