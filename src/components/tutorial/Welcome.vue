<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">Welcome aboard!</p>
      <div class="card-header-icon">
        <n-avatar round size="small"><font-awesome-icon icon="user-tie" /></n-avatar>
      </div>
    </header>

    <div class="card-content">
      <div class="content">
        Welcome! You've decided to give writing a shot eh? Well, here at Faded Journals our job is to introduce you
        to the subject (pun intended). First up is an introduction on how to interact with the system. Click "Continue"
        to progress to the next step.
      </div>
    </div>

    <footer class="card-footer">
      <a @click="$emit('getPenname')" class="card-footer-item">Continue</a>
      <a @click="$emit('logOut')" class="card-footer-item">Logout</a>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Welcome",
}
</script>

<style scoped>

</style>