import geopandas as gpd
import autoESDA_report

mygdf = gpd.read_file(r'example-data\rsa-census-jhb-wards\COJ_Descriptive.shp')
autoESDA_report.autoESDA_report(mygdf)