/*使用javascript来创建一个对象，也就是一个命名空间，然后可以在这个命名空间内动态的添加方法，调用方法的时候就可以直接的           使用                 命名空间.方法           的方式        来进行调用了，不会引起冲突*/
(function nameSpace() {
	this.seeSecond = function() {
		console.log("当前是seconde的命名空间");
	}
	Second = this;
})();
Second.haha = function() {
	document.getElementById("UserName").value = "李文强";
	alert("OK");
}
Second.xx= function (){
	$("#UserName").val("aaaa");
}
/*
function nameSpace(){
	this.xxx=function(){

	}

	Second = this;
}
nameSpace();
效果和上面的一样，只不过上面的是没有名称的方法，匿名方法  然后利用这一特性  立即执行方法，当加载的时候就把这些东西执行了  这个样子的话我们的命名空间就可以使用了
 * */