import pandas as pd


class joiner():
    def __init__(self,path):       

        ##### ----- load the file ----- #####
        self.datafile = pd.read_excel(path,sheet_name=None)
        self.sheets = {}

    ##### ----- get each sheet from excel file ----- #####
    def get_sheets(self):   
        for sheetname,sheet in self.datafile.items():            
            self.sheets[sheetname]=sheet
        print("Finished processing and sheets returned.")
        return self.sheets
    
    ##### ----- join two sheets on a specific column ----- #####
    def join(self, sheet1,sheet2,colum_name ="",join_type=""):

        joined_df = pd.merge(sheet1,sheet2,on=colum_name,how=join_type)
        return joined_df
        
        
                


if __name__ =="__main__":

    path = "D:\Projects\Data Analysis\Robot Assisted surgery EDA\Data\RCS_MASTERY metrics report 2022.10.17\RCS_MASTERY metrics report 2022.10.17\Patient_Session_Tracker.xlsx"
    joiner = joiner(path)
    for name,sheet in joiner.sheets.items():

        print(name)


















