import dash
from dash.dependencies import Input, Output
from layout import create_layout
from src.data_loader import load_data
import callbacks

# Load the data
df = load_data(r"C:\Users\beerp\Data\NIPE\public_data_april.xlsx")

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the layout of the app
app.layout = create_layout(df)

# Register callbacks
callbacks.register_callbacks(app, df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
