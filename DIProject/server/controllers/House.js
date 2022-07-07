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

module.exports = houseController