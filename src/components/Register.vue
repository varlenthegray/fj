<template>
  <div class="container">
    <Form>
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left">
          <Field name="username" class="input" :rules="ruleUsername" placeholder="Username" />
          <span class="icon is-small is-left"><font-awesome-icon icon="user" /></span>
        </div>

        <ErrorMessage name="username" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Email Address</label>
        <div class="control has-icons-left">
          <Field name="email_address" class="input" :rules="ruleEmail_address" placeholder="Email Address" />
          <span class="icon is-small is-left"><font-awesome-icon icon="envelope" /></span>
        </div>

        <ErrorMessage name="email_address" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left">
          <Field name="password" type="password" class="input" :rules="rulePassword" placeholder="Password" />
          <span class="icon is-small is-left"><font-awesome-icon icon="lock" /></span>
        </div>

        <ErrorMessage name="password" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Re-enter Password</label>
        <div class="control has-icons-left">
          <Field name="password2" type="password" class="input" :rules="rulePassword2" placeholder="Re-type Password" />
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
  setup() {
    return {
      ruleUsername: yup.string().required().min(3),
      rulePassword: yup.string().required().min(3),
      rulePassword2: yup.string().oneOf([yup.ref('rulePassword'), null], 'Passwords must match'),
      ruleEmail_address: yup.string().email().required()
    }
  },
}
</script>

<style scoped>

</style>