from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("OnePieceArcs.csv")

fig = px.bar(df, x="TotalEpisodes", y="TotalPages", color="Arc", barmode="group")

opcoes = list(df['Arc'].unique())
opcoes.append("All Arcs")

app.layout = html.Div(children=[
    html.H1(children="Minutos por episodio One Piece"),
    html.H2(children="Gráfico com episodios por páginas separados por Arco"),
    dcc.Dropdown(opcoes, value='All Arcs', id='listaArcos'),

    dcc.Graph(
        id='grafico',
        figure=fig
    )
])

@app.callback(
    Output('grafico', 'figure'),
    Input('listaArcos', 'value')
)

def updateOutput(value):
    if value == "All Arcs":
        fig = px.bar(df, x="TotalEpisodes", y="TotalPages", color="Arc", barmode="group")
    else:
        tabelaFiltrada = df.loc[df['Arc'] == value, :]
        fig = px.bar(tabelaFiltrada, x="TotalEpisodes", y="TotalPages", color="Arc", barmode="group"    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)