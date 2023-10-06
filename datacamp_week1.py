
import pandas as pd
tweets_df=pd.read_csv("./tweets.csv")
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    for col_name in args:
         # Extract column from DataFrame: col
         col = df[col_name]
         for entry in col:
               if entry in langs_count.keys():
                    langs_count[entry]+=1
               else:
                    langs_count[entry]=1
         return  langs_count        
                     
    
  

# Call count_entries(): result
result=count_entries(tweets_df,"lang")
result2=count_entries(tweets_df,"sources")

# Print the result
print(result)
print(result2)