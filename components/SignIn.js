import React from 'react';
import { Text, View, Button, StyleSheet, TextInput,Alert } from 'react-native';
import firebaseApp from './firebaseConfig.js';

class SignIn extends React.Component {
  static navigationOptions = {
    title: 'Login',
  };

 constructor(props) {
    super(props)
    this.state = {
      userEmail: '',
      userPassword: ''
    }
  }

async signIn() {
    if (this.state.userEmail != '' && this.state.userPassword != '') {
      try {
        await firebaseApp.auth().signInWithEmailAndPassword(this.state.userEmail, this.state.userPassword);
        console.log(this.state.userEmail + ' signed in');
        this.props.navigation.navigate('Rooms');
      } catch(error) {
        console.log(error.toString());
        Alert.alert(error.toString());
      }
    }
    else {
      Alert.alert(
        'Invalid Sign In',
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

  render() {
    return (
      <View>
        <Text style={styles.title}>Email:</Text>
        <TextInput
          style={styles.nameInput}
          placeHolder="enter email"
           value={this.state.email}
          onChangeText={this.onChangeTextEmail}
         
        />
        <Text style={styles.title}>Password:</Text>
        <TextInput
          style={styles.nameInput}
          placeHolder="enter pass"
          value={this.state.password}
          onChangeText={this.onChangeTextPassword}
          
        />
        <Button
          title="Login"
          style={styles.buttonText}
          onPress={this.signIn.bind(this)}
        />

        <Button
          title="create new account"
          style={styles.buttonText}
          onPress={() => this.props.navigation.navigate('SignUp')}
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

export default SignIn;
