const express = require('express');
const router = express.Router();

//const product = require('./product/product');
//const blog = require('./blog/posts');
//const admin = require('./admin/admin');
//const order = require('./order/order');
//const inventory = require('./inventory/inventory');


//router.use('/products', product);
//router.use('/post', blog);
//router.use('/order',order);
//router.use('/inventory',inventory);
//router.use('/admin',admin);

router.get('/',(req,res,next)=>{
    res.json({"success":"done"});
})

module.exports = router;