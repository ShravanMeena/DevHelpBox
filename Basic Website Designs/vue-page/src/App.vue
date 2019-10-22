<template>
  <div id="app" class="near-black bg-white">
    <h1 class="db bg-light-green ma0 pa3">Vue Page Template</h1>
    <nav id="section-nav" class="bg-green pa3">
      <a
        href="#hello-world"
        class="bg-light-green pa2 br2 mh1 near-black shadow-hover grow-hover"
      >Hello World</a>
      <a
        href="#list"
        class="bg-light-green pa2 br2 mh1 near-black shadow-hover grow-hover"
      >Components List</a>
      <a
        href="#color-slider"
        class="bg-light-green pa2 br2 mh1 near-black shadow-hover grow-hover"
      >Color Slider</a>
    </nav>

    <div id="logo">
      <img alt="Vue logo" src="./assets/logo.png" class="grow-hover" />
    </div>

    <HelloWorld id="hello-world" msg="Welcome to Your Vue.js App" class="bg-washed-green" />
    <List id="list" />
    <SliderExample id="color-slider" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import List from "./components/List.vue";
import SliderExample from "./components/SliderExample.vue";

export default {
  name: "app",
  components: {
    HelloWorld,
    List,
    SliderExample
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-flow: column nowrap;
  color: #2c3e50;
}

#section-nav {
  position: sticky;
  position: -webkit-sticky;
  top: 0px;

  z-index: 100;
}

#logo {
  text-align: center;
}

.grow-hover {
  transition: 0.5s;
  z-index: 10;
}
.grow-hover:hover {
  transform: scale(1.25, 1.25);
  z-index: 200;
}
</style>
