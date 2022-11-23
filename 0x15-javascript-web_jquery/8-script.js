$.get('https://swapi.co/api/films/?format=json', (data) => {
  $.each(data.results, (index, value) => {
    $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
  });
});
