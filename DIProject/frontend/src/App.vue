<template>
  <div id="app">
    <TopHeader/>
    <HomeView/>
<!--    <div class="content-wrapper">-->
<!--      <router-view/>-->
<!--    </div>-->
  </div>
</template>

<script>
import TopHeader from './components/Header.vue'
import HomeView from "./views/HomeView";

export default {
  name: 'App',
  components: {
    TopHeader,
    HomeView,
  }
}
</script>

<style>
</style>