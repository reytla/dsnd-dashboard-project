# Import any dependencies needed to execute sql queries
from sqlite3 import connect
from pathlib import Path
from .sql_execution import QueryMixin


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
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):
        
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column

        # Import pandas to handle dataframes
        import pandas as pd
        # Connect to the database using the QueryMixin's connect method
        conn = self.connect()
        # Create a cursor to execute SQL queries
        cursor = conn.cursor()
        # Define the SQL query to count events
        query = f"""
        SELECT event_date,
               SUM(CASE WHEN event_type = 'positive' THEN 1 ELSE 0 END) AS positive_count,
               SUM(CASE WHEN event_type = 'negative' THEN 1 ELSE 0 END) AS negative_count
        FROM {self.name}
        WHERE id = ?    
        GROUP BY event_date
        ORDER BY event_date;
        """
        # Execute the query with the provided id
        cursor.execute(query, (id,))
        # Fetch all results from the executed query
        results = cursor.fetchall()
        # Create a pandas DataFrame from the results
        df = pd.DataFrame(results, columns=['event_date', 'positive_count', 'negative_count'])
        # Close the cursor and connection
        cursor.close()
        conn.close()
        # Return the DataFrame containing event counts
        return df
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

