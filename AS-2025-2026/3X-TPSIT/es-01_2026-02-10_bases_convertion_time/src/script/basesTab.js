'use strict';
const bases = document.querySelector('#bases');
for (let i = -128; i < 256; i++) {
	bases.innerHTML += `
		<tr>
			<th scope="col">${i}</th>
			<td>0b${(i>>>0).toString(2).padStart(32,'0')}</td>
			<th>${((i>>>0) & 0b1111_1111).toString()}</th>
			<td>0o${(i>>>0).toString(8).padStart(12,'0')}</td>
			<td>0x${(i>>>0).toString(16).padStart(8,'0')}</td>
			<td>${String.fromCharCode(i)}</td>
		</tr>
	`;
}