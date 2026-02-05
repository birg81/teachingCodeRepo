'use strict';

function loadHeroes() {
	const xhr = new XMLHttpRequest();
	xhr.open('GET', './jsondata.php', true);
	xhr.send();
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4) {
			if (xhr.status === 200) {
				const heroes = JSON.parse(xhr.responseText);
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
			} else {
				console.error('Errore AJAX:', xhr.status);
			}
		}
	};
}

loadHeroes();