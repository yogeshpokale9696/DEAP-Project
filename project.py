import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time as tm


df = pd.read_csv("Crop.csv")
print(df)
count_row = df.shape[0]
count_col = df.shape[1]
print("No of rows in data:-",count_row)
print("No of columns in data:-",count_col)

# Crops Names

crops=['Rice','Wheat','Pearl Millet','Maize','Chick pea','Pigeon pea','Groundnut','Sesamum','Sunflower','Soyabean','Sugarcane','Cotton']
# crop production column names
crproduction=['RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','PEARL MILLET PRODUCTION (1000 tons)','MAIZE PRODUCTION (1000 tons)','CHICKPEA PRODUCTION (1000 tons)','PIGEONPEA PRODUCTION (1000 tons)','GROUNDNUT PRODUCTION (1000 tons)','SESAMUM PRODUCTION (1000 tons)','SUNFLOWER PRODUCTION (1000 tons)','SOYABEAN PRODUCTION (1000 tons)','SUGARCANE PRODUCTION (1000 tons)','COTTON PRODUCTION (1000 tons)']

#print(df.head())

# in data there is a columns named (state code,state name) and data is only of maharashtra that's why we deleted state code and state name column column
# we also deleted column named dist code this column data doesn't find that much useful
df = df.drop(['State Code','State Name','Dist Code'], axis=1)
# There is district called Bombay we all know that Bombay is Urban Area and land aquire for agriculture is too small and in that land pepole only do farming of rice which also less than 2-3 (1000 thousand) ton so we delete Bombay district data
indexAge = df[ (df['Dist Name'] =='Bombay')].index
df.drop(indexAge , inplace=True)
# Updated Rows and Columns
count_row = df.shape[0]
count_col = df.shape[1]
print("Updated No of rows in data:-",count_row)
print("Updated No of columns in data:-",count_col)

# District wise production
# District names
def dict():
    init = []
    for i in df['Dist Name']:
        if(i not in init):
            init.append(i)
    init = sorted(init)
    return init

District =dict()
print(District)


# Pie chart With For loop

def piechart():
    for i in range(0,len(crops)):
        listforproduction = []
        for j in District:
            dfd = df[df['Dist Name'] == j]
            listforproduction.append(sum(dfd[crproduction[i]]))

        print(listforproduction)
        data = {
            'District': District,
            'Production': listforproduction
        }
        dfforrice = pd.DataFrame(data)
        # Sorting by Production
        dfforrice.sort_values(['Production'], ascending=False, inplace=True)
        # Finding Total Production till date
        totalprod = sum(listforproduction)
        # deleting districts whose production is less than 1 %

        indexAge = dfforrice[(dfforrice['Production'] < totalprod*1/100)].index
        dfforrice.drop(indexAge, inplace=True)
        print(dfforrice)
        # plotting
        plt.pie(dfforrice['Production'], labels=dfforrice['District'], autopct='%1.1f%%', radius=1.3)
        tstring=crops[i]
        ttstring="Production of {} in Districts".format(tstring)
        plt.title(ttstring, bbox={'facecolor': (0.7, 0.1, 0.1), 'pad': 4}, pad=56)
        print("Hello")
        fig1 = plt.gcf()
        plt.show()
        #plt.draw()
        fname='pie_{}'.format(crops[i])
        fig1.savefig('{}.png'.format(fname), dpi=800)
        #tm.sleep(1)

#piechart()

#total production per crops of each district

def barplot():
    for i in  District:
        dfd = df[df['Dist Name'] == i]
        listforttl=[]
        for j in crproduction:
            listforttl.append(sum(dfd[j]))

        print(listforttl)
        datad = {
                    'Crops': crops,
                    'Production': listforttl
                }
        print(datad)


        Crops = list(datad['Crops'])
        Production = list(datad['Production'])

        #fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(Crops, Production,color =['red','orange','yellow','green','blue','indigo','violet','purple','pink','silver','gold','beige'],width=0.4)

        plt.xlabel("Crops Name's")
        plt.ylabel("Production (*1000 Tons)")
        plt.title("Production of Each Crop of {} District".format(i))
        fig1 = plt.gcf()
        plt.show()
        #plt.draw()
        #fig1.savefig('tessstttyyy.png', dpi=800)
        fname = 'bar_{}'.format(i)
        fig1.savefig('{}.png'.format(fname), dpi=800)
       # tm.sleep(1)

piechart()
#barplot()