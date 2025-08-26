import plotly.express as px
from data_simulation import customers_data

def figs():
    df = customers_data()
    top = df.sort_values(by='Totale Speso (€)', ascending=False).head(10)
    fig_top = px.bar(top, x='ID Cliente', y='Totale Speso (€)', title='Top spender (Top 10)')
    fig_pref = px.histogram(df, x='Prodotto Preferito', title='Distribuzione prodotto preferito')
    fig_ticket = px.scatter(df, x='Numero Acquisti', y='Ticket Medio (€)', color='Prodotto Preferito',
                            size='Totale Speso (€)', title='Ticket medio vs frequenza acquisti')
    return df, fig_top, fig_pref, fig_ticket
