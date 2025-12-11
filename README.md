
# Table of Contents

1.  [Status - Refactoring](#org0f6e5d5)
2.  [Intro](#orgff10b67)
    1.  [Obiettivo](#org8b61a91)
3.  [Features](#orga15c88a)
4.  [Tech Stack](#org5fbc844)
    1.  [Database - MySQL Server](#org9fae2d2)
        1.  [Implementation - Coming Soon &#x2026;](#orgc4b6234)
    2.  [Backend - Python](#orgb813d3e)
        1.  [Implementation - Coming Soon &#x2026;](#orgc4597b6)
    3.  [Frontend - HTML - CSS - JavaScript Vanilla](#org669ccfd)
        1.  [Implementation - Coming Soon &#x2026;](#orgfbd5ce0)
5.  [Local Setup](#org0bd94f4)
    1.  [MySQL Server](#orgde2af51)
        1.  [Linux](#orgf7c6f89)
        2.  [MacOS - Coming Soon &#x2026;](#org84c4cc0)
        3.  [Windows - Coming Soon &#x2026;](#org71c9233)
    2.  [Venv Python](#org71c6f5e)
6.  [Contact Info](#org86026c1)

p#+TITLE: Cryptotype - Cryptocurrencies Trading Platform Simulator


<a id="org0f6e5d5"></a>

# Status - Refactoring

Dopo aver creato un primo prototipo per testare e validare le idee fondamentali, il progetto è attualmente in fase di revisione completa. Processo atto a condensare quanto appreso e sviluppato, in un prodotto completo e ottimizzato, con desing rivisto e funzionalità complete.

-   **Nota**: attualmente l'aspetto grafico del progetto non è completo e presenta bug, lasciati irrisolti poichè è in corso un refactoring completo.


<a id="orgff10b67"></a>

# Intro

Cryptotype è un prototipo di una Web Application che simula una piattaforma di trading di criptovalute, da cui il nome *Crypto = Criptovaluta* | *Type = Prototype*, un ambiente in cui effettettuare analisi, scegliere l'asset preferito, compravendita, visualizzazione portafoglio, dati in real-time, permettendo un'esperienza dinamica.


<a id="org8b61a91"></a>

## Obiettivo

Questo progetto nasce grazie a diverse motivazioni:

-   **Pratica**: dalla volontà di praticare e affinare le capacità di sviluppo, relative ad un progetto Full-Stack e al suo ciclo di vita completo.
-   **Studio e Dettaglio**: introdurre nuovi argomenti allo studio, approfondire concetti e l'interazione tra essi.
-   **Passione e Piacere**: dare spazio alla semplice voglia di praticare e creare, esternare ciò che si ha all'interno per visualizzarlo all'esterno, ottenendo punti di vista e prospettive differenti, acquisendo così maggiore consapevolezza, riuscendo a comprendere ciò che non era stato compreso analizzandolo solo dall'interno. Questo aspetto è ricorrente in quasi tutte, se non tutte le azioni dell'essere Umano e credo sia la forza trainante di ogni decisione effettuata, consapevolmente o inconsapevolmente.


<a id="orga15c88a"></a>

# Features

Cryptotype mette a disposizione dell'utente diverse funzionalità, permettendo un'esperienza dinamica:

-   **Analisi**: è possibile utilizzare grafici interattivi per analizzare l'andamento del prezzo e altre informazioni.
-   **Visualizzazione Criptovalute**: fornisce una lista di criptovalute, con parametri annessi in real-time, permettendo la selezione dell'asset preso in considerazione.
-   **Creazione Account**: tramite un form di registrazione, è possibile creare il proprio account, tramite campi *username*, *email* e *password* (hashed), ottenendo così:
    -   **Portafoglio**: sezione dedicata alla visualizzazione del portafoglio e alle relative informazioni.
        -   **Saldo**: funzionalità di deposito e ritiro di un saldo simulato per effettuare transazioni.
        -   **Sezione Assets**: dedicata alla visualizzazione delle criptovalute detenute.
-   **Spot Trading Simulator**: sezione che fornisce funzionalità per effettuare transazioni simulate di tipo *Spot* (transazione specifica basata sull'acquisto/vendita di un asset finanziario al suo prezzo di mercato corrente).
-   **Login**: accesso al proprio account con le relative informazioni e componenti.


<a id="org5fbc844"></a>

# Tech Stack

La scelta delle tecnologie utilizzate per sviluppare Cryptotype è basata sulla volontà di operare senza particolari astrazioni, per implementare manualmente e in modo granulare vari aspetti e funzionalità.


<a id="org9fae2d2"></a>

## Database - MySQL Server

Ottimo equilibrio tra prestazioni, facilità e affidabilità.


<a id="orgc4b6234"></a>

### Implementation - Coming Soon &#x2026;

-   Connection Pooling&#x2026;
-   Integrity&#x2026;


<a id="orgb813d3e"></a>

## Backend - Python

Rapidità nella prototipazione e testing ed ecosistema di librerie specializzate ai fini di Cryptotype.


<a id="orgc4597b6"></a>

### Implementation - Coming Soon &#x2026;

-   HTTPS Server&#x2026;
-   WebSocket Server&#x2026;
-   Hash Function/Salt&#x2026;
-   API/RESTful API&#x2026;
-   Asynchronous Programming&#x2026;


<a id="org669ccfd"></a>

## Frontend - HTML - CSS - JavaScript Vanilla

La scelta di utilizzare JavaScript vanilla è stata fatta per implementare e gestire manualmente le logiche di funzionamento e per comprendere a pieno il funzionamento sottostante i Framework moderni il principcio di SoC - Separation of Concerns - e Design Patterns (SSOT, Singletone, Observer/Publish-Subscribe)


<a id="orgfbd5ce0"></a>

### Implementation - Coming Soon &#x2026;

-   WebSocket&#x2026;
-   Asynchronous Programming&#x2026;
-   SoC - Separation of Concerns&#x2026;
-   Design Patterns&#x2026;
    -   SSOT - Single Source of Truth&#x2026;
    -   Singletone&#x2026;
    -   Observer/Publish-Subscribe
-   DOM Manipulation&#x2026;


<a id="org0bd94f4"></a>

# Local Setup


<a id="orgde2af51"></a>

## MySQL Server


<a id="orgf7c6f89"></a>

### Linux

-   **Installazione**:
    
        sudo apt update
        sudo apt install mysql-server

-   **Configurazione**:
    
        sudo mysql_secure_installation   # Seguire l'installazione guidata
        
        ################################
        # Secure Installation Guide
        # 1. VALIDATE PASSWORD component - BUG:
        #   In questo step è presente un BUG, viene chiesto se imporre password
        #   per tutti gli utenti (incluso root), prevenendo password deboli.
        #   In alcuni casi l'impostazione di una password viene completamente saltata.
        #
        #   Soluzione:
        #     1. Avviare mysql
        #     2. Se verrà chiesto di inserire una password, inserire qualunque
        #        carattere, l'accesso andrà a buon fine.
        #     3. Eseguire il comando seguente, sostituendo al placeholder "new_password"
        #        la vostra password:
        #        ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'new_password';
        #     4. I prossimi accessi dovranno essere eseguiti tramite "mysql -u root -p"
        #
        # 2. Anonymous User:
        #   Nello step 2 dell'installazione, MySQL indica la presenza,
        #   per default, di utenti anonimi.
        #   Lasciare utenti anonimi comporta una grave vulnerabilità di sicurezza.
        #   Permette a chiunque di connettersi al db senza username o password.
        #   Rimuovere gli utenti anonimi per una sicurezza maggiore.
        #
        # 3. Remote Access:
        #   Negare la possibilità di effettuare l'accesso remoto all'utente root.
        #################################

-   **Script Initialization**: script di inizializzazione del database
    
        SET FOREIGN_KEY_CHECKS = 0;
        
        DROP DATABASE IF EXISTS cryptotype;
        CREATE DATABASE cryptotype;
        USE cryptotype;
        
        DROP TABLE IF EXISTS user;
        DROP TABLE IF EXISTS portfolio;
        DROP TABLE IF EXISTS position;
        
        CREATE TABLE user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(30) NOT NULL UNIQUE,
            email VARCHAR(254) NOT NULL UNIQUE,
            password CHAR(60) NOT NULL
        );
        
        CREATE TABLE portfolio (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,
            FOREIGN KEY (user_id) REFERENCES user(id)
        );
        
        CREATE TABLE position (
            id INT AUTO_INCREMENT PRIMARY KEY,
            portfolio_id INT NOT NULL,
            ticker VARCHAR(50) NOT NULL,
            execution_price DECIMAL(20,8) NOT NULL,
            size DECIMAL(20,8) NOT NULL,
            status ENUM('open', 'closed') NOT NULL DEFAULT 'open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            closed_at TIMESTAMP NULL DEFAULT NULL,
            FOREIGN KEY (portfolio_id) REFERENCES portfolio(id)
        );
        
        SET FOREIGN_KEY_CHECKS = 1;

-   **Official Doc**: <https://dev.mysql.com/doc/>


<a id="org84c4cc0"></a>

### MacOS - Coming Soon &#x2026;


<a id="org71c9233"></a>

### Windows - Coming Soon &#x2026;


<a id="org71c6f5e"></a>

## Venv Python

    # Creazione ambiente virtuale e installazione dipendenze
    # Best Practice: installare il venv nella root del progetto
    python[3] -m venv .venv           # [3]: versione python
    source .venv/bin/activate         # (Windows: .venv\Scripts\activate)
    pip install -r requirements.txt
    
    # Modificare il file "/backend/config/settings.py", inserendo nella chiave
    # "password", il valore relativo alla vostra password del database
    
    # Avvio di Cryptotype
    python main.py

-   **Official Doc**: <https://www.python.org/doc/>

-   **VSC Note**: se l'editor utilizzato è Visual Studio Code, questo potrebbe mostrare errori legati alla risoluzione dei paths relativi ai packages/modules installati tramite "pip".
    -   Assicurarsi che l'interprete Python utilizzato dall'editor sia quello del venv (.venv/bin/python)
    -   **Errore tipo**: Import "aiomysql" could not be resolved Pylance (reportMissingImports)
    -   **Risoluzione**:
        -   "Ctrl+Shift+P" (Command Palette)
        -   "Python: Select Interpreter"
        -   Selezionare "python" presente nel venv


<a id="org86026c1"></a>

# Contact Info

-   **Email**: valeriodellamorte.info@gmail.com
-   **Linkedin**: <https://www.linkedin.com/in/valerio-della-morte>

