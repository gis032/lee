/**
 * 这个方式是扩展jquery类，是给jQuery类添加类方法
 在自己定义的时候，要注意{}()的匹配情况，这个是将这个方法直接添加到jquery对象中，然后我们在使用的时候就可以$.function()了，添加的方法  这里要注意的是方法，方法不是属性
*/
jQuery.extend({
	xxaa: function() {
		console.log("这个方式是扩展jquery类，是给jQuery类添加类方法+aa");
	}
});
jQuery.extend({
	xxbb: function() {
		console.log("这个方式是扩展jquery类，是给jQuery类添加类方法+aa");
	}
});