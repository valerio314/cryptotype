import { CONFIG } from './core/Config.js';
import { UIManager } from './services/UIManager.js';
import { WebSocketManager } from './services/WebSocketManager.js';

class CryptotypeApp {
    constructor() {
        this.init();
    }

    init() {
        try {
            const ws = new WebSocketManager(CONFIG.WS_URL);
            const iu = new UIManager();

            console.log('Cryptotype App initialized successfully');
            
        } catch (error) {
            console.error('Failed to initialize Cryptotype App:', error);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.cryptotypeApp = new CryptotypeApp();
});