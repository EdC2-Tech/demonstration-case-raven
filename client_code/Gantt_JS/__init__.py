from ._anvil_designer import Gantt_JSTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import Foo

class Gantt_JS(Gantt_JSTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.image_1.item = None
    # Any code you write here will run before the form opens.
