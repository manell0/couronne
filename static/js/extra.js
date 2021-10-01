// Code from Bootstrap
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

  // Modal
  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

  // Does not allow users to use the enter key because then modal is not activated (window.location.pathname;)
  if (top.location.pathname === '/update/')
  {
    $(document).ready(function() {
      $(window).keydown(function(event){
        if(event.keyCode == 13) {
          event.preventDefault();
          return false;
        }
      });
    });
    
  }
