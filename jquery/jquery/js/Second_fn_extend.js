/*
 * 这个方式是扩展插件的方法，使用的时候用来扩展jquery的属性，我们在使用的时候将这个属性作用到
 * jQuery.fn = jQuery.prototype
 * 使用方式首先要获得当前的jquery对象，然后在调用这个属性，这个属性是个方法
 * $("#id").aaa();
 */
jQuery.fn.extend({
	aaa:function(){
		console.log("jQuery.fn.extend(");
	}
});

jQuery.fn.extend({
	bbb:function(){
		console.log("jQuery.fn.extend(");
	}
});