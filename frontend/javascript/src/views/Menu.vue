<template>
    <div class="fullscreen-menu">
        <img alt="Ouronova" class="logo" src="@/../../../img/image.png" />
        <nav>
            <ul>
                <li>
                    <RouterLink to="/reference1"
                        >Desafio - Reference 1</RouterLink
                    >
                </li>
                <li>
                    <RouterLink to="/reference2"
                        >Desafio - Reference 2</RouterLink
                    >
                </li>

                <!-- Adicione mais links de navegação conforme necessário -->
            </ul>
        </nav>
    </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>
/* Estilos para o menu em tela cheia */
.fullscreen-menu {
    align-items: center;
    justify-content: center;

    width: 100%;
    height: 100%;
    color: white;

    padding: 10px 0;
}

ul {
    list-style: none;
    padding: 0;
    text-align: center;
}

li {
    display: inline;
    margin-right: 20px;
}

li:hover {
    background-color: #ff0046;
    padding: 10px;
    border-radius: 5px;
}
a {
    text-decoration: none;
    color: black;
    font-size: 18px;
}

a:hover {
    text-decoration: none;
    color: white;
}
.logo {
    display: flex;
    width: 80%;
    margin: 0 auto 1rem;
    justify-content: center;
    align-items: center;
}
</style>
