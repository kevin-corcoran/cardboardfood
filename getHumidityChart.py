import pygal
import json
from datetime import datetime

# read data
with open('data.txt') as json_file:
    data = json.load(json_file)

    # convert desired data to python list
    xs = [datetime(t['year'],t['month'],t['day'],t['hour'],t['minute'],t['second']) for t in data['date']]
    ys = [hum['humidity'] for hum in data['humidity']]
    print(xs)
    print(ys)

    # create chart
    line_chart = pygal.Line()
    line_chart.title = 'Humidity'
    line_chart.x_labels = map(str, xs)
    line_chart.add('humidity', ys)

    line_chart.render_to_file('humidity_chart.svg')
