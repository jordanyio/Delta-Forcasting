<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/deltalogo.png" style="height: 200px; " >
    <!-- <HelloWorld msg="Delta Forecasting Engine"/> -->
    <PlotView />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import PlotView from './components/Plot-View.vue'

export default {
  name: 'App',
  components: {
   
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
  color: #000000;
  background-color: rgb(77, 77, 100);
}
</style>
