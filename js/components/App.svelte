<script>
	import Plotly from '../frameworks/plotly-latest.min.js';

	import { store, server } from '../data/store';
	import { call } from '../data/call-api';

	import { tick } from 'svelte';

	import Form from './Form.svelte';
	import Variables from './Variables.svelte';
	import Loader from './Loader.svelte';

	let promise = null;

	async function submit() {
		promise = call($store);

		try {
			const data = await promise;
			await tick();
			renderGraph(data);
			scrollTo('graph');
		} catch (error) {
			await tick();
			scrollTo('error');
			throw error;
		}
	}

	function scrollTo(id) {
		document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
	}

	function renderGraph(data) {
		const trace1 = {
			histfunc: 'sum',
			x: data.histogram.map((result, index) => `[${result.start}; ${index < ($store.intervalSize - 1) ? data.histogram[index + 1].start : '∞'}`),
			y: data.histogram.map(result => result.count * 100 / $store.sampleSize),
			type: 'histogram',
			xbins: {
				//size: (response.data.max - response.data.min) / intervalSize,
			},
		};

		Plotly.newPlot('graph', [trace1], { bargap: 0 });

		const ranges = data.xiles.map((result, index) => {
			const diff = index * (255 / ($store.xileSize - 1));
			return { range: [result.low, result.high], color: `rgb(${255 - diff}, 0, ${diff})` }
		});

		const bullet = {
			type: 'indicator',
			mode: 'gauge',
			//value: 10,
			domain: { x: [0, 1], y: [0, 1] },
			title: { text: 'Xiles' },
			delta: { reference: 200 },
			gauge: {
				shape: 'bullet',
				axis: { range: [ranges[0].range[0], ranges[ranges.length - 1].range[1]] },
				/*threshold: {
					line: { color: 'red', width: 2 },
					thickness: 0.75,
					value: 280,
				},*/
				steps: ranges,
			},
  	};

		Plotly.newPlot('bullet', [bullet], { width: 600, height: 250 }, { responsive: true });
	}
</script>

<style>
</style>

<div class="container">
	<div class="row">
		<Form on:submit={submit}></Form>
	</div>
	{#await promise}
		<div class="row center-align">
			<Loader></Loader>
		</div>
	{:then}
		<div class="row">
			<div id="graph"></div>
			<div id="bullet"></div>
		</div>
	{:catch error}
		<span class="row red-text">{error}</span>
	{/await}
</div>
