import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import re

class dayinter():
    # This class is used to interpolate the missing values in the time series data.
    # The data is interpolated using the linear interpolation method.
    # The class takes two arguments: date and values.
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
    
    def __init__(self, date, values):
        self.date = date
        getform = self.get_date_format(self.date.iloc[1].astype(str))
        self.date = pd.to_datetime(self.date, format=getform)
        self.values = values
        self.df = pd.DataFrame({self.date.name: self.date, self.values.name: self.values})
        self.df = self.df.reset_index(drop=True)
        
    def day_interpolation(self):
        self.df = self.df.set_index('Date')
        self.df = self.df.resample('D')
        self.df = self.df.interpolate(method='linear')
        self.df = self.df.reset_index()
        return self.df
                        
            
        
    def main(self):
        if self.day_interpolation() is not None:
            return self.day_interpolation()
        else:
            return None
