import plotly.express as px
from data_simulation import pricing_data

def figs():
    df = pricing_data()
    fig_margin_compare = px.bar(df, x='Nome Prodotto',
                                y=['Margine Totale (€)','Margine Previsionale con Aumento (€)'],
                                barmode='group', title='Margine attuale vs post-aumento')
    return df, fig_margin_compare
