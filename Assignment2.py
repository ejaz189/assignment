

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
def read(name):
    '''
    reading data from read function
    '''
    # read data
    df = pd.read_csv(name,skiprows=4)
    
    origdata=df.drop(['Country Code', 'Indicator Code'],axis=1)
    
    countdata=df.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis=1)
    
    yedata= df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',],axis=1).T
    
    yedata.index.name='Years'
    
    # print the data of head
    print(yedata.head)
    print(countdata.head)
    print(origdata.head)
    print(origdata.T)
    
    # return data value of year and column
    return countdata,yedata,origdata

    # plot a lie graph
def agriculture_line_graph(data,indicator,indicator_name):
    '''
    this function plot graph line plot of specific country 
    '''
    # create a dataframe
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="Zambia"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Brazil"].drop(['Country Name','Indicator Name'],axis=1)
    
    morocco=fdata[fdata["Country Name"]=="Peru"].drop(['Country Name','Indicator Name'],axis=1)
    
    mexico=fdata[fdata["Country Name"]=="Sweden"].drop(['Country Name','Indicator Name'],axis=1)
  
    # year data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),uk.iloc[0].dropna().to_numpy() , label = "Zambia",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),latvia.iloc[0].dropna().to_numpy() , label = "Brazil",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),morocco.iloc[0].dropna().to_numpy() , label = "Peru",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),mexico.iloc[0].dropna().to_numpy() , label = "Sweden",linestyle="-.")
    
      
    # x axis name
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # title of graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()
    
def urban_line_graph(data,indicator,indicator_name):
    '''
    this function plot graph line plot of 4 country
    '''
    # create a dataframe
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="Zambia"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Brazil"].drop(['Country Name','Indicator Name'],axis=1)
    
    morocco=fdata[fdata["Country Name"]=="Peru"].drop(['Country Name','Indicator Name'],axis=1)
    
    mexico=fdata[fdata["Country Name"]=="Sweden"].drop(['Country Name','Indicator Name'],axis=1)
  
    # year data frame
    year=data.drop(['Country Name','Indicator Name'],axis=1).T.index
    
    print(year)
    
    # plotting the points 
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),uk.iloc[0].dropna().to_numpy() , label = "Zambia",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),latvia.iloc[0].dropna().to_numpy() , label = "Brazil",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),morocco.iloc[0].dropna().to_numpy() , label = "Peru",linestyle="-.")
    plt.plot(pd.to_numeric(year[0:60].to_numpy()),mexico.iloc[0].dropna().to_numpy() , label = "Sweden",linestyle="-.")
    
      
    # x axis name
    plt.xlabel('year')
    # naming the y axis
    plt.ylabel('data')
    plt.legend()
    # title of graph
    plt.title(indicator_name)
      
    # function to show the plot
    plt.show()
    
   
    
 # plot a bar graoh  
