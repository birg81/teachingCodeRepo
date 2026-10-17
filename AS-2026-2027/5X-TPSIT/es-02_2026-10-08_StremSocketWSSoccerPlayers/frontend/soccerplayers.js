'use strict';
const loadSoccerPlayers = async () =>
	await fetch("http://localhost:8080")
		.then(res => res.json())
		.then(soccerplayers => [...soccerplayers].sort(
			(a, b) => a.fullname.localeCompare(b.fullname, 'it', { sensitivity: 'base' })
		))
		.then(soccerplayers => document.querySelector('#SoccerPlayersTab')
			.innerHTML = soccerplayers.map(
				player => `
					<tr>
						<td>${player.n}</td>
						<td>${player.fullname}</td>
						<td>${player.age}</td>
						<td>${player.role}</td>
						<td>${player.soccerteam}</td>
					</tr>
				`
			).join('')
		)
		.catch(e => {
			console.log('Errore nel caricamento dei calciatori:', e);
			document.querySelector('#SoccerPlayersTab').innerHTML = `
				<tr>
					<td colspan="5">
						Errore nel caricamento dei dati
					</td>
				</tr>
			`;
		});

loadSoccerPlayers();