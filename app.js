const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');
const passport = require('passport');
const mongoose = require('mongoose');
const config = require('./config/database');

//Connect to database
mongoose.connect(config.database);

//On connection 
mongoose.connection.on('connected', () => {
    console.log('Connected to database'+config.database)
});

//On Error
mongoose.connection.on('error', (err) => {
    console.log('Database error: '+err);
})

const app = express();
const api = require('./routes/index.js');

//Port Number
const port = 3000;

//CORS Middleware
app.use(cors());

//Body Parser Middleware
app.use(bodyParser.json());

//Set Static Folder
app.use(express.static(path.join(__dirname, 'public')))

//Passport Middleware
app.use(passport.initialize());
app.use(passport.session());

//require('./config/passportAdmin')(passport);
//Index Route
app.use('/api', api);

app.get('/', (req, res) => {
    res.send("Invalid EndPoint");
});

app.listen(port, ()=>{
    console.log('Server is started at port : ' + port);
});
