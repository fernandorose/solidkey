import { createApp } from "vue";

import "@fontsource-variable/geist-mono/wght.css";
import "@fontsource-variable/roboto/wght.css";
import "./styles/globals.css";

import App from "./App.vue";
import router from "./router";

createApp(App).use(router).mount("#app");
