'use strict';
function choiceDataType() {
	switch(document.querySelector('#choicheDataType').value) {
		case 'json':
			loadJsonData();
			break;
		case 'xml1':
			loadXml1Data();
			break;
		case 'xml2':
			loadXml2Data();
			break;
		default:
			document.querySelector('#charactersTab').innerHTML = '';
	}
}
function printCharacters(characters) {
	document.querySelector('#charactersTab').innerHTML =
		characters.map(
			character => `
				<tr class="${!character.isMale ? 'fe' : ''}male">
					<td>${character.firstname}</td>
					<td>${character.lastname}</td>
					<td>${character.isMale ? '♂️' : '♀️'}</td>
				</tr>
			`
		).join('');
}
async function loadJsonData() {
	await fetch('./src/thesimpsons.json')
		.then(response => response.json())
		.then(characters => printCharacters(characters))
		.catch(error => console.log('Errore'));
}
async function loadXml1Data() {
	let characters = [];
	await fetch('./src/futurama.xml')
		.then(response => response.text())
		.then(txt => new DOMParser().parseFromString(txt, 'text/xml').querySelectorAll('character'))
		.then(charactersNodeList => charactersNodeList.forEach(character =>
			characters.push({
				firstname: character.querySelector('firstname').textContent,
				lastname: character.querySelector('lastname').textContent,
				isMale: character.querySelector('isMale').textContent === 'true'
			})
		))
		.catch(e => console.error(e));
	printCharacters(characters);
}
async function loadXml2Data() {
	let characters = [];
	await fetch('./src/americandad.xml')
		.then(response => response.text())
		.then(txt => new DOMParser().parseFromString(txt, 'text/xml').querySelectorAll('character'))
		.then(charactersNodeList => charactersNodeList.forEach(character =>
			characters.push({
				firstname: character.getAttribute('firstname'),
				lastname: character.getAttribute('lastname'),
				isMale: character.getAttribute('isMale') === 'true'
			})
		))
		.catch(e => console.error(e));
	printCharacters(characters);
}