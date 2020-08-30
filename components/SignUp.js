import React from 'react';
import { Text, View, Button,StyleSheet,TextInput,Alert } from 'react-native';
import firebaseApp from './firebaseConfig.js';

class SignUp extends React.Component {
  static navigationOptions = {
    title: 'SignUp',
  };

  constructor(props) {
    super(props)
    this.state = {
      userEmail: '',
      userPassword: ''
    }
  }

async signUp() {
    if (this.state.userEmail != '' && this.state.userPassword != '') {
      try {
        await firebaseApp.auth().createUserWithEmailAndPassword(this.state.userEmail, this.state.userPassword);
        console.log(this.state.userEmail + ' signed up');
        this.props.navigation.navigate('Rooms');
      } catch(error) {
        console.log(error.toString());
        Alert.alert(error.toString());
      }
    }
    else {
      Alert.alert(
        'Invalid Sign Up',
        'The Email and Password fields cannot be blank.',
        [
          {text: 'OK', onPress: () => console.log('OK Pressed')},
        ],
        { cancelable: false }
      )
    }
  }

  onChangeTextEmail = userEmail => this.setState({ userEmail });
  onChangeTextPassword = userPassword => this.setState({ userPassword });
//  onChangeTextName = name => this.setState({ name });

  render() {
    return (
      <View>
        <Text style={styles.title}>Email:</Text>
        <TextInput
          style={styles.nameInput}
          placeHolder="test10@gmail.com"
          onChangeText={this.onChangeTextEmail}
       //   onChangeText={(text) => this.setState({ userEmail: text })}
          value={this.state.email}
        />
        <Text style={styles.title}>Password:</Text>
        <TextInput
          style={styles.nameInput}
          onChangeText={this.onChangeTextPassword}
          value={this.state.password}
        />
        <Button
          title="Create Account"
          style={styles.buttonText}
           onPress={this.signUp.bind(this)}
        />
          <Button
          title="Go To Login"
          style={styles.buttonText}
          onPress={() => this.props.navigation.goBack()}
        />
        
      </View>
    );
  }
}

const offset = 16;
const styles = StyleSheet.create({
  title: {
    marginTop: offset,
    marginLeft: offset,
    fontSize: offset,
  },
  nameInput: {
    height: offset * 2,
    margin: offset,
    paddingHorizontal: offset,
    borderColor: '#111111',
    borderWidth: 1,
    fontSize: offset,
  },
  buttonText: {
    marginLeft: offset,
    fontSize: 42,
  },
  
});

export default SignUp;