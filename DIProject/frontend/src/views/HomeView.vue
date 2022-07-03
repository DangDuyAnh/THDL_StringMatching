<template>
  <div class="home">
    <div class="left-box">
      <LeftBar/>
    </div>
    <div class="item-list">
      <ItemList/>
    </div>
    <Pagination
        :current-page="currentPage"
        :total="total"
        :total-pages="totalPages"
    />
  </div>
</template>

<script>
import ItemList from "../components/ItemList";
import LeftBar from "../components/LeftBar"
import Pagination from "../components/Pagination";
export default {
  components: {
    ItemList,
    LeftBar,
    Pagination,
  },
  data() {
    return {
      currentPage: 1,
      total: 0,
      totalPages: 0,
    }
  }
}
</script>

<style>
.home {
  /*background-color: peachpuff;*/
  display: flex;
}
.item-list {
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
}
</style>