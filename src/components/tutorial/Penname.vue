<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">Pick your Pen Name</p>
      <div class="card-header-icon">
        <n-avatar round size="small"><font-awesome-icon icon="user-tie" /></n-avatar>
      </div>
    </header>

    <div class="card-content">
      <div class="content">
        Excellent. You seem to understand the basics of how to interact with me. Next, you're going to create a pen name.
        This must be unique (to the game), no special characters, and can contain a space, if desired. Once you've picked
        your Pen Name, you cannot change it. This is how players will find and get to know your work.

        <div class="field mt-3">
          <label class="label">Pen Name</label>
          <div class="control">
            <input class="input" type="text" placeholder="e.g. Alex Smith">
          </div>
        </div>
      </div>
    </div>

    <footer class="card-footer">
      <a @click="" class="card-footer-item">Continue</a>
      <a @click="" class="card-footer-item">Previous</a>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Penname"
}
</script>

<style scoped>

</style>