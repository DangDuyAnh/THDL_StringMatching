<template>
  <div class="home">
    <div class="left-box">
      <LeftBar/>
      <Pagination
          :current-page="currentPage"
          :total="total"
          :per-page="numOfHousesPerPage"
          :total-pages="totalPages"
          @pagechanged="onPageChange"
      />
    </div>
    <div class="right-box">
      <div class="item-list">
        <ItemList
          :houseList="getRenderHouse(currentPage)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ItemList from "../components/ItemList";
import LeftBar from "../components/LeftBar"
import Pagination from "../components/Pagination";
// import {mapGetters} from 'vuex';
export default {
  components: {
    ItemList,
    LeftBar,
    Pagination,
  },
  props: {
    numOfHousesPerPage: {
      type: Number,
      default: 20,
    }
  },
  data() {
    return {
      currentPage: 1,
      total: 0,
      totalPages: 0,
      houseList: [],
      firstIndex: 0,
      lastIndex: this.numOfHousesPerPage - 1,
    }
  },
  methods: {
    async getData() {
      try {
        const response = await this.$http.post(
            "http://localhost:5000/house-list"
            // {
            //   page: this.currentPage
            // }
        );
        console.log(response.data.houselist)
        // JSON responses are automatically parsed.
        this.houseList = response.data.houselist;
        this.total = response.data.soLuong;
        this.totalPages = Math.ceil(this.total / this.numOfHousesPerPage);
        console.log(this.totalPages)
        console.log(this.total)
        console.log(this.houseList)
      } catch (error) {
        console.log(error);
      }
    },
    getRenderHouse() {
      let first = this.firstIndex
      let last = this.lastIndex
      if (this.houseList != null) {
        return this.houseList.slice(first, last + 1);
      } else {
        return []
      }
    },
    onPageChange(page) {
      // console.log(page)
      this.currentPage = page;
      this.firstIndex = (page - 1) * this.numOfHousesPerPage;
      this.lastIndex = Math.min(page * this.numOfHousesPerPage - 1, this.total - 1);
    },
  },
  computed: {

  },
  mounted() {
    this.getData()
  }
}
</script>

<style>
.home {
  /*background-color: peachpuff;*/
  display: flex;
}
.right-box {
  padding-right: 2em;
  width: 100%;
  height: calc(100% - 70px);
  box-sizing: border-box;
  position: relative;
  height: 350px;
  display: flex;
}
.left-box {
  width: 30%;
  height: 100%;
  color: black;
  /*opacity: 0;*/
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  flex-direction: column;
}
</style>