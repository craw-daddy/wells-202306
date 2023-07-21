import streamlit as st

from database import query_db
from plot import plot_wells

def app():
    st.title("Wells Application")
    st.markdown('Welcome to my application.  Please enjoy your stay!')
    st.markdown('Input the **minimum well depth** and **minimum temperature gradient** in the boxes below.')

    depth = st.number_input('Min depth (m):', 0, 10000, value=5000, step=100)
    gradient = st.number_input('Min gradient (°C/m):', 0.0, 0.150, value=0.010, step=0.005)

    data = query_db(depth, gradient)

    #  Print a message if the query was too restrictive
    if len(data) == 0:
        st.write('Your query returned no results, please try again!')
    #  Otherwise let's plot the wells.  Here we are accounting for the fact that
    #  the input might be very large by writing the data to a file, and the
    #  plot_wells method is expecting to receive a filename as input.  
    else:
        filename = 'wells_data.json'
        data.to_json(filename, orient='records')
        st.write(plot_wells(filename))

if __name__ == '__main__':
    app()

