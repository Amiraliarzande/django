$(window, document, undefined).ready(function() {

  $('input').blur(function() {
    var $this = $(this);
    if ($this.val())
      $this.addClass('used');
    else
      $this.removeClass('used');
  });

  var $ripples = $('.ripples');

  $ripples.on('click.Ripples', function(e) {

    var $this = $(this);
    var $offset = $this.parent().offset();
    var $circle = $this.find('.ripplesCircle');

    var x = e.pageX - $offset.left;
    var y = e.pageY - $offset.top;

    $circle.css({
      top: y + 'px',
      left: x + 'px'
    });

    $this.addClass('is-active');

  });

  $ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function(e) {
  	$(this).removeClass('is-active');
  });

});

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('signupForm');
  const password1 = document.getElementById('password1');
  const password2 = document.getElementById('password2');
  const errorMsg = document.getElementById('error-message');

  if (form && password1 && password2) {
    form.addEventListener('submit', function (e) {
      if (password1.value !== password2.value) {
        e.preventDefault();
        errorMsg.style.display = 'block';
      } else {
        errorMsg.style.display = 'none';
      }
    });
  }
});
