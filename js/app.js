var config = require('./public/jsons/config');
var path = require('path')
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
var async = require('async');
var mkdirp = require('mkdirp');
var multer = require("multer");
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    var dest = 'uploads/' + Date.now() + '/';
    mkdirp.sync(dest);
    cb(null, dest);
  }
});

var upload = multer({storage: storage });

var PROTO_PATH = '../protos/protobuf/topicgeneration.proto';

var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {keepCase: true, longs: String, enums: String, defaults: true, oneofs: true});
var topic_gen_proto = grpc.loadPackageDefinition(packageDefinition).grpc.document;
var client = new topic_gen_proto.TopicGeneration('localhost:50051', grpc.credentials.createInsecure());


// Express configuration
app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.use(express.json());
app.use(express.static(__dirname + '/public'));
app.use(express.static('node_modules'));

app.get('/', function(req, res) {
    res.render('index', {title: 'Home'});
});

// Create a function at '/topicgen' that receives a GET request and returns a response
app.get('/topicgen', function(req, res){
  res.render('topicgen', {title: 'Topic generation'});
});

app.post("/topicupload", upload.single('file'), function(req, res, next){
     var loc = {location: req.file.destination};
     client.GenerateTopicsDirect(loc, function(err, response) {
       if (err){
         console.log(err);
       }
       if (response) {
         var obj = {
           topics: response.topics
        };

         res.send(JSON.stringify(obj));
         console.log('Received from python: ', response.topics);
       }
     });
});


// Create a function at '/' that receives a GET request and returns a response
app.get('/summarygen', function(req, res){
  res.render('summarygen', {title: 'Summary generation'});
});

// Listen on port 3000
server.listen(3000, '0.0.0.0');


function sendTopics(topics){
  io.sockets.emit(topics); //send to all clients not the best for right now
}

function sendSummary(summary){

}
