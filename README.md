# nep-challenge

## Getting Started

1. Clonare la repository

```
git clone https://github.com/Nico769/nep-challenge.git
```

2. Creare un ambiente virtuale (qui viene usato `pyenv`)

```
pyenv virtualenv nep-challenge
```

3. Attivare l'ambiente virtuale appena creato

```
pyenv shell nep-challenge
```

4. Installare le dipendenze

```
pip install -r requirements.txt
```

5. Eseguire le migrazioni

```
python manage.py migrate
```

6. Eseguire lo script per popolare il DB con un'utenza superuser `admin`, alcuni utenti applicativi e le fixture in `core/fixtures`

```
chmod +x setup-db-data-dev.sh
./setup-db-data-dev.sh
```

7. Eseguire l'applicativo

```
python manage.py runserver
```

## TODO

- autenticazione utente tramite token
- Role-based Access Control per l'utente autenticato
- aggiunta di una risorsa ad un nodo parent
- Suite di test minimale
