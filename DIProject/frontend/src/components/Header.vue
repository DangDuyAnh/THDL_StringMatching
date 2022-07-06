<template>
<!--  <div class="nav" v-on:click="highLight">-->
    <div id="header">
      <div id="bannerimage">
        <div id="header">
          <span>
            <h1>TRANG THÔNG TIN BẤT ĐỘNG SẢN</h1>
          </span>
        </div>
      </div>

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
#bannerimage {
  width: 100%;
  background-image: url('../assets/pngtree-technology-city-banner-background-image_261645.jpg');
  height: 100%;
  background-position: center;
  position: relative;
}
#header {
  height: auto;
  padding: 100px 100px;
  margin-top: 0;
}
h1 {
  color: white;
  text-align: center;
  font-family: Arial;
}
span {

}
</style>