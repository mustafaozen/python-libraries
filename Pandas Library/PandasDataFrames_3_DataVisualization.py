'''
This script provides simple examples to data visualization on DataFrames using built-in functions in Pandas library.
The Pandas library has some built-in visualization functions such as:
-- Histogram Plot
-- Density Plot
-- Bar Plot
-- Box Plot
-- Kernel Density Estimator Plot
-- Line Plot
-- Scatter Plot, etc.
Also using Matplotlib library, the figure can be further edited. See "Matplotlib Library" folder for more details.
'''

import pandas as pnd
import numpy as npy
import matplotlib.pyplot as plt
npy.random.seed(101)


# Menu #
while(True):
    inp = input('What type of figure would you like to see? \n'
                '1. Histogram Plot\n'
                '2. Density/KDE Plot\n'
                '3. Bar Plot\n'
                '4. Scatter Plot\n'
                '5. Hexagonal Bin Plot\n'
                '6. Box Plot\n'
                '7. Exit \n\n'
                'Your choice is: '
                )

    if(inp.isdigit()):
        choice = int(inp)

        # Create a random DataFrame
        dFrame = pnd.DataFrame(data = npy.random.randn(3000,2), columns = ['Col1', 'Col2'])
        #print(dFrame.head(),'\n') # .head() function returns top 5 rows of the DataFrame

        ## 1. Histogram Plot ##

        # Simply use .hist() function:
        if(choice == 1):

            plt.figure(1)
            dFrame['Col1'].hist(bins = 50)
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title('Histogram Plot 1')
            plt.annotate("Code:\ndFrame['Col1'].hist(bins = 50)\n"
                      "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
            plt.show()

            # Another way:
            plt.figure(2)
            dFrame['Col1'].plot.hist(bins = 30)
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title('Histogram Plot 2')
            plt.annotate("Code:\ndFrame['Col1'].plot.hist(bins = 30)\n"
                         "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
            plt.show()

        # ----------------------------------
        ## 2. Density % KDE Plot ##
        elif(choice == 2):
            plt.figure(1)
            dFrame['Col1'].plot.density()
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title("Density Plot")
            plt.annotate("Code:\ndFrame['Col1'].plot.density()\n"
                         "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
            plt.show()

            # Similar to the density plot, .kde() function also plots the Kernel Density Estimation of the data
            plt.figure(2)
            dFrame['Col1'].plot.kde()
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title("KDE Plot")
            plt.annotate("Code:\ndFrame['Col1'].plot.kde()\n"
                         "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
            plt.show()

        # ----------------------------------
        ## 3. Bar Plot ##
        elif(choice == 3):
            dict = {'Col1': [1, 1, 2, 3, 3, 2, 5, 2], 'Col2': [4, 2, 3, 3, 5, 5, 5, 5], 'Col3': [1, 4, 2, 4, 5, 1, 5, 1]}
            dFrame2 = pnd.DataFrame(dict)

            inp2 = input('Please select the type of bar plot you want:\n'
                         '1. Stacked Bar Plot\n'
                         '2. Unstacked Bar Plot\n\n'
                         'Your choice is: ')

            if(int(inp2) == 1 & inp2.isdigit()):
                # Stacked bar plot:
                dFrame2.plot.bar(stacked=True)
                plt.xlabel('x label')
                plt.ylabel('y label')
                plt.title("Stacked Bar Plot")
                plt.annotate("Code:\ndFrame2.plot.bar(stacked=True)\n"
                             "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
                plt.show()
            elif(int(inp2) == 2 & inp2.isdigit()):
                # Unstacked Bar Plot:
                dFrame2.plot.bar()
                plt.xlabel('x label')
                plt.ylabel('y label')
                plt.title("Unstacked Bar Plot")
                plt.annotate("Code:\ndFrame2.plot.bar()\n"
                             "plt.show()", xy=(0.55, 0.85), xycoords='axes fraction')
                plt.show()
            else:
                print('Not a proper choice! Please enter either 1 or 2 next time!')

        ## 4. Scatter Plot ##
        elif(choice == 4):
            dFrame.plot.scatter(x = 'Col1', y = 'Col2')
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title("Scatter Plot")
            plt.annotate("Code:\ndFrame.plot.scatter(x = 'Col1', y = 'Col2')\n"
                         "plt.show()", xy=(0.2, 0.85), xycoords='axes fraction')
            plt.show()

        ## Hexagonal Bin Plot ##
        # Alternative to scatter plot
        elif(choice == 5):
            dFrame.plot.hexbin(x = 'Col1', y = 'Col2', gridsize = 20)
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title("Hexagonal Bin Plot")
            plt.annotate("Code:\ndFrame.plot.hexbin(x = 'Col1', y = 'Col2', gridsize = 20)\n"
                         "plt.show()", xy=(0.02, 0.85), xycoords='axes fraction')
            plt.show()

        ## Box Plot ##
        elif(choice == 6):
            dFrame.plot.box()
            plt.xlabel('x label')
            plt.ylabel('y label')
            plt.title("Box Plot")
            plt.annotate("Code:\ndFrame.plot.box()\n"
                         "plt.show()", xy=(0.4, 0.85), xycoords='axes fraction')
            plt.show()

        # Exit #
        elif(choice == 7):
            quit()

        else:
            print("Please enter numbers between 1 and 7!\n")
    else:
        print("Please enter numbers between 1 and 7!\n")