# dav-homework6

                            Interactive plots
====================================================================

In previous exercises we focused on static and animated plots. 
We now move to so-called interactive plots.

====================================================================

We will focus on a few python libraries:
- mpld3     http://mpld3.github.io
- pygal     http://www.pygal.org/en/stable/
- plotly    https://plotly.com/python
- Bokeh     https://docs.bokeh.org
- HoloViews http://holoviews.org
- Altair    https://altair-viz.github.io/gallery/index.html#interactive-charts

====================================================================

The task:

From the six libraries above choose three.

Next using each library generate two, separate, interactive plots 

For instance:

mpld3_plot1_data1.py
mpld3_plot2_data2.py

pygal_plot1_data3.py
pygal_plot2_data4.py

bokeh_plot1_data5.py
bokeh_plot2_data6.py

(Six plots in total)

You can use the data from previous exercises, but you do not need to.
You are not allowed to use examples from libraries tutorials/galleries 
(obviously, you can use them for learning purposes).

Hint: frequently the data used for making animated plots can be easily 
transformed into the interactive plot, but it may require to move to 
different plot type e.g. bar plot with time (the dimension upon we 
updated plot for population) can be scatter plot with tooltips

====================================================================

Extra task (aka redemption task):

You can earn up to an extra 50% if you generate each plot using each 
library on the same data from the main task (18 plots).

For instance: 

mpld3_data1.py      mpld3_data2.py      mpld3_data3.py
pygal_data1.py      pygal_data2.py      pygal_data3.py
bokeh_data1.py      bokeh_data2.py      bokeh_data3.py

mpld3_data4.py      mpld3_data5.py      mpld3_data6.py
pygal_data4.py      pygal_data5.py      pygal_data6.py
bokeh_data4.py      bokeh_data5.py      bokeh_data6.py

====================================================================

Prepare the homework as a project directory with the above plots. 

It should contain:
- the main report file in HTML form (with all the plots embedded)* 
- the data for plots
- the python scripts generating plots (one script per one plot)**
- the separate plots

*  static HTML without external dependencies
** plain python plots (*.py)- thus no jupyter notebooks

Additionally, the script should one parameter [0/1] for showing or 
saving the plot.

For instance typing in the terminal: 
python plot1.py 0      [will show the plot in interactive mode, plt.show()]
python plot1.py 1      [will store the plot in the file and print the path to the file]

All files should be sent until 03.05.2020
via email to lukaskoz@mimuw.edu.pl with the email subject:
'lab9_hw_Name_Surname' without email text body and with 
'lab9_hw_Name_Surname.7z' (ASCII letters only) attachment.

All emails with a different structure (the one that will not go 
through email filter to the proper email folder dedicated for 
home works) will be scored -10% 

Using non-English labels, legends, descriptions, etc. will be scored -10%

Additionally, all problems with the structure of the plot e.g.
the plot size, labels font size, etc. will also affect the grading. 
You need to follow the advice included in the lectures.
