<template>
  <div class="container">
    <h1 class="title is-1">Login to Play</h1>

    <Form :validation-schema="schema" method="post" @submit="handleLogin">
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left">
          <Field name="username" class="input" placeholder="Username" />
          <span class="icon is-small is-left"><font-awesome-icon icon="user" /></span>
        </div>

        <ErrorMessage name="username" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left">
          <Field name="password" type="password" class="input" placeholder="Password" />
          <span class="icon is-small is-left"><font-awesome-icon icon="lock" /></span>
        </div>

        <ErrorMessage name="password" class="help is-danger" />
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link" type="submit">Log In</button>
        </div>
        <div class="control">
          <button class="button is-link is-light" type="button" @click="$router.push('/register')">Register</button>
        </div>
      </div>
    </Form>
  </div>
</template>

<script>
import { Field, Form, ErrorMessage } from 'vee-validate';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";
import * as yup from "yup";
import { useMessage } from "naive-ui";

library.add(faUser, faLock);

export default {
  components: { Field, Form, ErrorMessage },
  data() {
    const schema = yup.object({
      username: yup.string()
          .required('Please enter your username.')
          .min(3, 'Username must be at least 3 characters long'),
      password: yup.string()
          .required('Please enter your password.')
          .min(3, 'Password must be at least 3 characters long.')
    })

    return { schema }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if(this.loggedIn) {
      this.$router.push("/home");
    }
  },
  setup() { window.$message = useMessage() },
  methods: {
    handleLogin(user) {
      this.$store.dispatch("auth/login", user)
          .then(
              () => {
                window.$message.success('Logged in successfully.');
                this.$router.push("/home");
              },
              (error) => {
                window.$message.error('Unable to log in, please try again.');
              }
          );
    },
  },
}
</script>

<style scoped>

</style>