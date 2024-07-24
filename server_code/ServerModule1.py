import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email
import anvil.server
from datetime import datetime

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
def delete_resource(resource):
  resource.delete()

@anvil.server.callable
def get_resource():
  return [(row["resource_value"]) for row in app_tables.resource.search()]
  
@anvil.server.callable
def get_dependency():
  return app_tables.dependency.search()

@anvil.server.callable
def add_dependency(dependency_value, dependency_description, resource):
  app_tables.dependency.add_row(dependency_value=dependency_value,
                                dependency_description=dependency_description,
                                resource=resource
                               )
  
@anvil.server.callable
def edit_dependency(dependency_value):
  app_tables.dependency.update(dependency_value=dependency_value)
  