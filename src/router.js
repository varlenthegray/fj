import { createWebHistory, createRouter } from "vue-router";
import Login from "./components/user/Login.vue";
import Register from "./components/user/Register.vue";
import Home from "./components/Home.vue";
import Logout from "./components/user/Logout.vue";
import Index from "./components/Index.vue";
import Chapter from "./components/writing/create/Chapter.vue";
import Comic from "./components/writing/create/Comic.vue";
import Scrap from "./components/writing/create/Scrap.vue";
import Book from "./components/writing/create/Book.vue";
import Character from "./components/writing/create/Character.vue";

const history = createWebHistory();

const routes = [
  { path: "/", component: Index },
  { path: "/register", component: Register },
  { path: "/login", component: Login },
  { path: "/home", component: Home },
  { path: "/logout", component: Logout },
  { path: "/writing/create", component: Chapter },
  { path: "/writing/create/comic", component: Comic },
  { path: "/writing/create/scrap", component: Scrap },
  { path: "/writing/create/book", component: Book },
  { path: "/writing/create/character", component: Character },
];

const router = createRouter({ history, routes });
export default router;