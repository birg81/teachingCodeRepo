'use strict';
const seekMovies = async () => {
	const seekStr = document.querySelector('#searchMovies').value.trim();
	await fetch(`./api/${seekStr.length > 0 ? seekStr : '_'}`)
		.then(res => res.json())
		.then(movies =>
			document.querySelector('#moviesList').innerHTML = movies.length > 0
			? movies.map(
				movie => `
					<tr>
						<th scope="row">${movie.film_id}</th>
						<td>${Math.floor(movie.length / 60)}:${('' + movie.length % 60).padStart(2, '0')}</td>
						<td>${movie.title}</td>
						<td>${movie.description}</td>
					</tr>
				`).join('')
			: '<tr><td colspan="4">💔 Mi spiace non ci sono film! 🍿</td></tr>'
		)
		.catch(e => `<tr><td colspan="4">💔 Mi spiace non ci sono film! 🍿 errore ${e}</td></tr>`);
};
seekMovies();