# Table of Contents

1.  [Status - Refactoring](#org35cdd0a)
2.  [Intro](#org50e7d41)
    1.  [Obiettivo](#org201f232)
3.  [Features](#org40889ca)
4.  [Tech Stack <code>[1/3]</code>](#orgb4a24f0)
    1.  [Database - MySQL Server <code>[5/5]</code>](#orgbf39422)
        1.  [Integrità Referenziale](#orge73cac7)
        2.  [Autenticazione e Sicurezza](#orgfa589b1)
        3.  [Gruppo Sequenziale e Validato di Operazioni](#org6dc5500)
        4.  [Isolation](#org91ccb1e)
        5.  [Durability](#org8c6cc84)
    2.  [Backend - Python <code>[1/8]</code>](#org8ab5fc3)
        1.  [Venv](#org31d3eb8)
        2.  [Database Connection](#org9478df0)
        3.  [HTTP Server](#org5823c5f)
        4.  [WebSocket Server](#orgbad4f4e)
        5.  [DBManager API](#orgaea79c9)
        6.  [WebSocket Manager API](#org2a253a2)
        7.  [Asynchronous Programming](#orgd6ef665)
    3.  [Frontend - HTML - CSS - JavaScript Vanilla](#org673be3a)
        1.  [Features](#orgaa42b18)
5.  [Local Setup](#org4cc43fc)
6.  [Contact Info](#org908a07a)



<a id="org35cdd0a"></a>

# Status - Refactoring

Dopo aver creato un primo prototipo per testare e validare le idee
fondamentali, il progetto è attualmente in fase di revisione
completa. Processo atto a condensare quanto appreso e sviluppato, in un
prodotto completo e ottimizzato, con desing rivisto e funzionalità complete.

-   **Nota**: il sorgente verrà pubblicato sul repository al completamento del
    progetto.


<a id="org50e7d41"></a>

# Intro

Cryptotype è un prototipo di una Web Application (SPA - CSR) che simula una
piattaforma di trading di criptovalute, da cui il nome:

-   **Crypto:** Criptovaluta
-   **Type:** Prototype

Ambiente che fornisce diverse funzionalità:

-   Effettettuare **analisi di mercato**
-   Scegliere l'**asset preferito**
-   Svolgere **compravendita**
-   Visualizzare e modificare il **portafoglio**
-   Esaminare dati in **real-time**

Il tutto implementato in modo tale da offrire un'esperienza **fluida** e
**dinamica**.


<a id="org201f232"></a>

## Obiettivo

Questo progetto nasce grazie a diverse motivazioni:

-   **Pratica**: dalla volontà di praticare e affinare le capacità di sviluppo,
    relative ad un progetto Full-Stack e al suo ciclo di vita completo.

-   **Studio e Dettaglio**: introdurre nuovi argomenti allo studio, approfondire
    concetti e l'interazione tra essi.

-   **Passione e Piacere**: dare spazio alla semplice voglia di fare e applicare
    concretamente la passione personale per l'informatica

-   **Natura Umana**: **esternare** ciò che si ha all'**interno** per visualizzarlo
    all'**esterno**, ottenendo punti di vista e prospettive **differenti**,
    acquisendo così maggiore **consapevolezza**.
    Questo processo, ricorrente in tutte le azioni dell'Uomo, permette di
    comprendere più a fondo un fonemoneo che non è stato compreso dalla sola
    analisi interna. Esternare e **materializzare** un pensierio, un concetto,
    un'emozione, consente l'interazione di esso con i nostri **sensi**, permettendo
    un'**esperienza** più completa.


<a id="org40889ca"></a>

# DONE Features

Con Cryptotype, l'utente può svolgere diverse attività in modo dinamico:

-   **Analisi di Mercato**: è possibile utilizzare grafici interattivi per
    analizzare l'andamento del prezzo e altre informazioni.

-   **Visualizzazione Criptovalute**: visualizzare una lista di criptovalute, con
    parametri annessi in real-time, permettendo la selezione dell'asset preso in
    considerazione.

-   **Creazione Account**: tramite un form di registrazione, è possibile creare il
    proprio account, tramite campi "username", "email" e "password" (hashed),
    ottenendo così il componente "Portafoglio" e "Spot Trading Simulator".

-   **Portafoglio**: sezione dedicata alla visualizzazione del portafoglio, creato
    automaticamente dopo la creazione dell'account, e alle relative
    informazioni.
    -   **Saldo**: funzionalità di deposito e ritiro di un saldo simulato per
        effettuare transazioni.
    -   **Sezione Assets**: dedicata alla visualizzazione delle criptovalute
        detenute.

-   **Spot Trading Simulator**: fornisce funzionalità per effettuare transazioni
    simulate di tipo "Spot" (transazione specifica basata sull'acquisto/vendita
    di un asset finanziario al suo prezzo di mercato corrente).

-   **Login**: accesso al proprio account con le relative informazioni e
    componenti.


<a id="orgb4a24f0"></a>

# TODO Tech Stack <code>[1/3]</code>

La scelta delle tecnologie utilizzate per sviluppare Cryptotype è basata sulla
volontà di operare senza particolari astrazioni, per implementare manualmente
e in modo granulare vari aspetti e funzionalità.


<a id="orgbf39422"></a>

## DONE Database - MySQL Server <code>[5/5]</code>

Il RDBMS MySQL Server con storage engine InnoDB, garantisce le proprietà e
funzionalità di cui necessitano dati finanziari e la logica di business di
Cryptotype.


<a id="orge73cac7"></a>

### DONE Integrità Referenziale

Definire e mantenere relazioni e vincoli tra i dati.

-   **Esempio**: portafoglio associato a uno e un solo account.

-   **Implementazione**: InnoDB fornisce le "Foreign Key Constraints".


<a id="orgfa589b1"></a>

### DONE Autenticazione e Sicurezza

I dati devono essere accessibili solo agli utenti autorizzati.

-   **Esempio**: un utente può visualizzare solo il portafoglio associato al suo
    account.

-   **Implementazione**: MySQL fornisce un sistema di privilegi (GRANT/REVOKE)
    per autenticazione e autorizzazione.


<a id="org6dc5500"></a>

### DONE Gruppo Sequenziale e Validato di Operazioni

Eseguire determinate operazioni al database in modo sequenziale e validate,
trattate come un'unità indivisibile (tutte eseguite correttamente o nessuna
viene applicata).

-   **Esempio**: l'operazione di "acquisto di un asset" deve necessariamente
    essere susseguita dall'operazione di "modifica del saldo", ed entrambe
    eseguite con successo, o nessuna deve avere effetto.

-   **Implementazione**: InnoDB soddisfa questo requisito tramite le
    "Transazioni ACID", nello specifico, con la proprietà "A-tomicity".


<a id="org91ccb1e"></a>

### DONE Isolation

Le transazioni concorrenti che operano sugli stessi dati, o referenziati tra
loro, devono essere eseguite in modo sequenziale, anche se esse possono
essere inviate dal client in modo concorrenziale, dando l'illusione di
un'esecuzione parallela.

-   **Esempio**: l'invio di richiesta di esecuzione di due ordini di acquisto
    può essere effettuata in modo simultaneo e concorrenziale, ma l'esecuzione
    effettiva deve avvenire in sequenza.

-   **Implementazione**: InnoDB soddisfa questo requisito tramite le
    "Transazioni ACID", nello specifico, con la proprietà "I-solation".


<a id="org8c6cc84"></a>

### DONE Durability

Lo stato e gli effetti modificati da una operazione confermata devono
persistere permanentemente. I dati devono sopravvivere a crash improvvisi e
fallimenti del sistema, o risultare rigenerabili attraverso algoritmi.

-   **Esempio**: dopo l'acquisto di un asset, questo deve persistere nel
    portafoglio, anche in caso di riavvio del server o guasti.

-   **Implementazione**: InnoDB soddisfa questo requisito tramite le
    "Transazioni ACID", nello specifico, con la proprietà "D-urability".


<a id="org8ab5fc3"></a>

## TODO Backend - Python <code>[1/8]</code>

Python permette un bilanciamento tra produttività, controllo e apprendimento.
Essendo un linguaggio interpretato, il codice può essere modificato e testato
rapidamente, inoltre fornisce un ecosistema di librerie specializzate ai fini di
Cryptotype.
Il back-end di Cryptotype implementa le seguenti funzionlità:


<a id="org31d3eb8"></a>

### DONE Venv

Ambiente virtuale di esecuzione isolato, ovvero lo spazio in cui il progetto
viene eseguito, che comprende:

-   Versione Interprete Python
-   Packages e Modules
-   Versioni dei Packages e Modules

Il venv permette di riprodurre esattamente lo stesso ambiente tramite
l'installazione delle dipendenze al suo interno.


<a id="org9478df0"></a>

### TODO Database Connection

La connessione al database viene effettuata con `aiomysql`, un driver connector
asincrono, che permette operazioni parallele al database tramite Event-Loop
Single-Thread, riuscendo così a gestire le richieste derivanti dal WebSocket.

1.  TODO MySQL Async Protocol

    Il conncetor aiomysql implementa nativamente il protocollo MySQL su socket non
    bloccanti, consentendo quindi un vero parallelismo.


<a id="org5823c5f"></a>

### TODO HTTP Server

Entry point per effettuare l'handshake inziale con il frontend, a cui
inviare l'intera applicazione client e lavorare in contesto SPA tramite
l'aggiornamento della connessione a WebSocket.


<a id="orgbad4f4e"></a>

### TODO WebSocket Server

Entry point per gestire la connessione persistente con l'API JavaScript
client-side.


<a id="orgaea79c9"></a>

### TODO DBManager API


<a id="org2a253a2"></a>

### TODO WebSocket Manager API


<a id="orgd6ef665"></a>

### TODO Asynchronous Programming


<a id="org673be3a"></a>

## TODO Frontend - HTML - CSS - JavaScript Vanilla

La scelta di utilizzare JavaScript vanilla è stata fatta per implementare e
gestire in modo granulare le logiche sottostanti ai Framework moderni,
sviluppare Design Patterns e continuare a sviluppare skills "concrete".


<a id="orgaa42b18"></a>

### TODO Features

-   Asynchronous Programming
-   SoC - Separation of Concerns
-   Design Patterns:
    -   SSOT - Single Source of Truth
    -   Singletone
    -   Observer/Publish-Subscribe
-   DOM Manipulation
-   Browsers API
-   &#x2026;


<a id="org4cc43fc"></a>

# TODO Local Setup

-   Linux - MacOS - Windows
-   MySQL Server
-   Script Initializazion
-   Python Venv
-   VSC Note


<a id="org908a07a"></a>

# TODO Contact Info

-   **Email**: valeriodellamorte.info@gmail.com
-   **Linkedin**: <https://www.linkedin.com/in/valerio-della-morte>
