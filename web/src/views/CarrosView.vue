<script setup></script>

<template>
  <h2>Loja:</h2>

  <div class="cards">
    <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 1" />
      <h3>Nome do Veículo 1</h3>
      <p>Ano: 2023</p>
      <p>Preço: $30,000</p>
    </div>

    <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 2" />
      <h3>Nome do Veículo 2</h3>
      <p>Ano: 2022</p>
      <p>Preço: $25,000</p>
    </div>

    <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 3" />
      <h3>Nome do Veículo 3</h3>
      <p>Ano: 2021</p>
      <p>Preço: $20,000</p>
    </div>

    <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 4" />
      <h3>Nome do Veículo 4</h3>
      <p>Ano: 2021</p>
      <p>Preço: $20,000</p>
    </div>

    <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 5" />
      <h3>Nome do Veículo 5</h3>
      <p>Ano: 2021</p>
      <p>Preço: $20,000</p>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgb(81, 81, 81);
}
.sobre {
  flex: 0 0 50%;
  padding: 60px;
}

.imgSobre img{
  height: 45rem;
  object-fit: none;
}

img {
  width: 100%;
  height: 35vw;
  object-fit: cover;
  object-position: center -300px;
}

h1{
  padding-top: 30px;
  padding-bottom: 10px;
}

h2{
  padding: 40px 0 40px 15px;
}
.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  flex: 0 0 calc(33.33% - 20px);
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  text-align: center;
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: scale(1.05);
}

.card img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  object-position: center -100px;
  border-radius: 6px;
  transition: transform 0.3s ease-in-out;
}

.card:hover img {
  transform: scale(1);
}
</style>
