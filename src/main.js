import { createApp } from 'vue';
import App from './App.vue';
import router from "./router";
import 'bulma/css/bulma.css';
import naive from 'naive-ui';
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import store from './store';

let app = createApp(App)
    .use(naive)
    .use(router)
    .use(store)
    .component("font-awesome-icon", FontAwesomeIcon)

app.mount('#app');