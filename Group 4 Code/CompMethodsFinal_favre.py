Ford F.

#Importing matplotlib and csv in order to read csv files and plot their data.
import matplotlib.pyplot as plt
import csv

#Scatterplot for Austin Bergstrom-------------------

#Reading the Data in teh csv file format:
data=[]
with open('AustinBergstrom_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
#Setting up variables for refrence when plotting the correct data on the graphs:
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

#Using matplotlib to plot the data:
plt.plot(p01i, valid, 'co')

#Ploting the x data with title:
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')

#Rotating x-labels 45 degrees to make plots easier to read and fix oversaturation of values:
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)

#Plotting the y data with title:
plt.ylabel('Precipitation Fallen in 1 hr (in)')

#Creating Title for the Graph and creating a gridded plot with x and y data:
plt.title('1 hr Precipitation for Austin Bergstrom Int. Airport, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Same process is repeated for all other plots:

#Scatterplot for Austin Camp Mabry------------------
data=[]
with open('AustinCampMabry_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Austin Camp Mabry, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Austin EDC------------------------
data=[]
with open('AustinEDC_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Austin City METAR, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Georgetown----------------------
data=[]
with open('Georgetown_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Georgetown, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Giddings------------------------
data=[]
with open('Giddings_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Giddings, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Horseshoe-----------------------
data=[]
with open('Horseshoe_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Horseshoe, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for Lago Vista----------------------
data=[]
with open('LagoVista_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for Lago Vista, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for New Braunfels------------------
data=[]
with open('NewBraunfels_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for New Braunfels, TX')
plt.grid(True)
plt.tight_layout()
plt.show()

#Scatterplot for San Marcos---------------------
data=[]
with open('SanMarcos_METAR.csv','r') as file:
    csv.file = csv.DictReader(file)
    for row in csv.file:
        data.append(dict(row))
                    
valid = [x["p01i"] for x in data]
p01i = [y["valid"] for y in data]

x="valid"
valid = [eval(i) for i in valid]
y="p01i"

plt.plot(p01i, valid, 'co')
plt.xlabel('Time Valid for 10/31/2013 (Local Time)')
plt.xticks(range(0,len(p01i),2),p01i[::2], rotation=45)
plt.ylabel('Precipitation Fallen in 1 hr (in)')
plt.title('1 hr Precipitation for San Marcos, TX')
plt.grid(True)
plt.tight_layout()
plt.show()