<template>
  <div id="app">
    <TopHeader/>
    <item-list/>
<!--    <div class="content-wrapper">-->
<!--      <router-view/>-->
<!--    </div>-->
  </div>
</template>

<script>
import TopHeader from './components/Header.vue'
import itemList from './components/ItemList.vue'

export default {
  name: 'App',
  components: {
    TopHeader,
    itemList,
  }
}
</script>

<style>
</style>