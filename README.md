
# Table of Contents

1.  [Status - Refactoring](#org1caff91)
2.  [Intro](#org329f36c)
    1.  [Obiettivo](#orgb9c93c4)
3.  [Features](#org3c2f919)
4.  [Tech Stack](#org58eefab)
    1.  [Database - MySQL Server](#orgc8c835d)
        1.  [Implementation - Coming Soon &#x2026;](#org648cba5)
    2.  [Backend - Python](#org4a06830)
        1.  [Implementation - Coming Soon &#x2026;](#org0861231)
    3.  [Frontend - HTML - CSS - JavaScript Vanilla](#orgc359546)
        1.  [Implementation - Coming Soon &#x2026;](#org3ca914e)
5.  [Local Setup](#org0be2578)
    1.  [MySQL Server](#orgb52d6e6)
        1.  [Linux](#orga547223)
        2.  [MacOS - Coming Soon &#x2026;](#orgb1f541d)
        3.  [Windows - Coming Soon &#x2026;](#org24cce3d)
    2.  [Venv Python](#orgd7b1785)
6.  [Contact Info](#org7f42974)



<a id="org1caff91"></a>

# Status - Refactoring

Dopo aver creato un primo prototipo per testare e validare le idee fondamentali, il progetto è attualmente in fase di revisione completa. Processo atto a condensare quanto appreso e sviluppato, in un prodotto completo e ottimizzato, con desing rivisto e funzionalità complete.

-   **Nota**: attualmente l'aspetto grafico del progetto non è completo e presenta bug, lasciati irrisolti poichè è in corso un refactoring completo.


<a id="org329f36c"></a>

# Intro

Cryptotype è un prototipo di una Web Application che simula una piattaforma di trading di criptovalute, da cui il nome *Crypto = Criptovaluta* | *Type = Prototype*, un ambiente in cui effettettuare analisi, scegliere l'asset preferito, compravendita, visualizzazione portafoglio, dati in real-time, permettendo un'esperienza dinamica.


<a id="orgb9c93c4"></a>

## Obiettivo

Questo progetto nasce grazie a diverse motivazioni:

-   **Pratica**: dalla volontà di praticare e affinare le capacità di sviluppo, relative ad un progetto Full-Stack e al suo ciclo di vita completo.
-   **Studio e Dettaglio**: introdurre nuovi argomenti allo studio, approfondire concetti e l'interazione tra essi.
-   **Passione e Piacere**: dare spazio alla semplice voglia di praticare e creare, esternare ciò che si ha all'interno per visualizzarlo all'esterno, ottenendo punti di vista e prospettive differenti, acquisendo così maggiore consapevolezza, riuscendo a comprendere ciò che non era stato compreso analizzandolo solo dall'interno. Questo aspetto è ricorrente in quasi tutte, se non tutte le azioni dell'essere Umano e credo sia la forza trainante di ogni decisione effettuata, consapevolmente o inconsapevolmente.


<a id="org3c2f919"></a>

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


<a id="org58eefab"></a>

# Tech Stack

La scelta delle tecnologie utilizzate per sviluppare Cryptotype è basata sulla volontà di operare senza particolari astrazioni, per implementare manualmente e in modo granulare vari aspetti e funzionalità.


<a id="orgc8c835d"></a>

## Database - MySQL Server

Ottimo equilibrio tra prestazioni, facilità e affidabilità.


<a id="org648cba5"></a>

### Implementation - Coming Soon &#x2026;

-   Connection Pooling&#x2026;
-   Integrity&#x2026;


<a id="org4a06830"></a>

## Backend - Python

Rapidità nella prototipazione e testing ed ecosistema di librerie specializzate ai fini di Cryptotype.


<a id="org0861231"></a>

### Implementation - Coming Soon &#x2026;

-   HTTPS Server&#x2026;
-   WebSocket Server&#x2026;
-   Hash Function/Salt&#x2026;
-   API/RESTful API&#x2026;
-   Asynchronous Programming&#x2026;


<a id="orgc359546"></a>

## Frontend - HTML - CSS - JavaScript Vanilla

La scelta di utilizzare JavaScript vanilla è stata fatta per implementare e gestire manualmente le logiche di funzionamento e per comprendere a pieno il funzionamento sottostante i Framework moderni il principcio di SoC - Separation of Concerns - e Design Patterns (SSOT, Singletone, Observer/Publish-Subscribe)


<a id="org3ca914e"></a>

### Implementation - Coming Soon &#x2026;

-   WebSocket&#x2026;
-   Asynchronous Programming&#x2026;
-   SoC - Separation of Concerns&#x2026;
-   Design Patterns&#x2026;
    -   SSOT - Single Source of Truth&#x2026;
    -   Singletone&#x2026;
    -   Observer/Publish-Subscribe
-   DOM Manipulation&#x2026;


<a id="org0be2578"></a>

# Local Setup


<a id="orgb52d6e6"></a>

## MySQL Server


<a id="orga547223"></a>

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

-   **Official Doc**: <https://dev.mysql.com/doc/>


<a id="orgb1f541d"></a>

### MacOS - Coming Soon &#x2026;


<a id="org24cce3d"></a>

### Windows - Coming Soon &#x2026;


<a id="orgd7b1785"></a>

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


<a id="org7f42974"></a>

# Contact Info

-   **Email**: valeriodellamorte.info@gmail.com
-   **Linkedin**: <https://www.linkedin.com/in/valerio-della-morte>

