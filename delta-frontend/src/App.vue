<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <PlotView />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import PlotView from './components/Plot-View.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    PlotView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: rgb(77, 77, 100);
}
</style>
