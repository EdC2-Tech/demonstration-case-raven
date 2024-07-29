from ._anvil_designer import Gantt_JSTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import google

import gviz_api

class Gantt_JS(Gantt_JSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    google.charts.load('current')
    google.charts.setOnLoadCallback(self.drawChart())
    

  def drawChart(self):
    page_template = """
      <html>
        <head>
          <!--Load the AJAX API-->
          <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
          <script type="text/javascript">
      
            // Load the Visualization API and the corechart package.
            google.charts.load('current', {'packages':['corechart']});
      
            // Set a callback to run when the Google Visualization API is loaded.
            google.charts.setOnLoadCallback(drawChart);
      
            // Callback that creates and populates a data table,
            // instantiates the pie chart, passes in the data and
            // draws it.
            function drawChart() {
      
              // Create the data table.
              var data = new google.visualization.DataTable();
              data.addColumn('string', 'Topping');
              data.addColumn('number', 'Slices');
              data.addRows([
                ['Mushrooms', 3],
                ['Onions', 1],
                ['Olives', 1],
                ['Zucchini', 1],
                ['Pepperoni', 2]
              ]);
      
              // Set chart options
              var options = {'title':'How Much Pizza I Ate Last Night',
                            'width':400,
                            'height':300};
      
              // Instantiate and draw our chart, passing in some options.
              var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
              chart.draw(data, options);
            }
          </script>
        </head>
      
        <body>
          <!--Div that will hold the pie chart-->
          <div id="chart_div"></div>
        </body>
      </html>
    """
    # Creating the data
    description = {"name": ("string", "Name"),
                  "salary": ("number", "Salary"),
                  "full_time": ("boolean", "Full Time Employee")}
    data = [{"name": "Mike", "salary": (10000, "$10,000"), "full_time": True},
            {"name": "Jim", "salary": (800, "$800"), "full_time": False},
            {"name": "Alice", "salary": (12500, "$12,500"), "full_time": True},
            {"name": "Bob", "salary": (7000, "$7,000"), "full_time": True}]
  
    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)
    # Any code you write here will run before the form opens.


