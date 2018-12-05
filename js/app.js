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
    var folderByDate = new Date();
    var dd = folderByDate.getDate();
    var mm = folderByDate.getMonth() + 1;
    var yyyy = folderByDate.getFullYear();

    if (dd < 10){
      dd = '0' + dd;
    }
    if (mm < 10) {
      mm = '0' + mm;
    }

    folderByDate = mm + '-' + dd + '-' + yyyy;

    var dest = 'uploads/' + folderByDate + '/';
    mkdirp.sync(dest);
    cb(null, dest);
  }
});

var uploadMultiple = multer({storage : storage}).array('files', 10)

var upload = multer({storage: storage });

var PROTO_PATH = '../protos/protobuf/textminingservice.proto';

var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {keepCase: true, longs: String, enums: String, defaults: true, oneofs: true});
var text_mining_proto = grpc.loadPackageDefinition(packageDefinition).grpc_protos.textmining;
var client = new text_mining_proto.TextMining('localhost:50051', grpc.credentials.createInsecure());


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

app.post("/topicupload", upload.array("file"), function(req, res, next){
  var filesUploaded = req.files.length;
  var call = client.GenerateTopics();
  var topicsByDoc = new Array();

  call.on('data', function(topicsObj) {
    var topicsForDoc = {documentName:req.files[topicsByDoc.length].originalname, topics: new Array()};
    topicsForDoc.topics = topicsObj.topics;

    // Add the array of topics to the array of topics per documents
    topicsByDoc.push(topicsForDoc);

    if (topicsByDoc.length == filesUploaded){
      var json = JSON.stringify(topicsByDoc);
      res.send(json)
    }
  });

  for (var i = 0; i < filesUploaded; i++){
    var loc = {location: __dirname + "/" + req.files[i].path};
    call.write(loc)
  }
});


// Create a function at '/sumnmarygen' that receives a GET request and returns a response
app.get('/summarygen', function(req, res){
  res.render('summarygen', {title: 'Summary generation'});
});

app.post("/summaryupload", upload.array("file"), function(req, res, next){
    var filesUploaded = req.files.length;
    var call = client.GenerateTextSummary();
    var summaries = new Array();
    call.on('data', function(summaryProto) {
      var summaryObj = {documentName:req.files[summaries.length].originalname, summary: ""};
      summaryObj.summary = summaryProto.summary;

      summaries.push(summaryObj);

      if (summaries.length == filesUploaded){
        var json = JSON.stringify(summaries);
        res.send(json);
      }
    });

    for (var i = 0; i < filesUploaded; i++){
      var loc = {location: __dirname + "/" + req.files[i].path};
      call.write(loc)
    }

});

// Listen on port 3000
server.listen(3000, '0.0.0.0');


function sendTopics(topics){
  io.sockets.emit(topics); //send to all clients not the best for right now
}

function sendSummary(summary){

}
