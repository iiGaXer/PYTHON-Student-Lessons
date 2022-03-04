from datetime import datetime
import csv
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from datetime import datetime, timedelta
import os

os.system("rm -rf *.*")

file_name = 'COVID-19 Canada DATA.csv'

with open(file_name) as file:
    reader = csv.reader(file)
    header = next(reader)
    Years = []
    Tests_completed = []
    Tests_daily = []
    
    for row in reader:
        time = row[0]
        Case = int(row[1])
        Tests = int(row[2])
        Years.append(time)
        Tests_completed.append(Case)
        Tests_daily.append(Tests)

# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()

my_config.x_label_rotation = 59
my_config.show_legend = False
my_style.title_font_size = 29
my_style.label_font_size = 20
my_style.major_label_font_size = 28
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1500

chart = pygal.Line(my_config, style=my_style)
chart.title = 'COVID-19 Tests done in Canda, AB'
print(Years)

chart.add('COVID-19: Daily Tests', Tests_daily)
chart.render_to_file('COVID-19 Daily Tests AB Graph.svg')

