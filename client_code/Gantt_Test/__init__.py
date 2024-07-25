from ._anvil_designer import Gantt_TestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Gantt_Test(Gantt_TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.plot_1.figure = anvil.server.call('plotly_test')
    
  # Any code you write here will run before the form opens.
  

    
    