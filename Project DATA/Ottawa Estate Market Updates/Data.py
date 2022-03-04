from datetime import datetime
import csv
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import os

os.system("rm -rf *.*")

file_name = 'Ottawa Market Stats.csv'


with open(file_name) as file:
    reader = csv.reader(file)
    header = next(reader)
    Years = []
    Yearly_money = []
    for row in reader:
        time = int(row[0])
        average = int(row[1])
        Years.append(time)
        Yearly_money.append(average)

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()

my_config.x_label_rotation = 59
my_config.show_legend = False
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Ottawa Real-Estate Market Updates'
print(Years)
chart.x_labels = Years

chart.add('AVERAGE PRICE', Yearly_money)
chart.render_to_file('Ottawa Real Estate Graph.svg')