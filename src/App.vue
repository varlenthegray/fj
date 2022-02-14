<template>
  <Header />

  <div class="container mt-5">
    <n-message-provider>
      <router-view />
    </n-message-provider>
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  components: { Header },
}
</script>

<style>
/* intentionally left blank */
</style>