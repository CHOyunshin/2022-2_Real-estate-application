import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table
import json
import pandas as pd
import base64


'''
    페이지 1번 contents : 
'''
def page01_dash_html_layout():
    image_filename = '/Users/yscho/github-desktop/2022-2_Realestate_project/application_by_DASH/2022-2_Real-estate-application/layout/Result1.png'
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    # ...
    return html.Div(id='my_id', 
        className='my_class',
        children=[
            html.H1(children='Hello Dash'),
            html.Div(children='''Dash: A web application framework for Python.'''),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {'title': 'Dash Data Visualization'}
                }
            ),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image)),
        ])


'''
    페이지 2번 간단한 choropleth_mapbox
'''
def page02_dash_html_layout():
    with open('data/geojson/seoul_HangJeongDong.geojson', 'r') as f:
        seoul_geo = json.load(f)

    seoul_info = pd.read_csv('/Users/yscho/github-desktop/2022-2_Realestate_project/application_by_DASH/2022-2_Real-estate-application/layout/mapboxgl/sample.txt', delimiter='\t')
    seoul_info = seoul_info.iloc[3:,:]
    seoul_info = seoul_info[seoul_info['동']!='소계']
    seoul_info['full_name'] = '서울특별시'+' '+seoul_info['자치구']+' '+seoul_info['동']
    seoul_info['full_name'] = seoul_info['full_name'].apply(lambda x: x.replace('.','·'))
    seoul_info['인구'] = seoul_info['인구'].apply(lambda x: int(''.join(x.split(','))))

    fig = px.choropleth_mapbox(seoul_info,
                           geojson=seoul_geo,
                           locations='full_name',
                           color='인구',
                           color_continuous_scale='viridis',
                           featureidkey = 'properties.adm_nm',
                           mapbox_style='carto-positron',
                           zoom=9.5,
                           center = {"lat": 37.563383, "lon": 126.996039},
                           opacity=0.5,
                          )
    return fig

# make dash plotly 