# Spatial_databases
Create (generate/sample) some data, visualize it, do queries on it, and visualize the query results.

1. I have collected latitude,longitude pairs (ie. spatial coordinates) for 15 locations, in the University of Southern California campus (UPC). I have collected them under 3 categories(5 each) - Prks, Cafes, Libraries

2. Now that I have 15 coordinates and their labels and categories, I am going to create a KML file (.kml format, which is XML) . Specifically, each location will be a 'placemark' in your .kml file (with a label, and coords), under three groups/categories. The KML file is <a href="https://github.com/Niranjani29/Spatial_databases/blob/master/Q5_merged.kml"> here </a>

3. I have visualized it as follows :

<img src='https://github.com/Niranjani29/Spatial_databases/blob/master/Q3.png'>


4. a. I have computde the convex hull for your 15 points [a convex hull for a set of 2D points is the smallest convex polygon that contains the point set]. I have Postgres for computing the query. The query used is <a href="https://github.com/Niranjani29/Spatial_databases/blob/master/README.txt"> here </a>

Visualization using Google Earth is as follows : 
<img src='https://github.com/Niranjani29/Spatial_databases/blob/master/Q5_convexhull.png'>



b. I have computed  the four nearest neighbors of one of your 15 locations [look up the spatial function of your DB, to do this]. Use the query's results, to create four line segments in your .kml file: line(loc,neighbor1), line(loc,neighbor2), line(loc,neighbor3), line(loc,neighbor4). The query used is <a href="https://github.com/Niranjani29/Spatial_databases/blob/master/README.txt"> here </a>


 Visualization using Google Earth is as follows : 
<img src='https://github.com/Niranjani29/Spatial_databases/blob/master/Q5_knn.png'>

5. Use OpenLayers (a JavaScript API) to visualize your location data. The idea is to store your 15 sampled points, via your web browser, in a browser cache area in your local machine, where the data would persist [even after you close the browser]; then you'd read back the stored values, and visualize them, using the OpenLayers API. To store and load points, you'll use 'HTML5 localStorage', which is a key-value based standard WWW API for storing data locally on your device.

I have used JSFiddle.net
Link to my project is The query used is <a href="http://jsfiddle.net/Niranjani29/rv6ws0j1/5/"> here </a>
