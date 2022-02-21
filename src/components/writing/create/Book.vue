<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create/book" aria-current="page">Book</router-link></li>
    </ul>
  </nav>

  <div class="field">
    <label class="label">Title</label>
    <div class="control"><input class="input" type="text" :placeholder="bookTitle"></div>
  </div>

  <div class="field">
    <label class="label">Tags</label>
    <n-dynamic-tags v-model:value="tags" />
  </div>

  <div class="field is-grouped">
    <label class="checkbox"><input type="checkbox"> Published</label>
    <label class="checkbox mx-3"><input type="checkbox"> NSFW (17+)</label>
  </div>

  <div class="field">
    <label class="label">Synopsis</label>
    <div class="control"><QuillEditor theme="snow" toolbar="minimum" style="overflow: auto; max-height: 450px;" /></div>
  </div>
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { ref } from "vue";

const title_start = [
  "Killer ",
  "Brown Suede ",
  "George Harry's  ",
  "Yellow River ",
  "Farmer's Choice of ",
];

const title_end = [
  "Rabbits",
  "Grass",
  "Shoes",
  "Cliffhanger",
  "Bananas",
  "Candy",
];

export default {
  name: "Chapter",
  components: {
    QuillEditor,
  },
  setup() {
    return {
      tags: ref(["Scrap"]),
      bookTitle: "e.g. " + title_start[Math.floor(Math.random()*title_start.length)] + title_end[Math.floor(Math.random()*title_end.length)],
    }
  }
}
</script>

<style scoped>

</style>