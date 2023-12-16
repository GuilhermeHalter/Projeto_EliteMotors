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
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.header-text {
  margin: 0; 
}

.header-buttons {
  display: flex;
  gap: 1rem; 
}

.logo{
  width: 100px;
  height: 100px;
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
  font-size: 18px;
}
.button:hover{
  cursor: pointer;
  color: #FFD700;
  transition: 1s;
}
</style>
