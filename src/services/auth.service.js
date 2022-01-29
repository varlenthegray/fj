import axios from "axios";

const API_URL = 'http://localhost:8000/api/v1';

class AuthService {
  login(user) {
    // TODO: Find a way to send data properly
    axios({
      method: 'POST',
      url: `${API_URL}/author/login_temp`,
      data: {
        email_address: 'bbeach@innovated.tech',
        username: 'Hithere'
      }
    })

    // console.log(axios.post(`${API_URL}/author/login_temp`, {email_address: 'bbeach@innovated.tech', password: 'Yellow'}));


    /*return fetch(`${API_URL}/author/login`, {
      method: 'POST',
      headers: { "Content-type": "application/json; charset=UTF-8" },
      body: JSON.stringify(user)
    }).then(response => {
      if(response.data.accessToken) {
        localStorage.setItem('user', JSON.stringify(response.data));
      }

      return response.data;
    })*/

    /*$.ajax({
      url: `${API_URL}/author/login`,
      data: user,
      method: 'POST'
    }).done(function(data) {
      if(data !== undefined) {
        localStorage.setItem('user', JSON.stringify(data));
        return data;
      }
    });

    return null;*/


    /*const kyLogin = ky.create({
      prefixUrl: `${API_URL}/author/login`,
      hooks: {
        afterResponse: [
          res => {
            console.log(res);
          }
        ]
      }
    });

    return kyLogin.get(user)*/


    /*return axios
        .post(API_URL + 'login', new URLSearchParams(user))
        .then(response => {
          if(response.data.accessToken) {
            localStorage.setItem('user', JSON.stringify(response.data));
          }

          return response.data;
        });*/
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    // TODO: Fix this so it relies on KY
    return axios.post(API_URL + 'signup', new URLSearchParams({
      username: user.username,
      email: user.email_address,
      password: user.password
    }));
  }
}

export default new AuthService();