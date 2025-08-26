import plotly.express as px
from data_simulation import sales_data

def figs():
    df = sales_data()
    fig_trend = px.line(df, x='Mese', y=['Vendite Totali (€)','Vendite Prodotto Top (€)'], markers=True,
                        title='Andamento vendite mensili')
    fig_margin = px.bar(df, x='Mese', y='Margine di Profitto (€)', title='Margine di Profitto per mese (€)')
    fig_growth = px.bar(df, x='Mese', y='Crescita Vendite (%)', title='Crescita % mese su mese')
    return df, fig_trend, fig_margin, fig_growth
