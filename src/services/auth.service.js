import axios from "axios";

const API_URL = 'http://localhost:8000/api/v1';

class AuthService {
  login(user) {
    return axios
        .post(`${API_URL}/author/login`, new URLSearchParams(user))
        .then(response => {
          if(response.data.accessToken) {
            localStorage.setItem('user', JSON.stringify(response.data));
          }

          return response.data;
        });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
      console.log(user)

    return axios.post(`${API_URL}/author/signup`, {
      username: user.username,
      email: user.email_address,
      password: user.password
    });
  }
}

export default new AuthService();