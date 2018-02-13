import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
	{
		'title': "This Website",
		'href': "https://despenny.rocks",
		'desc': "Lorem ipsum yadayadayada",
		'image': {
			'desc': "screenshot of the infrastructure involved",
			'src': "images/example1.png",
			'comment': ""
		}
	},
	{
		'title': "FavourSoup",
		'href': "https://www.favoursoup.com",
		'desc': "Lorem ipsum yadayadayada",
		'image': {
			'desc': "screenshot of favoursoup",
			'src': "images/example2.png",
			'comment': ""
		}
	},
	{
		'title': "IAC",
		'href': "https://despenny.rocks",
		'desc': "Lorem ipsum yadayadayada",
		'image': {
			'desc': "screenshot of ansible and terraform",
			'src': "images/example3.png",
			'comment': ""
		}
	}
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
