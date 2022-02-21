<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create" aria-current="page">Chapter</router-link></li>
    </ul>
  </nav>

  <div class="field">
    <label class="label">Chapter Name</label>
    <div class="control"><input class="input" type="text" :placeholder="chapterTitle"></div>
  </div>

  <div class="field">
    <label class="label">Tags</label>
    <n-dynamic-tags v-model:value="tags" />
  </div>

  <div class="block">
    <label class="label">Book</label>
    <div class="control">
      <n-select v-model:value="selectedValue" filterable placeholder="Please select a book" :options="options" />
    </div>
  </div>

  <QuillEditor theme="snow" toolbar="full" style="overflow: auto; max-height: 450px;" />
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { ref } from "vue";

const title_start = [
  "Attack of the ",
  "Knitting with the ",
  "A hoard of ",
  "The revenge of ",
  "Glory of the ",
  "A battle of ",
  "The lost ",
  "I found the ",
  "The battle of the ",
  "The curtains and the ",
  "My kitchen ate my "
];

const title_end = [
  "centipedes",
  "kittens",
  "teapots",
  "lunch lady",
  "mittens",
  "Geoff's",
  "tape rolls",
  "shirts",
  "nose",
  "sound bytes",
  "closets",
  "leftovers"
];

export default {
  name: "Chapter",
  components: {
    QuillEditor
  },
  setup() {
    return {
      tags: ref(["Chapter"]),
      chapterTitle: "e.g. " + title_start[Math.floor(Math.random()*title_start.length)] + title_end[Math.floor(Math.random()*title_end.length)],
      selectedValue: ref(null),
      options: [
        {label: "Drive My Car", value: "book1"},
      ]
    }
  }
}
</script>

<style scoped>

</style>