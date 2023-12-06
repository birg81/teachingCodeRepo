'use strict';

const modifyItem = (id = 0, oldItem = '') => {
	let item = prompt(`Fornisci il nuovo nuovo valore a ${oldItem}`, oldItem).trim().toLowerCase();
	if(item != null && item != '' && item != oldItem.toLowerCase())
		document.location = `./update?id=${id}&item=${encodeURIComponent(item)}`;
};