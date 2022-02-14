<template>
<!-- intentionally left blank -->
</template>

<script>
export default {
  name: "Logout",
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    this.$store.dispatch("auth/logout")
        .then(
            () => {
              window.$message.info('Logged out successfully.');
              this.$router.push("/");
            })

    if(!this.loggedIn) {
      this.$router.push("/");
    }
  }
}
</script>

<style scoped>
/* intentionally left blank */
</style>