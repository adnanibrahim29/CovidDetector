// Your web app's Firebase configuration
var firebaseConfig = {
	apiKey: "AIzaSyBiLaWU8IpdGqANhA1hWd9r79atHBMWbbQ",
	authDomain: "lc-project-7eb68.firebaseapp.com",
	databaseURL: "https://lc-project-7eb68-default-rtdb.firebaseio.com",
	projectId: "lc-project-7eb68",
	storageBucket: "lc-project-7eb68.appspot.com",
	messagingSenderId: "967838972513",
	appId: "1:967838972513:web:41c83efec70516ce6e4820"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize Firebase, this code never changes
firebase.initializeApp(firebaseConfig);

//List to hold you Firebase data (name your list whatever is relvenant to your data)
var Cold = [];
var Hot = [];
var Room = [];

//Connect to your firebase branch (in this case temperature)
//Check in your firebase to see what name the branch is
var myDBConn2 = firebase.database().ref("Cold");
//var myDBConn2 = firebase.database().ref("Hot");
//var myDBConn2 = firebase.database().ref("Room");

//These two lines willnever change. Copy them exactly		
myDBConn2.on("child_added", function(data, prevChildKey) {
	var DataPoint = data.val();
	
	//Add my values from firebase to my list.
	//I am adding the value called Temperature. 
	//Change DataPoint. to whatever the item is called in your firebase
	Cold.push(DataPoint.Cold);
	//Hot.push(DataPoint.Hot);
	//om.push(DataPoint.Room);
	
	var Temp = [1,2,3,4,5]
	//Just change y to the name of your list
	var trace1 = {
	y: Temp,
	type: "Line"
	};
	
		
	//You can multiple traces if you have multiple listStyleType
	//eg humidity and temperature	
		
	//Add as many traces as you have
	var data = [trace1];

	//This does not change
	Plotly.newPlot("graph", data);
	});