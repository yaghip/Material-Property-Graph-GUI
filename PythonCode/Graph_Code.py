import pyodbc
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

def load_sql(filename):
    with open (filename) as file:
        return file.read() #openin file 

def thickness_check(thickness, composition, heattreatment, paintbake): 
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./TensileData_Database.accdb;')
    cursor = conn.cursor() 

    cursor.execute(load_sql('load_alldata.sql'), composition, heattreatment, paintbake, thickness) #corresponds to above inputs
    
    list30uts = []
    list30ys = []
    list30el = []
    list30date = []

    list25uts = []
    list25ys = []
    list25el = []
    list25date = []

    list23uts = []
    list23ys = []
    list23el = []
    list23date = []

    for row in cursor.fetchall():
        date, UTS, YS, El = row
        if thickness == "30":
            list30uts.append(UTS)
            list30ys.append(YS)
            list30el.append(El)
            list30date.append(date)
        elif thickness == "25":
            list25uts.append(UTS)
            list25ys.append(YS)
            list25el.append(El)
            list25date.append(date)
        elif thickness == "23":
            list23uts.append(UTS)
            list23ys.append(YS)
            list23el.append(El)
            list23date.append(date)

    if thickness == "30":
        options = {
            "Ultimate Tensile Strength" : list30uts,
            "Yield Strength" : list30ys,
            "Percent Elongation" : list30el,
            "Date" : list30date
        }
        return options
    elif thickness == "25":
        options = {
            "Ultimate Tensile Strength"  : list25uts,
            "Yield Strength" : list25ys,
            "Percent Elongation" : list25el,
            "Date" : list25date
        }
        return options
    else:
        options = {
            "Ultimate Tensile Strength"  : list23uts,
            "Yield Strength" : list23ys,
            "Percent Elongation" : list23el,
            "Date" : list23date
        }
        return options

def alldata_func(composition, heattreatment, paintbake, thickness, xaxis, yaxis): 
    
    options = thickness_check(thickness, composition, heattreatment, paintbake)
    
    x_data = options[xaxis]
    y_data = options[yaxis]
    
    # x = np.array(x_data)
    # y = np.array(y_data)
    # m, b = np.polyfit(x, y, 1)

    fig=plt.figure() 

    ax=fig.add_subplot(111)
    ax.scatter(options[xaxis], options[yaxis], color='black', marker='.')
   
#    plt.plot(x, m*x + b) 

    xlabel = xaxis
    ax.set_xlabel(xlabel)
    ylabel = yaxis
    ax.set_ylabel(ylabel) 

    ax.set_title(xlabel + ' vs ' + ylabel +  '\n' + composition + " " + heattreatment + " " + paintbake + " " + thickness)

    plt.show()


#############################################################

def avgthickness_check(thickness, composition, heattreatment, paintbake): 
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./TensileData_Database.accdb;')
    cursor = conn.cursor() 

    cursor.execute(load_sql('averagedata.sql'), composition, heattreatment, paintbake, thickness)

    list30avguts = []
    list30avgys = []
    list30avgel = []
    list30avgdate = []
    list30stdevuts = []
    list30stdevys = []
    list30stdevel = []
    list30stdevdate = []

    list25avguts = []
    list25avgys = []
    list25avgel = []
    list25avgdate = []
    list25stdevuts = []
    list25stdevys = []
    list25stdevel = []
    list25stdevdate = []

    list23avguts = []
    list23avgys = []
    list23avgel = []
    list23avgdate = []
    list23stdevuts = []
    list23stdevys = []
    list23stdevel = []
    list23stdevdate = []

    for row in cursor.fetchall(): #cursor performs search, fetchall goes through all results 
        date, uts_avg, ys_avg, el_avg, uts_stdev, ys_stdev, el_stdev, date_stdev = row
        if thickness == "30":
            list30avguts.append(uts_avg)
            list30avgys.append(ys_avg)
            list30avgel.append(el_avg)
            list30avgdate.append(date)
            list30stdevuts.append(uts_stdev)
            list30stdevys.append(ys_stdev)
            list30stdevel.append(el_stdev)
            list30stdevdate.append(date_stdev)
        elif thickness == "25":
            list25avguts.append(uts_avg)
            list25avgys.append(ys_avg)
            list25avgel.append(el_avg)
            list25avgdate.append(date)
            list25stdevuts.append(uts_stdev)
            list25stdevys.append(ys_stdev)
            list25stdevel.append(el_stdev)
            list25stdevdate.append(date_stdev)
        elif thickness == "23":
            list23avguts.append(uts_avg)
            list23avgel.append(el_avg)
            list23avgys.append(ys_avg)
            list23avgdate.append(date)
            list23stdevuts.append(uts_stdev)
            list23stdevys.append(ys_stdev)
            list23stdevel.append(el_stdev)
            list23stdevdate.append(date_stdev)

    if thickness == "30":
        options = {
            "Ultimate Tensile Strength" : {tuple(list30avguts): list30stdevuts},
            "Yield Strength" : {tuple(list30avgys): list30stdevys},
            "Percent Elongation" : {tuple(list30avgel): list30stdevel}, 
            "Date" : {tuple(list30avgdate): list30stdevdate}
        }
        return options
    elif thickness == "25":
        options = {
            "Ultimate Tensile Strength"  : {tuple(list25avguts): list25stdevuts},
            "Yield Strength" : {tuple(list25avgys): list25stdevys},
            "Percent Elongation" : {tuple(list25avgel): list25stdevel}, 
            "Date" : {tuple(list25avgdate): list25stdevdate}
        }
        return options
    else:
        options = {
            "Ultimate Tensile Strength"  : {tuple(list23avguts): list23stdevuts},
            "Yield Strength" : {tuple(list23avgys): list23stdevys},
            "Percent Elongation" : {tuple(list23avgel): list23stdevel}, 
            "Date" : {tuple(list23avgdate): list23stdevdate}
        }
        return options

