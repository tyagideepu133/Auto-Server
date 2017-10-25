const express = require('express');
const router = express.Router();
const Drivers = require('../models/drivers');


router.get('/',(req,res,next)=>{
    res.json({"success":"done"});
})

router.post('/drivers/new', (req, res, next)=>{
    let newDriver =new  Drivers({
        driver_name: req.body.driver_name,
        driver_uid: req.body.driver_uid,
        driver_dob: req.body.driver_dob,
        driver_dl: req.body.driver_dl
    });
    Drivers.addDriver(newDriver,(err,driver)=>{
        if (err) {
            res.json({success:false, msg:"Failed to add the driver in database"});
            console.log(err);
        } else {
            res.json({success:true, msg:"Driver added succefully"});
        }
    })
});

router.get('/drivers/driver/all', (req, res, next)=>{
    Drivers.getDriverAll((err, driver)=>{
        if (err) {
            res.json({"error":"error"});
            console.log(err)
        } else {
            res.json(driver);
        }
    })
});

router.get('/drivers/driver/:name/:dob', (req, res, next)=>{
    let name = req.params.name;
    let dob = req.prams.dob;
    Drivers.getDriverByData(name, dob, (err, driver)=>{
        if (err) {
            res.json({"error":"error"});
            console.log(err)
        } else {
            res.json(driver);
        }
    })
});



module.exports = router;