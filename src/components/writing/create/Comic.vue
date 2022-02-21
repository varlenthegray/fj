<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><span class="mx-3 has-text-weight-light">Writings</span></li>
      <li><span class="mx-3 has-text-weight-light">Create</span></li>
      <li class="is-active"><router-link to="/writings/create/comic" aria-current="page">Comic</router-link></li>
    </ul>
  </nav>

  <div class="field">
    <label class="label">Comic Strip Name</label>
    <div class="control"><input class="input" type="text" placeholder="e.g. Attack of the Furballs"></div>
  </div>

  <div class="field">
    <label class="label">Tags</label>
    <n-dynamic-tags v-model:value="tags" />
  </div>

  <div class="block">
    <label class="label">Series</label>
    <div class="control">
      <n-select v-model:value="selectedValue" filterable placeholder="Please select a series" :options="options" />
    </div>
  </div>

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
import {ref} from "vue";

export default {
  name: "Comic",
  components: {
    ArchiveIcon
  },
  setup() {
    return {
      tags: ref(["Comic"]),
      selectedValue: ref(null),
      options: [
        {label: "My fully expired milk", value: "series1"},
      ]
    }
  }
}
</script>

<style scoped>

</style>