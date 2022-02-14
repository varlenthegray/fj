import { createWebHistory, createRouter } from "vue-router";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import Home from "./components/Home.vue";
import Logout from "./components/Logout.vue";

const history = createWebHistory();

const routes = [
  { path: "/", component: Login },
  { path: "/register", component: Register },
  { path: "/login", component: Login },
  { path: "/home", component: Home },
  { path: "/logout", component: Logout },
];

const router = createRouter({ history, routes });
export default router;