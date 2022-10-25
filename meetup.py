import streamlit as st
from geopy import Nominatim, distance
import pandas as pd

locator = Nominatim(user_agent = 'myGeocoder')
def get_locations(locations):
    locations = locations.split(';')

    lats = []
    lons = []
    for location in locations:
        loc = locator.geocode(location)
        lats.append(loc.latitude)
        lons.append(loc.longitude)

    L = {'lat': lats, 'lon': lons}
    return pd.DataFrame(L)

def find_min(L):
    meet = L.mean() # Initial Location (guess)

    dist = []
    for i in range(len(L)):
        dist.append(distance.distance(meet, L.iloc[i]).kilometers)

    st.write(sum(dist))
    return meet

st.title('Where to meet?')
st.write('Find the perfect place to meet')

locations = st.text_input('Add Locations (Seperated by Semicolon)', value = 'Multivac Wolfertschwenden')
L = get_locations(locations)

meet = find_min(L)
L = L.append(meet, ignore_index = True)

st.write(meet)
st.map(data = L)