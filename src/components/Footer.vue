<template>
  <nav class="navbar is-transparent is-fixed-bottom mx-5" v-if="unsaved">
    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <button class="button is-success">Save changes</button>
          <button class="button is-danger">Cancel</button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Footer",
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