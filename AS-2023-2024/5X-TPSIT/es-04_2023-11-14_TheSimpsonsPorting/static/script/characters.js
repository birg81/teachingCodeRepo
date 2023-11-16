'use strict';

// This arrow function displays an message in error case in your data
const errorMsg = () =>
	document.querySelector('#charactersList')
		.innerHTML = `
			<tr><td colspan="4">
				<h1>I'm sorry 😞💔</h1>
				<h2>but I can't load the characters 🤷🏻‍♂️ you were looking for&hellip;</h2>
			</td></tr>
		`;

// Once it receives the array of objects, this function specifically takes care of showing them on the page
const drawCharacter =
	plst =>
		document.querySelector('#charactersList').innerHTML =
			plst.map(
				p => `
					<tr>
						<th>${p.id}</th>
						<td>${p.firstname}</td>
						<td>${p.lastname}</td>
						<td>${p.gender}</td>
					</tr>
			`).join('');

// This async function retrieves JSON data from servlet and transforms it into JavaScript objects,
// >> This function, after receiving the data, calls another function to display them on the web page.
const loadSoccerCharacters =
	async () =>
		await fetch('../api/v2/characters.json')
			.then(res => res.json())
			.then(
				characters =>
					characters.length > 0
						? drawCharacter(characters)
						: errorMsg()
			)
			.catch(e => {
				console.error(e);
				errorMsg()
			});

// The function is invoked to receive the data and display them on the web page.
loadSoccerCharacters();