$(document).ready(function(){
	$.getJSON("{{url_for('static',filename=musicdata.json_addr)}}",function(result){
		console.log("music$$$");
		$("#musicinfo").after(result["pubDate"]);          $("#musicinfo").after("；  发布时间：");
		$("#musicinfo").after(result["CD"]);          $("#musicinfo").after("；  专辑名：");
		$("#musicinfo").after(result["singer"]);          $("#musicinfo").after("；  歌手名：");
		$("#musicinfo").after(result["title"]);          $("#musicinfo").after("歌名：");

		$("#singerpage").attr('href',result["singer_addr"]);  
		$("#CDpage").attr('href',result["CD_addr"]);  
		var pic_addr0=result["pic_addr"];
		var music_addr0=result["music_addr"];
		$("#music_pic").attr('src','/static/'+pic_addr0); 
		$("#audio").attr('src','/static/'+music_addr0); 
		// var aObj = document.getElementById("singerpage");
		// aObj.href = result["singer_addr"];
	});
});

var audio=document.getElementById("audio");
var rotateVal = 0 // 旋转角度
var InterVal // 定时器
	window.onload = function () {
    document.getElementById("audio").onpause=function()
    {
      clearInterval(InterVal);
    }
    document.getElementById("audio").onplay=function()
    {
      rotate();
    }

	}
   
	// 设置定时器
	function rotate () {
		InterVal = setInterval(function () {
			var img = document.getElementById('disc_pic')
			rotateVal += 1//每次增加的角度
			// 设置旋转属性(顺时针)
			img.style.transform = 'rotate(' + rotateVal + 'deg)'
			// 设置旋转属性(逆时针)
			//img.style.transform = 'rotate(-' + rotateVal + 'deg)'
			// 设置旋转时的动画  匀速0.1s
			img.style.transition = '0.1s linear'
		}, 10)
	}
