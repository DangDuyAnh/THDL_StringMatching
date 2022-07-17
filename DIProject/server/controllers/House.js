const HouseModel = require('../models/houses')

const houseController = {}

houseController.list = async (req, res, next) => {
    try {
        const { page } = req.body

        if (page === undefined || page === null) {
            const houseList = await HouseModel.find()
            return res.status(200).json({
                soLuong: houseList.length,
                houselist: houseList
            })
        }

        else {
        const houseList = await HouseModel.find().skip((page-1)*20).limit(20)
        return res.status(200).json({
            soLuong: houseList.length,
            houselist: houseList
        })
        }
    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

houseController.total = async (req, res, next) => {
    try {
        const count = await HouseModel.countDocuments()
        return res.status(200).json({
            soLuong: count
        })

    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}


houseController.search = async (req, res, next) => {
    try {
        const house = await HouseModel.findById(req.params.id)
        return res.status(200).json({
            house: house
        })
    }
    catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

houseController.filter = async (req, res, next) => {
    try {
        let {
            giaMin,
            giaMax,
            tieuDe,
            thanhPho,
            quan,
            dienTichMin,
            dienTichMax,
            soPhongNguMin,
            soPhongNguMax,
            soToiletMin,
            soToiletMax,
            page
        } = req.body

        if (thanhPho === undefined || thanhPho === null) thanhPho = ''
        if (quan === undefined || quan=== null) quan = ''

        if (page === undefined || page === null) {

        let houseList = await HouseModel.find(
            { 
            MucGia: {$lte: giaMax || 1000000000, $gte: giaMin || 0},
            DienTich: {$lte: dienTichMax || 1000000000, $gte: dienTichMin || 0},
            TieuDe: { "$regex": tieuDe || "", "$options": "i"},
            $and: [
                {DiaChi:{ "$regex": thanhPho || "", "$options": "i"}},
                {DiaChi: { "$regex": quan || "", "$options": "i"}}
            ]
            }
            )

        return res.status(200).json({
            soLuong: houseList.length,
            houselist: houseList
        })
        } else {
            let houseList = await HouseModel.find(
                { 
                MucGia: {$lte: giaMax || 1000000000, $gte: giaMin || 0},
                DienTich: {$lte: dienTichMax || 1000000000, $gte: dienTichMin || 0},
                TieuDe: { "$regex": tieuDe || "", "$options": "i"},
                $and: [
                    {DiaChi:{ "$regex": thanhPho || "", "$options": "i"}},
                    {DiaChi: { "$regex": quan || "", "$options": "i"}}
                ]
                }
                ).skip((page-1)*20).limit(20)
    
            return res.status(200).json({
                soLuong: houseList.length,
                houselist: houseList
            })
        }
    } catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

houseController.getCities = async (req, res, next) => {
    try {
        let houseList = await HouseModel.find()
        let diaChi = houseList.map(item => item.DiaChi.replace("Xem bản đồ ",""))
        diaChi = diaChi.map(item => item.replace(" Tp",""))
        diaChi = diaChi.map(item => item.trim())
        diaChi = diaChi.map(item => {
            if (item[item.length - 1] == '.')
                return item.substring(0, item.length - 1)
            else
                return item
        })
        let diaChi_arr = diaChi.map(item => item.split(","))
        let cities =  diaChi_arr.map(item => item[item.length - 1])
        let cityDict = {}
        cities.forEach(item => {
            if (!cityDict[item]) {
                cityDict[item] = 1
            } else {
                cityDict[item] += 1
            }
        })
        let cityArr = []
        for (let [key, value] of Object.entries(cityDict)) {
            cityArr.push([key, value])
          }

        for (let i = 0; i < cityArr.length - 1; i++) {
            for (let j = i + 1; j < cityArr.length; j++) {
                if (cityArr[i][1] < cityArr[j][1]) {
                    let temp = cityArr[i]
                    cityArr[i] = cityArr[j]
                    cityArr[j] = temp
                }
            }
        }

        let sumOthers = 0
        let index = 25
        for (let i = index; i < cityArr.length; i++) {
            sumOthers += cityArr[i][1]
        }
        cityArr.splice(-(cityArr.length - index), (cityArr.length - index))
        cityArr.push(['Others', sumOthers])
          
        return res.status(200).json({
            cities: cityArr
        })

    } catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }

}

houseController.getCost = async (req, res, next) => {
    try {
        let houseList = await HouseModel.find()
        let cost = houseList.map(item => item.MucGia)
        let costDict = {}
        costDict['< 500 triệu'] = 0
        costDict['500 triệu - 1 tỷ'] = 0
        costDict['1 - 2 tỷ'] = 0
        costDict['2 - 3 tỷ'] = 0
        costDict['3 - 5 tỷ'] = 0
        costDict['5 - 7 tỷ'] = 0
        costDict['7 - 10 tỷ'] = 0
        costDict['10 - 20 tỷ'] = 0
        costDict['20 - 30 tỷ'] = 0
        costDict['30 - 40 tỷ'] = 0
        costDict['40 - 60 tỷ'] = 0
        costDict['> 60 tỷ'] = 0
        costDict['Thỏa thuận'] = 0
        cost.forEach(item => {
            if (item === undefined || item === null) costDict['Thỏa thuận'] += 1
            else if (item < 500) costDict['< 500 triệu'] += 1
            else if (item >= 500 && item <= 1000) costDict['500 triệu - 1 tỷ'] += 1
            else if (item > 1000 && item <= 2000) costDict['1 - 2 tỷ'] += 1
            else if (item > 2000 && item <= 3000) costDict['2 - 3 tỷ'] += 1
            else if (item > 3000 && item <= 5000) costDict['3 - 5 tỷ'] += 1
            else if (item > 5000 && item <= 7000) costDict['5 - 7 tỷ'] += 1
            else if (item > 7000 && item <= 10000) costDict['7 - 10 tỷ'] += 1
            else if (item > 10000 && item <= 20000) costDict['10 - 20 tỷ'] += 1
            else if (item > 20000 && item <= 30000) costDict['20 - 30 tỷ'] += 1
            else if (item > 30000 && item <= 40000) costDict['30 - 40 tỷ'] += 1
            else if (item > 40000 && item <= 60000) costDict['40 - 60 tỷ'] += 1
            else costDict['> 60 tỷ'] += 1
        })

        let costArr = []
        for (let [key, value] of Object.entries(costDict)) {
            costArr.push([key, value])
          }

        for (let i = 0; i < costArr.length - 1; i++) {
            for (let j = i + 1; j < costArr.length; j++) {
                if (costArr[i][1] < costArr[j][1]) {
                    let temp = costArr[i]
                    costArr[i] = costArr[j]
                    costArr[j] = temp
                }
            }
        }

        return res.status(200).json({
            prices: costArr
        })
    } catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

houseController.getCostByCity = async (req, res, next) => {
    try {
        let cities = [
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
            'Đắk Lắk'
        ]

        let houseList = await HouseModel.find()
        houseList = houseList.filter(item => item.MucGia !== undefined)
        let list2 = houseList
        houseList.forEach((item, index) => {
            let temp_Arr = item.DiaChi.split(",")
            let temp = temp_Arr[temp_Arr.length - 1]
            temp = temp.replace("Xem bản đồ ","")
            temp = temp.replace(" Tp","")
            temp = temp.trim()
            if (temp[temp.length - 1] == '.')
                temp.substring(0, temp.length - 1)
            if (!cities.includes(temp)) 
                temp = 'Others'
            list2[index].DiaChi = temp
        })

        return res.status(200).json({
            houseList: list2
        })

    } catch (e) {
        return res.status(500).json({
            message: e.message
        });
    }
}

module.exports = houseController