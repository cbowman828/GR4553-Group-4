# GR4553-Group-4
Project Overview:
This project is a case study of the “Halloween Floods” in Austin, Texas on October 31, 2013. Within this repository, there are plots depicting synoptic maps that show the synoptic setup behind the event. There is also radar data from a nearby NWS NEXRAD radar site that shows the base reflectivity on the day of the event. Plots depicting the hourly rainfall data at local METAR stations are also provided in the repository as well as plots showing water levels at three local creeks/rivers in the Austin Area.

 Radar Plots:
	Overview:
The radar codes (stored in the files KEWX - AUSTIN S ANT, TX Radar 1204 AM CDT 1031 code.py, KEWX – AUSTIN S ANT, TX Radar 602 AM CDT 1031 code.py, KEWX - AUSTIN S ANT, TX Radar 1203 PM 1031 code.py, and KEWX - AUSTIN S ANT, TX Radar 600 PM CDT 1031 code.py) provide radar base reflectivity plots for the KEWX National Weather Service Doppler Radar in New Braunfels, Texas which serves the Austin and San Antonio area. The code is for the times 12:04 AM, 6:02 AM, 12:03 PM, and 6:00 PM CDT on October 31 2013.
	Data Files:
•	https://noaa-nexrad-level2.s3.amazonaws.com/2013/10/31/KEWX/KEWX20131031_000403_V06.gz
•	https://noaa-nexrad-level2.s3.amazonaws.com/2013/10/31/KEWX/KEWX20131031_060235_V06.gz
•	https://noaa-nexrad-level2.s3.amazonaws.com/2013/10/31/KEWX/KEWX20131031_120325_V06.gz
•	https://noaa-nexradlevel2.s3.amazonaws.com/2013/10/31/KEWX/KEWX20131031_180016_V06.gz.
Code:
	The code utilized was borrowed from a template created by Dr. Johna Rudzin at Mississippi State University for GR4553 Computer Methods in Meteorology.
	In order to run the code, one must first install and import metpy, cartopy.crs, matplotlib.gridspec, matplotlib.pyplot, and numpy.
	NEXRAD data can be obtained by going to NOAA’s National Centers for Environmental Information. The following is the url for the data that we obtained from the KEWX radar:
https://www.ncdc.noaa.gov/nexradinv/bdpdownload.jsp?id=KEWX&yyyy=2013&mm=10&dd=31&product=AAL2.
To plot radar data from a different file, simply replace the file in line 25 with the file that you want to use. For example, in KEWX - AUSTIN S ANT, TX Radar 1203 PM 1031 code.py, line 25 is f = Level2File('KEWX20131031_120325_V06') where KEWX20131031_120325_V06 can be replaced with a different file if desired. The title of the plot can be changed in line 94 using the plt.title() function.

Water Levels Plots:
	Overview:
The water levels codes (stored in the files Colorado River Levels code.txt, Walnut Creek Water Levels code.txt, and Williamson Creek Levels code.txt) plot the water levels (in feet) over the course of the day on October 31, 2013. The data used for these plots was obtained from the United States Geographical Survey’s (USGS) National Water Dashboard. Three monitoring stations were used: the Colorado River at Austin, TX site, the Walnut Creek at Webberville Road site, and the Williamson Creek at Jimmy Clay Road site. All of these stations saw significant increases in water levels in a short period of time on the day of the event.
	Code:
