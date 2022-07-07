<template>
  <div class="detail">
    <div class="info">

      <div class="info1">
        <h1 class="title">{{house.TieuDe}}</h1>
        <p class="subtitle">{{house.DiaChi}}</p>
      </div>

      <div class="image">
<!--        <vueper-slides>-->
<!--          <vueper-slide-->
<!--              v-for="(slide, i) in imgLinks"-->
<!--              :key="i"-->
<!--              :content="'<img src='+slide+'>'">-->
<!--          </vueper-slide>-->
<!--        </vueper-slides>-->
        <Slider
            animation="fade"
            :duration="5000"
            :speed="1000"
        >
          <SliderItem v-for="(i, index) in imgLinks" :key="index">
            <div class="center">
              <img :src="i">
            </div>
          </SliderItem>
        </Slider>
      </div>
      <br>
<!--      <div class="main-info">-->

<!--        <nav>-->
<!--          <h3>Mô tả</h3>-->
<!--          <p class="mota" v-for="des in description" v-bind:key="des">{{des}}</p>-->
<!--          <h3>Pháp lý</h3>-->
<!--          <p class="mota">{{house.PhapLy}}</p>-->
<!--          <h3 v-if="house.MucGia">{{house.MucGia}} triệu VNĐ</h3>-->
<!--          <h3>{{house.DienTich}} m<sup>2</sup></h3>-->
<!--        </nav>-->


<!--      </div>-->
<!--      <div class="info">-->
<!--        <div class="contact">-->

<!--          <p class="subtitle">Số phòng ngủ: {{house.SoPhongNgu}}</p>-->
<!--          <p class="subtitle">Số phòng vệ sinh: {{house.SoToilet}}</p>-->
<!--          <p class="subtitle">Nội thất: {{house.NoiThat}}</p>-->
<!--          <p class="subtitle">Hướng nhà: {{house.HuongNha}}</p>-->

<!--          <h4 class="heading">Thông tin liên lạc</h4>-->
<!--          <p class="subtitle">Tên người bán: {{house.TenNguoiBan}}</p>-->
<!--          <p class="subtitle">SĐT: {{house.SoDienThoai}}</p>-->
<!--          <a :href="house.OriginalLink" target="_blank">Link bài bán gốc</a>-->
<!--        </div>-->





<!--      </div>-->

      <h3>THÔNG TIN CHI TIẾT</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <tbody>
            <tr>
              <th>Diện tích</th>
              <td>
                <p v-if="house.DienTich">{{house.DienTich}} m<sup>2</sup></p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Mức giá</th>
              <td>
                <p v-if="house.MucGia">{{house.MucGia}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Mô tả</th>
              <td>
                <p v-for="des in description" v-bind:key="des">{{des}}</p>
              </td>
            </tr>
            <tr>
              <th>Pháp lý</th>
              <td>
                <p v-if="house.PhapLy">{{house.PhapLy}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Số phòng ngủ</th>
              <td>
                <p v-if="house.SoPhongNgu">{{house.SoPhongNgu}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Số phòng vệ sinh</th>
              <td>
                <p v-if="house.SoToilet">{{house.SoToilet}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Nội thất</th>
              <td>
                <p v-if="house.NoiThat">{{house.NoiThat}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Hướng nhà</th>
              <td>
                <p v-if="house.HuongNha">{{house.HuongNha}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Tên người bán</th>
              <td>
                <p v-if="house.TenNguoiBan">{{house.TenNguoiBan}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>SĐT liên lạc</th>
              <td>
                <p v-if="house.SoDienThoai">{{house.SoDienThoai}}</p>
                <p v-else>Chưa có thông tin</p>
              </td>
            </tr>
            <tr>
              <th>Bài viết gốc</th>
              <td>
                <p><a :href="house.OriginalLink" target="_blank">Link</a></p>
              </td>
            </tr>
          </tbody>
        </table>


      </div>
    </div>

  </div>
</template>

<script>
import { Slider, SliderItem } from 'vue-easy-slider'
export default {
  name: 'HouseDetail',
  components: {
    Slider,
    SliderItem
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

<style lang="scss" scoped>
.mota {
  text-indent: 20px;
}
.detail {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  background-color: #DFE7E7;
  padding: 5em 15em;
}
.info {
  background-color: white;
  box-shadow: 5px 5px 15px rgba(#89C2C2, .5);
  border-radius: 10px;
  padding: 2em;
}
.image {
  width: 50%;
  padding: 2em 15em;
}
img {
  align-content: center;
}
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
.table-wrapper {
  padding: 0 3em;
}
th {
  text-align: left;
  width: 10em;
}
th, td {
  border-bottom: 1px solid #eee;
}
.info1 {
  padding-left: 3em;
  p {
    font-size: 18px;
  }
}
</style>