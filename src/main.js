import { createApp } from 'vue';
import App from './App.vue';
import router from "./router";
import 'bulma/css/bulma.css';
import naive from 'naive-ui';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faUser);

let app = createApp(App)
    .use(naive)
    .use(router)
    .component("font-awesome-icon", FontAwesomeIcon)

app.mount('#app');