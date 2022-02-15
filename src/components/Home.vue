<template>
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