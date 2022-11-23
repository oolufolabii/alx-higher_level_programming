window.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + language, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
