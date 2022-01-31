import axios from "axios";
import Config from "../config";

const user = JSON.parse(localStorage.getItem('login'));
const initialState = user ? { status: { loggedIn: true }, user } : { status: { loggedIn: false }, user: null };
const API_URL = Config.API_URL;

export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    login({ commit }, user) {
      return axios({ method: 'POST', url: `${API_URL}/author/login`, data: new URLSearchParams(user)})
          .then(
              user => {
                const userData = user.data;
                localStorage.setItem('login', JSON.stringify(userData));
                commit('loginSuccess', userData);

                return Promise.resolve(user);
              },
              error => {
                commit('loginFailure');
                return Promise.reject(error);
              }
          );
    },
    logout({ commit }) {
      localStorage.clear();
      commit('logout');
    },
    register({ commit }, user) {
      return axios({
        method: 'POST',
        url: `${API_URL}/author/signup`,
        data: user
      }).then(
          response => {
            commit('registerSuccess');
            return Promise.resolve(response.data);
          },
          error => {
            commit('registerFailure');
            return Promise.reject(error);
          }
      );
    }
  },
  mutations: {
    loginSuccess(state, user) {
      state.status.loggedIn = true;
      state.user = user;
    },
    loginFailure(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    logout(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    registerSuccess(state) {
      state.status.loggedIn = false;
    },
    registerFailure(state) {
      state.status.loggedIn = false;
    }
  }
};