from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd


# reading the data into pandas
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


# instantiate dash app
app = Dash()


# it will also take colors as words like 'red'
app.layout = [
    html.H1(children='Title of Dash App',
            style={'textAlign':'center',
                   'background-color':'#84d8d8'}),
    dcc.Dropdown(df.country.unique(),
                #  if we don't give it a default start value it will have the 'Select..'
                 'Canada',
                 id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)