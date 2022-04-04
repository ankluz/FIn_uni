import React from 'react';
import { Text, View, Button } from 'react-native';

const HelloApp = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Hello World!</Text>
      <Button color = '#000000'></Button>
    </View>
  );
};

export default HelloApp;
