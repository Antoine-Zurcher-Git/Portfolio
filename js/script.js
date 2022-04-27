'use strict';

async function in_animations()
{
	await sleep(500);
	home_in_animations();
	about_in_animations();
}

window.onload = () =>
{
	document.documentElement.scrollLeft = 0;

	home_events();
	about_events();
	projet_events();
	//projects_events();

	//in_animations();
};
