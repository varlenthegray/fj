<template>
<!-- todo: i've totally messed this up, the entire site is a blunder... you shouldn't have to log in to read, fix it -->
  <div class="columns">
    <Actions />

    <div class="column">
      <div class="block">
        <component :is="actionCenter" @get-penname="goPenname" @go-welcome="goWelcome" />
      </div>

      <div class="block">
        <div class="box">
          Yep, this is the static box.
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// fixme: i'm doing this the wrong way, i need to use app as the "holder of things" and then leverage vue router to change content
import { library } from "@fortawesome/fontawesome-svg-core";
import { faUserTie, faUserCog } from "@fortawesome/free-solid-svg-icons";
import Welcome from "./tutorial/Welcome.vue";
import Penname from "./tutorial/Penname.vue";
import Actions from "./Actions.vue";

library.add(faUserTie, faUserCog);

export default {
  data() {
    return {
      actionCenter: Welcome
    }
  },
  components: {
    Actions,
    Welcome,
    Penname
  },
  methods: {
    goPenname() {
      this.actionCenter = Penname;
    },
    goWelcome() {
      this.actionCenter = Welcome;
    }
  }
}
</script>

<style scoped>

</style>