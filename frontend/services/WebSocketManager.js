import { eventBus } from '../core/EventBus.js';

export class WebSocketManager {

    constructor(url) {
        this.url = url;
        this.websocket = null;
        
        this.connect();
        this.initEventListener();
    }

    connect() {
        try {
            this.websocket = new WebSocket(this.url);
            this.eventHandler();
        } catch (error) {
            console.error(`WebSocket connection failed: ${error}`);
        }
    }

    eventHandler() {
        this.websocket.onopen = () => {
            console.log(`WebSocket Connected to [${this.url}]`);
        };

        this.websocket.onmessage = (event) => {
            try {
                const data = JSON.parse(event.data);
                eventBus.publish("message_from_ws", data);
            } catch (error) {
                console.error(`Error parsing WebSocket message: ${error}`);
            }
        };

        this.websocket.onclose = (event) => {
            console.log(`WebSocket connection closed: ${event.code}, ${event.reason}`);
        };

        this.websocket.onerror = (error) => {
            console.error(`WebSocket error: ${error}`);
        };
    }

    initEventListener() {
        eventBus.subscribe("ws_send_message", (message) => {
            this.send(message);
        });
    }

    send(message) {
        try {
            this.websocket.send(JSON.stringify(message));
            console.log("WebSocket Send Message Successful");
        } catch (error) {
            console.error(`Error sending WebSocket message: ${error}`);
        }
    }
}