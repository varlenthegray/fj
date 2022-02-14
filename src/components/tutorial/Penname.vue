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
        Excellent. Now, create a pen name. This must be unique (to the game), no special characters, and can contain a
        space, if desired. Once you've picked your Pen Name, you cannot change it. Your pen name is used throughout the
        community to identify your work.

        <Form>
          <div class="field mt-4">
            <label class="label">Pen Name</label>
            <div class="control"><Field name="penname" class="input" placeholder="e.g. Alex Smith" :rules="validPenname" /></div>
            <ErrorMessage name="penname" class="help is-danger" />
          </div>
        </Form>
      </div>
    </div>

    <footer class="card-footer">
      <!-- todo: how to setup linking on page that you've "continued" already -->
      <a @click="" class="card-footer-item">Continue</a>
      <a @click="$emit('goWelcome')" class="card-footer-item">Previous</a>
    </footer>
  </div>
</template>

<script>
import { Field, ErrorMessage, Form } from 'vee-validate';
import * as yup from 'yup';

export default {
  name: "Penname",
  components: { Field, ErrorMessage, Form },
  data() {
    return {
      validPenname: yup.string().required('You must enter a pen name to continue.').min(3)
    }
  }
}
</script>

<style scoped>

</style>