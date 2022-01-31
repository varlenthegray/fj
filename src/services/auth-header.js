export default function authHeader() {
  let user = JSON.parse(localStorage.getItem('login'));

  if(user['access_token']) {
    return { Authorization: `Bearer ${user['access_token']}` };
  } else {
    return {};
  }
}