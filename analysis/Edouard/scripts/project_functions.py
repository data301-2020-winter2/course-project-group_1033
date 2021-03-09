import pandas as pd
import numpy as np



def load_and_process(url_or_path_to_csv_file): 
    
    
    # method Chain 1 (load data + fix missing values + naming columns + fixing strings)

    df = (pd.read_csv("../../data/raw/nomenclature.csv",delimiter=",", header=15)
      .dropna()
      .rename(columns= { "# TRANSLATORS: (Phoebe); Argonaut, founder and king of Pherae in Thessaly." : "Planet Name", "Unnamed: 1" : "ID", "Unnamed: 3" : "Planetary Feature", "Unnamed: 2" : "FeatureName",  "Unnamed: 4" : "Latitude of Center of Planetary Feature", "Unnamed: 5" : "Longitude of Center of Planetary Feature", "Unnamed: 6" : "Size of Planetary Feature(km)"})
    .reset_index()


     )


    # method Chain 2 (String cleaning in the 'Name of Planetary Feature Column') 

    df2 = (df
    .assign(FeatureName = lambda x: x['FeatureName'].str.replace('"', " ")
    .str.strip("_")
    .str.lstrip('(')
    .str.rstrip(')')
    .str.strip(',')
           ))


    # method Chain 3 (Split the Name of Planetary Feature Column + reorder Columns + sortBy new FeatureType Column)
     
    df3 = (df2
      .assign(FeatureType = lambda x: x['FeatureName'].str.split(",").str[1],
              FeatureName = lambda x: x['FeatureName'].str.split(",").str[0])
      .loc[:, ['Planet Name','ID','FeatureName','FeatureType', 'Planetary Feature', 'Latitude of Center of Planetary Feature','Longitude of Center of Planetary Feature','Size of Planetary Feature(km)']]
      .sort_values('FeatureType', ascending = True )
      .reset_index()

       
      )
    
    return df3