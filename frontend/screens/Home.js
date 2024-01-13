import { StyleSheet, Text, View } from 'react-native';

const Home = () => {
  return (
    <View style={styles.container}>
      <View style={styles.welcomeOuter}>
        <Text style={styles.welcomeText}>
          Welcome to SmartCart!
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#E8F5FF',
    flex: 1,
    alignItems: 'center',
  },
  welcomeOuter: {
    backgroundColor: '#FFFF',
    width: 300,
    height: 80,
    marginTop: 30,
    borderRadius: 10,
  },
  welcomeText: {
    textAlign: 'center',
    marginTop: 30,
    fontWeight: 'bold',
  }
});

export default Home;