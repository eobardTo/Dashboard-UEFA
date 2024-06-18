from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import load_data

df = load_data()

def layout(df):
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.Div([
                html.H1("Обзорная карта победителей и финалистов"),
                html.Hr(),
                html.P("Карта отображает страны, которые выигрывали и были финалистами Лиги чемпионов УЕФА.")
            ]))
        ]),
        dbc.Row([
            dcc.Graph(id='map-view')
        ]),
        dbc.Row([
            dcc.Graph(id='tournament-count-chart')
        ])
    ])

@callback(
    Output('map-view', 'figure'),
    Input('url', 'pathname')
)
def update_map(pathname):
    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", hover_name="Season",
                         size="Attendance", projection="natural earth",
                         title="Места проведения и команды-победители",
                         color="Winners", symbol="Venue",
                         size_max=10) 

    fig.update_layout(
        xaxis_title="Широта",
        yaxis_title="Долгота"
    )

    return fig

@callback(
    Output('tournament-count-chart', 'figure'),
    Input('url', 'pathname')
)
def update_tournament_count_chart(pathname):
    tournament_count = df['Country'].value_counts().reset_index()
    tournament_count.columns = ['Country', 'Tournament_Count']
    tournament_count = tournament_count.sort_values(by='Tournament_Count', ascending=True)
    fig = px.bar(tournament_count, x='Tournament_Count', y='Country', orientation='h',
                 title='Количество турниров, проведенных в каждой стране')
    
    fig.update_layout(
        xaxis_title="Количество турниров",
        yaxis_title="Страна"
    )

    return fig
