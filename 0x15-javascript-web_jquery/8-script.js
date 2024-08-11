$.get(
'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data) {
    const movies = data.results;
    const list_movies = $('#list_movies');
    movies.forEach((movie) => {
      const listItems = $('<li>').text(movie.title);
      list_movies.append(listItems);
    });
  }
);
