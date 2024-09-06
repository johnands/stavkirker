import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


coordinates = {
    'Borgund stavkyrkje': (61.04715933142078, 7.812321962964252),
    'Eidsborg stavkyrkje': (59.46451727731189, 8.021935878274515),
    'Flesberg stavkirke': (59.86270449488184, 9.433067753611448),
    'Garmo stavkirke': (61.110937418854, 10.476350850583394),
    'Gol stavkirke': (59.90804314388714, 10.683353246855239),
    'Grip stavkirke': (63.2195386932188, 7.594048907744124),
    'Haltdalen stavkirke': (63.41789917942572, 10.355155561701164),
    'Hedalen stavkirke': (60.62243155972522, 9.690620455442733),
    'Heddal stavkyrkje': (59.57953736585766, 9.17626953887943),
    'Hegge stavkyrkje': (61.157716471317656, 9.023703236470594),
    'Hopperstad stavkyrkje': (61.07734874987817, 6.569010564075943),
    'Høre stavkyrkje': (61.15317845188762, 8.804809458556502),
    'Høyjord stavkirke': (59.36739320785945, 10.121105154306221),
    'Kaupanger stavkyrkje': (61.184172493226924, 7.233505821739648),
    'Kvernes stavkirke': (63.005451367413244, 7.721921513845581),
    'Lom stavkirke': (61.83976583648452, 8.566119194765072),
    'Lomen stavkyrkje': (61.13488927085116, 8.92389171745136),
    'Nore stavkirke': (60.16454621602835, 9.010355107596979),
    'Reinli stavkyrkje': (60.831407110672664, 9.49293989229013),
    'Ringebu stavkyrkje': (61.50930135097357, 10.172999640778269),
    'Rollag stavkirke': (60.02104059482222, 9.273212993474852),
    'Rødven stavkirke': (62.624189043149485, 7.493731328549946),
    'Røldal stavkyrkje': (59.830876657207014, 6.82267972292684),
    'Torpo stavkirke': (60.66386882686243, 8.708423641371034),
    'Undredal stavkyrkje': (60.95087591902275, 7.102278251189946),
    'Urnes stavkyrkje': (61.298247040390336, 7.322847410087165),
    'Uvdal stavkirke': (60.26510937381883, 8.834718984910587),
    'Øye stavkyrkje': (61.16793848647334, 8.400063334620398),
}

config = [
    {'name': 'Borgund stavkyrkje', 'lat': 61.04715933142078, 'lon': 7.812321962964252, 'link': '<a href="https://stavkirke.info/stavkirker/borgund/" target="_blank">https://stavkirke.info/stavkirker/borgund/</a>'},
    {'name': 'Eidsborg stavkyrkje', 'lat': 59.46451727731189, 'lon': 8.021935878274515},
    {'name': 'Flesberg stavkirke', 'lat': 59.86270449488184, 'lon': 9.433067753611448},
    {'name': 'Garmo stavkirke', 'lat': 61.110937418854, 'lon': 10.476350850583394},
    {'name': 'Gol stavkirke', 'lat': 59.90804314388714, 'lon': 10.683353246855239},
    {'name': 'Grip stavkirke', 'lat': 63.2195386932188, 'lon': 7.594048907744124},
    {'name': 'Haltdalen stavkirke', 'lat': 63.41789917942572, 'lon': 10.355155561701164},
    {'name': 'Hedalen stavkirke', 'lat': 60.62243155972522, 'lon': 9.690620455442733},
    {'name': 'Heddal stavkyrkje', 'lat': 59.57953736585766, 'lon': 9.17626953887943},
    {'name': 'Hegge stavkyrkje', 'lat': 61.157716471317656, 'lon': 9.023703236470594},
    {'name': 'Hopperstad stavkyrkje', 'lat': 61.07734874987817, 'lon': 6.569010564075943},
    {'name': 'Høre stavkyrkje', 'lat': 61.15317845188762, 'lon': 8.804809458556502},
    {'name': 'Høyjord stavkirke', 'lat': 59.36739320785945, 'lon': 10.121105154306221},
    {'name': 'Kaupanger stavkyrkje', 'lat': 61.184172493226924, 'lon': 7.233505821739648},
    {'name': 'Kvernes stavkirke', 'lat': 63.005451367413244, 'lon': 7.721921513845581},
    {'name': 'Lom stavkirke', 'lat': 61.83976583648452, 'lon': 8.566119194765072},
    {'name': 'Lomen stavkyrkje', 'lat': 61.13488927085116, 'lon': 8.92389171745136},
    {'name': 'Nore stavkirke', 'lat': 60.16454621602835, 'lon': 9.010355107596979},
    {'name': 'Reinli stavkyrkje', 'lat': 60.831407110672664, 'lon': 9.49293989229013},
    {'name': 'Ringebu stavkyrkje', 'lat': 61.50930135097357, 'lon': 10.172999640778269},
    {'name': 'Rollag stavkirke', 'lat': 60.02104059482222, 'lon': 9.273212993474852},
    {'name': 'Rødven stavkirke', 'lat': 62.624189043149485, 'lon': 7.493731328549946},
    {'name': 'Røldal stavkyrkje', 'lat': 59.830876657207014, 'lon': 6.82267972292684},
    {'name': 'Torpo stavkirke', 'lat': 60.66386882686243, 'lon': 8.708423641371034},
    {'name': 'Undredal stavkyrkje', 'lat': 60.95087591902275, 'lon': 7.102278251189946},
    {'name': 'Urnes stavkyrkje', 'lat': 61.298247040390336, 'lon': 7.322847410087165},
    {'name': 'Uvdal stavkirke', 'lat': 60.26510937381883, 'lon': 8.834718984910587},
    {'name': 'Øye stavkyrkje', 'lat': 61.16793848647334, 'lon': 8.400063334620398},
]

def main():
    st.title('Stavkirker i Norge')

    px.set_mapbox_access_token("pk.eyJ1Ijoiam9obmFuZHMiLCJhIjoiY2tsam5xOTYzMDZtbzJwcDI1d3ljOTgxeSJ9.eKgAQ_grxIxFxqEQT5zFKQ")

    #coords_df = pd.DataFrame.from_records(list(coordinates.values()), index=list(coordinates.keys()), columns=['lat', 'lon'])
    #coords_df = pd.DataFrame.from_dict(coordinates, orient='index', columns=['lat', 'lon'])
    data = pd.DataFrame().from_records(config)
    #coords_df = coords_df.reset_index().rename(columns={'index': 'name'})
    print(data)

    #st.map(coords_df)
    
    fig = px.scatter_mapbox(data, lat='lat', lon='lon', hover_name='name', zoom=3, mapbox_style='satellite', width=800, height=800, color_discrete_sequence=['red'], hover_data={"link": True})
    st.plotly_chart(fig)

    # df = pd.DataFrame(
    # np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    # columns=["lat", "lon"],
    # )
    # print(df)
    # st.map(df)


if __name__ == '__main__':
    main()