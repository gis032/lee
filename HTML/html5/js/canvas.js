//这个方法是话一个固定大小的没有边框的矩形
function drawNoCircle() {
	var temp = document.getElementById("can1");
	var obj = temp.getContext("2d");
	obj.fillStyle = "black";
	obj.fillRect(20, 20, 140, 140);
		obj.strokeStyle="brown";
	obj.strokeRect(0,0,170,170);
}

