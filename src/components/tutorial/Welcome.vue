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
        to the subject (pun intended). First up, how do you do things? Click "Continue" to find out!
      </div>
    </div>

    <footer class="card-footer">
      <a @click="$emit('getPenname')" class="card-footer-item">Continue</a>
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