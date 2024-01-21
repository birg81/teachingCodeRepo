'use strict';
const fields = ['firstname', 'lastname', 'age'];
// reload data and write on your page the data from remote server
const people = async _ => {
	document.querySelector('#buddylist').innerHTML = (await personList()).map( p => `
		<tr>
		<td id="firstname_${p.id}">${p.firstname}</td>
		<td id="lastname_${p.id}">${p.lastname}</td>
		<td id="age_${p.id}">${p.age}</td>
		<td id="toggle_${p.id}" class="toggle_on" onclick="editPerson(${p.id})"></td>
		<td id="abort_${p.id}" class="delete" onclick="removePerson(${p.id})"></td>
		</tr>
	`).join('');
	erase();
}
// edit mode
const editPerson = async (id) => {
	let p2edit = {};
	for(let field of fields) {
		p2edit[field] = document.querySelector(`#${field}_${id}`).innerHTML;
		document.querySelector(`#${field}_${id}`).innerHTML =
			`<input id="edit_${field}_${id}" class="form-control" type="${field === 'age' ?'number' :'text'}" value="${p2edit[field]}"/>`;
	}
	let toggle_btn = document.querySelector(`#toggle_${id}`);
	let abort_btn = document.querySelector(`#abort_${id}`);
	toggle_btn.className = 'toggle_off';
	abort_btn.className = 'abort';
	toggle_btn.onclick = _ => {
		const person =  {
			'id': id,
			'firstname': document.querySelector(`#edit_firstname_${id}`).value,
			'lastname': document.querySelector(`#edit_lastname_${id}`).value,
			'age': parseInt(document.querySelector(`#edit_age_${id}`).value)
		}
		console.log(JSON.parse(JSON.stringify(person)));
		modifyPerson(id, person);
	}
	abort_btn.onclick = _ => people();
};
// form clear
const erase = async _ => fields.map(leaf => document.querySelector(`#${leaf}_0`).value= '');
// CREATE
const addPerson = async _ => {
	const p = {
		'id': 1 + (await personList()).reduce((max, person) => (person.id > max ? person.id : max), 0),
		'firstname': document.querySelector('#firstname_0').value.trim(),
		'lastname': document.querySelector('#lastname_0').value.trim(),
		'age': parseInt(document.querySelector('#age_0').value.trim())
	};
	if(p.firstname !== '' && p.lastname !== '' && p.age !== NaN && p.age > -1) {
		await fetch(
			'./api/person', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(p)
			})
			.then(res => res.ok ? people() : console.error('Error!'))	// reload your page and update your data
			.catch(e => console.error(e));
	}
	else {
		alert('Something is wrong!');
	}
};
// READ
const personList = async _ => await fetch('./api/person')
	.then(res => res.json())
	.catch(e => console.error(e))
	.then(j => j.length === 0 ? [] : j.sort((p1, p2) => (p1.lastname > p2.lastname) ? 1 : -1));
// UPDATE
const modifyPerson = async (id = -1, p = {}) =>
	await fetch(`./api/person/${id}`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(p)
	})
		.then(res => res.ok ? people() : console.error('Error!'))
		.catch(e => console.error(e));
// DELETE
const removePerson = async (id = -1) =>
	await fetch(`./api/person/${id}`, {method: 'DELETE'})
		.then(res => res.ok ? people() : console.error('Error!'))
		.catch(e => console.error(e));