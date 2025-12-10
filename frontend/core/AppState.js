import { eventBus } from "./EventBus.js";
import { CONFIG } from "./Config.js";
/**
 * AppState: implementa il pattern "Singletone" (gestione stato centralizzato)
 * - Implementa la logica dello stato globale dell'app
 * - Rende accessibile stato e metodi ai components
 */
class AppState {
    //Costruttore: inizializza lo stato
    constructor() {
        this.state = {
            selectedCoin: CONFIG.DEFAULT_TICKER,
            coinsList: null,
            coinsData: new Map(),
            userAuth: null,
            activeModal: null,
            userInfo: {
                "id": null,
                "username": null,
                "email": null
            },
            portfolio: {
                "id": null,
                "userId": null,
                "balance": 0.00
            },
            positions: []
        };
        // Richiama la funzione appena viene istanziata nell'export
        this.initEventListeners();
    }

    initEventListeners() {
        /**
         * Inizializzatore di eventi
         * - Iscrive funzioni a eventi specifici
         */
        eventBus.subscribe("message_from_ws", (data) => {
            this.handleWSMessages(data);
        });

        eventBus.subscribe("coin_selected", (selectedCoin) => {
            this.state.selectedCoin = selectedCoin;
        });
    }

    handleWSMessages(data) {
        /**
         * Gestore WS Messages
         * - Aggiorna lo stato di AppState
         * - Pubblica gli eventi e fornisce il nuovo stato
         */
        switch (data.type) {
            case "coins_list":
                /**
                 * Handle
                 * - Aggiorna l'attributo di classe "coinsList"
                 * - Attiva l'evento correlato e passa "coinsList" come parametro
                 */
                this.state.coinsList = data.payload;
                eventBus.publish("coins_list_received", this.state.coinsList);
                break;

            case "coin_data":
                /**
                 * Handle
                 * - Aggiorna l'attributo di classe "coinsData"
                 * - Attiva l'evento correlato e passa "coinsData" come parametro
                 */
                const ticker = Object.keys(data.payload)[0];
                this.state.coinsData.set(ticker, data.payload[ticker]);
                eventBus.publish("coin_data_realtime", this.state.coinsData);
                break;

            case "signup_error":
                /**
                 * Handle:
                 * 1) "code": "username_exists"
                 * 2) "code": "email_exists"
                 */
                this.handleSignupErrors(data.code);
                break;

            case "login_error":
                /**
                 * Hanlde
                 * 1) "code": "email_exists"
                 * 2) "code": wrong_password"
                 */
                this.handleLoginErrors(data.code);
                break;

            case "signup_successful":
                /**
                 * Handle
                 * - Invia info a UI Manager: Show Signup Success Message in Sginup Modal in messages section
                 */
                break;

            case "login_successful":
                /**
                 * Handle
                 * - Close Login Modal: this.state.activeModal set null
                 * - Invia info a UI Manager:
                 * 1) Auth Section add --hide
                 * 2) Account Section remove --hide
                 * 3) Update User Data in Account Section
                 * 4) Update Portfolio con User Data (net positions - balance - equity - positions list)
                 * 5) Order Btns change da signup/login to buy/sell
                 */
                break;

            case "deposit_error_id_mismatch":
                /**
                 * Handle
                 * - Invia a UI Manager: Show message error in account modal nella sezione messages
                 */
                break;

            case "deposit_successful":
                /**
                 * Handle
                 * - Payload = balanceUpdated
                 */
                break;

            case "withdraw_error_id_mismatch":
                // Handle
                break;

            case "withdraw_successful":
                /**
                 * Handle
                 * - Payload = balanceUpdated
                 */
                break;

            case "order_executed":
                // Handle
                break;

            case "close_position_error_id_mismatch":
                // Handle
                break;

            case "position_closed":
                // Handle
                break;
        }
    }

    /* METHODS */
    // Data Access
    getUser() { return this.state.user; }

    getPortfolio() { return this.state.portfolio; }

    getSelectedCoin() { return this.state.selectedCoin; }

    getCoinData(ticker) { return this.state.coinsData.get(ticker); }

    // Data Update
    setUser(userData) { this.state.user = userData; }

    updateBalance(newBalance) { this.state.portfolio.balance = newBalance; }

    updateCoinsData(coinData) {
        const ticker = Object.keys(coinData)[0];
        this.state.coinsData.set(ticker, coinData[ticker]);
    }
}

/**
 * Export appState
 * - L'istruzione istanzia per la prima ed unica volta "AppState"
 * - I moduli che importano { appState } from '...' importeranno l'istanza creata
 * - appState risulta quindi come un oggetto globale
 */
export const appState = new AppState();