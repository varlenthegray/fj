<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create/scrap" aria-current="page">Scrap</router-link></li>
    </ul>
  </nav>

  <div class="field">
    <label class="label">Tags</label>
    <n-dynamic-tags v-model:value="tags" />
  </div>

  <QuillEditor theme="snow" toolbar="full" style="overflow: auto; max-height: 450px;" />
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { ref } from "vue";

export default {
  name: "Chapter",
  components: {
    QuillEditor
  },
  setup() {
    return {
      tags: ref(["Scrap"]),
    }
  }
}
</script>

<style scoped>

</style>