const express = require("express");
const router = express.Router();
const houseController = require('../controllers/House');
const {asyncWrapper} = require("../utils/asyncWrapper");

router.get("/", (req, res) => {
    res.send({ response: "Server is up and running." }).status(200);
});

router.post("/house-list", asyncWrapper(houseController.list))
router.post("/get-total", asyncWrapper(houseController.total))
router.get("/house-detail/:id", asyncWrapper(houseController.search))
router.post("/house-filter", asyncWrapper(houseController.filter))
router.get("/get-cities",asyncWrapper(houseController.getCities))
router.get("/get-prices",asyncWrapper(houseController.getCost))
router.get("/get-price-by-city",asyncWrapper(houseController.getCostByCity))
  
module.exports = router;