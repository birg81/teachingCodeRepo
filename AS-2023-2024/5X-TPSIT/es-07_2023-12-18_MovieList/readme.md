# progetto FastAPI con binding al DBMS senza ORM

FastAPI si connette al DB Sakila ed effettua una selezione di film che inizialmente mostrerà tutti i film in catalogo ma attraverso una comodizzima searchbar sarà possibile filtrare i risultati istantaneamente

## Base di dati

L'esempio funziona con il db [sakila](https://downloads.mysql.com/docs/sakila-db.zip)

Dopo averlo scaricato e installato, si avvii MySQL/MariaDB e solo successivamente si avvii il progetto

### Dipendenze

Per essere certi di avere installato tutte le dipendenze, basterà eseguire

```bash
pip install -r requirements.txt
```

#### In caso di errori
Nel caso il comando precedente non dovesse funzionare, magari perché l'ambiente python non è ben configurato, si provi a scrivere

```bash
python -m pip install -r requirements.txt
```

od in alternativa

```bash
python -m pip install -r requirements.txt
```