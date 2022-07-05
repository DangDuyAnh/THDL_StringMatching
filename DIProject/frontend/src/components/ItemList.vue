<template>
  <div class="">
    <div class="list" v-for="house in houseList" v-bind:key="house.TieuDe">
      <div class="item-box">
        <div class="info">

          <div class="image">
            <img v-if="house.Anh" :src=get1ImageLink(house.Anh)>
          </div>

          <div class="main-info">

            <div class="info1">
              <a :href="'/house/'+house._id" class="title">{{house.TieuDe}}</a>
              <p class="subtitle">{{house.DiaChi}}</p>
            </div>

            <nav>
              <h3 v-if="house.MucGia">{{house.MucGia}} triệu VNĐ</h3>
              <h3>{{house.DienTich}} m2</h3>
            </nav>


          </div>
          <div class="info">
            <div class="contact">

              <h4 class="heading">Thông tin liên lạc</h4>
              <p class="subtitle">Tên người bán: {{house.TenNguoiBan}}</p>
              <p class="subtitle">SĐT: {{house.SoDienThoai}}</p>
              <a :href="house.OriginalLink" target="_blank">Link bài bán gốc</a>
            </div>





          </div>








        </div>
      </div>
<!--      <Item :house="house"/>-->
    </div>
  </div>
</template>

<script>
// import * as axios from 'axios';
// import Item from "./Item";
export default {
  name: 'itemList',
  props: {
    houseList: null,
  },
  components: {
    // Item,
  },
  methods: {
    get1ImageLink(image_paths) {
      const arr = image_paths.split(',')
      return arr[0]
    },
  },
  computed : {

  },
  mounted() {
  }
}
</script>

<style scoped>
.item-box {
  padding-bottom: 1em;
  border-bottom: 1px solid #b5b5b5;
}
.info {

}
.image {
  /*width: 20em;*/
  /*height: 20em;*/
  /*display: inline-block;*/
  /*float: left;*/
  /*margin: 3px;*/
  /*padding: 1em;*/
  img {
    display: block;
    max-width:230px;
    max-height:95px;
    width: auto;
    height: auto;
  }
}
.main-info {
  padding: 1em;
  box-sizing: border-box;
  width: 20em;
  flex-direction: column;
  /*position: absolute;*/
  right: 0;
  top: 25px;
}
.info {

  display: flex;
}
.contact {
  padding: 1em;
  box-sizing: border-box;
  width: 20em;
  flex-direction: column;
  /*position: absolute;*/
  right: 0;
  top: 25px;
}
.title {
  font-size: 20px;
  color: blue;
  text-decoration: none;
  font-weight: bold;

}
</style>

