import altair as alt
import pandas as pd

from vega_datasets import data

def plot_wells(well_file):
    """Assumes that the well_file input is a string that points to a local
       JSON file that has the information that Altair needs to map
       the wells.
    """
    #  Create the US map
    states = alt.topo_feature(data.us_10m.url, feature='states')
    USmap = (alt.Chart(states)
             .mark_geoshape(fill='lightgray', stroke='white')
             .project('albersUsa')
             .properties(width=600, height=400)
            )

    #  Add the wells information to map
    well_coordinates = (alt.Chart(well_file)
                        .mark_circle()
                        .encode(latitude='latitude:Q',
                                longitude='longitude:Q',
                                color=alt.Color('gradient:Q', title='Gradient',
                                               scale=alt.Scale(scheme='inferno')),
                                tooltip=[alt.Tooltip('depth:Q', title='Depth (m)'),
                                         alt.Tooltip('gradient:Q', title='Gradient (°C/m)',
                                                    format='0.2f')])
                       )

    return USmap + well_coordinates

