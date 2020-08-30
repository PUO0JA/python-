import firebase from 'firebase';

// Initialize Firebase
// var firebaseConfig = {
//     apiKey: "AIzaSyCcwYbVvEuSS5RQ7xiwkobwGQf4Pyy_iNo",
//     authDomain: "chatdemo-e097d.firebaseapp.com",
//     databaseURL: "https://chatdemo-e097d.firebaseio.com",
//     projectId: "chatdemo-e097d",
//     storageBucket: "chatdemo-e097d.appspot.com",
//     messagingSenderId: "943602947861",
//     appId: "1:943602947861:web:29f175a02e00bb0f313b1c",
//     measurementId: "G-N858JNWEKD"
//   };
var firebaseConfig = {
	apiKey: 'AIzaSyCcwYbVvEuSS5RQ7xiwkobwGQf4Pyy_iNo',
	authDomain: 'chatdemo-e097d.firebaseapp.com',
	databaseURL: 'https://chatdemo-e097d.firebaseio.com',
	projectId: 'chatdemo-e097d',
	storageBucket: 'chatdemo-e097d.appspot.com',
	messagingSenderId: '943602947861',
	appId: '1:943602947861:web:29f175a02e00bb0f313b1c',
	measurementId: 'G-N858JNWEKD'
};
//const firebaseApp = firebase.initializeApp(firebaseConfig);
const firebaseApp = !firebase.apps.length ? firebase.initializeApp(firebaseConfig) : firebase.app();

export default firebaseApp;
