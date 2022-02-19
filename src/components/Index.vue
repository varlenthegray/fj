<template>
  <div class="card block">
    <header class="card-header">
      <p class="card-header-title"><n-skeleton text style="width: 40%;" /></p>

      <button class="card-header-icon" aria-label="more options">
        <span class="icon"><font-awesome-icon icon="angle-right" /></span>
      </button>
    </header>

    <div class="card-content">
      <h4 class="title is-4">“<n-skeleton text :repeat="2" style="width: 95%;" /> <n-skeleton text style="width: 60%;" />”</h4>
      <p class="subtitle"><n-skeleton text style="width: 40%;" /></p>
    </div>

    <footer class="card-footer">
      <p class="card-footer-item"><span><a>Read More</a></span></p>
      <p class="card-footer-item"><span>Share on <a href="#">Facebook</a></span></p>
    </footer>
  </div>

  <div class="card block">
    <header class="card-header">
      <p class="card-header-title"><n-skeleton text style="width: 36%;" /></p>

      <button class="card-header-icon" aria-label="more options">
        <span class="icon"><font-awesome-icon icon="angle-right" /></span>
      </button>
    </header>

    <div class="card-content">
      <h4 class="title is-4">“<n-skeleton text style="width: 97%;" /> <n-skeleton text style="width: 42%;" />”</h4>
      <p class="subtitle"><n-skeleton text style="width: 28%;" /></p>
    </div>

    <footer class="card-footer">
      <p class="card-footer-item"><span><a>Read More</a></span></p>
      <p class="card-footer-item"><span>Share on <a href="#">Facebook</a></span></p>
    </footer>
  </div>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faAngleRight } from "@fortawesome/free-solid-svg-icons";

library.add(faAngleRight);

export default {
  name: "Index"
}
</script>

<style scoped>

</style>