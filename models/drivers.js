const mongoose = require('mongoose');

const driverSchema = mongoose.Schema({
    driver_name : {
        type: String,
        required: true
    },
    driver_uid : {
        type: String,
        required: true
    },
    driver_dob : {
        type: String,
        required: true
    },
    driver_dl : {
        type: String,
        required: true
    }
});

const Drivers = module.exports = mongoose.model('drivers_data', driverSchema);


module.exports.getDriverByAddhaar = function(driver_uid, callback){
    const query = {driver_uid:driver_uid};
    Drivers.find(query, callback);
}

module.exports.getDriverByData = function(driver_name, driver_dob, callback){
    const query = {driver_dob:driver_dob,
        driver_name:driver_name
    };
    Drivers.find(query, callback);
}

module.exports.addDriver = function(newDriver, callback){
    newDriver.save(callback);
}