<template>
  <div class="container">
    <h1 class="title is-1">Register an Account</h1>

    <Form :validation-schema="schema">
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left">
          <Field name="username" class="input" placeholder="Username" />
          <span class="icon is-small is-left"><font-awesome-icon icon="user" /></span>
        </div>

        <ErrorMessage name="username" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Email Address</label>
        <div class="control has-icons-left">
          <Field name="email_address" class="input" placeholder="Email Address" />
          <span class="icon is-small is-left"><font-awesome-icon icon="envelope" /></span>
        </div>

        <ErrorMessage name="email_address" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left">
          <Field name="password" type="password" class="input" placeholder="Password" />
          <span class="icon is-small is-left"><font-awesome-icon icon="lock" /></span>
        </div>

        <ErrorMessage name="password" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Re-enter Password</label>
        <div class="control has-icons-left">
          <Field name="password2" type="password" class="input" placeholder="Re-type Password" />
          <span class="icon is-small is-left"><font-awesome-icon icon="lock" /></span>
        </div>

        <ErrorMessage name="password2" class="help is-danger" />
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link" type="submit">Register</button>
        </div>
        <div class="control">
          <button class="button is-link is-light" @click="$router.push('/')">Back to Login</button>
        </div>
      </div>
    </Form>
  </div>
</template>

<script>
import { Field, Form, ErrorMessage } from 'vee-validate';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faEnvelope, faLock } from "@fortawesome/free-solid-svg-icons";
import * as yup from 'yup';

library.add(faUser, faEnvelope, faLock);

export default {
  components: { Field, Form, ErrorMessage },
  data() {
    const schema = yup.object({
      username: yup.string()
          .required('Please enter a username.')
          .min(3, 'Username must be at least 3 characters long'),
      password: yup.string()
          .required('Please enter a password.')
          .min(3, 'Password must be at least 3 characters long.'),
      password2: yup.string()
          .required('Please re-enter your password.')
          .oneOf([yup.ref('password'), null], 'Passwords must match.'),
      email_address: yup.string()
          .email('Please enter a valid email address.')
          .required('Email address is required.')
    })

    return { schema }
  },
}
</script>

<style scoped>

</style>