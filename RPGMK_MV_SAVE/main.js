// ==UserScript==
// @name         RPGMaker MV Saver
// @version      0.1
// @description  雲存儲RPGMaker MV 游戲存檔
// @source       https://github.com/IaSoC/Meaningful
// @match        *
// @icon         https://www.google.com/s2/favicons?sz=64&domain=elementfx.com
// @require      https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js
// @grant GM_log
// @grant GM_xmlhttpRequest
// @grant GM_setValue
// @grant GM_getValue
// ==/UserScript==

(function() {
    'use strict';
    
    var ServerUrl = 'https://rpgmvsave.lilynet.work';


    if (GM_getValue('Github_token',null) === null){
        //跳轉登入
        window.open(ServerUrl);
    }else{

    }


    /*
    * OverWrite:
    * StorageManager.removeWebStorage
    * StorageManager.webStorageExists
    * StorageManager.webStorageBackupExists
    * StorageManager.loadFromWebStorageBackup
    * StorageManager.loadFromWebStorage
    * StorageManager.saveToWebStorage
    */

    StorageManager.saveToWebStorage = function(savefileId, json) {
        var key = this.webStorageKey(savefileId);
        var data = LZString.compressToBase64(json);
        localStorage.setItem(key, data);
    };
    
    StorageManager.loadFromWebStorage = function(savefileId) {
        var key = this.webStorageKey(savefileId);
        var data = localStorage.getItem(key);
        return LZString.decompressFromBase64(data);
    };
    
    StorageManager.loadFromWebStorageBackup = function(savefileId) {
        var key = this.webStorageKey(savefileId) + "bak";
        var data = localStorage.getItem(key);
        return LZString.decompressFromBase64(data);
    };
    
    StorageManager.webStorageBackupExists = function(savefileId) {
        var key = this.webStorageKey(savefileId) + "bak";
        return !!localStorage.getItem(key);
    };
    
    StorageManager.webStorageExists = function(savefileId) {
        var key = this.webStorageKey(savefileId);
        return !!localStorage.getItem(key);
    };
    
    StorageManager.removeWebStorage = function(savefileId) {
        var key = this.webStorageKey(savefileId);
        localStorage.removeItem(key);
    };

})();