
import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
import dash_table
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit'),

    html.Div(
        dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
)
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            multi=True,
            value="MTL"
        ),

        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) for i in range(10)},
            value=5,
        ),

        dcc.RangeSlider(
            marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
            min=-5,
            max=6,
            value=[-3, 4]
        ),

        dcc.Input(
            placeholder='Enter a value...',
            type='text',
            value=''
        ),

        dcc.Textarea(
            placeholder='Enter a value...',
            value='This is a TextArea component',
            style={'width': '100%'}
        ),

        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            values=['MTL', 'SF'],
            labelStyle={'display': 'inline-block'}
        ),

        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL',
            labelStyle={'display': 'inline-block'}
        ),
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=dt(1997, 5, 3),
            end_date_placeholder_text='Select a date!'
        ),

    )
])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)