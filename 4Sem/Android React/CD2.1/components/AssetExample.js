import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';

export default function AssetExample() {
  return (
    <View style={styles.container}>
      <Image style={styles.logo} source={require('../assets/prewiew-image.jpg')} />
      <Text style={styles.paragraph}>
        Как музыка может улучшить качество нашей жизни?
      </Text>
      <Text style = {styles.previewtext}>
        Музыка во все времена и в разных культурах играла очень важную роль. Наши предки погружались в нее и в горе, и в радости.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
  },
  previewtext:{
    fontSize: 14,
    margin: 8

  },
  paragraph: {
    margin: 8,
    marginBottom: 8,
    marginTop: 16,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'left',
  },
  logo: {
    height: 128,
    width: 150 ,
  }
});
