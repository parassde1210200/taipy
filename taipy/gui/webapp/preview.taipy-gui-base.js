!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define([],e):"object"==typeof exports?exports.TaipyGuiBase=e():t.TaipyGuiBase=e()}(this,(()=>(()=>{"use strict";var t,e={8380:(t,e,n)=>{n.r(e),n.d(e,{TaipyApp:()=>u,createApp:()=>p,default:()=>g});var a=n(3829);const s="TaipyClientId",i=new Worker(new URL(n.p+n.u(677),n.b));var o=n(7115),r=n(5364),d=n.n(r);class c{constructor(t){this._data={},this._init_data={},this.init(t)}init(t){const e={};for(const n in this._init_data)if(n in t)for(const a in this._init_data[n])a in t[n]||(n in e||(e[n]={}),e[n][a]=this._init_data[n][a]);else e[n]=this._init_data[n];0!==Object.keys(e).length&&console.error("Unmatched data tree! Removed changes: ",e),this._init_data=t,this._data={};for(const t in this._init_data)for(const e in this._init_data[t]){const n=this._init_data[t][e];this._data[n.encoded_name]=n.value}return e}getEncodedName(t,e){if(e in this._init_data&&t in this._init_data[e])return this._init_data[e][t].encoded_name}getName(t){for(const e in this._init_data)for(const n in this._init_data[e])if(this._init_data[e][n].encoded_name===t)return[n,e]}get(t){if(!(t in this._data))throw new Error(`${t} is not available in Taipy Gui`);return this._data[t]}getInfo(t){for(const e in this._init_data)for(const n in this._init_data[e]){const a=this._init_data[e][n];if(a.encoded_name===t)return Object.assign(Object.assign({},a),{value:this._data[t]})}}getDataTree(){return this._init_data}getAllData(){return this._data}update(t,e){if(!(t in this._data))throw new Error(`${t} is not available in Taipy Gui`);this._data[t]=e}}class h{}class l extends h{constructor(){super(),this.supportedMessageTypes=["MU","ID","GMC","GDT","AID","GR","AL","ACK"],this.initWsMessageTypes=["ID","AID","GMC"]}handleWsMessage(t,e){var n;if(t.type){if("MU"===t.type&&Array.isArray(t.payload))for(const a of t.payload){const t=a.name,{value:s}=a.payload;null===(n=e.variableData)||void 0===n||n.update(t,s),e.onChangeEvent(t,s)}else if("ID"===t.type){const{id:n}=t;(t=>{localStorage&&localStorage.setItem(s,t)})(n),e.clientId=n,e.updateContext(e.path)}else if("GMC"===t.type){const n=t.payload;if(e.context=n.context,null==n?void 0:n.metadata)try{e.metadata=JSON.parse(n.metadata||"{}")}catch(t){console.error("Error parsing metadata from Taipy Designer",t)}}else if("GDT"===t.type){const n=t.payload,a=n.variable,s=n.function;if(e.variableData&&e.functionData){const t=e.variableData.init(a),n=e.functionData.init(s),i=d()(t,n);(t||n)&&e.onReloadEvent(i)}else e.variableData=new c(a),e.functionData=new c(s),e.onInitEvent()}else if("AID"===t.type){const n=t.payload;if("reconnect"===n.name)return e.init(),!0;e.appId=n.id}else if("GR"===t.type){const n=t.payload;e.routes=n}else if("AL"===t.type){const n=t;e.onNotifyEvent(n.atype,n.message)}else if("ACK"===t.type){const{id:n}=t;e._ackList=e._ackList.filter((t=>t!==n)),e.onWsStatusUpdateEvent(e._ackList)}return this.postWsMessageProcessing(t,e),!0}return!1}postWsMessageProcessing(t,e){this.initWsMessageTypes.includes(t.type)&&""!==e.clientId&&""!==e.appId&&""!==e.context&&void 0!==e.routes&&e.sendWsMessage("GDT","get_data_tree",{})}}class u{constructor(t=void 0,e=void 0,n=void 0,a=void 0){a=a||(0,o.io)("/",{autoConnect:!1,path:`${this.getBaseUrl()}socket.io`}),this.onInit=t,this.onChange=e,this.variableData=void 0,this.functionData=void 0,this.clientId="",this.context="",this.metadata={},this.appId="",this.routes=void 0,this.path=n,this.socket=a,this.wsAdapters=[new l],this._ackList=[],((t,e)=>{t.on("connect",(()=>{e.onWsMessageEvent("connect",null),""!==e.clientId&&""!==e.appId||e.init()})),t.io.on("reconnect",(()=>{e.onWsMessageEvent("reconnect",null),console.log("WebSocket reconnected"),e.sendWsMessage("AID","reconnect",e.appId)})),t.on("connect_error",(n=>{e.onWsMessageEvent("connect_error",{err:n}),console.log("Error connecting WebSocket: ",n),setTimeout((()=>{t&&t.connect()}),500)})),t.on("disconnect",((n,a)=>{e.onWsMessageEvent("disconnect",{reason:n,details:a}),console.log("WebSocket disconnected due to: ",n,a),"io server disconnect"===n&&t&&t.connect()})),t.on("message",(t=>{e.onWsMessageEvent("message",t);for(const n of e.wsAdapters)if(n.supportedMessageTypes.includes(t.type)&&n.handleWsMessage(t,e))return})),t.connected||t.connect()})(a,this)}get onInit(){return this._onInit}set onInit(t){if(void 0!==t&&1!==t.length)throw new Error("onInit() requires one parameter");this._onInit=t}onInitEvent(){this.onInit&&this.onInit(this)}get onChange(){return this._onChange}set onChange(t){if(void 0!==t&&3!==t.length)throw new Error("onChange() requires three parameters");this._onChange=t}onChangeEvent(t,e){this.onChange&&this.onChange(this,t,e)}get onNotify(){return this._onNotify}set onNotify(t){if(void 0!==t&&3!==t.length)throw new Error("onNotify() requires three parameters");this._onNotify=t}onNotifyEvent(t,e){this.onNotify&&this.onNotify(this,t,e)}get onReload(){return this._onReload}set onReload(t){if(void 0!==t&&2!==(null==t?void 0:t.length))throw new Error("onReload() requires two parameters");this._onReload=t}onReloadEvent(t){this.onReload&&this.onReload(this,t)}get onWsMessage(){return this._onWsMessage}set onWsMessage(t){if(void 0!==t&&3!==(null==t?void 0:t.length))throw new Error("onWsMessage() requires three parameters");this._onWsMessage=t}onWsMessageEvent(t,e){this.onWsMessage&&this.onWsMessage(this,t,e)}get onWsStatusUpdate(){return this._onWsStatusUpdate}set onWsStatusUpdate(t){if(void 0!==t&&2!==(null==t?void 0:t.length))throw new Error("onWsStatusUpdate() requires two parameters");this._onWsStatusUpdate=t}onWsStatusUpdateEvent(t){this.onWsStatusUpdate&&this.onWsStatusUpdate(this,t)}init(){this.clientId="",this.context="",this.appId="",this.routes=void 0;const t=(t=>{const e=localStorage&&localStorage.getItem(t);return e||""})(s);this.sendWsMessage("ID",s,t),this.sendWsMessage("AID","connect",""),this.sendWsMessage("GR","",""),""!==t&&(this.clientId=t,this.updateContext(this.path))}sendWsMessage(t,e,n,s=void 0){void 0===s&&(s=this.context);const i=((t,e,n,s,i,o="",r=!0,d)=>{const c=(0,a.A)(),h={type:e,name:n,payload:s,propagate:r,client_id:i,ack_id:c,module_context:o};return null==t||t.emit("message",(t=>Object.keys(t||{}).reduce(((e,n)=>(void 0!==t[n]&&(e[n]=t[n]),e)),{}))(h),d),c})(this.socket,t,e,n,this.clientId,s);i&&(this._ackList.push(i),this.onWsStatusUpdateEvent(this._ackList))}registerWsAdapter(t){this.wsAdapters.unshift(t)}getEncodedName(t,e){var n;return null===(n=this.variableData)||void 0===n?void 0:n.getEncodedName(t,e)}getName(t){var e;return null===(e=this.variableData)||void 0===e?void 0:e.getName(t)}get(t){var e;return null===(e=this.variableData)||void 0===e?void 0:e.get(t)}getInfo(t){var e;return null===(e=this.variableData)||void 0===e?void 0:e.getInfo(t)}getDataTree(){var t;return null===(t=this.variableData)||void 0===t?void 0:t.getDataTree()}getAllData(){var t;return null===(t=this.variableData)||void 0===t?void 0:t.getAllData()}getFunctionList(){var t;const e=null===(t=this.functionData)||void 0===t?void 0:t.getDataTree()[this.context];return Object.keys(e||{})}getRoutes(){return this.routes}update(t,e){this.sendWsMessage("U",t,{value:e})}getContext(){return this.context}updateContext(t=""){t&&""!==t||(t=window.location.pathname.replace(this.getBaseUrl(),"")||"/"),this.sendWsMessage("GMC","get_module_context",{path:t||"/"})}trigger(t,e,n={}){n.action=t,this.sendWsMessage("A",e,n)}upload(t,e,n){return((t,e,n,a,s,o,r,d="/taipy-uploads")=>new Promise(((c,h)=>{i.onmessage=t=>{t.data.error?h(t.data.message):t.data.done?c(t.data.message):o(t.data.progress)},i.onerror=t=>h(t),i.postMessage({files:s,uploadUrl:d,varName:t,context:e,onAction:n,uploadData:a,id:r})})))(t,void 0,void 0,void 0,e,n,this.clientId)}getPageMetadata(){return this.metadata}getWsStatus(){return this._ackList}getBaseUrl(){return document.getElementsByTagName("base")[0].getAttribute("href")||"/"}}const p=(t,e,n,a)=>new u(t,e,n,a),g=u}},n={};function a(t){var s=n[t];if(void 0!==s)return s.exports;var i=n[t]={id:t,loaded:!1,exports:{}};return e[t](i,i.exports,a),i.loaded=!0,i.exports}a.m=e,t=[],a.O=(e,n,s,i)=>{if(!n){var o=1/0;for(h=0;h<t.length;h++){for(var[n,s,i]=t[h],r=!0,d=0;d<n.length;d++)(!1&i||o>=i)&&Object.keys(a.O).every((t=>a.O[t](n[d])))?n.splice(d--,1):(r=!1,i<o&&(o=i));if(r){t.splice(h--,1);var c=s();void 0!==c&&(e=c)}}return e}i=i||0;for(var h=t.length;h>0&&t[h-1][2]>i;h--)t[h]=t[h-1];t[h]=[n,s,i]},a.n=t=>{var e=t&&t.__esModule?()=>t.default:()=>t;return a.d(e,{a:e}),e},a.d=(t,e)=>{for(var n in e)a.o(e,n)&&!a.o(t,n)&&Object.defineProperty(t,n,{enumerable:!0,get:e[n]})},a.u=t=>t+".taipy-gui-base.js",a.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"==typeof window)return window}}(),a.o=(t,e)=>Object.prototype.hasOwnProperty.call(t,e),a.r=t=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},a.nmd=t=>(t.paths=[],t.children||(t.children=[]),t),(()=>{var t;a.g.importScripts&&(t=a.g.location+"");var e=a.g.document;if(!t&&e&&(e.currentScript&&"SCRIPT"===e.currentScript.tagName.toUpperCase()&&(t=e.currentScript.src),!t)){var n=e.getElementsByTagName("script");if(n.length)for(var s=n.length-1;s>-1&&(!t||!/^http(s?):/.test(t));)t=n[s--].src}if(!t)throw new Error("Automatic publicPath is not supported in this browser");t=t.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),a.p=t})(),(()=>{a.b=document.baseURI||self.location.href;var t={685:0};a.O.j=e=>0===t[e];var e=(e,n)=>{var s,i,[o,r,d]=n,c=0;if(o.some((e=>0!==t[e]))){for(s in r)a.o(r,s)&&(a.m[s]=r[s]);if(d)var h=d(a)}for(e&&e(n);c<o.length;c++)i=o[c],a.o(t,i)&&t[i]&&t[i][0](),t[i]=0;return a.O(h)},n=this.webpackChunkTaipyGuiBase=this.webpackChunkTaipyGuiBase||[];n.forEach(e.bind(null,0)),n.push=e.bind(null,n.push.bind(n))})();var s=a.O(void 0,[804],(()=>a(8380)));return a.O(s)})()));