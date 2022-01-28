<template>
  <div class="container">
    <div class="field">
      <label class="label">Username</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input is-success" type="text" placeholder="Text input" value="bulma" />
        <span class="icon is-small is-left"><font-awesome-icon icon="user" /></span>
      </div>

      <p class="help is-success">This username is available</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login"
}
</script>

<style scoped>

</style>