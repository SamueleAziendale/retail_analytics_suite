import dash
from dash import dcc, html, dash_table
import plotly.express as px

import analysis_sales, analysis_customers, analysis_inventory, analysis_pricing, analysis_reviews
from data_simulation import sales_data, customers_data, inventory_data
import os  # Necessario per gestire la porta su Render

# Inizializziamo l'app Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Retail Analytics Suite"

# IMPORTANTE: esponiamo il server per Render
server = app.server

# ------------------------
# Funzione per creare le tabelle
# ------------------------
def table_from_df(df, page_size=10):
    # Formattiamo tutti i numeri: due decimali, ma se .00 allora intero
    def format_number(x):
        if isinstance(x, (int, float)):
            if float(x).is_integer():
                return int(x)
            else:
                return round(x, 2)
        return x

    formatted_df = df.applymap(format_number)

    return dash_table.DataTable(
        columns=[{"name": c, "id": c} for c in formatted_df.columns],
        data=formatted_df.to_dict('records'),
        page_size=page_size,
        style_table={'overflowX': 'auto'},
        style_cell={
            'padding': '8px',
            'textAlign': 'left',
            'minWidth': '120px',
            'width': '120px',
            'maxWidth': '220px'
        },
        style_header={'fontWeight': '700'}
    )

# ------------------------
# Layout principale
# ------------------------
app.layout = html.Div([
    html.H1("Retail Analytics Suite"),
    dcc.Tabs([
        # -------------------------------
        # DASHBOARD
        # -------------------------------
        dcc.Tab(label="Dashboard", children=[
            # Prima riga: due grafici affiancati
            html.Div(className="grid two-cols", children=[
                html.Div(className="card", children=[
                    html.H3("Vendite Mensili per Prodotto (demo)"),
                    dcc.Graph(
                        figure=px.bar(
                            sales_data().assign(**{
                                'Nome Prodotto': [
                                    'Caffè', 'Cornetto', 'Spremuta', 'Pasticcino', 'Tè', 'Latte',
                                    'Croissant', 'Panettone', 'Cioccolato', 'Brioche', 'Caffè', 'Cornetto'
                                ]
                            }),
                            x='Nome Prodotto',
                            y='Vendite Totali (€)',
                            title="Vendite (proxy dai dati mensili)"
                        ),
                        style={"height": "400px"}
                    )
                ]),
                html.Div(className="card", children=[
                    html.H3("Inventario - Scorte vs Livello Ottimale"),
                    dcc.Graph(
                        figure=analysis_inventory.figs()[2],
                        style={"height": "400px"}
                    )
                ])
            ]),

            # Seconda riga: grafico sentiment recensioni sotto
            html.Div(className="grid one-col", children=[
                html.Div(className="card", children=[
                    html.H3("Sentiment Recensioni (overview)"),
                    dcc.Graph(
                        figure=analysis_reviews.figs()[1],
                        style={"height": "400px"}
                    )
                ])
            ]),
        ]),

        # -------------------------------
        # VENDITE
        # -------------------------------
        dcc.Tab(label="Vendite", children=[
            html.Div(className="card", children=[
                html.H3("Analisi Vendite"),
                dcc.Graph(figure=analysis_sales.figs()[1]),
                dcc.Graph(figure=analysis_sales.figs()[2]),
                dcc.Graph(figure=analysis_sales.figs()[3]),
                html.H4("Dati Vendite"),
                table_from_df(analysis_sales.figs()[0])
            ])
        ]),

        # -------------------------------
        # CLIENTI
        # -------------------------------
        dcc.Tab(label="Clienti", children=[
            html.Div(className="card", children=[
                html.H3("Analisi Clienti"),
                dcc.Graph(figure=analysis_customers.figs()[1]),
                dcc.Graph(figure=analysis_customers.figs()[2]),
                dcc.Graph(figure=analysis_customers.figs()[3]),
                html.H4("Dati Clienti"),
                table_from_df(analysis_customers.figs()[0])
            ])
        ]),

        # -------------------------------
        # INVENTARIO
        # -------------------------------
        dcc.Tab(label="Inventario", children=[
            html.Div(className="card", children=[
                html.H3("Ottimizzazione Inventario"),
                dcc.Graph(figure=analysis_inventory.figs()[1]),
                dcc.Graph(figure=analysis_inventory.figs()[2]),
                html.H4("Dati Inventario"),
                table_from_df(analysis_inventory.figs()[0])
            ])
        ]),

        # -------------------------------
        # PRICING
        # -------------------------------
        dcc.Tab(label="Pricing", children=[
            html.Div(className="card", children=[
                html.H3("Strategia di Pricing"),
                dcc.Graph(figure=analysis_pricing.figs()[1]),
                html.H4("Dati Pricing"),
                table_from_df(analysis_pricing.figs()[0])
            ])
        ]),

        # -------------------------------
        # RECENSIONI
        # -------------------------------
        dcc.Tab(label="Recensioni", children=[
            html.Div(className="card", children=[
                html.H3("Analisi Recensioni Online"),
                dcc.Graph(figure=analysis_reviews.figs()[1]),
                dcc.Graph(figure=analysis_reviews.figs()[2]),
                html.H4("Dati Recensioni"),
                table_from_df(analysis_reviews.figs()[0])
            ])
        ]),
    ]),
    html.Div(className="footer", children="Demo – dati fittizi; personalizzabile collegando fonti reali (CSV, DB, API).")
])

# ------------------------
# Avvio compatibile con Render/Heroku
# ------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=False)
