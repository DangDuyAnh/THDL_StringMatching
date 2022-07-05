<template>
  <div class="item-box">
    <div class="info">

      <div class="image">
        <div :v-for="link in getImageLinks">
          <img :src=link>
        </div>
        <div class="info1">
          <h2 class="title">{{house.TieuDe}}</h2>
          <h3 class="subtitle">{{house.DiaChi}}</h3>
        </div>
      </div>

      <div class="main-info">

        <nav>
          <p class="subtitle">{{house.MoTa}}</p>
          <p class="subtitle">{{house.PhapLy}}</p>
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
// import * as axios from 'axios';
export default {
  name: 'HouseDetail',
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
      }
    }
  },
  methods: {
    getImageLinks() {
      const arr = this.house.Anh.split(',')
      arr.pop()
      console.log(arr)
      return arr
    },
    async getData(id) {
      try {
        const response = await this.$http.get(
            `http://localhost:5000/house-detail/${id}`
        );
        this.house = response.data.house
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
.item-box {
  padding-bottom: 1em;
  border-bottom: 1px solid #b5b5b5;
}
.info {

}
.image {
  width: 20em;
  min-height: 20em;
  /*max-height: auto;*/
  float: left;
  margin: 3px;
  padding: 1em;
}
.img {
  max-width: 100%;
  height: auto;
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
.level {
  display: flex;
}
</style>