<script>
	import {
		store,
    distributionBiggestProperties,
    deleteVariable as storeDeleteVariable,
    addVariable as storeAddVariable,
  } from '../data/store';

	let variableName = '';
	let variableDistribution = 'uniform';
	let variableMin = '';
	let variableMax = '';
	let variableMean = '';
	let variableStd = '';

	function addVariable() {
		if (variableName === '') return;
		let variable = null;
		if (variableDistribution === 'uniform' && min !== '' && max !== '') {
			variable = { name: variableName, distribution: variableDistribution, params: { min: variableMin, max: variableMax }};
		} else if (variableDistribution === 'normal' && variableMean !== '' && variableStd !== '') {
			variable = { name: variableName, distribution: variableDistribution, params: { mean: variableMean, std: variableStd }};
		}
		storeAddVariable(variable);
	}

	function getAdditionalColumns(variable) {
		const paramsLength = Object.keys(variable.params).length;
		if (paramsLength < $distributionBiggestProperties.length) {
			return $distributionBiggestProperties.slice(paramsLength, $distributionBiggestProperties.length);
		}
		return [];
	}
</script>
<style>
	.variables {
		padding: 1rem;
    border: 1px solid grey;
		border-radius: 2px;
	}

	.add-col {
		margin-top: 1.5rem;
	}

	h4 {
		margin-top: 0;
		margin-bottom: 1rem;
	}
</style>

<div class="col s12 white variables">
  <h4>Variables</h4>
  <div class="row">
    <div class="col s1 input-field">
      <input id="variable-name" class="small" type="text" bind:value="{variableName}" />
      <label for="variable-name">Name</label>
    </div>
    <div class="col s2 input-field">
      <select id="distribution" bind:value="{variableDistribution}">
        <option value="uniform">Uniform</option>
        <option value="normal">Normal</option>
      </select>
      <label for="distribution">Distribution</label>
    </div>
    {#if variableDistribution === 'uniform'}
      <div class="col s2 input-field">
        <input id="min" class="small" type="number" bind:value="{variableMin}" />
        <label for="min">Min</label>
      </div>
      <div class="col s2 input-field">
        <input id="max" class="small" type="number" bind:value="{variableMax}" />
        <label for="max">Max</label>
      </div>
    {:else if variableDistribution === 'normal'}
      <div class="col s2 input-field">
        <input id="mean" class="small" type="number" bind:value="{variableMean}" />
        <label for="mean">Mean</label>
      </div>
      <div class="col s2 input-field">
        <input id="std" class="small" type="number" bind:value="{variableStd}" />
        <label for="std">STD</label>
      </div>
    {/if}
    <div class="col s2 input-field add-col">
      <button class="btn waves-effect waves-light" type="button" on:click="{addVariable}">Add<i class="material-icons right">add</i></button>
    </div>
  </div>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Distribution</th>
        {#each $distributionBiggestProperties as prop}
          <th></th>
        {/each}
        <th></th>
      </tr>
    </thead>
    <tbody>
      {#each $store.variables as variable, variableIndex}
        <tr>
          <td>{variable.name}</td>
          <td>{variable.distribution}</td>
          {#each Object.keys(variable.params) as distributionKey}
            <td>{distributionKey} : {variable.params[distributionKey]}</td>
          {/each}
          {#each getAdditionalColumns(variable) as column}
            <td></td>
          {/each}
          <td><button class="btn waves-effect waves-light" type="button" on:click="{e => storeDeleteVariable(variableIndex)}">Delete<i class="material-icons right">delete</i></button></td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>