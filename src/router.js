import { createWebHistory, createRouter } from "vue-router";
import Login from "./components/user/Login.vue";
import Register from "./components/user/Register.vue";
import Home from "./components/Home.vue";
import Logout from "./components/user/Logout.vue";
import Index from "./components/Index.vue";

const history = createWebHistory();

const routes = [
  { path: "/", component: Index },
  { path: "/register", component: Register },
  { path: "/login", component: Login },
  { path: "/home", component: Home },
  { path: "/logout", component: Logout },
];

const router = createRouter({ history, routes });
export default router;