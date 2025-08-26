import pandas as pd
import numpy as np

def sales_data():
    # Coerente con il documento progetto e l'esempio fornito
    mesi = ['Gen','Feb','Mar','Apr','Mag','Giu','Lug','Ago','Set','Ott','Nov','Dic']
    vendite_tot = [4000,4200,4500,4700,6000,6200,5900,7000,6800,7200,7500,9000]
    clienti = [120,125,140,130,160,170,150,180,175,190,200,230]
    prodotto_top = ['Caffè','Cornetto','Caffè','Cornetto','Caffè','Spremuta','Caffè','Spremuta','Caffè','Cornetto','Caffè','Caffè']
    vendite_top = [1500,1600,1800,1700,2000,2200,2100,2400,2300,2500,2700,3200]
    margine_pct = [30,28,32,29,33,35,31,34,32,33,34,36]

    df = pd.DataFrame({
        'Mese': mesi,
        'Vendite Totali (€)': vendite_tot,
        'Clienti': clienti,
        'Prodotto Top': prodotto_top,
        'Vendite Prodotto Top (€)': vendite_top,
        'Margine di Profitto (%)': margine_pct
    })
    df['Margine di Profitto (€)'] = df['Vendite Prodotto Top (€)'] * df['Margine di Profitto (%)'] / 100.0
    df['Crescita Vendite (%)'] = df['Vendite Totali (€)'].pct_change() * 100.0
    return df

def customers_data():
    rng = np.random.default_rng(7)
    ids = [f"C{i:03d}" for i in range(1,51)]
    acquisti = rng.integers(1, 30, size=len(ids))
    speso = (acquisti * rng.uniform(10, 50, size=len(ids))).round(2)
    preferiti = rng.choice(['Caffè','Cornetto','Spremuta','Pasticcino','Tè','Latte'], size=len(ids))
    mesi = rng.choice(['Gen','Feb','Mar','Apr','Mag','Giu','Lug','Ago','Set','Ott','Nov','Dic'], size=len(ids))
    df = pd.DataFrame({
        'ID Cliente': ids,
        'Numero Acquisti': acquisti,
        'Totale Speso (€)': speso,
        'Prodotto Preferito': preferiti,
        'Ultimo Acquisto (Mese)': mesi
    })
    df['Ticket Medio (€)'] = (df['Totale Speso (€)'] / df['Numero Acquisti']).round(2)
    return df

def inventory_data():
    prodotti = ['Caffè','Cornetto','Spremuta','Pasticcino','Tè','Latte','Croissant','Panettone','Cioccolato','Brioche']
    ids = [f"P{i:03d}" for i in range(1, len(prodotti)+1)]
    qty = [20,50,30,10,60,40,15,5,25,12]
    vendite_mensili = [200,150,180,100,120,90,110,50,140,80]
    lead = [5,7,4,6,3,5,7,10,6,4]

    df = pd.DataFrame({
        'ID Prodotto': ids,
        'Nome Prodotto': prodotti,
        'Quantità Disponibile': qty,
        'Vendite Mensili': vendite_mensili,
        'Tempo di Riordino (giorni)': lead
    })
    df['Livello Ottimale'] = df['Vendite Mensili'] * df['Tempo di Riordino (giorni)'] / 30.0
    df['Da Riordinare'] = (df['Livello Ottimale'] - df['Quantità Disponibile']).clip(lower=0).round(0)
    return df

def pricing_data():
    df = pd.DataFrame({
        'ID Prodotto': [f"P{i:03d}" for i in range(1,11)],
        'Nome Prodotto': ['Caffè','Cornetto','Spremuta','Pasticcino','Tè','Latte','Croissant','Panettone','Cioccolato','Brioche'],
        'Prezzo di Vendita (€)': [1.5,2.0,3.5,2.2,1.8,1.4,2.5,6.0,4.0,2.5],
        'Costo di Produzione (€)': [0.8,1.0,1.2,1.0,0.6,0.7,1.1,2.5,1.5,1.2],
        'Volume Vendite (unità mensili)': [1000,800,1200,600,500,700,950,300,450,800]
    })
    df['Margine di Profitto (€)'] = df['Prezzo di Vendita (€)'] - df['Costo di Produzione (€)']
    df['Margine Totale (€)'] = df['Margine di Profitto (€)'] * df['Volume Vendite (unità mensili)']
    df['Prezzo Aumentato (€)'] = df['Prezzo di Vendita (€)'] * 1.10
    df['Vendite Previste con Aumento'] = df['Volume Vendite (unità mensili)'] * 0.95
    df['Margine Previsionale con Aumento (€)'] = (df['Prezzo Aumentato (€)'] - df['Costo di Produzione (€)']) * df['Vendite Previste con Aumento']
    return df

def reviews_data():
    df = pd.DataFrame({
        'ID Recensione': [f"R{i:03d}" for i in range(1,21)],
        'Piattaforma': ['Google','TripAdvisor','Google','Facebook','Google','Facebook','TripAdvisor','Google','Facebook','Google']*2,
        'Testo Recensione': [
            'Ottimo caffè e personale cordiale!',
            'Servizio lento e poco attento.',
            'Mi è piaciuto molto il cornetto, tornerò sicuramente.',
            'Esperienza deludente, troppa attesa.',
            'Ambiente pulito e confortevole.',
            'Il barista è stato scortese.',
            'Cibo buono ma porzioni piccole.',
            'Adoro questo posto, ci vado ogni mattina.',
            'Posto carino ma prezzi alti.',
            'Il miglior caffè della zona!'
        ]*2
    })
    return df
