<template>
  <div class="item-box">
    <div class="info">

      <div class="image">
        <vueper-slides>
          <vueper-slide
              v-for="(slide, i) in imgLinks"
              :key="i"
              :content="'<img src='+slide+'>'">
          </vueper-slide>
        </vueper-slides>
        <div class="info1">
          <h2 class="title">{{house.TieuDe}}</h2>
          <h3 class="subtitle">{{house.DiaChi}}</h3>
        </div>
      </div>
      <br>
      <div class="main-info">

        <nav>
          <h3>Mô tả</h3>
          <p class="mota" v-for="des in description" v-bind:key="des">{{des}}</p>
          <h3>Pháp lý</h3>
          <p class="mota">{{house.PhapLy}}</p>
          <h3>{{house.MucGia}} VNĐ</h3>
          <h3>{{house.DienTich}}</h3>
        </nav>


      </div>
      <div class="info">
        <div class="contact">

          <p class="subtitle">Số phòng ngủ: {{house.SoPhongNgu}}</p>
          <p class="subtitle">Số phòng vệ sinh: {{house.SoToilet}}</p>
          <p class="subtitle">Nội thất: {{house.NoiThat}}</p>
          <p class="subtitle">Hướng nhà: {{house.HuongNha}}</p>

          <h4 class="heading">Thông tin liên lạc</h4>
          <p class="subtitle">Tên người bán: {{house.TenNguoiBan}}</p>
          <p class="subtitle">SĐT: {{house.SoDienThoai}}</p>
          <a :href="house.OriginalLink" target="_blank">Link bài bán gốc</a>
        </div>





      </div>

    </div>

  </div>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
export default {
  name: 'HouseDetail',
  components: {
    VueperSlides,
    VueperSlide
  },
  data() {
    return {
      house: {
        OriginalLink: {
          type: String,
        },
        TieuDe: {
          type: String,
        },
        TenNguoiBan: {
          type: String,
        },
        Anh: {
          type: String,
        },
        SoDienThoai: {
          type: String
        },
        DiaChi: {
          type: String
        },
        MoTa: {
          type: String
        },
        MucGia: {
          type: Number
        },
        DienTich: {
          type: Number
        },
        HuongNha: {
          type: String
        },
        SoToilet: {
          type: String
        },
        SoPhongNgu: {
          type: String
        },
        PhapLy: {
          type: String
        },
        NoiThat: {
          type: String
        }
      },
      imgLinks: [],
      description: []
    }
  },
  methods: {
    async getData(id) {
      try {
        const response = await this.$http.get(
            `http://localhost:5000/house-detail/${id}`
        );
        this.house = response.data.house
        const arr = this.house.Anh.split(',')
        if (arr.length > 1)
          arr.pop()
        this.imgLinks = arr
        const arr1 = this.house.MoTa.split('.-')
        this.description = arr1
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getData(this.$route.params.id)
  }
}
</script>

<style lang="css" scoped>
.mota {
  text-indent: 20px;
}
/*.item-box {*/
/*  padding-bottom: 1em;*/
/*  border-bottom: 1px solid #b5b5b5;*/
/*}*/
/*.info {*/

/*}*/
/*.image {*/
/*  width: 20em;*/
/*  min-height: 20em;*/
/*  !*max-height: auto;*!*/
/*  float: left;*/
/*  margin: 3px;*/
/*  padding: 1em;*/
/*}*/
/*.img {*/
/*  max-width: 100%;*/
/*  height: auto;*/
/*}*/
/*.main-info {*/
/*  padding: 1em;*/
/*  box-sizing: border-box;*/
/*  width: 20em;*/
/*  flex-direction: column;*/
/*  !*position: absolute;*!*/
/*  right: 0;*/
/*  top: 25px;*/
/*}*/
/*.info {*/

/*  display: flex;*/
/*}*/
/*.contact {*/
/*  padding: 1em;*/
/*  box-sizing: border-box;*/
/*  width: 20em;*/
/*  flex-direction: column;*/
/*  !*position: absolute;*!*/
/*  right: 0;*/
/*  top: 25px;*/
/*}*/
/*.level {*/
/*  display: flex;*/
/*}*/
</style>