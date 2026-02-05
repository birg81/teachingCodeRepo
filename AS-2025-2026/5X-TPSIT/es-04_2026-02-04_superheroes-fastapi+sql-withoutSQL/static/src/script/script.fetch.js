'use strict';

const loadHeroes = async () => {
	const heroes = await fetch(
		'./api/superheroes'
	).then(
		data => data.json()
	).catch(
		console.log('Errore')
	);
	let heroesTabHtml = '';
	for(const hero of heroes) {
		heroesTabHtml +=
		`
			<tr>
			<th>${hero.id}</th>
			<td><i>${hero.supername}</i></td>
			<td>${hero.isHuman === 1 ? '🧑' : '👽'}</td>
			<td>${hero.firstname}</td>
			<td>${hero.lastname}</td>
			</tr>
		`;
	}
	document.querySelector('#heroeslist').innerHTML = heroesTabHtml;
};

loadHeroes();