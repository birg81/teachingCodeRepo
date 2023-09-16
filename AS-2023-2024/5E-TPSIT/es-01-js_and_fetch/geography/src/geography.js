'use strict';
// stampa le informazioni del paese
function printInfo(countries) {
	// controlla la presenza della proprietà message che idetntifica un errore
	if(countries !== '' && !countries.hasOwnProperty('message'))
		// se non ci sono errori stampa le info del primo paese che corrisponde alla ricerca
		document.querySelector('#country-info').innerHTML = `
			<h5>
				possibili corrispondenze:
				<i>${countries.map(country => country.name.common).join(', ')}</i>
			</h5>
			<h1>Dettagli sul Paese</h1>
			<p>Nome del Paese: <b>${countries[0].name.common}</b></p>
			<p>Capitale: <b>${countries[0].capital[0]}</b></p>
			<p>Popolazione: <b>${countries[0].population.toLocaleString()}</b> abitanti</p>
			<p>Area: <b>${countries[0].area.toLocaleString()}</b> km²</p>
		`;
	else
		// in caso di errori stampa un messaggio
		document.querySelector('#country-info').innerHTML = `
			<h1>Mi dispiace 😔 ma non trovo il paese che stai cercando 💔.</h1>
		`;
}
// funzione che cerca il paese
async function countryInfo() {
	// cattura il nome del paese
	const countryName = document.querySelector('#search-country').value.trim();
	// controlla che il paese non sia nullo
	if(countryName !== '')
		// Effettua una richiesta GET all'API
		await fetch(`https://restcountries.com/v3/name/${countryName}`)
			// trasforma il dato ricevuto in formato json
			.then(response => response.json())
			//Aggiorna gli elementi HTML con i dati ricevuti dall'API
			.then(countriesList => printInfo(countriesList))
			// in caso di errore stampa sulla console del browser un errore
			.catch(error => console.error(`Si è verificato un errore nella richiesta: ${error}`));
	else
		printInfo('');
}