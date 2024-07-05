from dash import dcc, html

def create_layout(df):
    """Creates the layout of the app."""
    return html.Div([
        html.H1("Data Analysis Tool"),
        dcc.Dropdown(
            id='column-selector',
            options=[{'label': col, 'value': col} for col in df.columns],
            placeholder="Select a column to plot"
        ),
        dcc.RadioItems(
            id='preprocess-selector',
            options=[
                {'label': 'Original Data', 'value': 'original'},
                {'label': 'Month-over-Month Growth Rate', 'value': 'mom'},
                {'label': 'Year-over-Year Growth Rate', 'value': 'yoy'}
            ],
            value='original',
            labelStyle={'display': 'inline-block'}
        ),
        html.Label('Select Index Range:'),
        dcc.Dropdown(id='start-index', placeholder='Start index'),
        dcc.Dropdown(id='end-index', placeholder='End index'),
        dcc.Graph(id='data-plot')
    ])
