# Retail Analytics Suite

Una web app Dash che integra:
- Analisi Vendite
- Analisi Clienti
- Ottimizzazione Inventario
- Strategia di Pricing
- Analisi Sentiment Recensioni
- Dashboard panoramica

## Requisiti
- Python 3.10+
- Vedere `requirements.txt`

## Installazione
```bash
python -m venv .venv
source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Poi apri il browser su http://127.0.0.1:8050/

## Struttura
- `app.py`: applicazione Dash con schede (tab) per ogni analisi
- `data_simulation.py`: genera i dataset fittizi
- `analysis_*.py`: funzioni che restituiscono figure Plotly e tabelle
- `assets/style.css`: piccolo tema CSS

I dataset sono sintetici e seguono il progetto allegato.
