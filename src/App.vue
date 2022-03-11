<template>
  <n-message-provider>
    <Header />

    <div class="container mt-5">
      <div class="columns">
        <div class="column is-one-quarter">
          <div class="box" v-if="!loggedIn">
            <Login @is-register="isRegistration = !isRegistration" v-if="!isRegistration" />

            <Register @is-register="isRegistration = !isRegistration" v-else />
          </div>

          <Actions v-else />
        </div>

        <div class="column">
          <div v-if="!loggedIn" class="mb-5">
            <section class="hero is-medium is-link">
              <div class="hero-body">
                <p class="title">Faded Journals</p>
                <p class="subtitle">Where writing feels at home.</p>
              </div>
            </section>

            <div class="box">
              <h2 class="title is-2">What we do</h2>
              <p>Want to write but don't know how to get started? Want to play a game that's centered around the idea of
                writing? Here at Faded Journals, our goal is to gamify writing to make it more fun and interactive.</p>
            </div>
          </div>

          <router-view />
        </div>
      </div>
    </div>

    <Footer />
  </n-message-provider>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import { Field, Form, ErrorMessage } from 'vee-validate';
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUser, faLock, faEnvelope, faAngleRight } from "@fortawesome/free-solid-svg-icons";
import Actions from "./components/Actions.vue";
import Login from "./components/user/Login.vue";
import Register from "./components/user/Register.vue";

library.add(faUser, faEnvelope, faLock, faAngleRight);

export default {
  components: { Header, Actions, Login, Register, Field, Form, ErrorMessage, Footer },
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

<style>
/* intentionally left blank */
</style>