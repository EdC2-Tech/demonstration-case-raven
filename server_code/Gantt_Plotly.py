import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.express as px

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def plotly_test():
  data = px.data.iris()
  fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species", trendline="ols")
  return fig

@anvil.server.callable
def plotly_version1():
    start = {"name": "start", "begin": 1, "end": 3}
    a     = {"name": "a", "begin": 3, "end": 4}
    b     = {"name": "b", "begin": 3, "end": 5}
    c     = {"name": "c", "begin": 5, "end": 6}
    d     = {"name": "d", "begin": 6, "end": 7}
    e     = {"name": "e", "begin": 7, "end": 8}
    f     = {"name": "f", "begin": 7, "end": 8}
    g     = {"name": "g", "begin": 6, "end": 8}
    h     = {"name": "h", "begin": 8, "end": 9}
    end   = {"name": "end", "begin": 9, "end": 11}

    all_L = (start, a, b, c, d, e, f, g, h, end)

    activity_L = list()
    begin_L    = list()
    end_L      = list()

    for i in all_L:
        activity_L.append(i["name"])
        begin_L.append(i["begin"])   
        end_L.append(i["end"])     

    graph = {"start": [a, d, f],
             "a": [b],
             "b": [c],
             "c": [g,h],
             "d": [e],
             "e": [c],
             "f": [c],
             "g": [end],
             "h": [end],
             "end": [],
    }

    fig = px.timeline(all_L, x_start=begin_L, x_end=end_L, y=activity_L, title="Plotly Gantt Version 1")
    #fig.update_yaxes(autorange='reversed')

    return fig