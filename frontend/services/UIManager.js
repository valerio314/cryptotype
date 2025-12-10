import { eventBus } from '../core/EventBus.js';
import { appState } from '../core/AppState.js';

export class UIManager {
    constructor() {
        // Components
        this.signupModal = document.getElementById("signup-modal");
        this.loginModal = document.getElementById("login-modal");
        this.accountModal = document.getElementById("account-modal");
        this.userSection = document.querySelector(".header__user-section");
        this.coinSelectedContainer = {
            "logoElement": document.getElementById("coin-selected-logo"),
            "tickerElement": document.getElementById("coin-selected-ticker"),
            "priceElement": document.getElementById("coin-selected-price"),
            "chg24hElement": document.getElementById("coin-selected-chg24h"),
            "vol24hElement": document.getElementById("coin-selected-vol24h"),
            "vol24hTHElement": document.getElementById("coin-selected-th-vol24h")
        };

        this.orderSection = document.querySelector(".header__create-order");
        this.coinsTableContainer = {
            "srcInputElement": document.getElementById("search-coins"),
            "tbodyElement": document.getElementById("coins-table-items")
        }
        this.chartContainer = document.getElementById("chart");
        this.portfolio = document.querySelector(".main-right__portfolio");

        // Init
        this.initEventListeners();
    }

    initEventListeners() {
        eventBus.subscribe("coins_list_received", (coinsList) => {
            this.initDefaultUI(coinsList);
        });

        eventBus.subscribe("coin_data_realtime", (coinsData) => {
            this.updateCoinsListData(coinsData);
        });

        eventBus.subscribe("coin_selected", (coinSelected) => {
            this.updateCoinSelected(coinSelected);
        });

        eventBus.subscribe("coin_data_realtime", (coinsData) => {
            this.updateCoinSelectedData(coinsData);
        });

        eventBus.subscribe("coin_selected", (coinSelected) => {
            this.updateCoinChart(coinSelected);
        })

        eventBus.subscribe("coin_selected", () => {
            this.resetOrderBtnsValue();
        });

        eventBus.subscribe("coin_data_realtime", (coinData) => {
            this.updateOrderBtns(coinData);
        });
    }

    initDefaultUI(coinsList) {
        // Chart
        this.chartContainer.innerHTML = "";
        new TradingView.widget({
            "container_id": "chart",
            "symbol": `BINANCE:${appState.getSelectedCoin()}`,
            "allow_symbol_change": true,
            "calendar": false,
            "details": false,
            "hide_side_toolbar": false,
            "hide_top_toolbar": false,
            "hide_legend": false,
            "hide_volume": false,
            "hotlist": false,
            "interval": "D",
            "locale": "en",
            "save_image": true,
            "style": "1",
            "theme": "dark",
            "timezone": "Europe/Zurich",
            "backgroundColor": "#0F0F0F",
            "gridColor": "rgba(242, 242, 242, 0.06)",
            "withdateranges": false,
            "autosize": true
        });

        // Coin Selected
        this.coinSelectedContainer.logoElement.src = `assets/img/${appState.getSelectedCoin().replace("USDT", "").toLowerCase()}.png`;
        this.coinSelectedContainer.logoElement.alt = `${appState.getSelectedCoin().replace("USDT", "").toUpperCase()} Logo`;
        this.coinSelectedContainer.tickerElement.textContent = appState.getSelectedCoin();
        this.coinSelectedContainer.vol24hTHElement.textContent = `24 Vol (${appState.getSelectedCoin().replace("USDT", "").toUpperCase()})`;

        // Coins List
        this.coinsTableContainer.tbodyElement.innerHTML = '';
        coinsList.forEach(ticker => {
            const row = document.createElement('tr');
            row.setAttribute("id", `table-item-${ticker.toUpperCase()}`);
            row.innerHTML = `
                <td class="table-item__logo"><img src="assets/img/${ticker.replace("usdt", "").toLowerCase()}.png" alt="${ticker}"></td>
                <td class="table-item__ticker">${ticker.toUpperCase()}</td>
                <td class="table-item__price">-</td>
                <td class="table-item__change24h">-</td>
            `;
            
            row.addEventListener("click", () => {
                eventBus.publish('coin_selected', ticker.toUpperCase())
            });
            
            this.coinsTableContainer.tbodyElement.appendChild(row);
        });

        // Search Input Coins List
        this.coinsTableContainer.srcInputElement.oninput = (e) => {
            const inputValue = e.target.value.toUpperCase();
            const rows = this.coinsTableContainer.tbodyElement.querySelectorAll("tr");

            rows.forEach(row => {
                // Prendi bene il ticker
                const coinTicker = row.querySelector(".table-item__ticker").textContent;
                row.style.display = coinTicker.includes(inputValue) ? "" : "none";
            });
        }
    }

