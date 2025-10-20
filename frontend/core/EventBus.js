/* MEDIATOR PATTERN */
class EventBus {
    constructor() {
        this.events = new Map();
        /**
         * events: Map Object, implementa il pattern Observe (pubblicazione/sottoscrizione):
         *   1) Tiene traccia degli eventi
         *   2) Ogni evento avra' delle funzioni correlate
         *   3) Quando un evento viene triggerato, dovranno essere chiamate le funzioni correlate
         */
    }

    subscribe(event, callback) {
        /**
         * Subscribe: iscrive la funzione all'evento corrispondente
         * - Riceve evento e funzione
         * - Se l'evento e' presente in "listeners" { iscrivi la funzione all'evento }
         * - Se l'evento non esiste { crea evento e iscrivi la funzione }
         */
        if (!this.events.has(event)) {
            this.events.set(event, new Set());
        }
        this.events.get(event).add(callback);
    }

    unsubscribe(event, callback) {
        // Disiscrizione
        if (this.events.has(event)) {
            this.events.get(event).delete(callback);
        }
    }

    publish(event, data) {
        /**
         * Publisher: funzione di "notifica"
         * - Riceve l'evento triggerato
         * - Receve il nuovo stato
         * - Richiama le funzioni registrate all'evento e invia il nuovo stato
         * - Le funzioni si occuperanno di modificare i propri componenti
         */
        if (this.events.has(event)) {
            this.events.get(event).forEach(callback => callback(data));
        }
    }
}

export const eventBus = new EventBus();