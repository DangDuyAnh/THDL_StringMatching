<template>
  <div id="app">
    <TopHeader/>
    <item-component/>
<!--    <div class="content-wrapper">-->
<!--      <router-view/>-->
<!--    </div>-->
  </div>
</template>

<script>
import TopHeader from './components/Header.vue'
import itemComponent from './components/Item.vue'

export default {
  name: 'App',
  components: {
    TopHeader,
    itemComponent
  }
}
</script>

<style>
</style>