    updateCoinsListData(coinsData) {
        for (let [ticker, coinData] of coinsData) {
            // Aggiorna riga nella lista
            const row = document.getElementById(`table-item-${ticker}`);
            if (row) {
                const priceCell = row.querySelector(".table-item__price");
                const chg24hCell = row.querySelector(".table-item__change24h");
                
                if (priceCell) priceCell.textContent = `$${coinData.price}`;
                if (chg24hCell) {
                    const change = parseFloat(coinData.change_24h);
                    chg24hCell.textContent = `${change >= 0 ? '+' : ''}${coinData.change_24h}%`;
                    chg24hCell.className = `table-item__change24h ${change >= 0 ? '--green' : '--red'}`;
                }
            }
        }
    }

    updateCoinSelected(coinSelected) {
        this.coinSelectedContainer.logoElement.src = `assets/img/${appState.getSelectedCoin().replace("USDT", "").toLowerCase()}.png`;
        this.coinSelectedContainer.logoElement.alt = `${appState.getSelectedCoin().replace("USDT", "").toUpperCase()} Logo`;
        this.coinSelectedContainer.tickerElement.textContent = appState.getSelectedCoin();
        this.coinSelectedContainer.vol24hTHElement.textContent = `24h Vol (${appState.getSelectedCoin().replace("USDT", "")})`;
    }

    updateCoinSelectedData(coinsData) {
        for (let [ticker, coinData] of coinsData) {
            // Aggiorna Coin Data Selected
            if (appState.getSelectedCoin() == ticker) {
                const change24h = coinData.change_24h;
                this.coinSelectedContainer.priceElement.textContent = "$" + coinData.price;
                this.coinSelectedContainer.chg24hElement.textContent = `${change24h >= 0 ? "+" : ""}${change24h}%`;
                this.coinSelectedContainer.vol24hElement.textContent = coinData.volume_24h;
                this.coinSelectedContainer.chg24hElement.className = `${parseFloat(coinData.change_24h) >= 0 ? "--green" : "--red"}`;
            }
        }
    }

    updateCoinChart(coinSelected) {
        this.chartContainer.innerHTML = "";
        new TradingView.widget({
            "container_id": "chart",
            "symbol": `BINANCE:${appState.getSelectedCoin()}`,
            "allow_symbol_change": true,
            "calendar": false,
            "details": false,
            "hide_side_toolbar": false,
            "hide_top_toolbar": false,
            "hide_legend": false,
            "hide_volume": false,
            "hotlist": false,
            "interval": "D",
            "locale": "en",
            "save_image": true,
            "style": "1",
            "theme": "dark",
            "timezone": "Europe/Zurich",
            "backgroundColor": "#0F0F0F",
            "gridColor": "rgba(242, 242, 242, 0.06)",
            "withdateranges": false,
            "autosize": true
        });
    }

    resetOrderBtnsValue() {
        document.getElementById("order-size-usd").value = "";
        document.getElementById("order-size-base-unit").value = "";
    }

    updateOrderBtns(coinDataReceived) {
        const coinData = coinDataReceived.get(appState.getSelectedCoin());

        if (!coinData) return;
        const inputUSDAmount = document.getElementById("order-size-usd");
        const inputBUAmount = document.getElementById("order-size-base-unit");

        inputUSDAmount.placeholder = `USD | Min $${coinData.min_notional}`;
        inputBUAmount.placeholder = `${appState.getSelectedCoin().replace("USDT", "")} | Min ${coinData.min_size}`;

        inputUSDAmount.addEventListener("input", (e) => {
            let value = e.target.value;
            value = value.replace(/[^\d]/g, "");

            if (value == "") {
                e.target.value = "";
                inputBUAmount.value = "";
                return;
            }

            if (Number(value) < Number(coinData.min_notional)) {
                value = value.replace(value, String(coinData.min_notional));
            }
            e.target.value = value;

            const baseUnit = Number(value) / Number(coinData.price);
            inputBUAmount.value = baseUnit.toFixed(6);
        });
    }

    
}