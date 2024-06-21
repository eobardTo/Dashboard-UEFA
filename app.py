import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from pages import map_view, season_stats, team_analysis, home
from data import load_data

df = load_data()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("UEFA Champions League", className="display-6"),
        html.Hr(),
        html.P(
            "Проект студента БСБО-15-21", className="lead"
        ),
        html.P(
            "Ефимов И.А.", className="lead"
        ),

        dbc.Nav(
            [
                dbc.NavLink("О проекте", href="/", active="exact"),
                dbc.NavLink("Обзорная карта", href="/map-view", active="exact"),
                dbc.NavLink("Статистика по сезонам", href="/season-stats", active="exact"),
                dbc.NavLink("Анализ команд", href="/team-analysis", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return home.layout()
    elif pathname == "/map-view":
        return map_view.layout(df)
    elif pathname == "/season-stats":
        return season_stats.layout(df)
    elif pathname == "/team-analysis":
        return team_analysis.layout(df)
    return html.Div([
        html.H1("404: Not Found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognized..."),
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
