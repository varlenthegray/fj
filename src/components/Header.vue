<template>
  <nav class="navbar is-fixed-top mx-5" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><!--suppress HtmlUnknownTarget -->
        <img src="/icon.png" alt="Logo" width="28" height="28"> <strong>Faded Journals</strong>
      </router-link>

      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <router-link to="" class="navbar-item">Random Story</router-link>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">Genre</a>

          <div class="navbar-dropdown">
            <router-link to="" class="navbar-item">Sci-Fi</router-link>
            <router-link to="" class="navbar-item">Fantasy</router-link>
            <router-link to="" class="navbar-item">Fiction</router-link>
            <router-link to="" class="navbar-item">Children</router-link>
            <router-link to="" class="navbar-item">Fanfic</router-link>
            <router-link to="" class="navbar-item">Action & Adventure</router-link>
            <router-link to="" class="navbar-item">Detective/Mystery</router-link>
            <router-link to="" class="navbar-item">Historical Fiction</router-link>
            <router-link to="" class="navbar-item">Horror</router-link>
            <router-link to="" class="navbar-item">Suspense/Thrillers</router-link>
            <router-link to="" class="navbar-item">Biography</router-link>
            <router-link to="" class="navbar-item">Poetry</router-link>
            <router-link to="" class="navbar-item">True Crime</router-link>
          </div>
        </div>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">More</a>

          <div class="navbar-dropdown">
            <router-link to="" class="navbar-item">About</router-link>
            <router-link to="" class="navbar-item">Jobs</router-link>
            <router-link to="" class="navbar-item">Contact</router-link>
            <hr class="navbar-divider">
            <router-link to="" class="navbar-item">Report an issue</router-link>
          </div>
        </div>
      </div>

      <div class="navbar-end" v-if="loggedIn">
        <div class="navbar-item">
          <div class="dropdown is-right is-hoverable">
            <div class="dropdown-trigger">
              <button class="button is-white" aria-haspopup="true" aria-controls="dropdown-menu">
                <span class="mx-2"><strong>{{ getUsername }}</strong></span>
                <n-avatar round size="small" :style="{color: 'rgb(0,0,0)', backgroundColor: 'rgb(173,208,173)'}">
                  <font-awesome-icon icon="user" />
                </n-avatar>
              </button>
            </div>

            <div class="dropdown-menu" id="dropdown-menu" role="menu">
              <div class="dropdown-content has-text-left">
                <router-link to="" class="dropdown-item">Profile</router-link>
                <router-link to="" class="dropdown-item">Statistics</router-link>
                <hr class="dropdown-divider">
                <router-link to="/logout" class="dropdown-item">Logout</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Header",
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
    getUsername() {
      if(this.loggedIn) {
        return this.$store.state.auth.user['author'].pen_name;
      }
    }
  },
}
</script>

<style scoped>

</style>