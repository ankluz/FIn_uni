import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import Constants from 'expo-constants';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.paragraph}>
        Lorem ipsum dolor sit amet
      </Text>
      <View style = {styles.header}>
      <Text>
      consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </Text>
      </View>
      <View style={styles.body}>
      <Text>
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
      </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    paddingTop: Constants.statusBarHeight,
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  paragraph: {
    margin: 24,
    marginBottom: 8,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  header: {
    flex: 1,
    justifyContent: 'center',
    marginLeft: 16,
    marginRight: 16,
    fontSize: 16,
    padding: 14,
    backgroundColor: '#969696',
  },
  body:{
    flex: 4,
    marginLeft: 16,
    marginRight: 16,
    fontSize: 14,
    padding: 14,
    backgroundColor: '#757575',
  }
});
