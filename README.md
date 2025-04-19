# Flask API – Analiza danych w czasie rzeczywistym

Aplikacja Flask realizująca prostą regułę decyzyjną na podstawie dwóch zmiennych (`x1` i `x2`). Projekt stworzony na podstawie pliku `Lab2.ipynb` w ramach zajęć z analizy danych w czasie rzeczywistym.

---

## 📁 Zawartość repozytorium

- `app.py` – aplikacja Flask z regułą decyzyjną
- `script1.py` – zapytanie do API (requests)
- `script2.py` – test jednostkowy
- `script3.py` – tworzenie środowiska wirtualnego
- `requirements.txt` – lista bibliotek
- `Dockerfile` – konteneryzacja aplikacji

---

## ▶️ Uruchomienie lokalne (Python)

```bash
# 1. Utwórz i aktywuj środowisko wirtualne
python3 -m venv .venv
source .venv/bin/activate

# 2. Zainstaluj zależności
pip install -r requirements.txt

# 3. Uruchom aplikację
python app.py
```

### 🔄 Wysłanie zapytania (w drugim terminalu):

```bash
python script1.py
```

---

## 🐳 Uruchomienie w kontenerze Docker

```bash
# 1. Zbuduj obraz Dockera
docker build -t flask-api .

# 2. Uruchom kontener
docker run -p 5000:5000 flask-api
```

### 🔄 Wysłanie zapytania do API:

```bash
python script1.py
```

---

## 📬 Autor
Projekt zaliczeniowy na podstawie materiałów z przedmiotu **Analiza danych w czasie rzeczywistym**.
