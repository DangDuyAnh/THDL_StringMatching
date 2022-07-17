<template>
    <div >
        <div class="da-box" :style="{backgroundColor: '#c2fbd7'}">
            <h1>Tìm kiếm dữ liệu</h1>
            <h2>Tìm kiếm những căn nhà phù hợp nhất với bạn</h2>
            <a href="/data" target="_blank">Learn more  →</a>
        </div>  
        
        <div class="da-box" :style="{backgroundColor: '#f8f8f8'}">
            <h1>Thống kê dữ liệu</h1>
            <h2>Tìm hiểu về dữ liệu qua những biểu đồ thú vị</h2>
            <a href="/charts" target="_blank">Learn more  →</a>        
        </div>  
    </div>
</template>

<style>
.da-box {
    width: 1230px;
    height: 210px;
    border-radius: 24px;
    cursor: pointer;
    margin: 18px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: rgb(0 0 0 / 10%) 0 1px 2px 0;
    padding: 40px;
    box-sizing: border-box;
}

.da-box h1 {
    margin: 0;
    padding: 0;
    font-size: 28px;
    font-family: Arial;
}

.da-box h2 {
    opacity: 0.8;
    color: #333;
    margin-top: 15px;
    margin-bottom: 25px;
    font-size: 19px;
    font-family: Arial;
    font-weight: 200;
}

.da-box a {
    color: rgb(15, 15, 15);
    font-size: 20px;
    text-decoration: none;
}

.da-box a:hover {
    text-decoration: underline;
}
</style>