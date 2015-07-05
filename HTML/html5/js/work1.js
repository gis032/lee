var objWork2 = new Worker("../../js/work2.js");

function $$(id) {
	return document.getElementById(id);
}

function loadpag() {
	objWork2.addEventListener("message", function(event) {
		$$("showMes").style.display = "block";
		$$("showMes").innerHTML = event.data;
	}, false);
}

function doMath() {
	var val = $$("getNum").value;
	if (val.length>0) {
		objWork2.postMessage(val);
		$$("getNum").value="";
	}
}
self.onmessage=function(event){
	if(event.data%2==0){
		self.postMessage("偶数");
	}else{
		self.postMessage("基数");
	}
	self.close();
}
