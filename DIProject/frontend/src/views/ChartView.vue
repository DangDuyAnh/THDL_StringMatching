<script>
import VueApexCharts from 'vue-apexcharts'
export default {
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
            hasPrice: false,
            hasCities: false,
            hasPriceCity: false,
            prices: [],
            priceTags: [],
            priceValues: [],
            seriesPrice: null,
            chartOptionsPrice: null,
            seriesCities: null,
            chartOptionsCities: null,
            hasPriceArea: false,
            cityMap: {
                'Hà Nội': 0,         'Hồ Chí Minh': 1,
                'Bình Dương': 2,        'Đà Nẵng': 3,
                'Đồng Nai': 4,          'Khánh Hòa': 5,
                'Long An': 6,           'Hưng Yên': 7,
                'Lâm Đồng': 8,          'Bình Thuận': 9,
                'Bình Phước': 10,        'Quảng Nam': 11,
                'Bà Rịa Vũng Tàu': 12,   'Cần Thơ': 13,
                'Hòa Bình': 14,          'Quảng Ninh': 15,
                'Hải Phòng': 16,         'Kiên Giang': 17,
                'Vĩnh Long': 18,         'Quảng Bình': 19,
                'Bắc Ninh': 20,          'Bình Định': 21,
                'Bà Rịa - Vũng Tàu': 22, 'Thanh Hóa': 23,
                'Đắk Lắk': 24,           'Others': 25
            },
            cityMap2 : [
                'Hà Nội',            'Hồ Chí Minh',
                'Bình Dương',        'Đà Nẵng',
                'Đồng Nai',          'Khánh Hòa',
                'Long An',           'Hưng Yên',
                'Lâm Đồng',          'Bình Thuận',
                'Bình Phước',        'Quảng Nam',
                'Bà Rịa Vũng Tàu',   'Cần Thơ',
                'Hòa Bình',          'Quảng Ninh',
                'Hải Phòng',         'Kiên Giang',
                'Vĩnh Long',         'Quảng Bình',
                'Bắc Ninh',          'Bình Định',
                'Bà Rịa - Vũng Tàu', 'Thanh Hóa',
                'Đắk Lắk',       'Others'
            ]
            ,
            seriesPriceCity: null,
            optionsPriceCity : null,
            seriesPriceArea: null,
            optionsPriceArea: null
        }
    },
    methods: {
        async getPrice() {
            try {
                const response1 = await this.$http.get(
                    "http://localhost:5000/get-prices"
                )
                let prices = response1.data.prices
                let tags = []
                let values = []
                prices.forEach(item => {
                    tags.push(item[0])
                    values.push(item[1])
                })
                this.priceTags = [...tags]
                this.priceValues = [...values]
                this.seriesPrice = [...values]
                this.chartOptionsPrice = {
                    chart: {
                        width: 380,
                        type: 'pie',
                    },
                    labels: [...tags],
                    responsive: [{
                        breakpoint: 480,
                        options: {
                        chart: {
                            width: 200
                        },
                        legend: {
                            position: 'bottom'
                        }
                        }
                    }]
                },
                this.hasPrice = true
            } catch (error) {
                this.hasData = false;
                console.log(error);
            }
        },

        async getCities() {
            try {
                const response1 = await this.$http.get(
                    "http://localhost:5000/get-cities"
                )
                let cities = response1.data.cities
                let tags = []
                let values = []
                cities.forEach(item => {
                    tags.push(item[0])
                    values.push(item[1])
                })
                this.seriesCities = [{
                    data: [...values]
                }]
                this.chartOptionsCities = {
                    chart: {
                    type: 'bar',
                    height: 350
                    },
                    plotOptions: {
                    bar: {
                        borderRadius: 4,
                        horizontal: true,
                    }
                    },
                    dataLabels: {
                    enabled: false
                    },
                    xaxis: {
                    categories: [...tags],
                    }
                },
                this.hasCities = true
            } catch (error) {
                this.hasData = false;
                console.log(error);
            }
        },

        async getPriceByCity() {
           try {
            console.log(this.cityMap2[parseInt(0.0)])
                const response1 = await this.$http.get(
                    "http://localhost:5000/get-price-by-city"
                )
                let houseList = response1.data.houseList
                let array = []
                houseList = houseList.filter(item => item.MucGia < 300000)
                houseList.forEach(item => {
                    array.push([this.cityMap[item.DiaChi], item.MucGia])
                })
                this.seriesPriceCity = [{
                data: array
                }]
                this.optionsPriceCity = {
                    chart: {
                    type: 'scatter',
                    zoom: {
                        enabled: true,
                        type: 'xy'
                    }
                    },
                    xaxis: {
                    tickAmount: 25,
                    labels: {
                        formatter: function(val) {
                            if (val == 0) return 'Hà Nội'
                            else if (val == 1) return 'Hồ Chí Minh'
                            else if (val === 2) return 'Bình Dương'
                            else if (val === 3) return 'Đà Nẵng'
                            else if (val === 4) return 'Đồng Nai'
                            else if (val === 5) return 'Khánh Hòa'
                            else if (val === 6) return 'Long An'
                            else if (val === 7) return 'Hưng Yên'
                            else if (val === 8) return 'Lâm Đồng'
                            else if (val === 9) return 'Bình Thuận'
                            else if (val === 10) return 'Bình Phước'
                            else if (val === 11) return 'Quảng Nam'
                            else if (val === 12) return 'Bà Rịa Vũng Tàu'
                            else if (val === 13) return 'Cần Thơ'
                            else if (val === 14) return 'Hòa Bình'
                            else if (val === 15) return 'Quảng Ninh'
                            else if (val === 16) return 'Hải Phòng'
                            else if (val === 17) return 'Kiên Giang'
                            else if (val === 18) return 'Vĩnh Long'
                            else if (val === 19) return 'Quảng Bình'
                            else if (val === 20) return 'Bắc Ninh'
                            else if (val === 21) return 'Bình Định'
                            else if (val === 22) return 'Bà Rịa - Vũng Tàu'
                            else if (val === 23) return 'Thanh Hóa'
                            else if (val === 24) return 'Đắk Lắk'
                            else return 'Others'
                            }
                    }
                    },
                    yaxis: {
                    tickAmount: 10
                    }
                }
                this.hasPriceCity = true
            } catch (error) {
                this.hasData = false;
                console.log(error);
            }
        },

        async getPriceByArea() {
            try {
                const response1 = await this.$http.post(
                    "http://localhost:5000/house-list"
                )
                let houseList = response1.data.houselist
                let array = []
                houseList = houseList.filter(item => item.MucGia < 300000)
                houseList = houseList.filter(item => item.DienTich < 1000)     
                houseList.forEach(item => {
                    array.push([item.DienTich, item.MucGia])
                }) 
                this.seriesPriceArea = [{
                data: array
                }]
                this.optionsPriceArea = {
                    chart: {
                    type: 'scatter',
                    zoom: {
                        enabled: true,
                        type: 'xy'
                    }
                    },
                    xaxis: {
                    tickAmount: 20,
                    labels: {
                        formatter: function(val) {
                            return parseFloat(val).toFixed(1)
                            }
                    }
                    },
                    yaxis: {
                    tickAmount: 10
                    }
                }
                this.hasPriceArea = true           
            } catch (error) {
                this.hasData = false;
                console.log(error);
            }
        }

    },
    mounted() {
        this.getPrice()
        this.getCities()
        this.getPriceByCity()
        this.getPriceByArea()
    }
}
</script>
<template>
    <div class="da-container">
    <div :style="{display: 'flex', alignItems: 'center', justifyContent: 'space-around', width: '100%'}">
        <div class="da-card" v-if="hasPrice">
            <h1 class="da-text">Phân bố giá</h1>
            <div id="chart">
            <apexchart type="pie" width="600" :options="chartOptionsPrice" :series="seriesPrice" :style="{fontSize: '24px'}"/>
            </div>
        </div>

        <div class="da-card" v-if="hasCities">
            <h1 class="da-text">Phân bố địa chỉ</h1>
            <div id="chart">
                <apexchart type="bar" width="600" height="420" :options="chartOptionsCities" :series="seriesCities"></apexchart>
            </div>
        </div>
    </div>

    <div class="da-center-card" v-if="hasPriceCity">
        <div :style="{width: '100%'}">
            <h1 class="da-text">Mức giá và địa chỉ</h1>
            <apexchart type="scatter" width="1000" height="420" :series="seriesPriceCity" :options="optionsPriceCity"></apexchart>
        </div>
    </div>

    <div class="da-center-card" v-if="hasPriceArea">
        <div :style="{width: '100%'}">
            <h1 class="da-text">Mức giá và Diện tích</h1>
            <apexchart type="scatter" width="1000" height="420" :series="seriesPriceArea" :options="optionsPriceArea"/>
        </div>
    </div>

    </div>
</template>

<style>
.da-container {
    width: 100%;
    background-color: #f1f2f6;
    margin: 0;
    padding-top: 40px;
    margin-top: -20px;
    min-height: 470px;
    padding-bottom: 10px;
}

.da-card {
    background-color: white;
    border-radius: 10px;
    margin: 20px;
    padding: 20px;
    width: 700px
}

.da-center-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
    margin-bottom: 40px;
    margin-left: auto;
    margin-right: auto;
    width: 1000px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.da-text {
    font-size: 24px;
    font-weight: 700;
}
</style>