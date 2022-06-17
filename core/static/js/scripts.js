setVideoPlayer()

function handler(e) {
	e.preventDefault();
	videotarget = this.getAttribute("href");
	source = document.querySelector("#videos-wrapper iframe");
	source.src = videotarget;
    refreshDiv()
}

function setVideoPlayer(){
     var container = document.getElementById("videos-wrapper");
     var content = container.innerHTML;
     container.innerHTML= content;
     
    var video_player = document.getElementById("videos-wrapper"),
    links = video_player.getElementsByTagName('a');
    for (var i=0; i<links.length; i++) {
	    links[i].onclick = handler;
    }
}