/* CONFIGURATON */
export const CONFIG = {
    // WebSocket
    WS_URL: "ws://localhost:8000",
    
    // Market Data
    DEFAULT_TICKER: "BTCUSDT",
    
    // TradingView
    TRADINGVIEW_CONFIG: {
        interval: "15",
        timezone: "Europe/Rome",
        theme: "dark",
        style: "1",
        locale: "en"
    }

    /**
     * EVENTS: {
     *      eventBus.publish("message_from_ws", data);
     *      eventBus.subscribe("ws_send_message", (message) => { this.send(message); });
     * 
     *      eventBus.publish("coins_list_received", this.state.coinsList);
     *      eventBus.publish("coin_data_realtime", this.state.coinsData);
     * 
     *      return {"type": "signup_error", "code": "username_exists"}
     *      return {"type": "signup_error", "code": "email_exists"}
     *      return {"type": "signup_successful"}
     * 
     *      return {"type": "login_error", "code": "email_exists"}
     *      return {"type": "login_error", "code": "wrond_password"}
     *      return {"type": "login_successful", "payload": {user_data}}
     * 
     *      return {"type": "deposit_error_id_mismatch"}
     *      return {"type": "deposit_successful", "payload": {balanceUpdated}}
     * 
     *      return {"type": "withdraw_error_id_mismatch"}
     *      return {"type": "withdraw_successful", "payload": {balanceUpdated}}
     * 
     *      return {"type": "order_executed"}
     *      return {"type": "close_position_error_id_mismatch"}
     *      return {"type": "positon_closed"}
     * }
     */
};