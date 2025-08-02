# Import any dependencies needed to execute sql queries
# from sqlite3 import connect
# from pathlib import Path
from .sql_execution import QueryMixin
import pandas as pd


# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):
    """Base class for querying the employee_events database.
    This class provides methods to query employee events,
    event counts, and notes associated with events.
    """

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = "" # e.g. "employee_events"

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):
        # Use correct id column based on class attribute
        id_col = "employee_id" if self.name == "employee" else "team_id"
        query = f"""
        SELECT event_date,
               SUM(positive_events) AS positive_count,
               SUM(negative_events) AS negative_count
        FROM employee_events
        WHERE {id_col} = {id}
        GROUP BY event_date
        ORDER BY event_date;
        """
        return self.pandas_query(query)
            
    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

    def notes(self, id):
        # Determine join and filter columns based on the class attribute
        join_col = "employee_id" if self.name == "employee" else "team_id"
        query = f"""
        SELECT n.note_date, n.note
        FROM notes n
        JOIN {self.name} e ON n.{join_col} = e.{join_col}
        WHERE n.{join_col} = {id}
        ORDER BY n.note_date;
        """
        return self.pandas_query(query)
