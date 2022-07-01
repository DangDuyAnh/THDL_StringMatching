const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const houseSchema = new Schema({
    OriginalLink: {
        type: String,
    },
    TieuDe: {
        type: String,
    },
    TenNguoiBan: {
        type: String,
    },
    Anh:{
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
});

houseSchema.set('timestamps', true);
const house = mongoose.model('house', houseSchema);

module.exports = house;