<script>
	import { onMount, createEventDispatcher } from 'svelte';

	import { store } from '../data/store';
	import Variables from './Variables.svelte';

	const dispatch = createEventDispatcher();

	async function submit() {
		dispatch('submit');
	}
</script>

<style>
	h3 {
		margin-top: 0;
		margin-bottom: 1rem;
	}

	.variables-row {
		margin-bottom: 0;
	}
</style>

<form class="col s12 card grey lighten-5" on:submit|preventDefault="{submit}">
	<div class="card-content">
		<h3>Monte Carlo Simulation</h3>

		<div class="row">
			<div class="col s4 input-field">
				<input id="interval-size" class="small" type="number" min="1" max="10000" bind:value="{$store.intervalSize}" />
				<label for="interval-size">Interval size</label>
			</div>
			<div class="col s4 input-field">
				<input id="sample-size" type="number" min="0" max="10000000" bind:value="{$store.sampleSize}" />
				<label for="sample-size">Sample size</label>
			</div>
			<div class="col s4 input-field">
				<input id="xile-size" type="number" min="1" max="10000" bind:value="{$store.xileSize}" />
				<label for="xile-size">Xile size</label>
			</div>
		</div>
		<div class="row">
			<div class="col s12 input-field">
				<textarea id="expression" class="materialize-textarea" bind:value="{$store.expression}"></textarea>
				<label for="expression">Expression</label>
			</div>
		</div>
		<div class="row variables-row">
			<Variables></Variables>
		</div>
	</div>
	<div class="card-action">
		<button class="btn waves-effect waves-light" type="submit">Generate<i class="material-icons right">send</i></button>
	</div>
</form>
