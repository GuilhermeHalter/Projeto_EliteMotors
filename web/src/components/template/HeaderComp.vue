<template>
  <div class="header">
    <img src="@/media/logo-elite-motors-PhotoRoom.png" class="logo"/>
    <div class="header-buttons">
      <router-link to="/" class="button">Home</router-link>
      <router-link to="/ofertas" class="button">Ofertas</router-link>
    </div>
  </div>
</template>

<style scoped>
.header {
  background-color:#001F3F;
  display: flex;
  height: 70px;
  justify-content: space-between;
  align-items: center;
  padding: 2.5rem;
}

.header-text {
  margin: 0; 
}

.header-buttons {
  display: flex;
  gap: 1rem; 
}

.logo{
  width: 70px;
  height: 70px;
  mix-blend-mode:  difference;
}

.header-buttons router-link {
  text-decoration: none;
  color: white;
  font-weight: bold;
}
.button{
  color: rgb(146, 146, 146);
  background-color: none;
  text-decoration: none;
  font-size: 17px;
  font-family: 'Times New Roman', Times, serif;
}
.button:hover{
  cursor: pointer;
  color: #FFD700;
  transition: 1s;
  font-size: 20px;
}
</style>
