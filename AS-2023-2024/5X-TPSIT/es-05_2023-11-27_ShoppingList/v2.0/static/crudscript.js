'use strict';

// print items on Html page
const updatePageData = async (outTag = 'ul#shoppingList') => {
	const itemsList = await loadItems();
	document.querySelector(outTag).innerHTML = itemsList.length === 0
		? `
			<li class="list-group-item">
				&#x1f494; Sorry we have some problem &#x1f41b;<br/>
				Probably you have an empty list<br/>
				or maybe server is broke &#x1f61f;
			</li>
		`
		: itemsList.map(
			(item, id) => `
				<li class="list-group-item">
					<div class="btn-group" role="group">
						<button class="btn btn-outline-danger" onclick="removeItem(${id})">&#x274c;</button>
						<button class="btn btn-outline-warning" onclick="modifyItem(${id},'${item}')">&#x270d;</button>
					</div>
					<b>${item}</b>
				</li>
			`
		).join('');
};

// CREATE new item and add them to itemsList
const addItem = async (item = '') => {
	if(item !== null && item.trim() !== ''){
		const data = await fetch(`./api/${item.trim()}`, {method: 'POST'})
			.then(res => res.json())
			.catch(e => console.error(e));
		if (data.success === true)
			updatePageData();
	}
};

// READ (load) all items
const loadItems =
	async () => await fetch('./api')
		.then(res => res.json())
		.catch(e => console.error(e));

// UPDATE (modify) a selected item by index
const modifyItem = async (id = -1, oldItem = '') => {
	const item =
		prompt(`give a new value for "${oldItem}"`, oldItem)
			.trim().toLowerCase();
	if(id > -1 && item !== null && item !== '' && item !== oldItem.toLowerCase()) {
		const data = await fetch(`./api/${id}/${item}`, {method: 'PUT'})
			.then(res => res.json())
			.catch(e => console.error(e));
		if (data.success === true)
			updatePageData();
	}
};

// DELETE (remove) a selected item by index
const removeItem = async (id = -1) => {
	if(id > -1) {
		const data = await fetch(`./api/${id}`, {method: 'DELETE'})
			.then(res => res.json())
			.catch(e => console.error(e));
		if(data.success === true)
			updatePageData();
	}
};

updatePageData();