def averagedata_func(composition, heattreatment, paintbake, thickness, xaxis, yaxis): 
    
    options = avgthickness_check(thickness, composition, heattreatment, paintbake)

 
    x_data = options[xaxis]
    y_data = options[yaxis]   
    date_data = options["Date"]

    for k1, v1 in x_data.items():
        x_dataavg = list(k1)
        x_datastdev = v1

    for k2, v2 in y_data.items():
        y_dataavg = list(k2)
        y_datastdev = v2

    for k3, v3 in date_data.items():
        data_avg = list(k3)


    fig=plt.figure() 
    ax=fig.add_subplot(111)
    # ax.scatter(x_dataavg, y_dataavg, color='r', marker='1')

    plt.errorbar(x_dataavg, y_dataavg, yerr = y_datastdev, xerr = x_datastdev, fmt='.', color='black', ecolor='lightgray', capsize=2)

    xlabel = xaxis
    ax.set_xlabel(xlabel)
   
    ylabel = yaxis
    ax.set_ylabel(ylabel) 
    
    for i, txt in enumerate(data_avg):
        ax.annotate(txt, (x_dataavg[i], y_dataavg[i]))

    ax.set_title(xlabel + ' vs ' + ylabel + ' (Average)' + '\n' + composition + " " + heattreatment + " " + paintbake + " " + thickness)
    plt.show()
    print(x_dataavg)
    print(y_dataavg)

# def avg_stdev_conf_data(composition, heattreatment, paintbake, thickness, xaxis, yaxis):
#     options = avgthickness_check(thickness, composition, heattreatment, paintbake)

 
#     x_data = options[xaxis]
#     y_data = options[yaxis]   
  
    
#     for k1, v1 in x_data.items():
#         x_dataavg = list(k1)
#         x_datastdev = v1

#     for k2, v2 in y_data.items():
#         y_dataavg = list(k2)
#         y_datastdev = v2
    
#     fig=plt.figure() 
#     ax=fig.add_subplot(111)
#     ax.scatter(x_dataavg, y_dataavg, color='r', marker='1')
#     plt.errorbar(x_dataavg, y_dataavg, yerr = y_datastdev , fmt='o')
#     ax = sns.regplot(x_dataavg, y_dataavg)
#     xlabel = xaxis
#     ax.set_xlabel(xlabel)
   
#     ylabel = yaxis
#     ax.set_ylabel(ylabel) 
    
#     ax.set_title(xlabel + ' vs ' + ylabel + ' (Average)')
#     plt.show()

def ave_alldata(composition, heattreatment, paintbake, thickness, xaxis, yaxis):

    options = avgthickness_check(thickness, composition, heattreatment, paintbake)

 
    x_data = options[xaxis]
    y_data = options[yaxis]   
    date_data = options["Date"]

    for k1, v1 in x_data.items():
        x_dataavg = list(k1)
        x_datastdev = v1

    for k2, v2 in y_data.items():
        y_dataavg = list(k2)
        y_datastdev = v2

    for k3, v3 in date_data.items():
        data_avg = list(k3)

    options = thickness_check(thickness, composition, heattreatment, paintbake)
    x_data = options[xaxis]
    y_data = options[yaxis]
    
    fig=plt.figure() 
    ax=fig.add_subplot(111) 
    ax.scatter(options[xaxis], options[yaxis], color='black', marker='.')
    plt.errorbar(x_dataavg, y_dataavg, yerr = y_datastdev, xerr = x_datastdev, fmt='.', color='red', ecolor='lightgray', capsize=2)
    
    
    xlabel = xaxis
    ax.set_xlabel(xlabel)
   
    ylabel = yaxis
    ax.set_ylabel(ylabel) 
    
   
    ax.set_title(xlabel + ' vs ' + ylabel + ' (Average + Raw Data)' + '\n' + composition + " " + heattreatment + " " + paintbake + " " + thickness)
    
    plt.show()
