var fs = require('fs');
var path = require('path');
var log4js = require('log4js');
var DEFAULT_LOG_FILE = __dirname + path.sep + 'logs' + path.sep + 'log4js.log'

var getLogger = function(level, logFile) {

    if (level === undefined) level = 'debug';
    if (logFile === undefined) logFile = path.normalize(DEFAULT_LOG_FILE);
    
    var logger = log4js.getLogger(level);
    var logDir = path.dirname(logFile);
    
    fs.mkdir(logDir, function (error) {
        if (error && error.stack.indexOf('EEXIST') === -1) {
            logger.error('Unable to create directory ' + logDir + error.stack);
            return;
        }
        logger.info('Saving logs under dir: ', logDir);
    });

    log4js.configure({
        appenders: {
            consoleLog: { type: 'console' },
            fileLog: { type: 'file', filename: path.normalize(logFile) }
        },
		categories: {
			file: { appenders: ['fileLog'], level: level },
			default: { appenders: ['fileLog', 'consoleLog'], level: 'debug' }
		}
    });

    return logger;
}

module.exports.getLogger = getLogger;