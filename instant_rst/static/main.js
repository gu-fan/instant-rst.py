console.log("Hello")

let socket = io()
socket.on('connect', function (data) {
  console.log('connected')
  socket.emit('socket connected', { my: 'data' });
  socket.emit('message', 'hello')

})

socket.on('updatingContent', function (data) {
  if (data.HTML != undefined){document.body.innerHTML= data.HTML;}

  var doc_height = $(document).height();
  // Note: $(window).height is not correct.
  var win_height = window.innerHeight;
  var pos = (data.pos != undefined) ? parseFloat(data.pos) : 0; 

  // Put the cursor at the center of browser window.
  // Instead of at the top
  var center_pos = doc_height*pos - win_height/2;

  $("html, body").animate({ scrollTop: center_pos }, 0);
});




socket.on('die', function(newHTML) {
  window.open('', '_self', '');
  window.close();

  var firefoxWarning =
  "<h1>Oops!</h1>" +
  "<h3>Firefox doesn't allow windows to self-close.</h3>" +
  "<h3>If you want the preview window to close automatically like in other browsers, go to about:config and set dom.allow_scripts_to_close_windows to true.</h3>"
  document.body.innerHTML = firefoxWarning;
});


