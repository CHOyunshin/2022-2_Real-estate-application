from mapboxgl.viz import *
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops

# 읽을 geo 데이터 선택
geo_data = 'layout/mapboxgl/older_seoul.geojson'
# mapbox 토큰 설정 부분 
token = 'pk.eyJ1IjoieXVuc2hpbmNobyIsImEiOiJjbGJxNWMyaXQwZmJ5M3FyN3drYjlsenQwIn0.EhOKGEak-6G4vqj--BxC5w'



# 파일을 파이썬에서 읽습니다.
import json
with open(geo_data) as f:
    data = json.loads(f.read())

def make_viz():
    # 읽을 geo 데이터 선택
    geo_data = 'layout/mapboxgl/older_seoul.geojson'
    with open(geo_data) as f:
        data = json.loads(f.read())
    # mapbox 토큰 설정 부분 
    token = 'pk.eyJ1IjoieXVuc2hpbmNobyIsImEiOiJjbGJxNWMyaXQwZmJ5M3FyN3drYjlsenQwIn0.EhOKGEak-6G4vqj--BxC5w'


    # 서울시 중심부의 경도, 위도 입니다. 
    center = [126.986, 37.565]

    # 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
    color_breaks = [0, 10000, 20000, 30000, 40000, 50000]
    color_stops = create_color_stops(color_breaks, colors='BuPu')
    # color_stops 에는 다음과 같은 값이 들어갑니다.
    # color_stops = [
    #     [0, 'rgb(237,248,251)'],
    #     [10000, 'rgb(191,211,230)'],
    #     [20000, 'rgb(158,188,218)'],
    #     [30000, 'rgb(140,150,198)'],
    #     [40000, 'rgb(136,86,167)'],
    #     [50000, 'rgb(129,15,124)']
    # ]

    # ChoroplethViz 를 그립니다.
    viz = ChoroplethViz(
        access_token=token,
        data=data,
        color_property='인구',
        color_stops=color_stops,
        center=center,
        zoom=10)


    # 맵을 -15도 만큼 좌우 회전하고, 45도 만큼 상하 회전합니다.
    viz.bearing = -15
    viz.pitch = 45

    # 각 데이터에 '인구'를 기준으로 height 값을 줍니다.
    viz.height_property = '인구'

    # 높이의 값을 '인구' 에 따라 0 ~ 50000 사이의 값을 0 ~ 3000 사이의 값으로 매핑합니다.
    numeric_stops = create_numeric_stops([0, 10000, 20000, 30000, 40000, 50000], 0, 3000)
    # numeric_stops 에는 다음과 같은 값이 들어갑니다.
    # numeric_stops = [
    #     [0, 0.0],
    #     [10000, 500.0],
    #     [20000, 1000.0],
    #     [30000, 1500.0],
    #     [40000, 2000.0],
    #     [50000, 2500.0]
    # ]

    viz.height_stops = numeric_stops
    viz.height_function_type = 'interpolate'
    
    return viz



# render again
# viz.show()

html = open("layout/mapboxgl/output/viz_3d.html", "w", encoding="UTF-8")
html.write(viz.create_html())
html.close()