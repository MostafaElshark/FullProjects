import pandas as pd
import re


class interpolator():
    # This class is used to interpolate the missing values in the time series data.
    # The data is interpolated using the linear interpolation method.
    # The class takes two arguments: dataframe1 and dataframe2.
    # The dataframes should have two columns: date and values.
    # The date column should be the first column and the values column should be the second column.
    
    def get_date_format(self, date):
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            return "%Y-%m-%d"
        elif re.match(r"^\d{2}-\d{2}-\d{4}$", date):
            return "%d-%m-%Y"
        elif re.match(r"^\d{2}/\d{2}/\d{4}$", date):
            return "%m/%d/%Y"
        elif re.match(r"^\d{4}/\d{2}/\d{2}$", date):
            return "%Y/%d/%m"
        elif re.match(r"^\d{4}\d{2}\d{2}$", date):
            return "%Y%m%d"
        elif re.match(r"^\d{2}\d{2}\d{4}$", date):
            return "%d%m%Y"
        elif re.match(r"^\d{4}/\d{2}/\d{4}$", date):
            return "%Y/%m/%d"
        elif re.match(r"^\d{2} \w{3} \d{4}$", date):
            return "%d %b %Y"
        elif re.match(r"^\d{2} \w{4,9} \d{4}$", date):
            return "%d %B %Y"
        else:
            return None
        
    def __init__(self, df1, df2):
        self.df1 = df1
        self.df2 = df2
        self.daten1 = self.df1.columns[0]
        self.daten2 = self.df2.columns[0]
        self.namer1 = self.df1.columns[1]
        self.namer2 = self.df2.columns[1]
        self.df1[self.daten1] = pd.to_datetime(self.df1[self.daten1], format=self.get_date_format(self.df1[self.daten1][0]))
        self.df2[self.daten2] = pd.to_datetime(self.df2[self.daten2], format=self.get_date_format(self.df2[self.daten2][0]))

    def removeNan(self, df):
        h = df.columns[1]
        for i in range(len(df)):
            if df[h][i] == df[h][i]:
                return df[i:]
    
    def removenanfromlast(self, df):
        h = df.columns[1]
        for i in range(len(df))[::-1]:
            if df[h][i] == df[h][i]:
                return df[:i+1]
    
    def interpolatetwo(self):
        self.df1 = self.df1.set_index(self.daten1)
        self.df2 = self.df2.set_index(self.daten2)
        newdf = self.df1.join(self.df2, how='outer')
        newdf = self.removeNan(newdf)
        newdf = self.removenanfromlast(newdf)
        newdf = newdf.interpolate(method='linear')
        newdf = newdf.reset_index()
        return newdf
    
    def main(self):
        newdf = self.interpolatetwo()
        return newdf.dropna()       
        