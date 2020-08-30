import React, { Component } from 'react';
import { Text, TextInput, TouchableHighlight, StatusBar, ListView, FlatList, View, StyleSheet } from 'react-native';
import Constants from 'expo-constants';
import firebaseApp from './firebaseConfig.js';

export default class Rooms extends Component {
	static navigationOptions = {
		title: 'Rooms',
		header: null
	};
	constructor(props) {
		super(props);
		var firebaseDB = firebaseApp.database();
		this.roomsRef = firebaseDB.ref('rooms');
		this.state = {
			rooms: [],
			newRoom: ''
		};
	}

	componentDidMount() {
		this.listenForRooms(this.roomsRef);
	}

	listenForRooms(roomsRef) {
		console.log('roomsRef: ' + roomsRef);
		roomsRef.on('value', dataSnapshot => {
			var roomsFB = [];
			dataSnapshot.forEach(child => {
				roomsFB.push({
					name: child.val().name,
					key: child.key
				});
			});
			this.setState({ rooms: roomsFB });
		});
	}

	addRoom() {
		if (this.state.newRoom === '') {
			return;
		}
		this.roomsRef.push({ name: this.state.newRoom });
		this.setState({ newRoom: '' });
	}

	openMessages(room) {
		this.props.navigation.navigate('Messages', { roomKey: room.key, roomName: room.name });
	}

	renderRow(item) {
		return (
			<TouchableHighlight onPress={() => this.openMessages(item)}>
				<Text>{item.name}</Text>
			</TouchableHighlight>
		);
	}

	render() {
		return (
			<View style={styles.roomsContainer}>
				<View style={{ flexDirection: 'row', borderWidth: 1, borderColor: 'black' }}>
					<TextInput
						style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}
						placeholder={'New Room Name'}
						onChangeText={text => this.setState({ newRoom: text })}
						value={this.state.newRoom}
					/>
					<TouchableHighlight
						style={{ alignItems: 'center', justifyContent: 'center' }}
						underlayColor="#fff"
						onPress={() => this.addRoom()}
					>
						<Text>Create</Text>
					</TouchableHighlight>
				</View>

				<View>
					<FlatList data={this.state.rooms} renderItem={({ item }) => this.renderRow(item)} />
				</View>
			</View>
		);
	}
}
const styles = StyleSheet.create({
	roomsContainer: {
		flex: 1,
		paddingTop: Constants.statusBarHeight
	}
});
