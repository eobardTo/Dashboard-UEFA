from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import load_data

df = load_data()

def layout(df):
    return dbc.Container([
        dbc.Row([
            dbc.Col(html.Div([
                html.H1("Анализ команд"),
                html.Hr(),
                html.P("Подробная информация по достижениям отдельных команд.")
            ]))
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='team-dropdown',
                    options=[{'label': team, 'value': team} for team in df['Winners'].unique()],
                    value=df['Winners'].unique()[0]
                )
            ], width=4)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='team-goals-chart'), width=12)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='team-goals-pie-chart'), width=12, style={'display': 'flex', 'justify-content': 'center'})
        ])
    ])

@callback(
    Output('team-goals-chart', 'figure'),
    Input('team-dropdown', 'value')
)
def update_team_goals_chart(team):
    df_team = df[df['Winners'] == team]
    fig = px.bar(df_team, x='Season', y='WinnerScore', title=f"Количество голов у команды {team} по сезонам")
    fig.update_layout(
        xaxis_title="Сезон",
        yaxis_title="Голы"
    )
    return fig

@callback(
    Output('team-goals-pie-chart', 'figure'),
    Input('team-dropdown', 'value')
)
def update_team_goals_pie_chart(team):
    df_team = df[df['Winners'] == team]
    df_team = df_team.sort_values(by='WinnerScore', ascending=False)
    top_scorer = df_team.iloc[0]
    fig = px.pie(df_team, names='Season', values='WinnerScore', 
                 title=f"Самый результативный сезон для команды {team}: {top_scorer['Season']}, {top_scorer['WinnerScore']} голов")
    fig.update_traces(hole=.4)
    fig.update_layout(
        height=600,  # Увеличение высоты
        width=800,   # Увеличение ширины
        title_x=0.5  # Центрирование заголовка
    )
    return fig
