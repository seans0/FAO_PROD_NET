from collections import defaultdict
from pyvis.network import Network
import networkx as nx
import pandas as pd

fao_data=pd.read_csv("/Users/sean/Library/CloudStorage/OneDrive-DemeterPublishingLimited/Weekly content/Week 2 - The power of friendship/nodes_tester_norm.csv")

country = fao_data["Area"]
crop = fao_data["Item"]
edge_data = zip(country, crop)
data = list(edge_data)

grouped = defaultdict(list)

for country, item in data:
    grouped[country].append(item)


unique_tuple= {"Almonds, in shell", "Apples", "Apricots", "Grapes", "Olives", "Oranges", 
         "Pistachios, in shell", "Potatoes", "Rice", "Walnuts, in shell", "Wheat", 
         "Cherries", "Dates", "Strawberries", "Tomatoes", "Bananas", "Hazelnuts, in shell", 
         "Blueberries", "Raspberries"}


updated_data = []
for country, items in grouped.items():
    country_set = set(items)
    
    difference = tuple(unique_tuple - country_set)
    
    updated_data.append((country, difference))

result_data = [(country, item) for country, items in updated_data for item in items]
def map_data(item_data,country_colour="#03DAC6",crop_colour ="#da03b3"):
    fao_net_not = Network(height="750px", width="100%", bgcolor="#222222", font_color="white",select_menu=True,filter_menu=True)
    for e in result_data:
        src = e[0]
        dst = e[1]

        fao_net_not.add_node(src,color=country_colour,label=src,title=src,size=100,labelHighlightBold=True)
        fao_net_not.add_node(dst,color=crop_colour,title=dst,shape="triangle",size=200,mass=100,labelHighlightBold=True)
        fao_net_not.add_edge(src, dst)
    fao_net_not.show_buttons(filter_=["physics"])
    fao_net_not.barnes_hut()
    fao_net_not.show("not_prod.html")

map_data(item_data=result_data)

    