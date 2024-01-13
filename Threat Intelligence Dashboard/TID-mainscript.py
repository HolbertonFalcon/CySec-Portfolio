import requests
import pandas as pd
import json
from I.display import display, HTML

class Dashboard(object):
    def __init__(self, data):
        """
        Initialize the Dashboard class with the data to be displayed.

        :param data: Pandas DataFrame containing the data to be displayed
        """
        self.data = data

    def generate_html(self):
        """
        Generate the HTML table for the dashboard.

        :return: HTML string for the table
        """
        html = """
        <table border="1">
            <tr>
                <th>Time</th>
                <th>Threat Description</th>
                <th>Recommended Action</th>
                <th>Threat Level</th>
            </tr>
        """

        # Iterate through the DataFrame
        for index, row in self.data.iterrows():
            html += f"""
            <tr>
                <td>{index}</td>
                <td>{row['threat_description']}</td>
                <td>{row['recommended_action']}</td>
                <td>{row['threat_level']}</td>
            </tr>
            """

        html += "</table>"

        return html

    def display(self):
        """
        Display the dashboard using I's display function.
        """
        display(HTML(self.generate_html()))


def run_dashboard():
    """
    Run the dashboard by parsing the command line arguments and displaying the dashboard.
    """
    # Parse the command line arguments
    command_line = sys.argv[1:]
    processed_args = security_analytics.parse(command_line)

    # Call the run method
    df = security_analytics.run(command_line, processed_args)

    # Create the Dashboard object
    dashboard = Dashboard(df)

    # Display the dashboard
    dashboard.display()


if __name__ == "__main__":
    run_dashboard()