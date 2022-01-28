<template>
  <div class="container">
    <Form>
      <div class="field">
        <label class="label">Username</label>
        <div class="control has-icons-left">
          <Field name="username" :rules="isRequired" class="input" placeholder="Username" />
          <span class="icon is-small is-left"><font-awesome-icon icon="user" /></span>
        </div>

        <ErrorMessage name="username" class="help is-danger" />
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left">
          <Field name="password" type="password" :rules="isRequired" class="input" placeholder="Password" />
          <span class="icon is-small is-left"><font-awesome-icon icon="lock" /></span>
        </div>

        <ErrorMessage name="password" class="help is-danger" />
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link" type="submit">Submit</button>
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

library.add(faUser, faLock);

export default {
  components: { Field, Form, ErrorMessage },
  methods: {
    isRequired(value) {
      if(value && value.trim()) {
        return true;
      }

      return 'This field is required.';
    }
  }
}
</script>

<style scoped>

</style>