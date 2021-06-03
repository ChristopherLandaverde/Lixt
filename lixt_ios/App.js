/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';

import {
  Grocery,
  LoadingUser,
  ReplaceGroceryItem,
} from 'react-native/Libraries/NewAppScreen';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import 'react-native-gesture-handler';

const Stack = createStackNavigator();

const App: () => React$Node = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{headerShown: false}}>
        <Stack.Screen name="Enter Name" component={LoadingUser} />
        <Stack.Screen name="Lixt" component={Grocery} />
        <Stack.Screen name="Edit" component={ReplaceGroceryItem} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
