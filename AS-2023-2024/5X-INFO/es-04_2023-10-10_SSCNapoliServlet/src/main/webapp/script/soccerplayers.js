'use strict';

// This arrow function displays an message in error case in your data
const errorMsg = () =>
	document.querySelector('#soccerPlayers')
		.innerHTML = `
			<tr><td colspan="5">
				<h1>I'm sorry 😞💔</h1>
				<h2>but I can't load the soccer players ⚽ you were looking for&hellip;</h2>
			</td></tr>
		`;

// Once it receives the array of objects, this function specifically takes care of showing them on the page
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

// This async function retrieves JSON data from servlet and transforms it into JavaScript objects,
// >> This function, after receiving the data, calls another function to display them on the web page.
const loadSoccerPlayers =
	async () =>
		await fetch('./api/v2/soccer.json')
			.then(res => res.json())
			.then(
				players =>
					players.length > 0
						? drawPlayer(players)
						: errorMsg()
			)
			.catch(e => {
				console.error(e);
				errorMsg()
			});

// The function is invoked to receive the data and display them on the web page.
loadSoccerPlayers();