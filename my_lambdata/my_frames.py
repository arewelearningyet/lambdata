import pandas

def add_state_names(parameter_list):
    """
    objective is to add a column of state names 
    to a dataframe that already has the abbreviations
    Param my_df is a pandas.DataFrame and should have a column of abbrev
    RETURN a copy of the DataFrame with a new column called 'name'
    """
    names_map = {"CT": "Conn","CO": "Colorado", "CA": "Cali",}         
    breakpoint() # py 3.7 or later, otehrwise use pdb module
    new_df = my_df.copy()
    new_df["name"] = my_df["abbrev"].map(names_map)
    return new_dff

df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
mutated_df = add_state_names(df) # desired invocation
print(mutated_df.head())

df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})
mutated_df2 = add_state_names(df2) # desired invocation
print(mutated_df2.head())


