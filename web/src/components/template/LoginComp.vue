<template>
  <div class="login-container">
    <div class="image-container">
      <h1 class="title">Welcome to the Elite Motors!!!</h1>
      <img src="" alt="Imagem de fundo" />
    </div>
    <div class="login-card">
      <h2>Faça Login</h2>
      <form>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />

        <label for="password">Senha:</label>
        <input type="password" id="password" v-model="password" required />

        <button @click.prevent="login">Entrar</button>
      </form>

      <p>Ainda não tem conta? <router-link to="/cadastro">Cadastre-se</router-link></p>

      <p>Logue também:</p>
      <div class="social-login">
        <button @click.prevent="loginWithGoogle">Google</button>
        <button @click.prevent="loginWithFacebook">Facebook</button>
        <button @click.prevent="loginWithApple">Apple</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      // Lógica de autenticação aqui
      console.log('Email:', this.email);
      console.log('Senha:', this.password);
      // Adicione a lógica de autenticação conforme necessário
    },
    loginWithGoogle() {
      // Lógica de autenticação com Google
      console.log('Login com Google');
    },
    loginWithFacebook() {
      // Lógica de autenticação com Facebook
      console.log('Login com Facebook');
    },
    loginWithApple() {
      // Lógica de autenticação com Apple
      console.log('Login com Apple');
    },
  },
};
</script>

<style>
/* Estilos para a tela de login */
.login-container {
  display: flex;
  height: 100vh;
  position: relative;
}

.title {
  position: absolute;
  margin-left: 150px;
  margin-top: 100px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color:  #001F3F;
}

.image-container {
  flex: 1;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: -170px;
}

.login-card {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.login-card h2 {
  margin-bottom: 20px;
}

form {
  width: 100%;
  max-width: 300px;
  text-align: center;
}

label {
  display: block;
  margin-bottom: 8px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
}

button {
  background-color: #007bff;
  color: #fff;
  padding: 10px;
  border: none;
  cursor: pointer;
  margin-bottom: 16px;
}

button:hover {
  background-color: #0056b3;
}

p {
  margin-bottom: 16px;
}

.social-login button {
  background-color: #fff;
  color: #000;
  padding: 10px;
  border: 1px solid #ccc;
  cursor: pointer;
  margin-right: 8px;
}

.social-login button:hover {
  background-color: #eee;
}
</style>
