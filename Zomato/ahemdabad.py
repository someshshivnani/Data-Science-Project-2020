def output2():
    #importing data
    import pandas as pd
    data = pd.read_csv('C:\\Users\\dell\\Downloads\\zomato-india-data-set\\Ahmedabad\\combined_csv.csv')
    #data.shape


    #printing the first 5 values
    data.head()


    #removing unwanted columns: ['URL', 'PAGE NO']
    data1 = data.drop(['URL', 'PAGE NO'], axis = 1)
    data1.shape


    data1.head()



    #checking the counts for different values of ratings (eg : rating 3.4 appears 178 times)
    data1.RATING.value_counts()



    #removing unwanted values from rating column
    data2 = data1[(data1.RATING != '-') & (data1.RATING != 'Opening') & (data1.RATING != 'NEW')]


    #checking no. of rows and columns
    data2.shape


    data2.head(40)


    #the updated rating column
    data2.RATING.value_counts()
    #sorting table on the basis of rating and votes column in descending order
    data2.sort_values(by = ["RATING","VOTES" ], axis = 0, ascending=False, inplace = True)
    #filtering rating column and printing only the excellent and good rating_type values
    df_filtered = data2[data2['RATING'] >= '4.0'] 
  
    # Print the new dataframe
    df_filtered.shape


    df_filtered.head()  


    #top rated restro names
    #print(df_filtered.NAME.values[:5])
    return df_filtered.NAME.values[:5]