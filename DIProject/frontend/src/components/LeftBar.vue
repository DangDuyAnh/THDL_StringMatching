<template>
  <div class="left-box">
      <div class="label-input">
        <input type="text" placeholder="Tiêu đề" v-model="field.title"><br><br>
      </div>
      <div class="label-input">
        <input type="text" placeholder="Tỉnh/Thành phố" v-model="field.city"><br><br>
      </div>
      <div class="label-input">
        <input type="text" placeholder="Quận/Huyện" v-model="field.district"><br><br>
      </div>
      <div class="label-input-2">
        <input type="number" placeholder="Giá lọc từ ... VNĐ" v-model="field.minPrice"><br><br>
        <input type="number" placeholder="đến ... VNĐ" v-model="field.maxPrice"><br><br>
      </div>
      <div class="label-input-2">
        <input type="number" placeholder="Diện tích từ ... m2" v-model="field.minSquare"><br><br>
        <input type="number" placeholder="đến ... m2" v-model="field.maxSquare"><br><br>
      </div>
      <div class="label-input">
        <button class="button" @click="handleFilter">Lọc</button>
      </div>
  </div>
</template>

<script>
export default {
  name: 'LeftBar',
  props: {

  },
  data() {
    return {
      field: {
        title: null,
        city: null,
        district: null,
        minPrice: null,
        maxPrice: null,
        minSquare: null,
        maxSquare: null
      },
      data: null,
    }
  },
  methods: {
    // async searchData() {
    //   try {
    //     console.log(this.field.city)
    //     const response = await this.$http.post(
    //       "http://localhost:5000/house-filter",
    //       {
    //         giaMin: this.field.minPrice,
    //         giaMax: this.field.maxPrice,
    //         tieuDe: this.field.title,
    //         thanhPho: this.field.city,
    //         quan: this.field.district,
    //         dienTichMin: this.field.minSquare,
    //         dienTichMax: this.field.maxSquare
    //       }
    //     );
    //     console.log(response.data.houselist)
    //     // JSON responses are automatically parsed.
    //     this.data = response.data
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    handleFilter() {
      // this.searchData()
      console.log(this.field)
      this.$emit('pageFilter', this.field)
    }
  }
}
</script>

<style>
.left-box {
  font-size: 15px;
  align-items: center;
  justify-content: center;
}
input {
  padding: 0.3em;
  width: 10em;
  margin-right: 1em;
}
label {
  font-size: 16px;
}
.label-input {
  display: flex;
  align-items: flex-start;
  width: 10em;
}
.label-input-2 {
  display: flex;
  align-items: flex-start;
  width: 5em;
}
.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 0.8em 1em;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  cursor: pointer;
  width: 5em;
  margin-right: 1em;
  margin-left: auto;
}
</style>