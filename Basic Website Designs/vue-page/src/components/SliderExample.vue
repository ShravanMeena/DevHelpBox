<template>
  <div class="bg-washed-green tc pt3 pb5">
    <h2>Change Some Value with Slider</h2>
    <div class="dib w-90 flex-nowrap flex-column justify-center mb2">
      <div :style="{backgroundColor: value}" class="br2 pa4 f1">Color Box</div>
      <vue-slider :data="dataArray" v-model="value" max="360" />
    </div>
  </div>
</template>

<script>
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/antd.css";

export default {
  name: "SliderExample",
  components: {
    VueSlider
  },
  data() {
    return {
      value: "yellow",
      dataArray: [
        "dark-red",
        "crimson",
        "red",
        "darkorange",
        "orange",
        "goldenrod",
        "gold",
        "yellow",
        "cornsilk",
        "lightyellow",
        "palegoldenrod",
        "khaki",
        "darkkhaki",
        "olive",
        "olivedrab",
        "yellowgreen",
        "greenyellow",
        "lime",
        "springgreen",
        "aquamarine",
        "aqua",
        "turquoise",
        "darkturquoise",
        "cadetblue",
        "cornflowerblue",
        "royalblue",
        "navy",
        "darkslateblue",
        "slateblue",
        "blueviolet",
        "darkviolet",
        "violet",
        "fuchsia",
        "hotpink",
        "deeppink",
        "mediumvioletred"
      ]
    };
  }
};
</script>

<style>
</style>