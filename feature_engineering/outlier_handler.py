import pandas as pd
import numpy as np


class outlier_handler():

    def __init__(self):

        pass

    def remove_outlier(self,df,column,neigh_size,no_neigh,error_case="raise"):
        # get the col
        col = df[column]
        index = 0
        diff,unique = True
        for val in col:
            try:
                val = pd.to_numeric(val,error_case)
                j = 0
                for val2 in col:
                    try:
                        val2 = pd.to_numeric(val2,errors="raise")
                        if(abs(val-val2)<neigh_size ):
                            diff = False
                        if(index != j):
                            if(val == val2):
                                unique = False
                    except:
                        j = j + 1
                        continue
            except:
                print(f"The {index}th datapoint is not in proper numeric form")
                index = index + 1
                continue
            if (diff and unique):
                    df = df.drop(index)
            else:
                index = index + 1

        return df

            
