'use strict';
const updatePageData = async (q = '', outTag = 'tbody#people') => {
	const people = await loadPeople(q);
	document.querySelector(outTag).innerHTML = people.length === 0
		? `
			<tr>
				<td colspan="4">
					&#x1f494; Sorry we have some problem &#x1f41b;<br/>
					Probably you have an empty list<br/>
					or maybe server is broke &#x1f61f;
				</td>
			</tr>
		`
		: people.map(
			(p, _) => `
				<tr>
					<th>${p.id}</th>
					<td>${p.firstname}</td>
					<td>${p.lastname}</td>
					<td>
					<div class="btn-group" role="group">
						<button class="btn btn-outline-danger" onclick="removeItem(${p.id})">&#x274c;</button>
						<button class="btn btn-outline-warning" onclick="modifyItem(${p.id})">&#x270d;</button>
					</div>
					</td>
				</tr>
			`
		).join('');
};

const loadPeople = async (q = '') => await fetch(`./api/v1.0/people.json${q.trim().length > 0 ? '?q='+q.trim().toLowerCase() : ''}`)
	.then(res => res.json())
	.catch(e => console.error(e));

const addPerson = async () => {
	const
		id_0 = parseInt(document.querySelector('#id_0').value.trim()),
		lastname_0 = document.querySelector('#lastname_0').value.trim(),
		firstname_0 = document.querySelector('#firstname_0').value.trim();
	if(id_0 >= 0 && firstname_0 !== '' && lastname_0 !== '') {
		const status = await fetch('./api/v1.0/people.json', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'charset': 'UTF-8'
			},
			body: JSON.stringify({
				id: id_0,
				firstname: firstname_0,
				lastname: lastname_0,
				age: 0
			})
		})
			.then(res => res.status)
			.catch(e => console.error(e));
		if (status === 200)
			updatePageData();
	}
};

const removeItem = async (id = -1) => {
	if(id > -1) {
		const status = await fetch(`./api/v1.0/people.json?id=${id}`, {method: 'DELETE'})
			.then(res => res.status)
			.catch(e => console.error(e));
		if(status === 200)
			updatePageData();
	}
};

updatePageData();