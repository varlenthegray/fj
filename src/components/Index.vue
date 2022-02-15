<template>
  <section class="hero is-medium is-link">
    <div class="hero-body">
      <p class="title">Welcome to Faded Journals</p>

      <p class="subtitle">A place where writing feels at home.</p>
    </div>
  </section>

  <div class="columns mt-3">
    <div class="column">
      <div class="card">
        <div class="card-content">
          <p class="title">“<n-skeleton text :repeat="2" style="width: 95%;" /> <n-skeleton text style="width: 60%;" />”</p>
          <p class="subtitle"><n-skeleton text style="width: 40%;" /></p>
        </div>

        <footer class="card-footer">
          <p class="card-footer-item"><span><a>Read More</a></span></p>
          <p class="card-footer-item"><span>Share on <a href="#">Facebook</a></span></p>
        </footer>
      </div>
    </div>

    <div class="column">
      <div class="card">
        <div class="card-content">
          <p class="title">“<n-skeleton text :repeat="2" style="width: 95%;" /> <n-skeleton text style="width: 60%;" />”</p>
          <p class="subtitle"><n-skeleton text style="width: 40%;" /></p>
        </div>

        <footer class="card-footer">
          <p class="card-footer-item"><span><a>Read More</a></span></p>
          <p class="card-footer-item"><span>Share on <a href="#">Facebook</a></span></p>
        </footer>
      </div>
    </div>

    <div class="column">
      <div class="card">
        <div class="card-content">
          <p class="title">“<n-skeleton text :repeat="2" style="width: 95%;" /> <n-skeleton text style="width: 60%;" />”</p>
          <p class="subtitle"><n-skeleton text style="width: 40%;" /></p>
        </div>

        <footer class="card-footer">
          <p class="card-footer-item"><span><a>Read More</a></span></p>
          <p class="card-footer-item"><span>Share on <a href="#">Facebook</a></span></p>
        </footer>
      </div>
    </div>
  </div>

  <div class="columns">
    <div class="column is-one-quarter">
      <div class="box" v-if="!loggedIn">
        <Login @is-register="isRegistration = !isRegistration" v-if="!isRegistration" />

        <Register @is-register="isRegistration = !isRegistration" v-else />
      </div>

      <Actions v-else />
    </div>

    <div class="column">
      <div class="box">
        <h1 class="title is-1">What is this?</h1>

        <p>Want to write but don't know how to get started? Looking for the perfect outlet to write just a few sentences
          each day? Our goal is to "gamify" writing. Don't feel like writing today but want to play around? Give this a shot!
          You might find that we're the right fit for your writing style.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { Field, Form, ErrorMessage } from 'vee-validate';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faLock, faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { useMessage } from "naive-ui";
import Register from "./user/Register.vue";
import Login from "./user/Login.vue";
import Actions from "./Actions.vue";

library.add(faUser, faEnvelope, faLock);

export default {
  name: "Index",
  components: {Actions, Login, Register, Field, Form, ErrorMessage },
  setup() { window.$message = useMessage() },
  data() {
    return {
      isRegistration: false,
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
}
</script>

<style scoped>

</style>