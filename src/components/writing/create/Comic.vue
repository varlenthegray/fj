<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create/comic" aria-current="page">Comic</router-link></li>
    </ul>
  </nav>

  <n-upload action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f">
    <n-upload-dragger>
      <div class="mb-3">
        <n-icon size="48" :depth="3"><archive-icon /></n-icon>
      </div>

      <n-text style="font-size: 16px;">Click or drag your comic to this area to upload</n-text>

      <n-p depth="3" class="mt-3">Do not upload sensitive information of any kind.</n-p>
    </n-upload-dragger>
  </n-upload>
</template>

<script>
import { ArchiveOutline as ArchiveIcon } from '@vicons/ionicons5'

export default {
  name: "Comic",
  components: {
    ArchiveIcon
  }
}
</script>

<style scoped>

</style>