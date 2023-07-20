import altair as alt
import pandas as pd

from vega_datasets import data

def plot_wells(well_coords):
    #  Create the US map
    states = alt.topo_feature(data.us_10m.url, feature='states')
    USmap = (alt.Chart(states)
             .mark_geoshape(fill='lightgray', stroke='white')
             .project('albersUsa')
             .properties(width=600, height=400)
            )

    #  Add the wells information to map
    columns = ['latitude', 'longitude', 'depth', 'gradient']
    well_coords = pd.DataFrame(well_coords, columns=columns)
    well_coordinates = (alt.Chart(well_coords)
                        .mark_circle()
                        .encode(latitude='latitude',
                                longitude='longitude',
                                color=alt.Color('gradient', title='Gradient',
                                               scale=alt.Scale(scheme='inferno')),
                                tooltip=[alt.Tooltip('depth', title='Depth (m)'),
                                         alt.Tooltip('gradient', title='Gradient (°C/m)',
                                                    format='0.2f')])
                       )

    return USmap + well_coordinates

