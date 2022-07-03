<template>
  <div class="">
    <div class="list" v-for="house in houseList" v-bind:key="house.TieuDe">
      <Item :house="house"/>
    </div>
  </div>
</template>

<script>
// import * as axios from 'axios';
import Item from "./Item";
export default {
  name: 'itemList',
  props: {
  },
  components: {
    Item,
  },
  data() {
    return {
      houseList: null,
    }
    // return {
    //   houselist: getDat
    // }
  },
  methods: {
    getHouseList() {
      return {
        houseList: [
          {
            OriginalLink: 'https://google.com',
            TieuDe: 'Nha mat pho',
            TenNguoiBan: 'Larue',
            Anh: '2',
            SoDienThoai: '024923592',
            DiaChi: '3 Dai Co Viet',
            MoTa: 'Nha to dep',
            MucGia: 450000000,
            DienTich: '350m2',
            HuongNha: 'Bac',
            SoToilet: '4',
            SoPhongNgu: '4',
            PhapLy: 'Khong co van de phap ly',
            NoiThat: 'Noi that day du'
          },
          {
            OriginalLink: '',
            TieuDe: '',
            TenNguoiBan: '',
            Anh: '',
            SoDienThoai: '',
            DiaChi: '',
            MoTa: '',
            MucGia: 0,
            DienTich: '',
            HuongNha: '',
            SoToilet: '',
            SoPhongNgu: '',
            PhapLy: '',
            NoiThat: ''
          },
          {
            OriginalLink: 'https://google.com',
            TieuDe: 'Nha mat pho',
            TenNguoiBan: 'Larue',
            Anh: '2',
            SoDienThoai: '024923592',
            DiaChi: '3 Dai Co Viet',
            MoTa: 'Nha to dep',
            MucGia: 450000000,
            DienTich: '350m2',
            HuongNha: 'Bac',
            SoToilet: '4',
            SoPhongNgu: '4',
            PhapLy: 'Khong co van de phap ly',
            NoiThat: 'Noi that day du'
          },
        ]
      }
    }
  },
  computed : {

  },
  mounted() {
    this.houseList = this.getHouseList().houseList
    console.log(this.houseList)
  }
}
</script>

<style scoped>
/*.title {*/
/*  border-left: 3px solid #31221F;*/
/*  color: #31221F;*/
/*  padding-left: 0.25em;*/
/*}*/
/*.column{*/
/*  padding: 0.75em 0 !important;*/
/*}*/
/*.konten{*/
/*  padding-top: 3em;*/
/*}*/
/*.media-content{*/
/*  width: 100%;*/
/*}*/
/*img{*/
/*  height: 100%;*/
/*  width: auto;*/
/*}*/
/*article{*/
/*  margin: 0 2em;*/
/*  padding: 1em;*/
/*  -webkit-box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);*/
/*  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);*/
/*}*/
/*p{*/
/*  white-space: pre-wrap;*/
/*}*/
/*.image {*/
/*  height: 200px;*/
/*  width: 200px;*/
/*}*/
/*.list {*/
/*  display: flex;*/
/*}*/
</style>
