# Insinöörilaskin

## Kehitysympäristön pystytys
1. Asenna Poetry ja Python 3.13.11.
2. Perusta ympäristö projektin juurihakemistossa komennolla 'poetry install'.

## Ajaminen paikallisesti

- Luo ja aktivoi ympäristö (jos ei vielä tehty):
```
poetry env use 3.13.11
poetry install
```

- Tapa 1: Konsolikomento (lisätty `pyproject.toml` → skripti `insinoorilaskin`)
```
poetry run insinoorilaskin
```

- Tapa 2: Python-moduulina
```
poetry run python -m insinoorilaskin
```

- Tapa 3: Suora tiedostoajo
```
poetry run python src/insinoorilaskin/main.py
```

Sovellus käynnistää yksinkertaisen HTTP-palvelimen, joka kuuntelee oletuksena porttia 8080 osoitteessa `0.0.0.0` ja pysyy käynnissä, kunnes sen keskeyttää (Ctrl+C). Palvelin alustaa myös lokituksen käyttäen paketin mukana tulevaa `src/insinoorilaskin/logger_config.toml`-tiedostoa ja luo `logs/`‑hakemiston nykyiseen työhakemistoon.

Kun palvelin on käynnissä, voit testata yhteyden:

```
curl http://localhost:8080/health
# tai
curl http://localhost:8080/
```

Molempien pitäisi vastata `OK` (HTTP 200).

### Konfigurointi (valinnainen)
- `.env`-tiedosto luetaan automaattisesti (python-dotenv).
- Voit yliajaa lokikonfiguraation polun asettamalla ympäristömuuttujan `insinoorilaskin_LOGGER_CONFIG_FILE`, esim. `.env`:
```
insinoorilaskin_LOGGER_CONFIG_FILE=/absoluuttinen/polku/oma_logger_config.toml
```

- Palvelimen osoitteen ja portin voi konfiguroida ympäristömuuttujilla:
```
insinoorilaskin_HOST=127.0.0.1
insinoorilaskin_PORT=8080
```
Oletukset: `HOST=0.0.0.0`, `PORT=8080`.

## Testien ajaminen
```
poetry run pytest
```
Kattavuusraportit kirjoitetaan hakemistoon `tests/reports/`.

## Vianetsintävinkkejä
- Python 3.13.11 puuttuu: asenna esimerkiksi `pyenv`illa ja suorita `poetry env use 3.13.11` uudelleen.
- Poetry ei löydy: lisää PATH:iin tai käynnistä terminaali uudelleen asennuksen jälkeen.
