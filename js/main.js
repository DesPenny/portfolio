import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
	{
		'title': "This Website",
		'href': "https://despenny.rocks",
		'desc': "This website is completely serverless. It uses S3 and lambda with CodeBuild and CodePipeline. It also allowed me to play with Reactjs.",
		'image': {
			'desc': "screenshot of the infrastructure involved",
			'src': "images/example1.png",
			'comment': ""
		}
	},
	{
		'title': "FavourSoup",
		'href': "https://www.favoursoup.com",
		'desc': "FavourSoup is my pet project built in python/flask and it allows people to exchange favours with eachother.",
		'image': {
			'desc': "screenshot of favoursoup",
			'src': "images/example2.png",
			'comment': ""
		}
	},
	{
		'title': "IAC",
		'href': "https://despenny.rocks",
		'desc': "As part of my current position, I'm using terraform and ansible to help migrate from linode to aws and keep the Infrastructure as Code.",
		'image': {
			'desc': "screenshot of ansible and terraform",
			'src': "images/example3.png",
			'comment': ""
		}
	}
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
