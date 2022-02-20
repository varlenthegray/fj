<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create" aria-current="page">Chapter</router-link></li>
    </ul>
  </nav>

  <QuillEditor theme="snow" toolbar="full" />
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

export default {
  name: "Chapter",
  components: {
    QuillEditor
  }
}
</script>

<style scoped>

</style>