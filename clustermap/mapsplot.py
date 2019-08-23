import gmplot
import pandas as pd


def mapping():
    df = pd.read_csv('out.csv')

    #declare the center of the map, and how much we want the map zoomed in

    gmap3 = gmplot.GoogleMapPlotter(1.2815683, 103.8636132, 13)

    # Scatter map

    gmap3.scatter(df['Latitude'], df['Longitude'], '#FF0000', size = 50, marker = False )

    # Plot method Draw a line in between given coordinates

    gmap3.plot(df['Latitude'], df['Longitude'], 'cornflowerblue', edge_width = 3.0)

    gmap3.apikey = "AIzaSyDtqmXTsWo0KPlcVXr-T67sPftH3mrkSPU"

    # Draw
    s = gmap3.draw("my_map.html")
    return s
