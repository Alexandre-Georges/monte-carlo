import App from './components/App.svelte';

const app = new App({
	target: document.body,
});

window.app = app;

document.addEventListener('DOMContentLoaded', function() {
	const elems = document.querySelectorAll('select');
	M.FormSelect.init(elems, {});
	//const instances = M.FormSelect.init(elems, {});
});

export default app;
