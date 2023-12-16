<script setup>
import { ref, reactive } from 'vue'
import { useAuthStore } from '@/stores/auth'
import Modal from '@/components/template/Modal.vue'

const authStore = useAuthStore()
const showForm = ref(false)
const user = reactive({
  username: '',
  password: ''
})

function closeForm() {
  showForm.value = false
  user.username = ''
  user.password = ''
}

async function login() {
  try {
    await authStore.login({ ...user })
    closeForm()
  } catch (error) {
    alert('Usuário ou senha inválidos')
  }
}
</script>

<template>
  <modal :visible="showForm" @close="showForm = false">
    <template #header>
      <h3>Login</h3>
    </template>
    <template #body>
      <form class="form">
        <div class="form-item">
          <input type="text" placeholder="Usuário" id="username" v-model="user.username" />
          <label for="username">Usuário</label>
        </div>
        <div class="form-item">
          <input type="password" placeholder="Senha" id="password" v-model="user.password" />
          <label for="password">Senha</label>
        </div>
      </form>
    </template>
    <template #footer>
      <div class="footerButtons">
        <button @click="closeForm">Cancelar</button>
        <button class="loginButton" @click="login">Login</button>
      </div>
    </template>
  </modal>
</template>

<style>
</style>