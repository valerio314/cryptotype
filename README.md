# Intro

-   Cryptotype è un prototipo di una Web Application che simula una piattaforma di trading di criptovalute.
-   Questo progetto rappresenta un'idea di base e non intende essere un prodotto pronto per il mercato, realizzato come esercizio per sviluppare competenze.
-   Lo scopo di Cryptotype è garantire e mostrare le capacità dello sviluppatore, fornendo una guida generale sulle competenze (in continuo sviluppo), sull'intraprendenza e soprattutto mettere in risalto la grande passione per l'Informatica e per i Mercati Finanziari

# Obiettivi Tecnici

-   Simulare un ambiente di trading realistico con dati aggiornati in real-time tramite WebSocket.
-   Applicare concetti di architettura software, asynchronous programming e separazione dei livelli logici.
-   Integrare design pattern fondamentali (Observer, Singleton, MVC) all’interno di una struttura modulare.
-   Realizzare un prototipo Full Stack, con backend, database e frontend integrati.

# User Experience

-   L'applicazione completa offre una UX dinamica, mettendo a disposizione dell'utente diverse funzionalità:
    -   Authentication: possibilita' di creare un account ed effettuare il login per riprendere la sessione
    -   Portfolio: associato automaticamente alla creazione dell'account:
        -   Saldo: possibilità di "Deposit" e "Withdraw", destinato all'attività di trading
    
    -   Dati Criptovalute: sezione dedicata alla visualizzazione di una lista di criptovalute con parametri di base
        -   Dati Real-Time
        -   Search Input: input che permette di cercare, per ticker, tra le cripto della lista
    
    -   Grafici: per analisi dell'andamento del prezzo e altri indicatori
    -   Trading: sezione dove simulare l'attività
        -   Quantità in USD
        -   Quantità in Base Unit
    
    -   Portfolio: sezione dedicata al portfolio, dove visualizzare le info annesse:
        -   Balance
        -   Equity
        -   Floating P&L
        -   Sezione dedicata alle posizioni aperte in tempo reale
    
    -   Tutti i dati verranno salvati in un database e al login l'utente potrà continuare la sessione

# Stack Tecnologico
## Database - MySQL

-   Schema SQL: progettato per tenere traccia dei dati relativi a:
    -   Utente
    -   Portfolio
    -   Posizioni

-   Migration Script: file contenente comandi per inizializzare il database

## Backend - Python

-   Programmazione asincrona
-   Connection Pooling
-   Hashing password
-   WebSocket Server per comunicazione e dati real-time
-   HTTP Server per Static File Hosting (in contesto SPA)

## Frontend - JavaScript Vanilla

-   Utilizzo di moduli ES6
-   CSS con sistema di design strutturato
-   TradingView Widget per grafici
-   Client WebSocket per dati real-time
-   Design Pattern:
    -   MVC
    -   Singletone
    -   Observe

# Stato Attuale del Progetto - 85% (20/10/2025)

-   Il progetto è alla fine del suo sviluppo, manca di poche funzionalità per essere terminato

# Quick Start (Esecuzione Locale)

-   Per eseguire Cryptotype in locale:
    
        # Creazione ambiente virtuale e installazione dipendenze
        python -m venv .venv
        source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
        pip install -r requirements.txt
        
        # Avvio del backend
        python main.py

-   VSC Note: se l'editore utilizzato è Visual Studio Code, questo potrebbe mostrare errori legati alla risoluzione dei paths relativi ai packages/modules installati tramite "pip".
    -   Assicurarsi che l'interprete Python utilizzato dall'editor sia quello del venv (.venv/bin/python)
    -   Errore tipo: Import "aiomysql" could not be resolved Pylance (reportMissingImports)
    -   Risoluzione:
        -   "Ctrl+Shift+P" (Command Palette)
        -   "Python: Select Interpreter"
        -   Selezionare "python" presente nel venv

-   /cryptotype/backend/config/settings.py: file contenente le specifiche di configurazione

# Note

-   Questo progetto è realizzato a scopo dimostrativo e di portfolio personale.
-   Autore: Valerio Della Morte

