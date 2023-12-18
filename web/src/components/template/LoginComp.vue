<template>
  <div class="login-container">
    <div class="image-container">
      <!-- Imagem grande ocupando 50% da tela -->
      <img src="" alt="Imagem de fundo" />
    </div>
    <div class="login-card">
      <!-- Card de login com inputs de email e senha -->
      <h2>Faça Login</h2>
      <form>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />

        <label for="password">Senha:</label>
        <input type="password" id="password" v-model="password" required />

        <button @click.prevent="login">Entrar</button>
      </form>
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
  },
};
</script>

<style>
/* Estilos para a tela de login */
.login-container {
  display: flex;
  height: 100vh;
}

.image-container {
  flex: 1;
  overflow: hidden;
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
}

button:hover {
  background-color: #0056b3;
}
</style>
