import plotly.express as px
from data_simulation import inventory_data

def figs():
    df = inventory_data()
    to_reorder = df[df['Da Riordinare'] > 0]
    fig_reorder = px.bar(to_reorder, x='Nome Prodotto', y='Da Riordinare',
                         title='Prodotti da riordinare (priorità)')
    fig_levels = px.bar(df, x='Nome Prodotto', y=['Quantità Disponibile','Livello Ottimale'],
                        barmode='group', title='Scorte vs livello ottimale')
    return df, fig_reorder, fig_levels
