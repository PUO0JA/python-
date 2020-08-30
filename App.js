import React,{Component} from 'react';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import Rooms from './components/Rooms';
import Messages from './components/Messages';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

const navigator = createStackNavigator({

    SignIn: {screen : SignIn},
    SignUp: { screen: SignUp },
    Rooms: { screen: Rooms },
    Messages: { name: 'Messages', screen: Messages}
  
});

export default class App extends Component{
  render(){
    
    const AppNavigator =  createAppContainer(navigator);
    return(
       <AppNavigator/>
    );
  }
}
