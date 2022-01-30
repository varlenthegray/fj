import axios from "axios";

const API_URL = 'http://localhost:8000/api/v1';

class AuthService {
    login(user) {
        return axios({
            method: 'POST',
            url: `${API_URL}/author/login`,
            data: new URLSearchParams(user)
        }).then(response => {
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
        return axios({
            method: 'POST',
            url: `${API_URL}/author/signup`,
            data: user
        });
    }
}

export default new AuthService();