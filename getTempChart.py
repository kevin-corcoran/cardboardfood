import pygal
import json
from datetime import datetime

# read data
with open('data.txt') as json_file:
    data = json.load(json_file)

    # convert desired data to python list
    xs = [datetime(t['year'],t['month'],t['day'],t['hour'],t['minute'],t['second']) for t in data['date']]
    ys = [temp['tempF'] for temp in data['temperature']]
    print(xs)
    print(ys)

    # create chart
    line_chart = pygal.Line()
    line_chart.title = 'Temperature'
    line_chart.x_labels = map(str, xs)
    line_chart.add('Temperature', ys)

    line_chart.render_to_file('temp_chart.svg')
