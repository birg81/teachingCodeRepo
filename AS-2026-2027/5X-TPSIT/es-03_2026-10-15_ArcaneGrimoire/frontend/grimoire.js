'use strict'

const loadingEl = document.getElementById('loading');
const errorEl = document.getElementById('error-message');
const errorTextEl = document.getElementById('error-text');
const emptyEl = document.getElementById('empty-message');
const containerEl = document.getElementById('ingredients-container');

const fetchIngredients = async () => {
	try {
		const res = await fetch('http://localhost:8080/');

		if (!res.ok)
			throw new Error(`HTTP error! Status: ${res.status}`);

		const ingredients = await res.json();

		loadingEl.classList.add('d-none');

		if (!Array.isArray(ingredients) || ingredients.length === 0) {
			emptyEl.classList.remove('d-none');
			return;
		}

		ingredients.forEach(item => {
			const card = document.createElement('div');
			card.className = 'card';

			card.innerHTML = `
				<div>
					<div class="card-header-top">
						<h3 class="card-title">${item.name}</h3>
						<span class="badge-id">#${item.id}</span>
					</div>
					<p class="card-text">${item.description}</p>
				</div>
				<div class="elemental-affinities">
					<div class="element-row">
						<div class="element-info text-earth"><span>🌱 Earth</span><span>${item.earth}/5</span></div>
						<div class="progress"><div class="progress-bar progress-bar-earth" style="width: ${(item.earth / 5) * 100}%"></div></div>
					</div>
					<div class="element-row">
						<div class="element-info text-water"><span>💧 Water</span><span>${item.water}/5</span></div>
						<div class="progress"><div class="progress-bar progress-bar-water" style="width: ${(item.water / 5) * 100}%"></div></div>
					</div>
					<div class="element-row">
						<div class="element-info text-fire"><span>🔥 Fire</span><span>${item.fire}/5</span></div>
						<div class="progress"><div class="progress-bar progress-bar-fire" style="width: ${(item.fire / 5) * 100}%"></div></div>
					</div>
					<div class="element-row">
						<div class="element-info text-air"><span>💨 Air</span><span>${item.air}/5</span></div>
						<div class="progress"><div class="progress-bar progress-bar-air" style="width: ${(item.air / 5) * 100}%"></div></div>
					</div>
				</div>
			`;
			containerEl.appendChild(card);
		});
	} catch (error) {
		loadingEl.classList.add('d-none');
		errorTextEl.textContent = `Error connecting to server: ${error.message}. Make sure your Python server is running on port 8080 with proper CORS headers.`;
		errorEl.classList.remove('d-none');
	}
}
fetchIngredients();