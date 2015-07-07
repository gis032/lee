self.onmessage=function(event){
	var val = event.data;
	var objWork1 = new Worker("js/work1.js");
	objWork1.postMessage(val);
	objWork1.onmessage=function (event){
		var strHTML = val;
		self.postMessage(val);
	}
}
