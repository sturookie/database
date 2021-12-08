import pandas as pd

df = pd.read_csv('State_University_of_New_York__SUNY__Campus_Locations_with_Websites__Enrollment_and_Select_Program_Offerings.csv')

School = pd.DataFrame(df, columns=['Campus Name', 'County', 'Institution Type','Institution Level','Undergraduate Enrollment','Graduate Enrollment','Campus Website'])

print(School)