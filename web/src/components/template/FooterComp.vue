<script setup></script>

<template>
  <div class="footer">
    <div class="info">
      <h3>Elite Motors</h3>
      <p>
        Av. Principal, 123 - Cidade, Estado
      </p>
      <p>
        Telefone: (12) 3456-7890 | Email: contato@elitemotors.com
      </p>
    </div>
    <div class="social">
      <h3>Siga-nos</h3>
      <a href="#" target="_blank">Facebook</a>
      <a href="#" target="_blank">Instagram</a>
      <a href="#" target="_blank">Twitter</a>
    </div>
  </div>
</template>

<style scoped>
.footer {
  background-color: rgb(40, 40, 40);
  color: white;
  padding: 20px;
  text-align: center;
  display: flex;
  justify-content: space-between;
}

.footer .info,
.footer .social {
  flex: 0 0 48%;
  text-align: left;
}

.footer .info h3,
.footer .social h3 {
  margin-bottom: 10px;
}

.footer a {
  display: block;
  margin-bottom: 5px;
  color: white;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.footer a:hover {
  color: #ccc;
}
</style>
