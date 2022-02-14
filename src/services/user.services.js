import axios from 'axios';
import authHeader from './auth-header';
import Config from "../config";

const API_URL = Config.API_URL;

class UserService {
  getUsername() {
    let loginKey = localStorage.getItem('login');

    if(loginKey) {
      const author = JSON.parse(localStorage.getItem('login')).author;

      if(author && author.pen_name) {
        return author.pen_name;
      } else if(author) {
        return author.username;
      } else {
        return '';
      }
    }
  }

  getPublicContent() {
    return axios.get(API_URL + 'all');
  }

  getUserBoard() {
    return axios.get(API_URL + 'user', { headers: authHeader() });
  }

  getModeratorBoard() {
    return axios.get(API_URL + 'mod', { headers: authHeader() });
  }

  getAdminBoard() {
    return axios.get(API_URL + 'admin', { headers: authHeader() });
  }
}

export default new UserService();