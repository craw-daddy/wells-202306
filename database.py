import os
import pandas as pd

from sqlalchemy import create_engine, text

WELLS_URL = os.getenv('WELLS_URL')

def query_db(min_depth, min_gradient):
    """Returns wells that fit the search criteria as a pandas DataFrame."""

    engine = create_engine(WELLS_URL)
    
    query = text(
            """
            SELECT latitude, longitude, depth, gradient
            FROM wells
            WHERE depth > :min_depth AND gradient > :min_gradient
            """
            )
    with engine.connect() as conn:
        results = (
                conn
                .execute(query, {'min_depth': min_depth, 'min_gradient': min_gradient})
                .fetchall()
                )

    columns = ['latitude', 'longitude', 'depth', 'gradient']
    results = pd.DataFrame(results, columns=columns)

    return results

if __name__ == '__main__':
    import sys

    min_depth = float(sys.argv[1])
    min_gradient = float(sys.argv[2])

    print(query_db(min_depth, min_gradient))

