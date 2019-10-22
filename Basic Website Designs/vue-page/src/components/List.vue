<template>
  <div class="exp-list bg-washed-blue pt3 pb4">
    <h2>Components List Example</h2>
    <h3 class="tl ml4">List of things:</h3>
    <div class="flex flex-wrap justify-around">
      <Item v-for="(obj, index) in thingsList" :key="index" :item="obj" :index="index" />
    </div>
  </div>
</template>

<script>
import Item from "@/components/Item.vue";

export default {
  name: "List",
  components: {
    Item
  },
  data: () => {
    return {
      thingsList: [
        "Something",
        "Anything",
        "Thing",
        "Probably a good ideia remember this",
        "Don't Mind",
        "Meaningless",
        "High Priority",
        "Don't Forget It!"
      ]
    };
  }
};
</script>

<style>
.exp-list {
  text-align: center;
}
</style>