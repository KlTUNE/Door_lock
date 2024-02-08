const http = require("http");
const fs = require("fs");

const server = http.createServer(function(request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end("lock_post");

    if(request.method === 'POST') {
        request.on('data', function(chunk) {
            let postData = '';
            postData = postData + chunk;

            postData = decodeURIComponent(postData);

            console.log(postData);
            fs.writeFile("/home/pi/lock/lock.status", postData, function (err){
                if (err) throw err;
                console.log("正常に書き込みが完了しました");
              });
        })
    }
}).listen(3000);

console.log("start listen");
