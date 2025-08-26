import plotly.express as px
from data_simulation import reviews_data
from textblob import TextBlob

def _sentiment(text):
    pol = TextBlob(text).sentiment.polarity
    if pol > 0.2: return 'Positiva'
    if pol < -0.2: return 'Negativa'
    return 'Neutra'

def figs():
    df = reviews_data()
    df['Sentiment'] = df['Testo Recensione'].apply(_sentiment)
    pie = px.pie(df, names='Sentiment', title='Distribuzione sentiment recensioni')
    hist = px.histogram(df, x='Piattaforma', color='Sentiment', barmode='group',
                        title='Sentiment per piattaforma')
    return df, pie, hist
