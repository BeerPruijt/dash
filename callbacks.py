from dash.dependencies import Input, Output
from src.callback_helpers import get_valid_indices, get_disabled_indices
from src.data_preprocessing import preprocess_data
import pandas as pd
import plotly.express as px

def register_callbacks(app, df):
    """Registers the callbacks with the app."""
    
    @app.callback(
        [Output('start-index', 'options'),
         Output('start-index', 'value'),
         Output('end-index', 'options'),
         Output('end-index', 'value')],
        [Input('column-selector', 'value'),
         Input('start-index', 'value'),
         Input('end-index', 'value')]
    )
    def update_indexes(selected_column, selected_start_index, selected_end_index):
        if selected_column is None:
            return [], None, [], None

        clean_df = df[selected_column].dropna()
        valid_idxs = get_valid_indices(clean_df)

        start_value = valid_idxs[0]['value'] if selected_start_index is None and valid_idxs else selected_start_index
        end_value = valid_idxs[-1]['value'] if selected_end_index is None and valid_idxs else selected_end_index

        end_options = get_disabled_indices(clean_df, pd.to_datetime(selected_start_index) if selected_start_index else None, 
                                           lambda i, comparator: comparator is not None and i <= comparator)
        start_options = get_disabled_indices(clean_df, pd.to_datetime(selected_end_index) if selected_end_index else None, 
                                             lambda i, comparator: comparator is not None and i >= comparator)

        return start_options, start_value, end_options, end_value

    @app.callback(
        Output('data-plot', 'figure'),
        [Input('column-selector', 'value'),
         Input('preprocess-selector', 'value'),
         Input('start-index', 'value'),
         Input('end-index', 'value')]
    )
    def update_graph(selected_column, preprocess_type, start_index, end_index):
        if selected_column is None:
            return {}

        df_copy = preprocess_data(df, selected_column, preprocess_type)
        
        if start_index is not None and end_index is not None:
            df_copy = df_copy.loc[start_index:end_index]
        
        fig = px.line(df_copy, x=df_copy.index, y=selected_column, title=f'{preprocess_type.upper()} for {selected_column}')
        return fig