def agriculture_bar_plot(data,indicator,indicator_name):
    '''
    function will show bar plot graph for the 4 countries year 1996 to 2016
    '''
    #  creating a data frame
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="Zambia"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Brazil"]
    
    morocco=fdata[fdata["Country Name"]=="Peru"]
    
    mexico=fdata[fdata["Country Name"]=="Sweden"]
    
    index = ['1996', '2000', '2004',
          '2008', '2012', '2016']
    
    df = pd.DataFrame({'Brazil':  [latvia['1996'].iloc[0],latvia['2000'].iloc[0],latvia['2004'].iloc[0],latvia['2008'].iloc[0],latvia['2012'].iloc[0],latvia['2016'].iloc[0],],
                       'Peru': [morocco['1996'].iloc[0],morocco['2000'].iloc[0],morocco['2004'].iloc[0],morocco['2008'].iloc[0],morocco['2012'].iloc[0],morocco['2016'].iloc[0],],
                       'Zambia':  [uk['1996'].iloc[0],uk['2000'].iloc[0],uk['2004'].iloc[0],uk['2008'].iloc[0],uk['2012'].iloc[0],uk['2016'].iloc[0],],
                    'Sweden':  [mexico['1996'].iloc[0],mexico['2000'].iloc[0],mexico['2004'].iloc[0],mexico['2008'].iloc[0],mexico['2012'].iloc[0],mexico['2016'].iloc[0],],
                    
                    }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()
    
def mortality_bar_plot(data,indicator,indicator_name):
    '''
    this function show bar plot graph for the 4 countries year 1996 to 2016
    '''
    #  creating a data frame
    fdata=data[data["Indicator Name"]==indicator]
    
    uk=fdata[fdata["Country Name"]=="Zambia"].drop(['Country Name','Indicator Name'],axis=1)

    latvia=fdata[fdata["Country Name"]=="Brazil"]
    
    morocco=fdata[fdata["Country Name"]=="Peru"]
    
    mexico=fdata[fdata["Country Name"]=="Sweden"]
    
    index = ['1996', '2000', '2004',
          '2008', '2012', '2016']
    
    df = pd.DataFrame({'Brazil':  [latvia['1996'].iloc[0],latvia['2000'].iloc[0],latvia['2004'].iloc[0],latvia['2008'].iloc[0],latvia['2012'].iloc[0],latvia['2016'].iloc[0],],
                      'Peru': [morocco['1996'].iloc[0],morocco['2000'].iloc[0],morocco['2004'].iloc[0],morocco['2008'].iloc[0],morocco['2012'].iloc[0],morocco['2016'].iloc[0],],
                      'Zambia':  [uk['1996'].iloc[0],uk['2000'].iloc[0],uk['2004'].iloc[0],uk['2008'].iloc[0],uk['2012'].iloc[0],uk['2016'].iloc[0],],
                   'Sweden':  [mexico['1996'].iloc[0],mexico['2000'].iloc[0],mexico['2004'].iloc[0],mexico['2008'].iloc[0],mexico['2012'].iloc[0],mexico['2016'].iloc[0],],
                   
                   }, index=index)
    
    # ploting bar graph
    ax = df.plot.barh(title=indicator_name)
    
    plt.show()

# plot a heatmap with annotation
def Brazil_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of latvia between indicators for better understanding
    '''
    
    #conditions applied on country name
        
    # create data frame
    fdata=pd.DataFrame()
        
    # getting indicator data
    bradata=data[data["Indicator Name"]=="Methane emissions (kt of CO2 equivalent)"]
        
    # get united states data 
    bradata=bradata[bradata['Country Name']=="Zambia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan values
    bradata=bradata.dropna().T
        
    # get urban population data
    fdata["Methane emissions (kt of CO2 equivalent)"]=bradata.iloc[0]
        
    #  get arable data
    bradata=data[data["Indicator Name"]=='Arable land (% of land area)']
        
        
    bradata=bradata[bradata['Country Name']=="Zambia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Arable land (% of land area)']=bradata.iloc[0]
        
    #  get cereal data
    bradata=data[data["Indicator Name"]=='Population growth (annual %)']
        
    bradata=bradata[bradata['Country Name']=="Zambia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Population growth (annual %)']=bradata.iloc[0]
        
    bradata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
    
    bradata=bradata[bradata['Country Name']=="Zambia"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
    
    fdata['Agricultural land (sq. km)']=bradata.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # ploting heatmap
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
                             
        annot=True,ax=ax
                
                )
        # add title
    ax.set_title('Zambia')
        
    plt.show()
    
# plot a heatmap with annotation
def Peru_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of latvia between indicators for better understanding
    '''
    
    #conditions applied on country name
        
    # create data frame
    fdata=pd.DataFrame()
        
    # getting indicator data
    bradata=data[data["Indicator Name"]=="Methane emissions (kt of CO2 equivalent)"]
        
    # get united states data 
    bradata=bradata[bradata['Country Name']=="Brazil"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan values
    bradata=bradata.dropna().T
        
    # get urban population data
    fdata["Methane emissions (kt of CO2 equivalent)"]=bradata.iloc[0]
        
    #  get arable data
    bradata=data[data["Indicator Name"]=='Arable land (% of land area)']
        
        
    bradata=bradata[bradata['Country Name']=="Brazil"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Arable land (% of land area)']=bradata.iloc[0]
        
    #  get cereal data
    bradata=data[data["Indicator Name"]=='Population growth (annual %)']
        
    bradata=bradata[bradata['Country Name']=="Brazil"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Population growth (annual %)']=bradata.iloc[0]
        
    bradata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
    
    bradata=bradata[bradata['Country Name']=="Brazil"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
    
    fdata['Agricultural land (sq. km)']=bradata.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # ploting heatmap
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
                             
        annot=True,ax=ax
                
                )
        # add title
    ax.set_title('Brazil')
        
    plt.show()


# plot a heatmap with annotation
def Zambia_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of latvia between indicators for better understanding
    '''
    
    #conditions applied on country name
        
    # create data frame
    fdata=pd.DataFrame()
        
    # getting indicator data
    bradata=data[data["Indicator Name"]=="Methane emissions (kt of CO2 equivalent)"]
        
    # get united states data 
    bradata=bradata[bradata['Country Name']=="Peru"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan values
    bradata=bradata.dropna().T
        
    # get urban population data
    fdata["Methane emissions (kt of CO2 equivalent)"]=bradata.iloc[0]
        
    #  get arable data
    bradata=data[data["Indicator Name"]=='Arable land (% of land area)']
        
        
    bradata=bradata[bradata['Country Name']=="Peru"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Arable land (% of land area)']=bradata.iloc[0]
        
    #  get cereal data
    bradata=data[data["Indicator Name"]=='Population growth (annual %)']
        
    bradata=bradata[bradata['Country Name']=="Peru"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Population growth (annual %)']=bradata.iloc[0]
        
    bradata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
    
    bradata=bradata[bradata['Country Name']=="Peru"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
    
    fdata['Agricultural land (sq. km)']=bradata.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # ploting heatmap
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
                             
        annot=True,ax=ax
                
                )
        # add title
    ax.set_title('Peru')
        
    plt.show()
        

        
# plot a heatmap with annotation
def Sweden_correlation_heatmap(data,name):
    '''
    this function show heatmap and correlations of latvia between indicators for better understanding
    '''
    
    #conditions applied on country name
        
    # create data frame
    fdata=pd.DataFrame()
        
    # getting indicator data
    bradata=data[data["Indicator Name"]=="Methane emissions (kt of CO2 equivalent)"]
        
    # get united states data 
    bradata=bradata[bradata['Country Name']=="Sweden"].drop(['Country Name','Indicator Name'],axis=1).T
        
    # drop nan values
    bradata=bradata.dropna().T
        
    # get urban population data
    fdata["Methane emissions (kt of CO2 equivalent)"]=bradata.iloc[0]
        
    #  get arable data
    bradata=data[data["Indicator Name"]=='Arable land (% of land area)']
        
        
    bradata=bradata[bradata['Country Name']=="Sweden"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Arable land (% of land area)']=bradata.iloc[0]
        
    #  get cereal data
    bradata=data[data["Indicator Name"]=='Population growth (annual %)']
        
    bradata=bradata[bradata['Country Name']=="Sweden"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
        
    fdata['Population growth (annual %)']=bradata.iloc[0]
        
    bradata=data[data["Indicator Name"]=='Agricultural land (sq. km)']
    
    bradata=bradata[bradata['Country Name']=="Sweden"].drop(['Country Name','Indicator Name'],axis=1).T
        
    bradata=bradata.dropna().T
    
    fdata['Agricultural land (sq. km)']=bradata.iloc[0]
        
    # plot a heatmap with annotation
        
    ax = plt.axes()
        
    # ploting heatmap
    heatmap = sns.heatmap(fdata.corr(), cmap="tab10",
                             
        annot=True,ax=ax
                
                )
        # add title
    ax.set_title('Sweden')
        
    plt.show()
   
                       
    
    # that is main function
if __name__ == "__main__":
    
    coundata,yedata,origdata=read("data.csv")
    
    agriculture_bar_plot(origdata,'Methane emissions (kt of CO2 equivalent)','Methane emissions (kt of CO2 equivalent)')
    
    mortality_bar_plot(origdata,'Population growth (annual %)','Population growth (annual %)')
    
    agriculture_line_graph(origdata, 'Arable land (% of land area)','Arable land (% of land area)')
    
    urban_line_graph(origdata, 'Agricultural land (sq. km)','Agricultural land (sq. km)')
    
    Brazil_correlation_heatmap(origdata,"France")
    
    Peru_correlation_heatmap(origdata,"Peru")
    
    Zambia_correlation_heatmap(origdata,"Zambia")
    
    Sweden_correlation_heatmap(origdata,"Sweden")
