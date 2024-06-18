from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import load_data

df = load_data()

# Функция для добавления столбца десятилетий
def add_decade_column(df):
    df['Year'] = df['Season'].str.extract(r'(\d{4})').astype(int)
    df['Decade'] = (df['Year'] // 10 * 10).astype(str) + 's'
    return df

df = add_decade_column(df)

def layout(df):
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.Div([
                html.H1("Статистика по сезонам"),
                html.Hr(),
                html.P("Распределение посещаемости по сезонам Лиги чемпионов УЕФА.")
            ]))
        ]),
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='team-dropdown',
                options=[{'label': team, 'value': team} for team in df['Winners'].unique()],
                value=df['Winners'].unique()[0]
            ), width=4)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='team-bar-chart'), width=12)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='season-pie-charts'), width=12, style={'display': 'flex', 'justify-content': 'center'})
        ])
    ])

@callback(
    Output('season-pie-charts', 'figure'),
    Input('url', 'pathname')
)
def update_season_pie_charts(pathname):
    df_grouped = df.groupby('Decade')['Attendance'].sum().reset_index()
    fig = px.pie(df_grouped, names='Decade', values='Attendance', title="Распределение посещаемости по десятилетиям")
    fig.update_traces(hole=.4)
    fig.update_layout(
        height=600,
        width=800,
        xaxis_title="Десятилетие",
        yaxis_title="Посещаемость"
    )
    return fig

@callback(
    Output('team-bar-chart', 'figure'),
    Input('team-dropdown', 'value')
)
def update_team_bar_chart(team):
    df_team = df[df['Winners'] == team]
    fig = px.bar(df_team, x='Season', y='Attendance', title=f"Взаимосвязь между сезонами и посещаемостью для команды {team}")
    fig.update_layout(
        xaxis_title="Сезон",
        yaxis_title="Посещаемость"
    )
    return fig
