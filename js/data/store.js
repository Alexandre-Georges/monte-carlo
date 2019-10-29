import { derived, writable } from 'svelte/store';

export let store = writable({
	intervalSize: 100,
	xileSize: 10,
	sampleSize: 100000,
	expression: 'output=x+y',
	variables: [
		{ name: 'x', distribution: 'uniform', params: { min: 0, max: 10 } },
		{ name: 'y', distribution: 'normal', params: { mean: 5, std: 2 } },
	],
});

export function addVariable(variable) {
	store.update(store => {
		const copy = Object.assign({}, store);
		copy.variables.push(variable);
		copy.variables = Array.from(copy.variables);
		return copy;
	});
};

export function deleteVariable(index) {
	store.update(store => {
		const copy = Object.assign({}, store);
		copy.variables.splice(index, 1);
		copy.variables = Array.from(copy.variables);
		return copy;
	});
};

export const distributionBiggestProperties = derived(
	store,
	$store => {
		if ($store.variables.length === 0) {
			return [];
		} else {
			return $store.variables.reduce((acc, variable) => {
				if (acc.length > Object.keys(variable.params).length) {
					return acc;
				}
				return Object.keys(variable.params);
			}, []);
		}
	}
);
