import { createApp } from 'vue';
import App from './App.vue';
import router from "./router";
import 'bulma/css/bulma.css';
import naive from 'naive-ui';
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

let app = createApp(App)
    .use(naive)
    .use(router)
    .component("font-awesome-icon", FontAwesomeIcon)

app.mount('#app');