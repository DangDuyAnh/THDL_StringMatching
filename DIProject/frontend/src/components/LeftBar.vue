<template>
  <div class="left-box">
    <input type="text" id="search-text">
    <button class="button">Tìm kiếm</button>
  </div>
</template>

<script>
export default {
  name: 'LeftBar',
  props: {

  }
}
</script>

<style>
.left-box {
  padding: 40px 0;
  font-size: 15px;
  align-content: center;
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
}
input {
  padding: 1em;
}
</style>