Running the code is relatively simple. First, one must install and import matplotlib.pyplot. To create a plot for a different set of data, replace the current text file in line 10. For example, in Colorado River Levels code.txt, line 10 is crl=open('coloradoriverlevels.txt') where crl is simply a variable that can be changed if desired and coloradoriverlevels.txt can be replaced with a different text file. 
Two arrays (rl and time) are defined as variables. A double for loop is used to append data into these variables within a specified range. The range of the initial for loop can be changed to encompass the number of times desired to be plotted. For example, in Colorado River Levels code.txt, the for loop is in the range 125-221 (this is in line 17). Changing this range will change the number of rows (which have river level values for different times when observations were taken). Since the times for the data are using a 24-hour clock, only choose times within a 24-hour period, or else the plot will not look right. The .split() function splits the data into separate columns. The sub for loop is where the data for the times and river levels is appended into the arrays mentioned above.
The data is then plotted using matplotlib.pyplot on a cartesian plane where the y-axis is the water level in feet (using the variable “rl”) and the x-axis is the time of day (using the variable “time”). The color of the plot can be changed in line 27 by changing the letter in single quotation marks in color=’’. Labels can be changed within the plt.xlabel and plt.ylabel parenthetical statements. Changing the number after the double colons in line 30 (plt.xticks(time[::180],rotation=45) changes how many times are displayed on the x-axis of the plot. The function plt.grid(True) plots gridlines on the meteogram). The function plt.title() changes the title of the meteogram.


Metar/ASOS plots:

	Overview:
This code is for plotting the METAR/ASOS Data observations for 1 hr precipitation that were taken from Iowa State's Website that houses archived data on the Environmental Mesonet page. I searched the Austin, TX region to find stations that reflect the scale of the impact from the flash flooding event that took place in the area. This code is using matplotlib and a CSV reader since the data was set in that format. The matplotlib code was used in order to plot the x and y data. The x data was the time series, and the y data was how much precipitation fell (in inches) for each hour interval.
Code:
To start, we used the csv reader to read the csv files located in excel. We read the dictionaries for both rows and columns. 
After this, we set up the variables that were going to be used in the plots. We defined the x and y data as the columns that had the amount of precipitation and the times they were recorded at. 
Then, we used matplotlib to plot the x and y data previously defined to properly set up the plots to be coded. I used a cyan color in order for the data to be read easier. I then plotted the x data along with a title to go with it. 
A problem that I ran into while using this code was that the time data names were cluttered together on the x axis and could not be read. To correct this, I wrote a small section of code to tilt the title fonts 45 degrees so that it could be read easier. 
After this, I plotted the precipitation data onto the y axis which measurement units being in inches. 
Finally, I wrote out the main title to the graph and plotted a grid to help align the point data to make it more comprehensive. I repeated this process for all other ASOS data that I collected.

Synoptic Charts:

	Overview:
For this code we utilize many of the mapping functions of cartopy as well as using the generic wpc surface bulletin code from metpy. For each of the synoptic maps the background maps are the same background utilizing adjustable settings for all of the background types of the map. 
Code:
To start with we import all of the needed packages such as cartopy, matplotlib, pygrib, and metpy. Additionally, the dataset that we want to work with needs to be given a variable. Any data sets can be used but some of the messages and metadata for these data will change depending on model or reanalysis data. 
As stated above, the background maps are all the same for the most part. We take the map and set it to the proper area needed to be displayed and to the projection that is required. Once the background map is built then you just need to parse the data you want to display on each map. First you define the message and then you take the values from the message. Next you make sure you have the correct bounds for your data using the lats, lons function. Repeat this for any data that you want to use on that map.
To plot the data, you use the contour or countourf function if you want to shade in the maps. When using these commands, you can define bounds as well as scale values however you want them to be displayed. For wind barbs, the barbs function is well suited. Additionally, a color bar can be added for any shaded or lined data that you want to be displayed as well as where you want it to be displayed. Finally, a title is set to describe the map that was created. This is the general form for all of the standard synoptic level maps.
For the surface front maps, we utilized the metpy parse_wpc_surface_bulletin commands as well as importing the correct plots from metpy. Similarly to above, you set up background map that is desired. First you need to download the bulletin you want to display. Alternatively, you could create code that grabs whatever data and time you desire. Then you run the parse wpc bulletin package to read the data and plot it. Once again you set a title to display the map you’ve plotted. 
At the end it is best to close the datasets and any documents that were opened. 
