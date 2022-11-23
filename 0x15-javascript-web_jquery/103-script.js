window.addEventListener('DOMContentLoaded', () => {
  $('INPUT#language_code').keypress((event) => {
    const keyCode = event.which;
    if (keyCode === 13) {
      const lang = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });

  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
