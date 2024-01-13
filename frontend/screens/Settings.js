import { StyleSheet, Text, View } from 'react-native';

const Settings = () => {
  return (
    <View style={styles.container}>
      <Text>Settings go here!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#E8F5FF',
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default Settings;