<template>
  <div class="container">
    <div class="columns">
      <div class="column is-11">
        <h1 class="title is-1">Welcome {{ getUsername }}</h1>
      </div>

      <div class="column has-text-right">
        <div class="dropdown is-right is-hoverable">
          <div class="dropdown-trigger">
            <button class="button is-white" aria-haspopup="true" aria-controls="dropdown-menu">
              <span class="icon"><font-awesome-icon icon="user-cog" /></span>
            </button>
          </div>

          <div class="dropdown-menu" id="dropdown-menu" role="menu">
            <div class="dropdown-content has-text-left">
              <a @click="" class="dropdown-item">Profile</a>
              <a @click="" class="dropdown-item">Statistics</a>
              <hr class="dropdown-divider">
              <a @click="logOut" class="dropdown-item">Logout</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column is-one-quarter">
        <div class="box">
          <aside class="menu">
            <p class="menu-label">Author Actions</p>
            <ul class="menu-list">
              <li>
                <a>Needs</a>
                <ul>
                  <li><a>Hygiene & Personal</a></li>
                  <li><a>Eat</a></li>
                  <li><a>Read</a></li>
                  <li><a>Sleep</a></li>
                  <li><a>Research</a></li>
                </ul>
              </li>
              <li>
                <a>Write</a>
                <ul>
                  <li><a>Book</a></li>
                  <li><a>Short Story</a></li>
                  <li><a>Comic</a></li>
                  <li><a>Blog</a></li>
                  <li><a>Novel</a></li>
                </ul>
              </li>
            </ul>

            <p class="menu-label">Items</p>
            <ul class="menu-list">
              <li>
                <a>Buy</a>

                <ul>
                  <li><a>Pen & Paper</a></li>
                  <li><a>Typewriter</a></li>
                  <li><a>Used Desktop</a></li>
                  <li><a>New Desktop</a></li>
                  <li><a>Used Laptop</a></li>
                  <li><a>New Laptop</a></li>
                </ul>
              </li>
              <li><a>Sell</a></li>
              <li><a>Upgrade</a></li>
            </ul>

            <p class="menu-label">Marketing</p>
            <ul class="menu-list">
              <li><a>Market Writings</a></li>
              <li><a>Attend Conference</a></li>
              <li><a>Book Signing</a></li>
            </ul>

            <p class="menu-label">Contract Work</p>
            <ul class="menu-list">
              <li>
                <a>Write for Money</a>

                <ul>
                  <li><a>Small Article</a></li>
                  <li><a>Medium Article</a></li>
                  <li><a>Large Article</a></li>
                </ul>
              </li>
              <li>
                <a>Advertise</a>

                <ul>
                  <li><a>City Outreach</a></li>
                  <li><a>County Outreach</a></li>
                  <li><a>State Outreach</a></li>
                  <li><a>National Outreach</a></li>
                  <li><a>International Outreach</a></li>
                </ul>
              </li>
              <li>
                <a>Hire Publisher</a>

                <ul>
                  <li><a>One Man Show</a></li>
                  <li><a>Small Firm</a></li>
                  <li><a>National Firm</a></li>
                  <li><a>Multi-national Firm</a></li>
                </ul>
              </li>
            </ul>
          </aside>
        </div>
      </div>

      <div class="column">
        <div class="block">
          <component :is="actionCenter" />
        </div>

        <div class="block">
          <div class="box">
            Yep, this is the static box.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUserTie, faUserCog } from "@fortawesome/free-solid-svg-icons";
import Welcome from "./tutorial/Welcome.vue";

library.add(faUserTie, faUserCog);

export default {
  computed: {
    getUsername() {
      let loginKey = localStorage.getItem('login');

      if(loginKey) {
        const author = JSON.parse(localStorage.getItem('login')).author;

        if(author && author.pen_name) {
          return author.pen_name;
        } else if(author) {
          return author.username;
        } else {
          return '';
        }
      }
    },
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
    actionCenter() {
      return Welcome
    },
    logOut() {
      this.$store.dispatch("auth/logout")
          .then(
              () => {
                window.$message.info('Logged out successfully.');
                this.$router.push("/");
              })
    },
  },
  created() {
    if(!this.loggedIn) {
      this.$router.push("/");
    }
  },
  components: {
    Welcome
  }
}
</script>

<style scoped>

</style>