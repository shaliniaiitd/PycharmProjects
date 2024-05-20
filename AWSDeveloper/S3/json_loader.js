

 window.onload = function () {
    readJsonFile(<PLACEHOLDER_FOR_S3_RESOURCE>, function (QuoteJson) {
        let QuoteObj = JSON.parse(QuoteJson);
        document.getElementById("Quote").innerHTML =
            "<i>" + QuoteObj.message + "</i>"
    });
}

function readJsonFile(file, callback) {
    let rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4 && rawFile.status === 200) {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}
