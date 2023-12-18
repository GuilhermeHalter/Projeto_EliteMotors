<script setup></script>

<template>
  <img src="../media/Ford_Mustang.jpg" alt="Ford Mustang" />

  <div class="container">
    <div class="sobre">
      <h1>
        Sobre a Elite Motors
      </h1>
      <p>
        Bem-vindo à Elite Motors, o seu destino premium para aquisição de carros de alto padrão e performance excepcional.
        Nós, na Elite Motors, estamos comprometidos em proporcionar uma experiência única de compra, onde luxo, qualidade
        e inovação se encontram para atender aos gostos mais refinados.
      </p>

      <div> 

      <h1>
         A Experiência Elite Motors:
      </h1>
      <p>
          Na Elite Motors, acreditamos que a paixão por carros vai além da simples locomoção; é uma expressão de estilo de vida e individualidade. 
          Nosso catálogo abrange uma seleção diversificada de veículos, desde elegantes sedans de luxo até poderosos supercarros. 
          Cada carro em nossa coleção é cuidadosamente selecionado, garantindo que atenda aos mais altos padrões de desempenho, design e inovação tecnológica.
      </p>
      </div>

      <h1>
        Equipe Especializada:
      </h1>
      <p>
        Nossa equipe dedicada de especialistas em automóveis está pronta para orientá-lo em cada etapa do processo de compra. 
        Seja para fornecer informações detalhadas sobre as especificações técnicas, orientar sobre opções de financiamento personalizadas ou organizar test drives exclusivos, 
        nossa equipe está comprometida em superar suas expectativas.
      </p>

    </div>
    <div class="imgSobre">
        <img src="../media/Ford_Mustang.jpg" alt="">
    </div>
  </div>
  
  <h2>Destaques:</h2>

  <div class="cards">
    <RouterLink to="/infos"> 
      <div class="card">
        <img src="../media/Ford_Mustang.jpg" alt="Car 1" />
        <h3>Nome do Veículo 1</h3>
        <p>Ano: 2023</p>
        <p>Preço: $30,000</p>
      </div>
    </RouterLink>
    
    <RouterLink to="/infos">
     <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 2" />
      <h3>Nome do Veículo 2</h3>
      <p>Ano: 2022</p>
      <p>Preço: $25,000</p>
     </div>
    </RouterLink>
   
    <RouterLink to="/infos">
     <div class="card">
      <img src="../media/Ford_Mustang.jpg" alt="Car 3" />
      <h3>Nome do Veículo 3</h3>
      <p>Ano: 2021</p>
      <p>Preço: $20,000</p>
     </div>
    </RouterLink>

   
    <RouterLink to="/infos">
      <div class="card">
        <img src="../media/Ford_Mustang.jpg" alt="Car 4" />
        <h3>Nome do Veículo 4</h3>
        <p>Ano: 2021</p>
        <p>Preço: $20,000</p>
      </div>
    </RouterLink>
    
    <RouterLink to="/infos">
      <div class="card">
        <img src="../media/Ford_Mustang.jpg" alt="Car 5" />
        <h3>Nome do Veículo 5</h3>
        <p>Ano: 2021</p>
        <p>Preço: $20,000</p>
      </div>
    </RouterLink>
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
  height: 200px;
  object-fit: cover;
  object-position: center -50px;
  border-radius: 6px;
  transition: transform 0.3s ease-in-out;
}

.card:hover img {
  transform: scale(1);
}

</style>
