import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web  # requires v0.6.0 or later
from datetime import datetime

USERNAME_PASSWORD_PAIRS = [
    ['batman', 'brucewayne']
]

app = dash.Dash()
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server

nsdq = pd.read_csv('data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace=True)
options = []

for tic in nsdq.index:
    options.append({'label': '{} {}'.format(tic, nsdq.loc[tic]['Name']), 'value': tic})

app.layout = html.Div([
    html.H1('NASDAQ Stock Dashboard', style={'color': '#007eff', 'font': '400 22px Arial'}),
    html.Div({
        html.H3('Pick a NASDAQ stock symbol:',
                style={'paddingRight': '30px', 'color': '#007eff', 'font': '400 22px Arial'}),
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'],
            multi=True
        )
    }, style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '30%', 'font': '400 22px Arial'}),
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed=datetime(2015, 1, 1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2018, 1, 1),
            end_date=datetime.today()
        )
    ], style={'display': 'inline-block', 'color': '#007eff', 'font': '400 22px Arial'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize': 20, 'marginLeft': '30px', 'color': '#007eff', 'font': '400 Arial'},
        ),
    ], style={'display': 'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
            'data': [
                {'x': [1, 2], 'y': [3, 1]}
            ]
        }
    )
])


@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_ticker_symbol', 'value'),
     State('my_date_picker', 'start_date'),
     State('my_date_picker', 'end_date')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic, 'iex', start, end)
        traces.append({'x': df.index, 'y': df.close, 'name': tic})
    fig = {
        'data': traces,
        'layout': {'title': ', '.join(stock_ticker) + ' Closing Prices'}
    }
    return fig


if __name__ == '__main__':
    app.run_server()
