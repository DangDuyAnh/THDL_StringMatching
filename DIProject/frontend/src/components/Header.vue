<template>
<!--  <div class="nav" v-on:click="highLight">-->
    <div class="title">
      <p>TRANG THÔNG TIN BẤT ĐỘNG SẢN</p>
<!--    <router-link class="page-link" to="/">Trang thông tin bất động sản</router-link>-->
  </div>
</template>

<script>
export default {
  name: 'TopHeader',
  // methods: {
  //   highLight(e) {
  //     const underlines = this.$refs.menu.querySelectorAll('.underline');
  //     underlines.forEach(u => {
  //       u.classList.remove('visible')
  //     });
  //     e.path[1].childNodes[1].classList.add('visible')
  //   }
  // }
}
</script>

<style lang="css" scoped>
.title {
  font-size: 30px;
  font-weight: bold;
  width: 100%;
  display: flex;
  align-items: center;
  padding-left: 10px;
}
</style>