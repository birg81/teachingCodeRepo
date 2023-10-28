'use strict';
const errorMsg =`
	<h1>I'm sorry 😞💔</h1>
	<h2>but I can't load the soccer players ⚽ you were looking for&hellip;</h2>
`;
const drawPlayer =
	plst =>
		document.querySelector('#soccerPlayers').innerHTML =
			plst.map(
				p => `
					<tr>
						<th>${p.n}</th>
						<td>${p.firstname}</td>
						<td>${p.lastname}</td>
						<td>${p.country}</td>
						<td>${p.role}</td>
					</tr>
			`).join('');
const loadSoccerPlayers =
	async () =>
		await fetch('./api/soccer')
			.then(res => res.json())
			.then(
				players =>
					players.length > 0
						? drawPlayer(players)
						: document.querySelector('#soccerPlayers').innerHTML = `<tr><td colspan="5">${errorMsg}</td></tr>`
			)
			.catch(e => {
				console.error(e);
				document.querySelector('#soccerPlayers').innerHTML = `<tr><td colspan="5">${errorMsg}</td></tr>`;
			});

loadSoccerPlayers();