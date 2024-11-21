from pyvis.network import Network
import networkx as nx
import pandas as pd

fao_data=pd.read_csv("nodes_tester_norm.csv")

country = fao_data["Area"]
crop = fao_data["Item"]
value = fao_data["Value_norm"]
edge_data = zip(country, crop, value)
def map_data(item_data,country_colour="#03DAC6",crop_colour ="#da03b3"):
    fao_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white",select_menu=True,filter_menu=True)
    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]

        fao_net.add_node(src,color=country_colour,title=src,size=100,labelHighlightBold=True)
        fao_net.add_node(dst,color=crop_colour,title=dst,shape="triangle",size=200,mass=100,labelHighlightBold=True)
        fao_net.add_edge(src, dst,width=w)
    fao_net.show_buttons(filter_=["physics"])
    fao_net.barnes_hut()
    fao_net.show("tester.html")

map_data(item_data=fao_data)
