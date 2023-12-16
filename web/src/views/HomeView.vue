<script setup></script>

<template>
  <div class="image-container">
    <img src="../media/Ford_Mustang.jpg" alt="Ford Mustang" />
  </div>
</template>

<style scoped>
.image-container {
  display: flex;
}

img {
  width: 100%;
  height: 50vw; 
  object-fit: cover;
  object-position: center -300px;
}
</style>
